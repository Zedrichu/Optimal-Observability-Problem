import itertools
import subprocess
import os
from concurrent.futures import ProcessPoolExecutor, as_completed

PERMS = list(itertools.permutations(range(4)))
MAX_PARALLEL = 4

def run_benchmark(perm):
    perm_str = ','.join(map(str, perm))
    file_id = '_'.join(map(str, perm))
    output_file = f"benchmark_repo/reorder-constraints/order-{file_id}.csv"
    if os.path.exists(output_file):
        print(f"Skipping {output_file} (already exists)")
        return
    print("Starting benchmark for order:", perm_str)
    cmd = [
        "python3", "-m", "dynamic_solvers.benchmark",
        "dynamic_solvers/configs/runtime-variance.csv",
        "-bf", "adapted",
        "--order-constraints", perm_str,
        "-o", output_file
    ]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if not sys.argv[1].isdigit():
            print("First argument must be an integer specifying max parallel processes.")
            sys.exit(1)
        MAX_PARALLEL = int(sys.argv[1])
        if not 0 < MAX_PARALLEL < 8:
            print("Max parallel processes must be between 1 and 7.")
            sys.exit(1)
        MAX_PARALLEL = int(sys.argv[1])
    futures = []
    try:
        with ProcessPoolExecutor(max_workers=MAX_PARALLEL) as executor:
            for perm in PERMS:
                perm_str = ','.join(map(str, perm))
                output_file = f"benchmark_repo/reorder-constraints/order-{perm_str}.csv"
                futures.append(executor.submit(run_benchmark, perm))
            for future in as_completed(futures):
                future.result()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Cleaning up...")
