import z3
from z3 import *

actions = ['l', 'r']


def navigate(num_states: int, state: int, action: str) -> int:
    if action == 'l':
        return max(0, state - 1)
    elif action == 'r':
        return min(num_states - 1, state + 1)
    else:
        raise ValueError("Invalid action")

def build_constraints(num_states: int, states_on: list[int], goal_state: int, p: float):
    constraints = []

    # Variables
    PI = [Real(f"pi{i}") for i in range(num_states)]
    X = [[Real(f"xo{i}{a}") for a in actions] for i in states_on]
    X.append([Real(f"xo⊥{a}") for a in actions])

    # Strategy constraints & Bellman equation for states with sensor ON
    for s, state in enumerate(states_on):
        constraints.extend([
            X[s][0] == int(state > goal_state),
            X[s][1] == int(state < goal_state),
            PI[state] == 1 + Sum([X[s][a] * PI[navigate(num_states, state, act)] for (a, act) in enumerate(actions)])
        ])

    # Strategy constraints & Bellman equation for states with sensor OFF
    # Probability of going left = p, probability of going right = 1 - p
    constraints.extend([X[-1][0] == p, X[-1][1] == 1 - p])
    constraints.extend([
        PI[s] == 1 + Sum([X[-1][a] * PI[navigate(num_states, s, act)] for (a, act) in enumerate(actions)])
        for s in range(num_states) if s not in states_on and s != goal_state
    ])

    # Bellman equation for goal state
    constraints.append(PI[goal_state] == 0)
    return constraints, PI

def solve(num_states:int, states_on: list[int], goal_state: int, p: float) -> float:
    constraints, PI = build_constraints(num_states=num_states, states_on=states_on, goal_state=goal_state, p=p)

    solver = Solver()
    solver.add(constraints)
    result = solver.check()
    if result == unsat:
        return float("inf")
    model = solver.model()
    return model.eval(Sum(PI)/(len(PI) - 1)).as_decimal(3).replace("?", "")

def main():
    print()

    num_states = 15
    goal_state = 7
    states_on = [1, 3, 5, 6]

    steps = 1001
    print("p ExpRew")
    for p in range(500, steps):
        p = p/(steps - 1)
        ExpRew = solve(num_states, states_on, goal_state, p)
        print(f"{p} {ExpRew}")


if __name__ == "__main__":
    main()