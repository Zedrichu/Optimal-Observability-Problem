import pandas as pd
import numpy as np
import glob

def parse_time(time_str: str) -> float:
    TIMEOUT = 180.0
    if time_str == 't.o.' or float(time_str) > TIMEOUT*0.975:
        return -1.0
    else:
        return float(time_str)

def output_variance_results(file_pattern: str):
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
        statuses = np.array([df.iloc[idx]['Status'] for df in dfs], dtype=np.str_)
        timeout_mask = (times == -1.0)
        timeout_count = np.count_nonzero(timeout_mask)
        unknown_mask = (statuses == 'UNKNOWN')
        unknown_count = np.count_nonzero(unknown_mask)
        # We are only interested in 'solving' runtimes. Filter out UNKNOWNs due to timeouts or z3 issues.
        valid_times = times[~unknown_mask]
        mean = np.nanmean(valid_times) if valid_times.size > 0 else "-"
        variance = np.var(valid_times) if valid_times.size > 0 else "-"
        std = np.nanstd(valid_times) if valid_times.size > 0 else "-"
        stats.append({
            'Instance': f"{dfs[0].iloc[idx]['Variant']}-{dfs[0].iloc[idx]['Model']}",
            'Mean Solve Time': mean,
            'Var. Solve Time': variance,
            'Std. Solve Time': std,
            '# Timeouts': timeout_count,
            '# UNKNOWN': unknown_count
        })
    stats_df = pd.DataFrame(stats)
    print(stats_df)

if '__main__' == __name__:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python dynamic_solvers/runtime_variance_results.py '<file_pattern>'")
        print("Note: This assumes all result files contain the benchmark for the same list of OOP instances.")
        sys.exit(1)

    output_variance_results(sys.argv[1])
