import subprocess
import os
from concurrent.futures import ProcessPoolExecutor, as_completed

MAX_PARALLEL = 4

def run_benchmark(run_id):
    output_file = f"benchmark_repo/runtime-variance/runtime-variance-results-{run_id}.csv"
    if os.path.exists(output_file):
        print(f"Skipping {output_file} (already exists)")
        return
    print("Starting benchmark #", run_id)
    cmd = [
        "python3", "-m", "dynamic_solvers.benchmark",
        "dynamic_solvers/configs/runtime-variance.csv",
        "-bf", "adapted",
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
            for i in range(1, 11):
                futures.append(executor.submit(run_benchmark, i))
            for future in as_completed(futures):
                future.result()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Cleaning up...")