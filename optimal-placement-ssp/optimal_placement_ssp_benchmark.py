from concurrent.futures import ProcessPoolExecutor, as_completed, wait
from enum import Enum
from multiprocessing.shared_memory import SharedMemory

from z3 import *
from dynamic_solvers.utils import parse_threshold

GOAL_STATE = 3
NUM_STATES = 7
PLACEMENTS = [[0, 1], [0, 2], [0, 4], [0, 5], [0, 6], [1, 2], [1, 4], [1, 5], [2, 4]]
actions = ['l', 'r']
TIMEOUT_MS = 3000

class Result(Enum):
    SAT = 1
    UNSAT = 2
    UNKNOWN = 3

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
    # We know the optimal strategy for states with sensors
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

def solve(shared_memory_name: str, states_on: list[int], threshold: ArithRef, pid: int) -> None:
    constraints = build_constraints(states_on, threshold)

    solver = Solver()
    solver.add(constraints)
    result = wrap_timeout_check(solver, TIMEOUT_MS)
    result = Result.SAT if result == sat \
        else Result.UNSAT if result == unsat \
        else Result.UNKNOWN

    shared_memory = None
    try:
        shared_memory = SharedMemory(name=shared_memory_name, create=False)
        shared_memory.buf[pid] = result.value
    except Exception as e:
        print(f"Error in process {pid}: {e}")
    finally:
        if shared_memory is not None:
            shared_memory.close()

def benchmark():
    shared_memory = None
    try:
        # Create shared memory for each process to write its result
        shared_memory = SharedMemory(create=True, size=len(PLACEMENTS))
        buffer = shared_memory.buf[:len(PLACEMENTS)]

        max_iterations = 20
        tolerance = 1e-12
        low = 2.0
        high = 20.0
        UNSATs = []

        for i in range(max_iterations):
            buffer[:len(PLACEMENTS)] = bytearray([0]*len(PLACEMENTS))

            threshold = (low + high) / 2
            print(f"Iteration {i + 1}: \u03C4 = {threshold}")

            for (p, placement) in enumerate(PLACEMENTS):
                if p not in UNSATs:
                    solve(shared_memory.name, placement, threshold, p)

            SATs = [r for r, result in enumerate(buffer) if result == Result.SAT.value]
            UNSATs = [r for r, result in enumerate(buffer) if result == Result.UNSAT.value]

            for r in SATs:
                print(f"SAT for SSP with (@s{PLACEMENTS[r][0]}, @s{PLACEMENTS[r][1]}) and τ: {threshold}")
            if len(SATs) == 1:
                print(f"The optimal sensor placement is (@s{PLACEMENTS[SATs[0]][0]}, @s{PLACEMENTS[SATs[0]][1]})")
                break
            elif len(SATs) > 1:
                print(f"{len(SATs)} SAT(s) found, decreasing threshold")
                high = threshold
            elif len(UNSATs) == len(PLACEMENTS):
                print("All UNSAT, increasing threshold and resetting UNSATs")
                low = threshold
                UNSATs = []
            else:
                print("Inconclusive results, stopping benchmark")
                break
            if high - low < tolerance:
                print("Converged threshold, stopping benchmark")
                break


    except Exception as e:
        print(f"Error in benchmark: {e}")
    finally:
        if shared_memory is not None:
            shared_memory.close()
            shared_memory.unlink()


if __name__ == "__main__":
    benchmark()