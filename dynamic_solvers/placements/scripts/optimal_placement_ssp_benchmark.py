import time
from enum import Enum
from itertools import combinations

from z3 import *


# Hyperparameters
NUM_STATES = 15
GOAL_STATE = (NUM_STATES - 1)//2
BUDGET = min(GOAL_STATE, NUM_STATES - 1 - GOAL_STATE)

BIN_SEARCH_LOW = BUDGET//2
BIN_SEARCH_HIGH = NUM_STATES

PLACEMENTS = list(combinations([i for i in range(NUM_STATES) if i != GOAL_STATE], BUDGET))

actions = ['l', 'r']

class Result(Enum):
    SAT = 1
    UNSAT = 2
    UNKNOWN = 3

def instance(states_on: Iterable[int], threshold: ArithRef | float) -> str:
    states_on = ", ".join([f"@s{state_on}" for state_on in states_on])
    return f"SSP with ({states_on}) and τ <= {threshold}"

def navigate(state: int, action: str) -> int:
    if action == 'l':
        return max(0, state - 1)
    elif action == 'r':
        return min(NUM_STATES - 1, state + 1)
    else:
        raise ValueError("Invalid action")

def build_constraints(states_on: list[int], threshold: ArithRef | float):
    constraints = []

    # Variables
    PI = [Real(f"pi{i}") for i in range(NUM_STATES)]
    X = [[Real(f"xo{i}{a}") for a in actions] for i in states_on]
    X.append([Real(f"xo⊥{a}") for a in actions])

    # Strategy constraints & Bellman equation for states with sensor ON
    for s, state in enumerate(states_on):
        constraints.extend([
            X[s][0] == int(state > GOAL_STATE),
            X[s][1] == int(state < GOAL_STATE),
            PI[state] == 1 + Sum([X[s][a] * PI[navigate(state, act)] for (a, act) in enumerate(actions)])
        ])

    # Strategy constraints for default/unknown strategy
    constraints.extend([bound for rate in X[-1] for bound in [rate <= 1, rate >= 0]])
    constraints.append(Sum(X[-1]) == 1)

    # Bellman equations for goal state and states with sensor OFF
    constraints.append(PI[GOAL_STATE] == 0)
    constraints.extend([
        PI[s] == 1 + Sum([X[-1][a] * PI[navigate(s, act)] for (a, act) in enumerate(actions)])
        for s in range(NUM_STATES) if s not in states_on and s != GOAL_STATE
    ])

    # Fully observable constraints
    constraints.extend([PI[state] >= abs(state - GOAL_STATE) for state in range(NUM_STATES) if state != GOAL_STATE])

    # Threshold constraint
    constraints.append(Sum([PI[s] for s in range(NUM_STATES) if s!=GOAL_STATE])/(NUM_STATES - 1) <= threshold)

    return constraints

def solve(states_on: list[int], threshold: ArithRef) -> Result:
    # print(f"Solving for {instance(states_on, threshold)}")
    constraints = build_constraints(states_on, threshold)

    solver = Solver()
    solver.add(constraints)
    result = solver.check()
    result = Result.SAT if result == sat \
        else Result.UNSAT if result == unsat \
        else Result.UNKNOWN

    # if result == Result.SAT:
        # print(f"\tSAT for {instance(states_on, threshold)}")

    return result

