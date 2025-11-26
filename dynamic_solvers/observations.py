import time

from TPMCSolver import TPMCSolver
from builders.TPMCFactory import TPMCFactory
from builders.POMDPSpec import POMDPAdapter
from collections.abc import Iterable

from z3 import sat


def stirling_partitions(n, k):
    """Generate all partitions of {0..n-1} into k unlabeled nonempty subsets."""
    items = list(range(n))

    def backtrack(i, curr, used):
        if i == n:
            if used == k:
                # Yield a sorted normalized form (unlabeled buckets)
                yield list(sorted(list(sorted(b)) for b in curr[:used]))
            return

        # Option 1: put item i into an existing bucket
        for b in range(used):
            curr[b].append(items[i])
            yield from backtrack(i+1, curr, used)
            curr[b].pop()

        # Option 2: create a new bucket (only if we have room)
        if used < k:
            curr[used].append(items[i])
            yield from backtrack(i+1, curr, used+1)
            curr[used].pop()

    # start with empty structure
    curr = [[] for _ in range(k)]
    yield from backtrack(0, curr, 0)

def prettify(obj, prefix: str):
    # Base case: if it's an int, prettify it
    if isinstance(obj, int):
        return f"{prefix}{obj}"
    # If it's an iterable (list/tuple/set), recurse into it
    if isinstance(obj, Iterable):
        container_type = type(obj)
        return container_type(prettify(item, prefix) for item in obj)
    return obj


if __name__ == "__main__":
    start = time.process_time()
    width = 3
    height = 3
    goal = 4
    budget = 3
    threshold = "<= Q(9,4)"
    verbose = False

    tpmc_instance = TPMCFactory.create(oop_variant='pop',
                                       puzzle_type='grid',
                                       width=width,
                                       height=height,
                                       goal=goal,
                                       budget=budget,
                                       determinism=False,
                                       precision='strict',
                                       bool_encoding=True,
                                       verbose=verbose)
    now = time.process_time()
    print(f"Initialized TPMC in {(now - start):.4f}s")
    start = now

    solver = TPMCSolver(tpmc_instance.ctx, verbose=verbose)
    adapter = POMDPAdapter(tpmc_instance)
    solver.prepare_constraints(adapter, threshold)

    now = time.process_time()
    print(f"Initialized Solver, POMDP adapter, and constraints in {(now - start):.4f}s")
    start = now

    clusters = tpmc_instance.clusters
    keys = list(clusters.keys())
    num_clusters = len(keys)

    print(f"\nClusters (goal = s{tpmc_instance.goal}):")
    for c, cluster_idx in enumerate(clusters):
        print(f"  {cluster_idx} (o{c}): {prettify(clusters[cluster_idx], "s")}")

    # Given a budget B, we generate all possible partitions for clusters into B buckets
    partitions = [(p, partition) for p, partition in enumerate(stirling_partitions(n=num_clusters, k=budget))]
    now = time.process_time()
    print(f"\nThere are S({num_clusters},{budget}) = {len(partitions)} partitions to explore")
    print(f"Generated partitions in {(now - start):.4f}s")
    start = now

    # For each partition, we place all states from each cluster in the specified bucket to form an observation function
    # We rank each observation function based on the number of blocks that follow an equivalence relation and break ties with the number of strategy constraints that it imposes
    ranked_obs_functions = []
    for p, partition in partitions:
        obs_function = [-1]*tpmc_instance.size
        strategy_constraints = []
        equivalence_score = 0
        for b, bucket in enumerate(partition):
            for cluster_idx in bucket:
                cluster = keys[cluster_idx]
                # Assign states in the cluster to the bucket/observation class
                for state in clusters[cluster]:
                    obs_function[state] = b

            # We can impose strategy constraints for an observation class based on its states' optimal action(s)
            actions_per_cluster = [keys[cluster_idx].actions for cluster_idx in bucket]
            actions_in_bucket = set.union(*actions_per_cluster)
            common_actions = set.intersection(*actions_per_cluster)
            common_action = None
            if len(common_actions) > 0:
                # All clusters in bucket follow an equivalence relation
                equivalence_score += 1
                # Choose one common action to be executed with 100% rate
                common_action = common_actions.pop()
                action_idx = tpmc_instance.actions.index(common_action)
                strategy_constraints.append(tpmc_instance.X[b][action_idx] == 1)
            for a, action in enumerate(tpmc_instance.actions):
                # If a common action is selected, all other actions should have rate 0
                if common_action is not None and action != common_action:
                    strategy_constraints.append(tpmc_instance.X[b][a] == 0)
                # If no common action can be selected, the actions not in the bucket's set of actions should have rate 0
                elif common_action is None and action not in actions_in_bucket:
                    strategy_constraints.append(tpmc_instance.X[b][a] == 0)

        ranked_obs_functions.append((partition, obs_function, strategy_constraints, equivalence_score))

    now = time.process_time()
    print(f"\nRanking of observation functions completed in {(now - start):.4f}s")
    start = now

    print("Ranked Observation Functions:")
    ranked_obs_functions = sorted(ranked_obs_functions, key=lambda ranked_partition: (-ranked_partition[3], -len(ranked_partition[2])))
    for partition, obs_function, strat_constraints, num_equivalences in ranked_obs_functions:
        print(f"{[[keys[cluster_idx].symbol for cluster_idx in bucket] for bucket in partition]}: {num_equivalences} equivalences, {len(strat_constraints)} strategy constraints")
        result = solver.evaluate_pomdp(adapter, obs_function, 30000, strat_constraints)
        print(f"Result: {result.solve_time:.4f}s | {result.result} | {result.reward}")
        # if result.result == sat:
        #     exit(0)
        # for i in range(3):
        #     time.sleep(1)
        #     print(f"Slept for {i+1}s")
