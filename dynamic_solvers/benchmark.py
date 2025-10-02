"""
Benchmarking unit for executing OOP problem instances.
Leverages existing dynamic_solvers classes for robust execution.
"""

import csv
import gc
import sys
import argparse
import os
import tempfile
from contextlib import nullcontext

from alive_progress import alive_bar
from typing import List, Dict, Any
from dataclasses import dataclass

from halo import Halo

from dynamic_solvers.TPMCSolver import TPMCSolver
from dynamic_solvers.builders.TPMCFactory import TPMCFactory, variant_from_string, puzzle_from_string
from dynamic_solvers.ResultTPMC import ResultTPMC

TIMEOUT = 90000

def is_docker_environment():
    """Check if running in Docker container."""
    return (
        os.path.exists('/.dockerenv') or
        os.environ.get('DOCKER_CONTAINER') == 'true' or
        not sys.stdout.isatty()
    )

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

    def __init__(self, output_csv: str = "benchmark_results.csv", verbose: bool = False):
        self.output_csv = output_csv
        self.results: List[Dict[str, Any]] = []
        self.verbose = verbose

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
                    print(f"⚠️  Warning: Skipping invalid row {row_num} in {csv_file}: {e}")

        return configs

    def load_all_csv_configurations(self, csv_files: List[str]) -> List[BenchmarkConfig]:
        """Load benchmark configurations from multiple CSV files consecutively."""
        all_configs = []

        for csv_file in csv_files:
            if self.verbose:
                print(f"📂 Loading configurations from: {csv_file}")

            configs = self.load_configurations_from_csv(csv_file)
            all_configs.extend(configs)

            if self.verbose:
                print(f"   Loaded {len(configs)} configurations from {csv_file}")

        return all_configs

    def _create_model_description(self, config: BenchmarkConfig) -> str:
        """Create model description like L(9), G(24), M(39)."""
        if config.world == 'line':
            return f"L({config.length})"
        elif config.world == 'grid':
            return f"G({config.width}x{config.height})"
        elif config.world == 'maze':
            return f"M({config.width}x{config.height})"
        return f"{config.world.upper()}(?)"

    def run_single_benchmark(self, config: BenchmarkConfig) -> Dict[str, Any]:
        """Run a single benchmark using dynamic_solvers classes."""
        model_desc = self._create_model_description(config)

        instance_text = f"{config.variant.upper()} instance {model_desc} w/ B: {config.budget}; τ: '{config.threshold}'"
        halo = Halo(text=f"Running ... {instance_text}", spinner="dots12", color="magenta")
        if self.verbose:
            halo.start()
            # halo.info(instance_text)

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
            solver.set_options(config.timeout)

            # Run solver execution on the current tpMC instance
            result: ResultTPMC = solver.solve(tpmc_instance, config.threshold, config.deterministic, config.timeout)

            # Determine result status
            if result.result.r == 1:  # sat
                result_status = "SAT"
            elif result.result.r == -1:  # unsat
                result_status = "UNSAT"
            else:  # unknown
                result_status = "UNKNOWN"

            benchmark_result = {
                'variant': config.variant,
                'model': model_desc,
                'threshold': config.threshold,
                'budget': config.budget,
                'time': result.solve_time if result.solve_time < config.timeout/1000.0 else -1.0,
                'reward': result.reward,
                'status': result_status,
                'error': None
            }

            if benchmark_result['time'] > 0:
                time_print = f"{benchmark_result['time']:.4f}s"
                timeout = False
            else:
                time_print = "TIMEOUT"
                timeout = True

            if self.verbose:
                # Clear out the spinner text if needed
                # sys.stdout.write('\033[1A')  # Move up
                sys.stdout.write('\033[2K')  # Clear line
                sys.stdout.write('\r')  # Move to the beginning
                sys.stdout.flush()

                halo_message = (f"{"Timed-out" if timeout else " Solved"}: {instance_text} "
                                f"| Time: {time_print} "
                                f"| Satisfiability: {result_status} "
                                f"| Reward: {result.reward if result.reward is not None else "N/A"}\n")

                if timeout:
                    halo.stop_and_persist("⌛", halo_message)
                else:
                    halo.succeed(halo_message)

            return benchmark_result

        except Exception as e:
            error_msg = str(e)
            halo.fail(f" Error on {instance_text}: {error_msg}")

            return {
                'variant': config.variant,
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
        print(f"🎯 Started benchmark run with {len(configs)} configurations\n")

        # Disable alive_bar in Docker environments or when verbose
        use_progress_bar = not self.verbose and not is_docker_environment()

        progress_context = (
            nullcontext() if not use_progress_bar
            else alive_bar(total= len(configs),
                           title= 'Benchmarking...',
                           length = 20,
                           bar='smooth',
                           spinner='dots',
                           stats=False)
        )

        with progress_context as bar:
            for i, config in enumerate(configs, 1):
                result = self.run_single_benchmark(config)
                self.results.append(result)
                if bar is not None:
                    bar()
                self.cleanup()

        print(f"\n🏁 Benchmark run completed! Results will be saved to: {self.output_csv}")

    def save_results_to_csv(self) -> None:
        """Save benchmark results to CSV file."""
        with open(self.output_csv, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write headers
            writer.writerow(['Variant', 'Model', 'Threshold', 'Budget', 'Time (s)', 'Reward', 'Status', 'Error'])

            # Write results
            for result in self.results:
                writer.writerow([
                    result['variant'].upper(),
                    result['model'],
                    result['threshold'],
                    result['budget'],
                    f"{result['time']:.6f}" if result['time'] and result['time'] > 0 else "t.o.",
                    result['reward'] if result['reward'] is not None else "N/A",
                    result['status'],
                    result['error'] or ""
                ])

    def cleanup(self) -> None:
        """Call garbage collection."""
        gc.collect()


def main():
    """Main entry point for the benchmark runner."""
    parser = argparse.ArgumentParser(
        description="Benchmark runner for OOP problem instances",
        epilog="Examples:\n  python3 benchmark.py config.csv --output results.csv\n  python3 benchmark.py config1.csv config2.csv --output results.csv"
    )

    parser.add_argument('config_csv', nargs='+', help='One or more CSV files with benchmark configurations')
    parser.add_argument('--output', '-o', default='benchmark_results.csv', help='Output CSV file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args = parser.parse_args()

    try:

        if not args.config_csv:
            parser.print_help()
            sys.exit(1)

        # Check that all config files exist
        for config_file in args.config_csv:
            if not os.path.exists(config_file):
                print(f"❌ Configuration file not found: {config_file}")
                sys.exit(1)

        # Run benchmarks
        runner = BenchmarkRunner(args.output, args.verbose)

        try:
            configs = runner.load_all_csv_configurations(args.config_csv)

            if not configs:
                print("❌ No valid configurations found")
                sys.exit(1)

            for i in range(10):
                output_csv = args.output.replace('.csv', f'-{i+1}.csv')
                if os.path.exists(output_csv):
                    print("⚠️  Output file exists, trying next:", output_csv)
                    continue
                runner.output_csv = output_csv
                runner.results = []
                runner.run_benchmarks(configs)
                runner.save_results_to_csv()

        finally:
            runner.cleanup()

    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
