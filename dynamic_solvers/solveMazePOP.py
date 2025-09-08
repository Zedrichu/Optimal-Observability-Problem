import gc
import re
import time
from logging import Logger
from typing import List
from z3 import (Solver, Context,
                z3, set_option, sat, unsat,
                Real, Q, Or)

from dynamic_solvers.BenchmarkResult import BenchmarkResult

class MazePOPChain:
    """
    Z3 API solver for "Maze" instances in the POP problem with benchmarking

    Part of the OOP problem suites.
    """
    def __init__(self, budget: int, goal: int, width: int, depth: int, det: int):
        self.budget = budget
        self.goal = goal
        self.width = width
        self.depth = depth
        self.size = width + 3*(depth - 1)  # Total number of states in the maze
        self.det = det

        self.actions = ['l', 'r', 'u', 'd']

        self.exp_rew = None
        self.obs_fun = None
        self.strategy = None

        self.ctx = None
        self.solver = None

        self.evaluator = None
        self.logger = Logger("MazePOPChain")

        self.reset()

    def reset(self):
        """Reset for fresh solving context"""
        gc.collect() # Clean memory before starting
        self.ctx = Context()
        self.solver = Solver(ctx=self.ctx)

    def declare_variables(self):
        self.exp_rew = self.compute_expected_rewards(self.size)
        self.obs_fun = self.create_observation_maps()
        self.strategy = self.create_policy_maps()

    def compute_expected_rewards(self, states) -> List[z3.ArithRef | None]:
        # Expected cost/reward of reaching the goal from each corresponding state.
        print("# Expected cost/reward of reaching the goal from each corresponding state.")
        expected_rewards = [Real(f'pi{s}', self.ctx) for s in range(states)]
        print(expected_rewards)
        return expected_rewards

    def create_observation_maps(self) -> List[List[z3.ArithRef | None]]:
        # Choice of observations on the states (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)
        state_to_observation = [[None for _ in range(0, self.budget + 1)] for _ in range(0, self.size)]
        print("# Choice of observations (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)")
        for s in range(0, self.size):
            if s == self.goal:
                continue
            for o in range(1, self.budget + 1):
                state_to_observation[s][o] = Real(f'ys{str(s)}o{str(o)}', self.ctx)
            print(state_to_observation[s])
        return state_to_observation

    def create_policy_maps(self) -> List[List[z3.ArithRef | None]]:
        # Rates of randomized strategies
        print("# Rates of randomized strategies")
        observation_to_action = [[None for _ in self.actions] for _ in range(self.budget + 1)]
        for s in range(1, self.budget + 1):
            for a in range(len(self.actions)):
                observation_to_action[s][a] = Real(f'xo{str(s)}{self.actions[a]}', self.ctx)
            print(observation_to_action[s])

        return observation_to_action

    def extend_full_obs_pomdp_constraints(self, exp_rewards):
        """Add basic POMDP constraints to the assigned solver context.
        A POMDP cannot do better than the fully observable variant.
        """
        constraints = []

        print("#We cannot do better than the fully observable case")

        # Maze-specific bounds calculation
        pomdp_bounds = []
        goal_column = self.goal if self.goal < self.width else (self.goal - self.width) % 3 * (self.width // 2)
        goal_height = 0 if self.goal < self.width else (self.goal - self.width) // 3 + 1
        for s in range(self.size):
            if s < self.width:
                bound_value = goal_height + abs(s - goal_column)
            else:
                column = (s - self.width) % 3 * (self.width // 2)
                row = (s - self.width) // 3 + 1
                diff = int(column != goal_column)
                bound_value = abs(column - goal_column) + abs(row - goal_height + 2 * goal_height * diff)
            constraints.append(exp_rewards[s] >= bound_value)
        print(constraints)
        return constraints

    def build_cost_rewards_equations(self, ExpRew, X, Y):
        constraints = []
        numbers = [i for i in range(self.size)]
        # Expected cost/reward equations
        print("# Expected cost/reward equations")

        for s in numbers:
            if s == self.goal:
                constraints.append(ExpRew[s] == 0)
                continue

            # Helper function to calculate next states for maze navigation
            def get_next_state(state, action):
                if action == 'l':
                    if 0 < state < width:
                        return state - 1
                elif action == 'r':
                    if 0 <= state < width - 1:
                        return state + 1
                elif action == 'u':
                    if state == width:
                        return 0
                    elif state == width + 1:
                        return (width - 1) // 2
                    elif state >= width + 2:
                        return state - 3
                else:  # action == 'd'
                    if state == 0:
                        return width
                    elif state == (width - 1) // 2:
                        return width + 1
                    elif width <= state <= numbers[-1] - 3:
                        return state + 3
                return state

            # Build action terms for each direction using transition tables
            action_terms = []
            for (a, act) in enumerate(self.actions):
                obs_strategy_terms = [Y[s][o]*X[o][a] for o in range(1, budget + 1)]
                obs_strategy_sum = sum(obs_strategy_terms)
                next_state = get_next_state(s, act)
                action_terms.append(obs_strategy_sum * (1 + ExpRew[next_state]))

            constraints.append(ExpRew[s] == sum(action_terms))

        print(constraints)
        return constraints

    def build_threshold_constraint(self, ExpRew, threshold):
        # We are dropped uniformly in the maze
        print("# We are dropped uniformly in the maze")
        # We want to check if the minimal expected cost is below some threshold {threshold}
        print(f"# We want to check if the minimal expected cost is below some threshold {threshold}")

        sum_rewards = sum(ExpRew[i] for i in range(self.size) if i != self.goal)
        sign_idx = threshold.find('<')
        if sign_idx == -1:
            return ValueError("No sign in threshold")
        sign = (lambda x, y: x <= y) if threshold[sign_idx + 1] == '=' else (lambda x, y: x < y)
        nominator, denominator = map(int, re.findall(r"\d+", threshold))

        self.evaluator = sum_rewards * Q(1, self.size - 1, self.ctx)
        print(sign(sum_rewards * Q(1, self.size - 1, self.ctx), Q(nominator, denominator, self.ctx)))

        constraint = sign(sum_rewards * Q(1, self.size - 1, self.ctx), Q(nominator, denominator, self.ctx))
        return constraint

    def extend_strategy_constraints(self, X, determinism: bool):
        # Randomised strategies (proper probability distributions)
        print('# Randomised strategies (proper probability distributions)')
        constraints = []
        act_no = len(self.actions)
        for o in range(1, budget + 1):
            for act in range(act_no):
                constraints.append(X[o][act] >= 0)
                constraints.append(X[o][act] <= 1)
            sum_prob = sum(X[o][act] for act in range(act_no))
            constraints.append(sum_prob == 1)

        if determinism:
            print('# Deterministic strategies activated (one-hot encoding or degenerate categorical distribution)\n')
            for o in range(1, budget + 1):
                for act in range(act_no):
                    constraints.append(Or(X[o][act] == 0, X[o][act] == 1))

        print(constraints)
        return constraints

    def extend_observation_constraints(self, Y):
        # Observation function constraints - every state should be mapped to some observable class
        print("# Observation function constraints - every state should be mapped to some observable class")
        constraints = []
        for s in range(0, self.size):
            if s == self.goal:
                continue
            for o in range(1, budget + 1):
                constraints.append(Or(Y[s][o] == 0, Y[s][o] == 1))

        print('# Every state should be mapped to exactly one equivalence class\n')

        for s in range(0, self.size):
            if s == self.goal:
                continue
            sum_state_obs = sum(Y[s][o] for o in range(1, budget + 1))
            constraints.append(sum_state_obs == 1)
        print(constraints)
        return constraints

    def set_solver_options(self, result_path: str, reward_path: str):
        set_option(max_args=1000000, max_lines=100000000)
        self.file_results = open(result_path, "w")
        self.file_rewards = open(reward_path, "w")
        return

    def solve_benchmark(self) -> BenchmarkResult:

        # Solving phase timing
        solve_start = time.perf_counter()
        result = self.solver.check()
        solve_time = time.perf_counter() - solve_start

        # Get model if satisfiable
        model = self.solver.model() if result == sat else None

        if result == sat:
            model = self.solver.model()
            print('✅Solution found!')
            self.file_results.write(str(model))
            self.file_rewards.write(str(model.eval(self.evaluator)))
        elif result == unsat:
            print('❌No solution!')
            self.file_rewards.write('N/A')
        else:
            print('❔Unknown!')

        return BenchmarkResult(
            solve_time=solve_time,
            result=result,
            model=model
        )

    def cleanup(self):
        if self.file_results:
            self.file_results.close()
        if self.file_rewards:
            self.file_rewards.close()

        # Clean up Z3 objects
        del tpMC.solver
        del tpMC.ctx
        gc.collect()
        pass


def benchmark_maze_pomdp(budget: int, target: int, size: int,
                         threshold: float, det: int, runs: int = 1) -> list:
    """Run multiple benchmark runs for statistical significance"""
    results = []

    for run in range(runs):
        solver = MazePOPChain(budget, target, size, det)
        result = solver.solve_benchmark(budget, target, size, threshold, det)
        results.append(result)

        # Clean up context
        del solver
        gc.collect()

    return results


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        width = int(sys.argv[1])
        depth = int(sys.argv[2])
        goal = int(sys.argv[3])
        budget = int(sys.argv[4])
        threshold = sys.argv[5]
        det = int(sys.argv[6])

        tpMC = MazePOPChain(budget, goal, width, depth, det)

        tpMC.declare_variables()

        solver = tpMC.solver

        ExpRew = tpMC.exp_rew
        X = tpMC.strategy
        Y = tpMC.obs_fun

        bound_constraints = tpMC.extend_full_obs_pomdp_constraints(ExpRew)
        cost_constraints = tpMC.build_cost_rewards_equations(ExpRew, X, Y)
        threshold_constraint = tpMC.build_threshold_constraint(ExpRew, threshold)
        strategy_constraints = tpMC.extend_strategy_constraints(X, determinism=det == 1)
        observation_constraints = tpMC.extend_observation_constraints(Y)
        solver.add(bound_constraints)
        solver.add(cost_constraints)
        solver.add(threshold_constraint)
        solver.add(strategy_constraints)
        solver.add(observation_constraints)

        tpMC.set_solver_options("results.txt", "reward.txt")

        try:
            result = tpMC.solve_benchmark()
            print(f"🚀Solve time: {result.solve_time:.4f}s")
            # print(f"Setup time: {result.setup_time:.4f}s")
            # print(f"Memory used: {result.memory_used / 1024 / 1024:.2f} MB")
            # print(f"Constraints: {result.constraint_count}")
        finally:
            tpMC.cleanup()