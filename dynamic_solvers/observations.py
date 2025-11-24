import time

from TPMCSolver import TPMCSolver
from builders.TPMCFactory import TPMCFactory
from builders.POMDPSpec import POMDPAdapter
from collections.abc import Iterable

from z3 import sat


def stirling_partitions(n, k):
    """Generate all partitions of {0..n-1} into k unlabeled nonempty subsets."""
    items = list(range(n))

    def backtrack(i, curr, used):
        if i == n:
            if used == k:
                # Yield a sorted normalized form (unlabeled buckets)
                yield list(sorted(list(sorted(b)) for b in curr[:used]))
            return

        # Option 1: put item i into an existing bucket
        for b in range(used):
            curr[b].append(items[i])
            yield from backtrack(i+1, curr, used)
            curr[b].pop()

        # Option 2: create a new bucket (only if we have room)
        if used < k:
            curr[used].append(items[i])
            yield from backtrack(i+1, curr, used+1)
            curr[used].pop()

    # start with empty structure
    curr = [[] for _ in range(k)]
    yield from backtrack(0, curr, 0)

def prettify(obj, prefix: str):
    # Base case: if it's an int, prettify it
    if isinstance(obj, int):
        return f"{prefix}{obj}"
    # If it's an iterable (list/tuple/set), recurse into it
    if isinstance(obj, Iterable):
        container_type = type(obj)
        return container_type(prettify(item, prefix) for item in obj)
    return obj


if __name__ == "__main__":
    width = 339
    height = 170
    goal = 844
    budget = 3
    # threshold = "<= Q(84,15)"
    # threshold = "<= Q(243191,845)"
    threshold = "<= Q(243191,1)"
    verbose = False

    tpmc_instance = TPMCFactory.create(oop_variant='pop',
                                       puzzle_type='maze',
                                       width=width,
                                       height=height,
                                       goal=goal,
                                       budget=budget,
                                       determinism=False,
                                       precision='strict',
                                       bool_encoding=True,
                                       verbose=verbose)

    solver = TPMCSolver(tpmc_instance.ctx, verbose=verbose)
    adapter = POMDPAdapter(tpmc_instance)
    solver.prepare_constraints(adapter, threshold)

    clusters = tpmc_instance.clusters
    keys = list(clusters.keys())
    num_clusters = len(keys)

    print(f"\nClusters (goal = s{tpmc_instance.goal}):")
    for c, cluster_idx in enumerate(clusters):
        # print(f"{cluster_idx} (o{c}): {prettify(clusters[cluster_idx], "s")}")
        print(f"{cluster_idx} (o{c}): {len(clusters[cluster_idx])}")

    # Given a budget B, we generate all possible partitions for clusters into B buckets
    partitions = [(p, partition) for p, partition in enumerate(stirling_partitions(n=num_clusters, k=budget))]

    # For each partition, we place all states from each cluster in the specified bucket to form the observation function
    for p, partition in partitions:
        obs_function = [-1]*tpmc_instance.size
        strategy_constraints = []
        for b, bucket in enumerate(partition):
            bucket_actions = set()
            for cluster_idx in bucket:
                cluster = keys[cluster_idx]
                # Assign states in the cluster to the bucket/observation class
                for state in clusters[cluster]:
                    obs_function[state] = b

                bucket_actions.update(cluster.actions)
            # We can add strategy constraints to a certain observation class based on the optimal actions present in it
            for a, action in enumerate(tpmc_instance.actions):
                if action not in bucket_actions:
                    strategy_constraints.append(tpmc_instance.X[b][a] == 0)


        print(f"\nPartition {p + 1}")
        print(f"Strategy constraints: {strategy_constraints}")
        # print(f"Buckets/partition: {prettify(partition, "o")}")
        print(f"Buckets/partition: {len(partition)}")
        print(f"POMDP: {obs_function}")

        result = solver.evaluate_pomdp(adapter, obs_function, 10000, strategy_constraints)
        print(f"Result: {result.solve_time}s | {result.result} | {result.reward}")
        if result.result == sat:
            exit(0)
        time.sleep(1)
