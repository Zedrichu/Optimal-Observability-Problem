import time

from z3 import sat, BoolRef, unknown

from ResultOOP import ResultOOP
from TPMCSolver import TPMCSolver
from builders.POMDPSpec import POMDPAdapter
from builders.pop.POPSpec import POPSpec
from direction import Direction
from utils import stirling_partitions


class ClusterPOPSolver:
    solver: TPMCSolver
    tpmc: POPSpec
    verbose: bool
    adapter: POMDPAdapter

    def __init__(self, solver: TPMCSolver, tpmc: POPSpec, verbose: bool, threshold: str) -> None:
        self.solver = solver
        self.tpmc = tpmc
        self.verbose = verbose
        self.adapter = POMDPAdapter(tpmc)
        self.solver.prepare_constraints(self.adapter, threshold)

    def solve(self, level: int, timeout_ms: int) -> ResultOOP:
        """
        Attempts to solve a POP instance by solving and evaluating the underlying POMDPs in it.

        The core algorithmic idea is to group states into 'atomic groups' based on their respective
        optimal action(s) in the underlying MDP, and then explore a constant number of observation
        functions that combine the atomic groups into observation classes.

        The observation functions are solved in an order specified by heuristic scores that estimate
        1) how close an observation function is to the optimal, and
        2) how much an observation function constraints its possible strategies.

        Args:
            level (int): The ranking level up to which the search should be performed.
            timeout_ms (int): The timeout in milliseconds for the solver.

        Returns:
            ResultOOP with solve time, result, reward, and model (if any was found).
        """
        number_atomic_groups = len(self.tpmc.clusters)
        number_blocks = self.tpmc.budget

        # Given a budget B, we generate all possible partitions for atomic groups into B blocks
        start = time.process_time()
        partitions = [partition for partition in stirling_partitions(n=number_atomic_groups, k=number_blocks)]

        now = time.process_time()
        if self.verbose:
            print(f"\nThere are S({number_atomic_groups},{number_blocks}) = {len(partitions)} partitions to explore")
            print(f"Generated partitions in {(now - start):.4f}s")
        start = now

        ranking_partitions = self.rank_partitions(partitions)
        now = time.process_time()
        if self.verbose:
            print(f"\nRanking of observation functions completed in {(now - start):.4f}s")
        start = now

        result = self.search(partitions, ranking_partitions, level, timeout_ms)
        now = time.process_time()
        if self.verbose:
            print(f"\nSearch completed in {(now - start):.4f}s")

        return result

    def search(self, partitions: list[list[list[int]]], ranking_partitions: list[tuple[int, int, int]], level, timeout_ms) -> ResultOOP:
        """
        Args:
            partitions (list[list[list[int]]]): The list of partitions (each partition is a list
                of blocks and each block is a list of atomic-group indices).
            ranking_partitions (list[tuple[int,int,int]]): Ranked metadata for partitions.
            level (int): Reserved. Intended to limit the number of ranked partitions to examine.
            timeout_ms (int): Timeout in milliseconds.

        Returns:
            ResultOOP: If a satisfiable model is found it is returned immediately. Otherwise, a
                ResultOOP with result=unknown and the elapsed solve_time is returned.
        """

        atomic_groups = list(Direction)
        start = time.process_time()
        for partition_idx, equivalence_score, constraint_score in ranking_partitions:
            if self.verbose:
                partition = [[atomic_groups[atomic_group_idx].name for atomic_group_idx in block] for block in partitions[partition_idx]]
                print(f"Evaluating partition: {partition} | h_equivalence_score = {equivalence_score}, h_constraint_score = {constraint_score}")
            observation_function, strategy_constraints = self.apply_partition_to_states(partitions[partition_idx])

            assert(constraint_score == len(strategy_constraints))

            result = self.solver.evaluate_pomdp(self.adapter, observation_function, timeout_ms, strategy_constraints)
            if result.result == sat:
                print(result)
                return result
            else:
                timeout_ms = timeout_ms - result.solve_time
                if timeout_ms <= 0:
                    break

        now = time.process_time()
        return ResultOOP(
            solve_time=now - start,
            result=unknown,
            reward=None,
            model=None
        )

    def rank_partitions(self, partitions: list[list[list[int]]]) -> list[tuple[int, int, int]]:
        """
        Compute heuristic scores for each partition and return a ranking of partition indices.

        Heuristics used:
        - equivalence_score: counts how many blocks in the partition contain a common action for
          all atomic groups in that block (i.e. an 'equivalence' relation where a single action
          is optimal across the block).
        - constraint_score: the number of constraints that can be imposed on the strategy
          variables when the partition is applied. For example, blocks with an equivalence relation
          can stay optimal when set the rate of a common action to 1 and the rest to 0 (adding |Act| constraints).

        Args:
            partitions (list[list[list[int]]]): The list of partitions to score.

        Returns:
            list[tuple[int,int,int]]: A list of tuples (partition_index, equivalence_score,
                constraint_score), sorted in descending order by (equivalence_score, constraint_score).
        """

        atomic_groups = list(Direction)
        ranking_partitions = []
        for (p, partition) in enumerate(partitions):
            equivalence_score = 0
            constraint_score = 0
            for block in partition:
                actions_per_atomic_group = [atomic_groups[atomic_group_idx].actions for atomic_group_idx in block]
                actions_in_block = set.union(*actions_per_atomic_group)
                equivalence_relation = True if len(set.intersection(*actions_per_atomic_group)) > 0 else False

                if equivalence_relation:
                    equivalence_score += 1
                    constraint_score += len(self.tpmc.actions)
                else:
                    for action in self.tpmc.actions:
                        if action not in actions_in_block:
                            constraint_score += 1
            ranking_partitions.append((p, equivalence_score, constraint_score))
        return sorted(ranking_partitions, key=lambda ranking: (ranking[1], ranking[2]), reverse=True)

    def apply_partition_to_states(self, partition: list[list[int]]) -> tuple[list[int], list[BoolRef]]:
        """
        Applies the given partition to the states, creating an observation function and strategy constraints.

        Args:
            partition (list[list[int]]): The partition to be applied, containing blocks of atomic group indices.

        Returns:
            tuple[list[int], list[BoolRef]]: A tuple containing the observation function and strategy constraints.
        """
        observation_function = [-1] * self.tpmc.size
        strategy_constraints = []
        atomic_groups = list(Direction)

        for b, block in enumerate(partition):
            actions_per_atomic_group = [atomic_groups[atomic_group_idx].actions for atomic_group_idx in block]
            actions_in_block = set.union(*actions_per_atomic_group)
            common_actions = set.intersection(*actions_per_atomic_group)
            common_action = None if len(common_actions) == 0 else common_actions.pop()

            for a, action in enumerate(self.tpmc.actions):
                if common_action is not None and action == common_action:
                    # If there's some common action, we can force it to 1 and others to 0.
                    strategy_constraints.append(self.tpmc.X[b][a] == 1)
                elif ((common_action is not None and action != common_action) or
                      common_action is None and action not in actions_in_block):
                    # Actions that do not appear in the block can be forced to 0. Any action that is not
                    # the common action (if any) can also be forced to 0.
                    strategy_constraints.append(self.tpmc.X[b][a] == 0)

            for atomic_group_idx in block:
                atomic_group = atomic_groups[atomic_group_idx]
                for state in self.tpmc.clusters[atomic_group]:
                    observation_function[state] = b

        return observation_function, strategy_constraints
