import gc
import time

from z3 import (set_option, Solver, Context,
                unsat, sat, unknown)

from dynamic_solvers.ResultOOP import ResultOOP
from dynamic_solvers.builders.OOPSpec import OOPSpec


class TPMCSolver:
    solver: Solver
    verbose: bool

    def __init__(self, ctx: Context, verbose: bool):
        self.verbose = verbose
        self.solver = Solver(ctx=ctx)
        # Set global Z3 options (call once per solver instance)
        set_option(max_args=1000000, max_lines=100000000)

    def set_timeout(self, timeout_ms: int):
        """Set solver-specific timeout."""
        self.solver.set("timeout", timeout_ms)
        return

    def wrap_timeout_check(self, timeout_ms: int):
        import threading
        result = []

        def check_wrapper():
            try:
                result.append(self.solver.check())
            except:
                result.append(unknown)

        thread = threading.Thread(target=check_wrapper, daemon=True)
        thread.start()
        thread.join(timeout_ms / 1000.0)

        if thread.is_alive():
            # Signal Z3 to interrupt its computation
            try:
                self.solver.interrupt()
                thread.join(timeout=5.0)  # Give Z3 time to cleanup gracefully
            except:
                del thread
                pass  # If interrupt fails, daemon thread won't block process exit
            return unknown

        return result[0] if len(result) > 0 else unknown

    def solve(self, tpmc: OOPSpec, threshold: str, timeout_ms: int) -> ResultOOP:
        tpmc.declare_variables()
        tpmc_constraints = tpmc.collect_constraints(threshold)
        self.solver.add(tpmc_constraints)

        if self.verbose:
            print(" ⚡  Solving...")
            print()

        # Solving phase timing for benchmarks (CPU time)
        cpu_start = time.process_time()
        result = self.wrap_timeout_check(timeout_ms)
        cpu_end = time.process_time()
        solve_time = cpu_end - cpu_start

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

        self.cleanup()

        return ResultOOP(
            solve_time=solve_time,
            result=result,
            reward=reward,
            model=model
        )

    def cleanup(self):
        """Clean up Z3 objects."""
        if self.solver is not None:
            del self.solver
            self.solver = None
        gc.collect()
