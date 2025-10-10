"""
Main script for solving instances of Optimal Observability Problem (OOP) with Positional (/Deterministic) Strategies.

Supports different problem variants (SSP, POP) and world types (Line, Grid, Maze) translated to location tpMC's.
Problem instances are configured with parameters for budget, goal state, dimensions, threshold and solver options.
"""

import argparse
import sys
import os
from collections import defaultdict

import z3
from z3 import sat

from dynamic_solvers.TPMCSolver import TPMCSolver
from dynamic_solvers.builders.TPMCFactory import TPMCFactory, variant_from_string, puzzle_from_string

VARIANT_CHOICES = ['ssp', 'pop']
PUZZLE_CHOICES = ['line', 'grid', 'maze']


def create_arg_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Solve an Optimal Observability Problem (OOP) with Positional Strategies.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Line SSP problem with budget=2, goal=2, size=5
  python solve_oop.py ssp line --budget 2 --goal 2 --size 5 --threshold "<=3/2"

  # Grid POP problem with budget=3, goal=12, 4x4 grid
  python solve_oop.py pop grid --budget 3 --goal 12 --width 4 --height 4 --threshold "<1/2"

  # Maze SSP problem with deterministic strategies
  python solve_oop.py ssp maze --budget 2 --goal 8 --width 5 --height 3 --deterministic --threshold "<=2/3"

  # With custom output files and timeout
  python solve_oop.py ssp line --budget 1 --goal 3 --size 5 --threshold "<=1/2" \\
                      --results custom_results.txt --rewards custom_rewards.txt --timeout 60000
        """
    )

    # Problem variant selection
    parser.add_argument(
        'variant',
        choices=VARIANT_CHOICES,
        help='Problem variant to solve (SSP: Sensor Selection, POP: Positional Observability)'
    )

    # World type selection
    parser.add_argument(
        'world',
        choices=PUZZLE_CHOICES,
        help='Type of world selected for the problem (Line, Grid, Maze)'
    )

    # Core problem parameters
    parser.add_argument(
        '--budget', '-b',
        type=int,
        required=True,
        help='Budget constraint (number of sensors/observation classes allowed)'
    )

    parser.add_argument(
        '--goal', '-g',
        type=int,
        required=True,
        help='Index of the goal state in the world'
    )

    parser.add_argument(
        '--threshold', '-t',
        type=str,
        required=True,
        help='Threshold constraint (e.g., "<=3/4", "<1/2", "<=Q(2,3)")'
    )

    # World-specific dimensions
    dimension_group = parser.add_argument_group('Dimensions')
    dimension_group.add_argument(
        '--length', '-ln',
        type=int,
        help='Length for line world (required for line)'
    )

    dimension_group.add_argument(
        '--width', '-wd',
        type=int,
        help='Width for grid/maze worlds (required for grid/maze)'
    )

    dimension_group.add_argument(
        '--height', '-hg',
        type=int,
        help='Height for grid/maze worlds (required for grid/maze)'
    )

    # Solver options
    solver_group = parser.add_argument_group('Solver Options')
    solver_group.add_argument(
        '--deterministic', '-d',
        action='store_true',
        help='Use deterministic strategies (default: randomized)'
    )

    solver_group.add_argument(
        '--timeout',
        type=int,
        default=30000,
        help='Solver timeout in milliseconds (default: 30000)'
    )

    # Output options
    output_group = parser.add_argument_group('Output Options')
    output_group.add_argument(
        '--results',
        type=str,
        default='results.txt',
        help='Output file for solver results (default: results.txt)'
    )

    output_group.add_argument(
        '--rewards',
        type=str,
        default='reward.txt',
        help='Output file for reward evaluation (default: reward.txt)'
    )

    output_group.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    output_group.add_argument(
        '--fullres', '-fr',
        action='store_true',
        help='Enable verbose output for results'
    )

    return parser


def validate_arguments(args: argparse.Namespace) -> None:
    """Validate argument combinations and requirements."""

    # Validate world-specific dimension requirements
    if args.world == 'line':
        if args.length is None:
            raise ValueError("Line world requires --length parameter")
        if args.length <= args.goal:
            raise ValueError("Goal state must be within world bounds")

    elif args.world in ['grid', 'maze']:
        if args.width is None or args.height is None:
            raise ValueError(f"{args.world.title()} world requires both --width and --height parameters")

        total_states = args.width * args.height
        if args.world == 'maze':
            # Maze has specific state calculation
            if args.width % 2 == 0:
                raise ValueError("Maze width must be odd")
            total_states = args.width + (args.height - 1) * 3

        if total_states <= args.goal:
            raise ValueError("Goal state must be within world bounds")

    # Validate budget
    if args.budget < 0:
        raise ValueError("Budget must be non-negative")

    # Validate threshold format
    if not any(op in args.threshold for op in ['<=', '<']):
        raise ValueError("Threshold must contain an upper bound comparison operator (<=, <)")


def solve_problem(args: argparse.Namespace, benchmark=False) -> None:
    """Main solving logic."""

    if not benchmark:
        print(f" 🚀 Starting {args.variant.upper()} {args.world.capitalize()} problem...")
        dim_print = f"Length: {args.length}" if args.world == 'line' \
                                                 else f"Dimensions: {args.width}x{args.height}"
        print(f"    Budget: {args.budget}, Goal: {args.goal}, {dim_print}")
        print(f"    Strategy: {'Deterministic' if args.deterministic else 'Randomized'}, Threshold: {args.threshold}")
        print()

    # Convert strings to enums, after which all comparisons are integer-based
    variant = variant_from_string(args.variant)
    world = puzzle_from_string(args.world)

    # Create a problem instance in location tpMC representation
    # Factory handles parameter selection - client runner just passes everything
    tpmc_instance = TPMCFactory.create(variant, world,
                                       length=args.length,
                                       width=args.width,
                                       height=args.height,
                                       goal=args.goal,
                                       budget=args.budget,
                                       determinism=args.deterministic,
                                       bool_encoding=False,
                                       verbose=args.verbose)
    solver = TPMCSolver(tpmc_instance.ctx, verbose=not benchmark)
    # Configure solver timeout
    solver.set_timeout(args.timeout)

    # Solve and get results
    result = solver.solve(tpmc_instance, args.threshold, args.timeout)

    if not benchmark:
        # Report results
        print(f" 🏁 Solve time: {result.solve_time:.4f}s")
        print(f"    Status: {result.result}")
        reward_str = f" ⭐  Reward: {result.reward}" if result.reward is not None else ""
        print(reward_str)

        file_res = open(args.results, 'w')
        if result.model is None:
            file_res.write("")
        else:
            model_groups = group_model_vars(result.model)
            sorted_prefixes = sorted(set(model_groups.keys()))

            for prefix in sorted_prefixes:
                sorted_group = sorted(model_groups[prefix], key=lambda  x: x[0])
                output = f"\n[{prefix}]\n" + '\n'.join([f"{name} = {value}" for name,value in sorted_group])
                file_res.write(output)
                if args.fullres and args.verbose:
                    tpmc_instance.console.print(output)
                if args.fullres:
                    print(output)
        file_res.close()

        file_rew = open(args.rewards, 'w')
        file_rew.write(f"{result.reward if result.result == sat else "N/A"}\n")
        file_rew.close()

        txt = tpmc_instance.console.export_text(clear=True)
        with open('log_record.txt', 'w') as f:
            f.write(txt)
            f.close()

    if args.verbose:
        print(f" 📁 Result model found and saved to: {args.results}; "
              f" Rewards written to: {args.rewards}")
        if result.model:
            print("    Model found and saved")

    solver.cleanup()


def group_model_vars(model: z3.ModelRef) -> defaultdict:
    # Extract and group variables in a Z3 model efficiently
    from collections import defaultdict
    # Clean Grouping by Keys: on missing keys, create empty list, w/o boilerplate key checking
    var_groups = defaultdict(list)
    for var in model.decls():
        # Extract prefix
        name = var.name()
        prefix = name[:2]
        var_groups[prefix].append((name, model[var]))
    return var_groups


def main():
    """Main entry point."""
    parser = create_arg_parser()
    args = parser.parse_args()

    try:
        # Validate arguments
        validate_arguments(args)

        # Ensure output directories exist
        os.makedirs(os.path.dirname(args.results) if os.path.dirname(args.results) else '.', exist_ok=True)
        os.makedirs(os.path.dirname(args.rewards) if os.path.dirname(args.rewards) else '.', exist_ok=True)

        # Solve the problem
        solve_problem(args)

    except ValueError as e:
        print(f"❌ Invalid arguments: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
