import copy
import gc
import sys
from typing import List, Tuple, Dict
import z3
from z3 import *

from OOP import BenchmarkResult


class LinePOPChain:
    def __init__(self, budget: int, goal: int, size: int, det: int):
        self.budget = budget
        self.goal = goal
        self.size = size

        self.puzzle_type = "line"
        # self.strat_type = "det" if det == 1 else "ran"

        self.actions = ['l', 'r']

        self.reset()

    def reset(self):
        """Reset for fresh solving context"""
        gc.collect()
        self.ctx = Context()
        self.solver = Solver(ctx=self.ctx)
        self.variables = {}

    def declare_variables(self):
        #TODO:
        return

    def create_expected_rewards(self) -> List[z3.ArithRef | None]:
        # Expected cost/reward of reaching the goal.
        expected_rewards = [None for _ in range(0, self.size)]
        print("# Expected cost/reward of reaching the goal.")
        for i in range(0, self.size):
            expected_rewards[i] = Real(f'pi{str(i)}', self.ctx)
            print(expected_rewards[i])

        return expected_rewards

    def create_observation_maps(self) -> List[List[z3.ArithRef | None]]:
        # Choice of observations on the states (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)
        state_to_observation = [[None for _ in range(0, self.budget + 1)] for _ in range(0, self.size)]
        print("# Choice of observations (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)")
        for i in range(0, self.size):
            if i == self.goal:
                continue
            for j in range(1, self.budget + 1):
                state_to_observation[i][j] = Real(f'ys{str(i)}o{str(j)}', self.ctx)
            print(state_to_observation[i])

        return state_to_observation

    def create_policy_maps(self) -> List[List[z3.ArithRef | None]]:
        # Rates of randomized strategies
        observation_to_action = [[None for _ in self.actions] for _ in range(budget + 1)]
        print("# Rates of randomized strategies")
        for i in range(1, budget + 1):
            for j in range(len(self.actions)):
                observation_to_action[i][j] = Real(f'xo{str(i)}{self.actions[j]}', self.ctx)
            print(observation_to_action[i])

        return observation_to_action

    def extend_full_obs_pomdp_constraints(self):
        """Add basic POMDP constraints to the assigned solver context.
        A POMDP cannot do better than the fully observable variant.
        """
        constraints = []
        expected_rewards = self.create_expected_rewards()

        print("#We cannot do better than the fully observable case")
        for i in range(size):
            # file.write(f'pi{str(i)} >= {str(abs(goal - i))}, ')
            constraints.append(expected_rewards[i] >= abs(self.goal - i))
            print(f"{expected_rewards[i]} >= {abs(self.goal - i)}")

        return constraints

    def build_cost_rewards_equations(self):
        return

    def set_threshold_constraint(self):
        return

    def extend_strategy_constraints(self):
        return

    def add_observability_mappings(self):
        return

    def solve_benchmark(self) -> BenchmarkResult:
        return


def benchmark_line_pomdp(budget: int, target: int, size: int,
                         threshold: float, det: int, runs: int = 1) -> list:
    """Run multiple benchmark runs for statistical significance"""
    results = []

    for run in range(runs):
        solver = LinePOPChain(budget, target, size, det)
        result = solver.solve_benchmark(budget, target, size, threshold, det)
        results.append(result)

        # Clean up context
        del solver
        gc.collect()

    return results


# Example usage matching your original function signature
def solve_line_constrained(budget: int, target: int, size: int, threshold: str, det: int):
    solver = LinePOPChain()
    result = solver.solve_benchmark(budget, target, size, float(threshold), det)

    print(f"Setup time: {result.setup_time:.4f}s")
    print(f"Solve time: {result.solve_time:.4f}s")
    print(f"Memory used: {result.memory_used / 1024 / 1024:.2f} MB")
    print(f"Constraints: {result.constraint_count}")

    if result.result == sat:
        print("Solution found:")
        print(result.model)
        return result.model
    elif result.result == unsat:
        print("No solution!!!")
        return None
    else:
        print("Unknown")
        return None

