from enum import Enum
from itertools import combinations as combine

from z3 import *


def compute_placements(num_states: int, goal_state: int, budget: int):
    placements = []
    # Add only unique placements (ignore symmetric ones)
    combinations = list(combine([i for i in range(num_states) if i != goal_state], budget))
    for combination in combinations:
        last_sensor = combination[-1]
        if last_sensor < goal_state:
            placements.append(combination)
            continue
        first_sensor = combination[0]
        dist_to_end = num_states - last_sensor - 1
        if first_sensor <= dist_to_end:
            placements.append(combination)
    return placements

# Hyperparameters
NUM_STATES = 21
GOAL_STATE = (NUM_STATES - 1)//2
N = (NUM_STATES - 1)//2
BUDGET = N - 1

if BUDGET < 1:
    print("ERROR: BUDGET must be greater than 1")
    print(f"NUM_STATES={NUM_STATES}, GOAL_STATE={GOAL_STATE}, N={N}, BUDGET={BUDGET}")

    exit(1)

BIN_SEARCH_LOW = N*(N+1)/2/N + (N - BUDGET)
BIN_SEARCH_HIGH = 2*BIN_SEARCH_LOW + (N - BUDGET)

PLACEMENTS = compute_placements(NUM_STATES, GOAL_STATE, BUDGET)

actions = ['l', 'r']

class Result(Enum):
    SAT = 1
    UNSAT = 2
    UNKNOWN = 3

def instance(states_on: Iterable[int], threshold: ArithRef | float) -> str:
    states_on = ", ".join([f"@s{state_on}" for state_on in states_on])
    return f"SSP with ({states_on}) and τ < {threshold}"

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
    constraints.append(Sum([PI[s] for s in range(NUM_STATES) if s!=GOAL_STATE])/(NUM_STATES - 1) < threshold)

    return constraints

def wrap_timeout_check(solver: Solver, timeout_ms: int):
    import threading
    result = []

    def check_wrapper():
        try:
            result.append(solver.check())
        except:
            result.append(unknown)

    thread = threading.Thread(target=check_wrapper, daemon=True)
    thread.start()
    thread.join(timeout_ms / 1000.0)

    if thread.is_alive():
        # Signal Z3 to interrupt its computation
        try:
            solver.interrupt()
            thread.join(timeout=2.0)  # Give Z3 time to cleanup gracefully
        except:
            del thread
            pass  # If interrupt fails, daemon thread won't block process exit
        return unknown

    return result[0] if len(result) > 0 else unknown

def solve(states_on: list[int], threshold: ArithRef) -> Result:
    print(f"Solving for {instance(states_on, threshold)}")
    constraints = build_constraints(states_on, threshold)

    solver = Solver()
    solver.add(constraints)
    result = solver.check()
    result = Result.SAT if result == sat \
        else Result.UNSAT if result == unsat \
        else Result.UNKNOWN

    if result == Result.SAT:
        print(f"\tSAT for {instance(states_on, threshold)}")

    return result

def benchmark():
    print()

    placements_to_ignore = set()

    max_iterations = 100
    tolerance = 1e-15
    low = BIN_SEARCH_LOW
    high = BIN_SEARCH_HIGH

    for i in range(max_iterations):
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
                exit(1)
            else:
                placements_to_ignore = set(unsats)
        else:
            if len(sats) > 0:
                [placements_to_ignore.add(r) for r in unsats]
        if len(sats) == 0:
            print("No SATs, increasing threshold")
            low = threshold
        elif len(sats) == 1:
            print(f"The optimal sensor placement is ({", ".join([f"@s{s}" for s in PLACEMENTS[sats[0]]])})")
            break
        elif len(sats) > 1:
            print(f"{len(sats)} SAT(s) found, decreasing threshold")
            high = threshold
        if high - low < tolerance:
            print(f"The search bounds of the binary search have converged.")
            return

if __name__ == "__main__":
    print("Running benchmark with the following hyperparameters:")
    print(f"NUM_STATES={NUM_STATES}, GOAL_STATE={GOAL_STATE}, N={N}, BUDGET={BUDGET}")
    print(f"BIN_SEARCH_LOW={BIN_SEARCH_LOW}, BIN_SEARCH_HIGH={BIN_SEARCH_HIGH}")
    print(f"PLACEMENTS={len(PLACEMENTS)}")

    benchmark()

    print()
    print("Ran benchmark with the following hyperparameters:")
    print(f"NUM_STATES={NUM_STATES}, GOAL_STATE={GOAL_STATE}, N={N}, BUDGET={BUDGET}")
    print(f"BIN_SEARCH_LOW={BIN_SEARCH_LOW}, BIN_SEARCH_HIGH={BIN_SEARCH_HIGH}")
    print(f"PLACEMENTS={len(PLACEMENTS)}")