def benchmark():
    placements_to_ignore = set()

    max_iterations = 100
    tolerance = 1e-15
    low = BIN_SEARCH_LOW
    high = BIN_SEARCH_HIGH

    for i in range(max_iterations):
        print()
        threshold = (low + high) / 2
        print(f"Iteration {i + 1}: \u03C4 = {threshold} (low = {low}, high = {high})")

        sats, unsats, unknowns = [], [], []
        for (p, placement) in enumerate(PLACEMENTS):
            if p not in placements_to_ignore:
                result = solve(placement, threshold)
                if result == Result.SAT:
                    sats.append(p)
                elif result == Result.UNSAT:
                    unsats.append(p)
                else:
                    unknowns.append(p)
        print(f"SATs: {len(sats)}, UNSATs: {len(unsats)}, UNKNOWNs: {len(unknowns)}")

        if i == 0:
            if len(sats) == 0:
                print("No solutions found in first search. Try again with a larger BIN_SEARCH_LOW value.")
                return
            else:
                placements_to_ignore = set(unsats)
        else:
            if len(sats) > 0:
                [placements_to_ignore.add(r) for r in unsats]
        if len(sats) == 0:
            # print("No SATs, increasing threshold.")
            low = threshold
        elif len(sats) == 1:
            print(f"The optimal sensor placement is ({", ".join([f"@s{s}" for s in PLACEMENTS[sats[0]]])})")
            break
        elif len(sats) == 2 and GOAL_STATE == (NUM_STATES - 1)//2:
            print(f"The optimal sensor placement is ({", ".join([f"@s{s}" for s in PLACEMENTS[sats[0]]])})")
            print(f"The optimal sensor placement is ({", ".join([f"@s{s}" for s in PLACEMENTS[sats[1]]])})")
            return
        elif len(sats) > 1:
            # print(f"{len(sats)} SAT(s) found, decreasing threshold.")
            high = threshold
        if high - low < tolerance:
            print(f"The search bounds of the binary search have converged.")
            return

## TO BENCHMARK FOR VARYING GOAL POSITION AND BUDGETS, UNCOMMENT BELOW
# if __name__ == "__main__":
#     import sys
#     sys.stdout = open("output.txt", "a")
#     for GOAL_STATE in range((NUM_STATES - 1)//2, 1, -1):
#         for BUDGET in range(GOAL_STATE, 0, -1):
#             PLACEMENTS = list(combinations([i for i in range(NUM_STATES) if i != GOAL_STATE], BUDGET))
#             BIN_SEARCH_LOW = 1
#             BIN_SEARCH_HIGH = 100
#
#             print(f"NUM_STATES={NUM_STATES} | GOAL_STATE={GOAL_STATE} | BUDGET={BUDGET} | PLACEMENTS={len(PLACEMENTS)}", file=sys.stderr)
#
#             print("#####################################################")
#             print("Running benchmark with the following hyperparameters:")
#             print(f"NUM_STATES={NUM_STATES}, GOAL_STATE={GOAL_STATE}, BUDGET={BUDGET}")
#             print(f"BIN_SEARCH_LOW={BIN_SEARCH_LOW}, BIN_SEARCH_HIGH={BIN_SEARCH_HIGH}")
#             print(f"PLACEMENTS={len(PLACEMENTS)}")
#
#             start_time = time.process_time()
#             benchmark()
#             end_tme = time.process_time()
#             print()
#
#             print(f"Benchmarked in {(end_tme - start_time):.2f}s")
#             print("Ran benchmark with the following hyperparameters:")
#             print(f"NUM_STATES={NUM_STATES}, GOAL_STATE={GOAL_STATE}, BUDGET={BUDGET}")
#             print(f"BIN_SEARCH_LOW={BIN_SEARCH_LOW}, BIN_SEARCH_HIGH={BIN_SEARCH_HIGH}")
#             print(f"PLACEMENTS={len(PLACEMENTS)}")
#             print()

if __name__ == "__main__":
    print("Running benchmark with the following hyperparameters:")
    print(f"NUM_STATES={NUM_STATES}, GOAL_STATE={GOAL_STATE}, BUDGET={BUDGET}")
    print(f"BIN_SEARCH_LOW={BIN_SEARCH_LOW}, BIN_SEARCH_HIGH={BIN_SEARCH_HIGH}")
    print(f"PLACEMENTS={len(PLACEMENTS)}")

    start_time = time.process_time()
    benchmark()
    end_tme = time.process_time()
    print()

    print(f"Benchmarked in {(end_tme - start_time):.2f}s")
    print("Ran benchmark with the following hyperparameters:")
    print(f"NUM_STATES={NUM_STATES}, GOAL_STATE={GOAL_STATE}, BUDGET={BUDGET}")
    print(f"BIN_SEARCH_LOW={BIN_SEARCH_LOW}, BIN_SEARCH_HIGH={BIN_SEARCH_HIGH}")
    print(f"PLACEMENTS={len(PLACEMENTS)}")