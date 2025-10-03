import pandas as pd
import numpy as np
import glob

def parse_time(time_str: str) -> float:
    if time_str == 't.o.':
        return 180.0
    else:
        return float(time_str)

def compute_variance_results(file_pattern: str):
    files = glob.glob(file_pattern)
    if not files:
        print(f"No files found matching pattern: {file_pattern}")
        return
    print(f"Found {len(files)} files matching pattern.")
    dfs = [pd.read_csv(f) for f in files]
    num_instances = len(dfs[0])
    stats = []
    for idx in range(num_instances):
        times = np.array([np.float64(parse_time(df.iloc[idx]['Time (s)'])) for df in dfs], dtype=np.float64)
        stats.append({
            'Instance': f"{dfs[0].iloc[idx]['Variant']}-{dfs[0].iloc[idx]['Model']}",
            'Time_mean': np.nanmean(times),
            'Time_var': np.nanvar(times),
        })
    stats_df = pd.DataFrame(stats)
    print(stats_df)

if '__main__' == __name__:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python dynamic_solvers/runtime_variance_results.py '<file_pattern>'")
        print("Note: This assumes all result files contain the benchmark for the same list of OOP instances.")
        sys.exit(1)

    compute_variance_results(sys.argv[1])
