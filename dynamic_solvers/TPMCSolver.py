import gc
import time

from z3 import set_option, Solver, unsat, sat, Context

from dynamic_solvers.BenchmarkResult import BenchmarkResult
from dynamic_solvers.builders.OOPSpec import OOPSpec


class TPMCSolver:
    def __init__(self, verbose: bool):
        self.solver = None
        self.verbose = verbose

        self.file_rewards = None
        self.file_results = None

    def reset(self, ctx: Context):
        """Reset for fresh solving context"""
        gc.collect()
        self.solver = Solver(ctx=ctx)

    def set_options(self, result_path: str, reward_path: str, timeout: int):
        set_option(max_args=1000000, max_lines=100000000)
        self.file_results = open(result_path, "w")
        self.file_rewards = open(reward_path, "w")
        self.solver.set("timeout", timeout)
        return

    def solve(self, tpmc: OOPSpec, threshold: str, determinism: bool) -> BenchmarkResult:
        tpmc.declare_variables()
        tpmc_constraints = tpmc.collect_constraints(threshold, determinism)
        self.solver.add(tpmc_constraints)

        if self.verbose:
            print("⚡ Solving...")

        # Solving phase timing for benchmarks
        solve_start = time.perf_counter()
        result = self.solver.check()
        solve_end = time.perf_counter()
        solve_time = solve_end - solve_start

        print()
        model = None
        reward = None
        if result == sat:
            print(' ✅  Solution found!')
            model = self.solver.model()
            reward = model.eval(tpmc.exp_rew_evaluator)
            self.file_results.write(str(model))
            self.file_rewards.write(str(reward))
        elif result == unsat:
            print(' ❌  No solution!')
            self.file_rewards.write('N/A')
        else:
            print(' ❔  Unknown!')

        self._cleanup()

        return BenchmarkResult(
            solve_time=solve_time,
            result=result,
            reward=reward,
            model=model
        )

    def _cleanup(self):
        if self.file_results:
            self.file_results.close()
        if self.file_rewards:
            self.file_rewards.close()

        # Clean up Z3 objects
        del self.solver
        gc.collect()
