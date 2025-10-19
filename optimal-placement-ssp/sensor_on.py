import time

from z3 import *
from dynamic_solvers.utils import parse_threshold


NUM_STATES = 7
GOAL_STATE = 3
actions = ['l', 'r']

def navigate(state: int, action: str) -> int:
    if action == 'l':
        return max(0, state - 1)
    elif action == 'r':
        return min(NUM_STATES - 1, state + 1)
    else:
        raise ValueError("Invalid action")

def build_constraints(states_on: list[int], threshold: ArithRef):
    constraints = []

    # Variables
    PI = [Real(f"pi{i}") for i in range(NUM_STATES)]
    Y = [Bool(f"y{i}") for i in range(NUM_STATES) if i != GOAL_STATE]
    X = [[Real(f"xo{i}{a}") for a in actions] for i in range(NUM_STATES) if i != GOAL_STATE]
    X.append([Real(f"xo⊥{a}") for a in actions])

    # Experiment constraints
    # We know what the optimal strategy is for states with sensors
    for state in states_on:
        idx = state if state < GOAL_STATE else state - 1
        constraints.extend([
            Y[idx] == True,
            X[idx][0] == int(state > GOAL_STATE),
            X[idx][1] == int(state < GOAL_STATE)
        ])

    # Fully observable constraints
    constraints.extend([PI[state] >= abs(state - GOAL_STATE) for state in range(NUM_STATES)])

    # Bellman equations
    for i in range(NUM_STATES):
        if i == GOAL_STATE:
            constraints.append(PI[i] == 0)
            continue

        obs = i if i < GOAL_STATE else i - 1
        constraints.append(Implies(Y[obs], PI[i] == 1 + Sum([X[obs][a] * PI[navigate(i, act)] for (a, act) in enumerate(actions)])))
        constraints.append(Implies(Not(Y[obs]), PI[i] == 1 + Sum([X[-1][a] * PI[navigate(i, act)] for (a, act) in enumerate(actions)])))

    # Threshold constraint
    constraints.append(Sum([PI[s] for s in range(NUM_STATES) if s!=GOAL_STATE])/(NUM_STATES - 1) <= threshold)

    # Strategy constraints
    for strategy in X:
        constraints.extend([bound for rate in strategy for bound in [rate <= 1, rate >= 0]])
        constraints.append(Sum(strategy) == 1)

    # Budget constraint
    constraints.append(PbEq([(y, 1) for y in Y], len(states_on)))

    return constraints


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python sensor_on.py <state_on_1> <state_on_2> <threshold>")
        sys.exit(1)

    states_on = list(map(int, sys.argv[1:3]))
    for state in states_on:
        if state == GOAL_STATE:
            raise ValueError("Cannot place sensor on goal state")
        if state < 0 or state >= NUM_STATES:
            raise ValueError(f"Sensor must be in a valid state (0 to {NUM_STATES})")

    terms, sign = parse_threshold(sys.argv[3])
    threshold = Q(terms[0], terms[1]) if len(terms) > 1 else terms[0]

    constraints = build_constraints(states_on, threshold)
    for constraint in constraints:
        print(str(constraint).replace('\n', '').replace('  ', ''))

    solver = Solver()
    solver.add(constraints)

    start_time = time.process_time()
    result = solver.check()
    end_time = time.process_time()

    print(f"Solving time: {(end_time - start_time):.4f} seconds")
    print(f"Result: {result}")
    if result == sat:
        model = solver.model()
        '''
        The goal of this experiment is to search for a sensor selection of size 2 that solves
        the optimization problem with the lowest threshold. It is therefore not necessary to
        find the optimal threshold, but rather to find a selection that achieves the lowest
        threshold compared to the other selections.
        
        TODO:
        1) Create a script that generates all sensor selections of size 2
        2) Assign a worker to each selection
        3) Search for the lowest threshold that still solves the problem for any selection
        4) Workers report back their findings through a shared data structure
        '''