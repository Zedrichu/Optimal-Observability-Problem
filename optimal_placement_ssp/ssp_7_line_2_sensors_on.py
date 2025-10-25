import re
import time

from z3 import *
from optimal_placement_ssp.optimal_placement_ssp_benchmark import GOAL_STATE, NUM_STATES, build_constraints, \
     instance, BIN_SEARCH_LOW, BIN_SEARCH_HIGH

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sensor_on.py <states_on> (comma-separated)")
        sys.exit(1)

    states_on = list(map(int, sys.argv[1].split(",")))
    for state in states_on:
        if state == GOAL_STATE:
            raise ValueError("Cannot place sensor on goal state")
        if state < 0 or state >= NUM_STATES:
            raise ValueError(f"Sensor must be in a valid state (0 to {NUM_STATES})")

    max_iterations = 100
    tolerance = 1e-15
    low = BIN_SEARCH_LOW
    high = BIN_SEARCH_HIGH

    strategies = {}
    thresholds = []
    model = None

    for i in range(max_iterations):
        threshold = (low + high) / 2
        thresholds.append(threshold)

        solver = Solver()
        constraints = build_constraints(states_on, threshold)
        solver.add(constraints)
        start_time = time.process_time()
        result = solver.check()
        end_time = time.process_time()

        if result == sat:
            print(f"Iteration {str(i + 1).rjust(2)}:   SAT for {instance(states_on, threshold)}")
            # Collect strategy for this iteration
            strategy = []
            model = solver.model()
            for d in model.decls():
                if "xo⊥" in d.name():
                    strategy.append((d.name(), model[d]))
            strategies[i] = sorted(strategy, key=lambda s: s[0])
            high = threshold
        elif result == unsat:
            print(f"Iteration {str(i + 1).rjust(2)}: UNSAT for {instance(states_on, threshold)}")
            low = threshold
        if high - low < tolerance:
            break

    print()
    for (i, strategy) in strategies.items():
        terms = [list(map(int, re.findall(r"\d+", str(strategy[a][1])))) for a in range(len(strategy))]
        strategy_strings = []
        for j, term in enumerate(terms):
            action_rate_var = strategy[j][0]
            action_rate_strat = terms[j][0]/terms[j][1] if len(terms) > 1 else terms[j][0]
            strategy_strings += [f"{action_rate_var} = {action_rate_strat}"]
        print(f"Strategy for iteration {i} (τ < {thresholds[i]}): {" | ".join(strategy_strings)}")
    print(f"The optimal sensor threshold is approximately {thresholds[max(strategies.keys())]} ± {tolerance}")
    print()
    if model is not None:
        print("Model for the latest (most refined) strategy:")
        for d in sorted(model.decls(), key=lambda x: x.name()):
            print(f"{d.name().rjust(6)}: {model[d]}")