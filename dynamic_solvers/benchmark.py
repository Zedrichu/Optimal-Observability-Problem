"""
Benchmarking unit for executing OOP problem instances.
Leverages existing dynamic_solvers classes for robust execution.
"""

import csv
import sys
import argparse
import os
import tempfile
from typing import List, Dict, Any
from dataclasses import dataclass

from halo import Halo

from dynamic_solvers.TPMCSolver import TPMCSolver
from dynamic_solvers.builders.TPMCFactory import TPMCFactory, variant_from_string, puzzle_from_string
from dynamic_solvers.ResultTPMC import ResultTPMC

TIMEOUT = 90000

@dataclass
class BenchmarkConfig(argparse.Namespace):
    """Configuration for a single benchmark instance."""
    variant: str
    world: str
    budget: int
    goal: int
    threshold: str
    length: int = None
    width: int = None
    height: int = None
    deterministic: bool = False
    timeout: int = TIMEOUT


class BenchmarkRunner:
    """Benchmarking unit using existing dynamic_solvers infrastructure."""

    def __init__(self, output_csv: str = "benchmark_results.csv"):
        self.output_csv = output_csv
        self.results: List[Dict[str, Any]] = []
        self.temp_dir = tempfile.mkdtemp()

    def load_configurations_from_csv(self, csv_file: str) -> List[BenchmarkConfig]:
        """Load benchmark configurations from CSV."""
        configs = []

        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)

            for row_num, row in enumerate(reader, start=2):
                try:
                    config = BenchmarkConfig(
                        variant=row['variant'].strip().lower(),
                        world=row['world'].strip().lower(),
                        budget=int(row['budget']),
                        goal=int(row['goal']),
                        threshold=row['threshold'].strip(),
                        length=int(row['length']) if row.get('length', '').strip() else None,
                        width=int(row['width']) if row.get('width', '').strip() else None,
                        height=int(row['height']) if row.get('height', '').strip() else None,
                        deterministic=row.get('deterministic', '').strip().lower() in ['true', '1', 'yes'],
                        timeout=int(row.get('timeout', str(TIMEOUT))),
                    )
                    configs.append(config)

                except (ValueError, KeyError) as e:
                    print(f"⚠️  Warning: Skipping invalid row {row_num}: {e}")

        return configs

    def _create_model_description(self, config: BenchmarkConfig) -> str:
        """Create model description like L(9), G(24), M(39)."""
        if config.world == 'line':
            return f"L({config.length})"
        elif config.world == 'grid':
            return f"G({config.width}x{config.height})"
        elif config.world == 'maze':
            return f"M({config.width}x{config.height})"
        return f"{config.world.upper()}(?)"

    def _build_command_args(self, config: BenchmarkConfig, results_file: str, rewards_file: str) -> List[str]:
        """Build command line arguments for the run.py script."""
        args = [
            sys.executable, self.run_script,
            config.variant, config.world,
            "--budget", str(config.budget),
            "--goal", str(config.goal),
            "--threshold", config.threshold,
            "--results", results_file,
            "--rewards", rewards_file,
            "--timeout", str(config.timeout)
        ]

        # Add dimension arguments based on world type
        if config.world == 'line' and config.length is not None:
            args.extend(["--length", str(config.length)])
        elif config.world in ['grid', 'maze']:
            if config.width is not None:
                args.extend(["--width", str(config.width)])
            if config.height is not None:
                args.extend(["--height", str(config.height)])

        # Add deterministic flag if needed
        if config.deterministic:
            args.append("--deterministic")

        return args

    @Halo(text=f"Solving instance", spinner="dots", color="green")
    def run_single_benchmark(self, config: BenchmarkConfig) -> Dict[str, Any]:
        """Run a single benchmark using dynamic_solvers classes."""
        model_desc = self._create_model_description(config)
        print(f"🚀 Running: {model_desc} - Budget: {config.budget}, Threshold: {config.threshold}")

        # Create temporary output files
        results_file = os.path.join(self.temp_dir, f"results_{len(self.results)}.txt")
        rewards_file = os.path.join(self.temp_dir, f"rewards_{len(self.results)}.txt")

        try:
            # Convert strings to enums using existing functions
            variant = variant_from_string(config.variant)
            world = puzzle_from_string(config.world)

            # Create TPMC instance using existing factory
            tpmc_instance = TPMCFactory.create(variant, world,
                                                   length = config.length,
                                                    width = config.width,
                                                   height = config.height,
                                                     goal = config.goal,
                                                   budget = config.budget,
                                                threshold = config.threshold )

            # Create a solver and configure
            solver = TPMCSolver(verbose=False)
            solver.reset(tpmc_instance.ctx)
            solver.set_options(results_file, rewards_file, config.timeout)

            # # Build command
            # cmd_args = self._build_command_args(config, results_file, rewards_file)
            #
            # try:
            #     # Execute subprocess with timeout
            #     start_time = time.perf_counter()
            #
            #     result = subprocess.run(
            #         cmd_args,
            #         timeout=config.timeout / 1000.0,  # Convert ms to seconds
            #         capture_output=True,
            #         text=True,
            #         cwd=os.path.dirname(__file__)
            #     )
            #
            #     end_time = time.perf_counter()
            #     solve_time = end_time - start_time
            #
            #     # Parse output to determine status
            #     if result.returncode == 0:
            #         # Success - parse output for timing info
            #         stdout_lines = result.stdout.strip().split('\n')
            #         actual_solve_time = self._extract_solve_time_from_output(stdout_lines)
            #         if actual_solve_time is not None:
            #             solve_time = actual_solve_time

            # Run solver execution on the current tpMC instance
            result: ResultTPMC = solver.solve(tpmc_instance, config.threshold, config.deterministic)

            # Determine result status
            if result.result.r == 1:  # sat
                result_status = "SAT"
            elif result.result.r == -1:  # unsat
                result_status = "UNSAT"
            else:  # unknown
                result_status = "UNKNOWN"

            benchmark_result = {
                'model': model_desc,
                'threshold': config.threshold,
                'budget': config.budget,
                'time': result.solve_time if result.solve_time < config.timeout/1000.0 else -1.0,
                'reward': result.reward,
                'status': result_status,
                'error': None
            }

            print(f"✅ Completed in {result.solve_time:.4f}s - Status: {result_status}, Reward: {result.reward}")
            return benchmark_result

        except Exception as e:
            error_msg = str(e)
            print(f"❌ Error: {error_msg}")

            return {
                'model': model_desc,
                'threshold': config.threshold,
                'budget': config.budget,
                'time': None,
                'reward': "N/A",
                'status': "ERROR",
                'error': error_msg
            }

    def run_benchmarks(self, configs: List[BenchmarkConfig]) -> None:
        """Run all benchmark configurations."""
        print(f"🎯 Starting benchmark run with {len(configs)} configurations")

        for i, config in enumerate(configs, 1):
            print(f"\n📊 Progress: {i}/{len(configs)}")
            result = self.run_single_benchmark(config)
            self.results.append(result)

        print(f"\n🏁 Benchmark run completed! Results will be saved to: {self.output_csv}")

    def save_results_to_csv(self) -> None:
        """Save benchmark results to CSV file."""
        with open(self.output_csv, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write headers
            writer.writerow(['Model', 'Threshold', 'Budget', 'Time (s)', 'Reward', 'Status', 'Description', 'Error'])

            # Write results
            for result in self.results:
                writer.writerow([
                    result['model'],
                    result['threshold'],
                    result['budget'],
                    f"{result['time']:.6f}" if result['time'] and result['time'] > 0 else "t.o.",
                    result['reward'],
                    result['status'],
                    result['error'] or ""
                ])

    def cleanup(self) -> None:
        """Clean up temporary files."""
        import shutil
        try:
            shutil.rmtree(self.temp_dir)
        except Exception:
            pass


def main():
    """Main entry point for the benchmark runner."""
    parser = argparse.ArgumentParser(
        description="Benchmark runner for OOP problem instances",
        epilog="Example: python3 benchmark.py config.csv --output results.csv"
    )

    parser.add_argument('config_csv', nargs='?', help='CSV file with benchmark configurations')
    parser.add_argument('--output', '-o', default='benchmark_results.csv', help='Output CSV file')

    args = parser.parse_args()

    try:

        if not args.config_csv:
            parser.print_help()
            sys.exit(1)

        if not os.path.exists(args.config_csv):
            print(f"❌ Configuration file not found: {args.config_csv}")
            sys.exit(1)

        # Run benchmarks
        runner = BenchmarkRunner(args.output)

        try:
            configs = runner.load_configurations_from_csv(args.config_csv)

            if not configs:
                print("❌ No valid configurations found")
                sys.exit(1)

            runner.run_benchmarks(configs)
            runner.save_results_to_csv()

        finally:
            runner.cleanup()

    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
