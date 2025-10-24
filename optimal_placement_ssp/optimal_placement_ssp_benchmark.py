from enum import Enum
from itertools import combinations
from multiprocessing.shared_memory import SharedMemory

from z3 import *

# Hyperparameters
NUM_STATES = 11
GOAL_STATE = 5
BUDGET = (NUM_STATES - 1)//2 - 1
PLACEMENTS = list(combinations([i for i in range(NUM_STATES) if i != GOAL_STATE], BUDGET))

BIN_SEARCH_LOW = 4.0
BIN_SEARCH_HIGH = 4.4

actions = ['l', 'r']
TIMEOUT_MS = 3000

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
            X[idx][1] == int(state < GOAL_STATE),
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
    constraints.append(Sum([PI[s] for s in range(NUM_STATES) if s!=GOAL_STATE])/(NUM_STATES - 1) < threshold)

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

def solve(shared_memory_name: str, states_on: list[int], threshold: ArithRef, pid: int, timeout_ms: int) -> None:
    print(f"Solving for {instance(states_on, threshold)}")
    constraints = build_constraints(states_on, threshold)

    solver = Solver()
    solver.add(constraints)
    result = wrap_timeout_check(solver, timeout_ms)
    result = Result.SAT if result == sat \
        else Result.UNSAT if result == unsat \
        else Result.UNKNOWN

    if result == Result.SAT:
        print(f"\tSAT for {instance(states_on, threshold)}")

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
    print(f"Searching for the optimal placement among {len(PLACEMENTS)} placements:")
    shared_memory = None
    try:
        # Create shared memory for each process to write its result
        shared_memory = SharedMemory(create=True, size=len(PLACEMENTS))
        buffer = shared_memory.buf[:len(PLACEMENTS)]

        max_iterations = 10
        low = BIN_SEARCH_LOW
        high = BIN_SEARCH_HIGH
        placements_to_ignore = set()
        timeout_ms = TIMEOUT_MS

        for i in range(max_iterations):
            buffer[:len(PLACEMENTS)] = bytearray([0]*len(PLACEMENTS))

            threshold = (low + high) / 2
            print(f"Iteration {i + 1}: \u03C4 = {threshold}, timeout={timeout_ms}ms")

            for (p, placement) in enumerate(PLACEMENTS):
                if p not in placements_to_ignore:
                    solve(shared_memory.name, placement, threshold, p, timeout_ms)

            sats = [r for r, result in enumerate(buffer) if result == Result.SAT.value]
            unsats = [r for r, result in enumerate(buffer) if result == Result.UNSAT.value]
            unknowns = [result for result in buffer if result != Result.SAT.value and result != Result.UNSAT.value]
            print(f"SATs: {len(sats)}, UNSATs: {len(unsats)}, UNKNOWNs: {len(unknowns)}")

            if i == 1:
                placements_to_ignore = set(unsats)
            else:
                if len(sats) > 0:
                    [placements_to_ignore.add(r) for r in unsats]
            if 0 < len(sats) <= 2:
                if len(unknowns) > 0:
                    # Try again to solve/refute the unknown instances with more time
                    timeout_ms = 1.5*timeout_ms
                else:
                    for p in sats:
                        print(f"The optimal sensor placement is ({", ".join([f"@s{s}" for s in PLACEMENTS[p]])})")
                        break
            elif len(sats) > 2:
                print(f"{len(sats)} SAT(s) found, decreasing threshold")
                high = threshold
            elif len(sats) == 0:
                print("No SATs, increasing threshold")
                low = threshold
    except Exception as e:
        print(f"Error in benchmark: {e}")
        pass
    finally:
        if shared_memory is not None:
            shared_memory.unlink()

if __name__ == "__main__":
    benchmark()