def create_line_constrained(budget: int, goal: int, size: int, threshold: str, det: int):
    puzzle_type = "line"
    strat_type = "det" if det == 1 else "ran"
    file = open(f'{puzzle_type}_{str(size)}_{strat_type}_dynamic_z3.py', 'w')
    actions = ['l', 'r']

    tpMC = LinePOPChain(budget, goal, size, det)

    tpMC.variables.update()

    # Expected cost/reward of reaching the goal.
    expected_rewards = [None for _ in range(0, size)]
    print("# Expected cost/reward of reaching the goal.")
    for i in range(0, size):
        expected_rewards[i] = Real(f'pi{str(i)}')
        print(expected_rewards[i])

    # Choice of observations (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)
    state_to_observation = [[None for _ in range(0, budget + 1)] for _ in range(0, size)]
    print("# Choice of observations (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)")
    for i in range(0, size):
        if i == goal:
            continue
        for j in range(1, budget + 1):
            state_to_observation[i][j] = Real(f'ys{str(i)}o{str(j)}')
        print(state_to_observation[i])

    # Rates of randomized strategies
    observation_to_action = [[None for _ in actions] for _ in range(budget + 1)]
    print("# Rates of randomized strategies")
    for i in range(1, budget + 1):
        for j in range(len(actions)):
            observation_to_action[i][j] = Real(f'xo{str(i)}{actions[j]}')
        print(observation_to_action[i])

    # file.write('solver = Solver()\n\n\n')
    solver = Solver()

    # We cannot do better than the fully observable case
    print("#We cannot do better than the fully observable case")
    for i in range(0, size):
        # file.write(f'pi{str(i)} >= {str(abs(goal - i))}, ')
        solver.add(expected_rewards[i] >= abs(goal - i))
        print(f"{expected_rewards[i]} >= {abs(goal - i)}")

    # Expected cost/reward equations
    print("# Expected cost/reward equations")
    for i in range(0, size):
        if i == goal:
            solver.add(expected_rewards[i] == 0)
            print(expected_rewards[i] == 0)
            continue
        # pi0 == (ys01*xo1l+ ys02*xo2l)*(1) + (ys01*xo1l+ ys02*xo2l)*(pi0) + (ys01*xo1r+ ys02*xo2r)*(1) + (ys01*xo1r+ ys02*xo2r)*(pi1),
        line = f'{expected_rewards[i]} == (ys{str(i)}o'
        for a in actions:
            for o in range(1, budget + 1):
                line = line + f'{str(o)}*xo{str(o)}{a}'
                if o < budget:
                    line = line + f'+ ys{str(i)}o'
                else:
                    if a == 'l':
                        line = line + ')*(1 + pi' + str(max(i - 1, 0)) + ') + (ys' + str(i)
                    else:
                        line = line + ')*(1 + pi' + str(min(i + 1, size - 1)) + ')'
        file.write(line + ',\n')



























    file.write(
        '# We are dropped uniformly in the line\n# We want to check if the minimal expected cost is below some threshold ' + str(
            threshold) + '\n')

    line = '('
    for i in range(0, size):
        if i == goal:
            continue
        if i < size - 1:
            if goal == size - 1:
                if i == size - 2:
                    line = line + 'pi' + str(i) + ')'
                else:
                    line = line + 'pi' + str(i) + '+'
            else:
                line = line + 'pi' + str(i) + '+'
        else:
            line = line + 'pi' + str(i) + ')'

    e = copy.deepcopy(line + ' * Q(1,' + str(size - 1) + ') ')

    line = line + ' * Q(1,' + str(size - 1) + ') ' + str(threshold) + ','

    file.write(line + '\n')

    file.write('# Randomised strategies (proper probability distributions)\n')
    for i in range(1, budget + 1):
        for a in actions:
            file.write('xo' + str(i) + a + '>= 0,\n')
            file.write('xo' + str(i) + a + '<= 1,\n')

    for i in range(1, budget + 1):
        for a in actions:
            if a == 'l':
                file.write('xo' + str(i) + a + ' + ')
            else:
                file.write('xo' + str(i) + a + ' == 1,\n')

    if det == 1:
        file.write('# Deterministic Strategies activated\n')
        for i in range(1, budget + 1):
            file.write('Or(xo' + str(i) + 'l ' + '== 0, xo' + str(i) + 'l' + ' == 1),\n')
            file.write('Or(xo' + str(i) + 'r ' + '== 0, xo' + str(i) + 'r' + ' == 1),\n')

    file.write('# ysNM is a function that should map every state N to some observable class M\n')

    for i in range(0, size):
        if i == goal:
            continue
        for j in range(1, budget + 1):
            file.write('Or(ys' + str(i) + str(j) + '== 0 , ys' + str(i) + str(j) + '== 1),\n')

    file.write('# Every state should be mapped to exactly one equivalence class\n')

    for i in range(0, size):
        if i == goal:
            continue
        for j in range(1, budget + 1):
            file.write('ys' + str(i) + str(j))
            if j < budget:
                file.write(' + ')
            else:
                file.write(' == 1')
        if i == size - 1:
            file.write('\n)\n\n')
        else:
            if i == size - 2:
                if goal == size - 1:
                    file.write('\n)\n\n')
                else:
                    file.write(',\n')
            else:
                file.write(',\n')

    file.write('set_option(max_args=1000000, max_lines=100000000)\n')

    file.write('file_results = open(\'results.txt\', \'w\')\n')

    file.write('file_reward = open(\'reward.txt\', \'w\')\n')

    file.write('if solver.check() == sat:\n\t')
    file.write('m = solver.model()\n\t')
    file.write('print(\'Solution found\')\n\t')
    file.write('file_results.write(str(m))\n\t')
    file.write('file_reward.write(str(m.eval(' + str(e) + ')))\n')
    file.write('elif solver.check() == unsat:\n\t')
    file.write('print(\'No solution!!!\')\n\t')
    file.write('file_reward.write(\'N/A\')\n')
    file.write('else:\n\t')
    file.write('print(\'Unknown\')')

if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 6:
        size = int(sys.argv[1])
        target = int(sys.argv[2])
        budget = int(sys.argv[3])
        threshold = sys.argv[4]
        det = int(sys.argv[5])

        create_line_constrained(budget, target, size, threshold, det)