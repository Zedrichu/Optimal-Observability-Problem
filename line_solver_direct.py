#!/usr/bin/python3
import time
import psutil
import gc
from z3 import *
from typing import Dict
from BenchmarkResult import *


class LinePOMDPSolver:
    """Direct Z3 API solver for line POMDP problems with benchmarking"""

    def create_variables(self, budget: int, target: int, size: int) -> Dict[str, any]:
        """Create all Z3 variables for the POMDP problem"""
        variables = {}


        # Observation mapping variables (skip target state)
        variables['ys'] = {}
        for i in range(size):
            if i == target:
                continue
            variables['ys'][i] = {}
            for j in range(1, budget + 1):
                variables['ys'][i][j] = Real(f'ys{i}o{j}', ctx=self.ctx)

        # Strategy variables
        variables['xo'] = {}
        actions = ['l', 'r']
        for i in range(1, budget + 1):
            variables['xo'][i] = {}
            for act in actions:
                variables['xo'][i][act] = Real(f'xo{i}{act}', ctx=self.ctx)

        self.variables = variables
        return variables

    def add_basic_constraints(self, target: int, size: int):
        """Add basic POMDP constraints"""
        constraints = []

        # Cannot do better than fully observable case
        for i in range(size):
            constraints.append(self.variables['pi'][i] >= abs(target - i))

        # Target state has zero cost
        constraints.append(self.variables['pi'][target] == 0)

        return constraints

    def add_strategy_constraints(self, budget: int, det: int):
        """Add strategy probability constraints"""
        constraints = []
        actions = ['l', 'r']

        # Probability bounds and normalization
        for i in range(1, budget + 1):
            prob_sum = 0
            for act in actions:
                var = self.variables['xo'][i][act]
                constraints.extend([var >= 0, var <= 1])
                prob_sum += var
            constraints.append(prob_sum == 1)

            # Deterministic constraints if requested
            if det == 1:
                for act in actions:
                    var = self.variables['xo'][i][act]
                    constraints.append(Or(var == 0, var == 1))

        return constraints

    def add_observation_constraints(self, budget: int, target: int, size: int):
        """Add observation mapping constraints"""
        constraints = []

        # Binary observation assignments
        for i in range(size):
            if i == target:
                continue
            obs_sum = 0
            for j in range(1, budget + 1):
                var = self.variables['ys'][i][j]
                constraints.append(Or(var == 0, var == 1))
                obs_sum += var
            # Each state maps to exactly one observation class
            constraints.append(obs_sum == 1)

        return constraints

    def add_cost_equations(self, budget: int, target: int, size: int):
        """Add expected cost equations"""
        constraints = []
        actions = ['l', 'r']

        for i in range(size):
            if i == target:
                continue

            # Build cost equation for state i
            cost_expr = 0
            for a_idx, a in enumerate(actions):
                # Probability of taking action `a` in state `i`
                action_prob = 0
                for o in range(1, budget + 1):
                    obs_prob = self.variables['ys'][i][o]
                    strategy_prob = self.variables['xo'][o][a]
                    action_prob += obs_prob * strategy_prob

                # Next state after action
                next_state = i - 1 if a == 'l' else i + 1
                next_state = max(0, min(next_state, size - 1))

                # Add to cost expression
                cost_expr += action_prob * (1 + self.variables['pi'][next_state])

            constraints.append(self.variables['pi'][i] == cost_expr)

        return constraints

    def add_threshold_constraint(self, threshold: float, target: int, size: int):
        """Add threshold constraint for average cost"""
        # Average cost over non-target states
        avg_cost = 0
        state_count = 0

        for i in range(size):
            if i != target:
                avg_cost += self.variables['pi'][i]
                state_count += 1

        if state_count > 0:
            avg_cost = avg_cost / state_count
            return [avg_cost <= threshold]
        return []

    def solve_with_benchmark(self, budget: int, target: int, size: int,
                           threshold: float, det: int) -> BenchmarkResult:
        """Solve POMDP with comprehensive benchmarking"""

        # Setup phase timing
        setup_start = time.perf_counter()
        process = psutil.Process()
        mem_before = process.memory_info().rss

        # Create variables and constraints
        self.create_variables(budget, target, size)

        all_constraints = []
        all_constraints.extend(self.add_basic_constraints(target, size))
        all_constraints.extend(self.add_strategy_constraints(budget, det))
        all_constraints.extend(self.add_observation_constraints(budget, target, size))
        all_constraints.extend(self.add_cost_equations(budget, target, size))
        all_constraints.extend(self.add_threshold_constraint(threshold, target, size))

        # Add all constraints to solver
        self.solver.add(all_constraints)

        setup_time = time.perf_counter() - setup_start

        # Solving phase timing
        solve_start = time.perf_counter()
        result = self.solver.check()
        solve_time = time.perf_counter() - solve_start

        # Memory measurement
        mem_after = process.memory_info().rss
        memory_used = mem_after - mem_before

        # Get model if satisfiable
        model = self.solver.model() if result == sat else None

        return BenchmarkResult(
            solve_time=solve_time,
            setup_time=setup_time,
            memory_used=memory_used,
            result=result,
            model=model,
            constraint_count=len(all_constraints)
        )

def benchmark_line_pomdp(budget: int, target: int, size: int,
                        threshold: float, det: int, runs: int = 1) -> list:
    """Run multiple benchmark runs for statistical significance"""
    results = []

    for run in range(runs):
        solver = LinePOMDPSolver()
        result = solver.solve_with_benchmark(budget, target, size, threshold, det)
        results.append(result)

        # Clean up context
        del solver
        gc.collect()

    return results

# Example usage matching your original function signature
def solve_line_constrained(budget: int, target: int, size: int, threshold: str, det: int):
    """Drop-in replacement for create_line_constrained with direct solving"""
    solver = LinePOMDPSolver()
    result = solver.solve_with_benchmark(budget, target, size, float(threshold), det)

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

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 6:
        size = int(sys.argv[1])
        target = int(sys.argv[2])
        budget = int(sys.argv[3])
        threshold = sys.argv[4]
        det = int(sys.argv[5])

        solve_line_constrained(budget, target, size, threshold, det)