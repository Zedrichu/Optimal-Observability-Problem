import gc
import time

from z3 import (set_option, Solver, Context,
                unsat, sat, unknown)

from dynamic_solvers.ResultTPMC import ResultTPMC
from dynamic_solvers.builders.OOPSpec import OOPSpec


class TPMCSolver:
    solver: Solver | None

    def __init__(self, verbose: bool):
        self.solver = None
        self.verbose = verbose

    def reset(self, ctx: Context):
        """Reset for fresh solving context"""
        gc.collect()
        self.solver = Solver(ctx=ctx)

    def set_options(self, timeout_ms: int):
        set_option(max_args=1000000, max_lines=100000000)
        self.solver.set("timeout", timeout_ms)
        return

    def wrap_timeout_check(self, timeout_ms: int):
        import threading
        result = []

        thread = threading.Thread(target=lambda : result.append(self.solver.check()))
        thread.daemon = False
        thread.start()
        thread.join(timeout_ms / 1000.0)

        if thread.is_alive():
            return unknown

        return result[0] if len(result) > 0 else unknown

    def solve(self, tpmc: OOPSpec, threshold: str, timeout_ms: int) -> ResultTPMC:
        tpmc.declare_variables()
        tpmc_constraints = tpmc.collect_constraints(threshold)
        self.solver.add(tpmc_constraints)

        if self.verbose:
            print(" ⚡  Solving...")
            print()

        # Solving phase timing for benchmarks
        solve_start = time.process_time()
        result = self.wrap_timeout_check(timeout_ms)
        solve_end = time.process_time()
        solve_time = solve_end - solve_start

        model = None
        reward = None
        if result == sat:
            if self.verbose:
                print(' ✅  Solution found!')
            model = self.solver.model()
            reward = model.eval(tpmc.exp_rew_evaluator)
        elif result == unsat:
            if self.verbose:
                print(' ❌  No solution!')
        else:
            if self.verbose:
                print(' ❔  Unknown!')

        self._cleanup()

        return ResultTPMC(
            solve_time=solve_time,
            result=result,
            reward=reward,
            model=model
        )

    def _cleanup(self):
        # Clean up Z3 objects
        del self.solver
        gc.collect()
