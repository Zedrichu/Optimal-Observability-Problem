import time

from TPMCSolver import TPMCSolver
from builders.TPMCFactory import TPMCFactory
from builders.POMDPSpec import POMDPAdapter
from builders.direction import Direction


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


from collections.abc import Iterable


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

    width = 5
    height = 3
    goal = 6
    budget = 3
    threshold = "<= 10"
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
    overlapping_clusters = [
        {Direction.NW, Direction.N, Direction.NE},
        {Direction.NW, Direction.W, Direction.SW},
        {Direction.SW, Direction.S, Direction.SE},
        {Direction.SE, Direction.E, Direction.NE},
    ]

    print(f"\nClusters (goal = s{tpmc_instance.goal}):")
    for c, cluster in enumerate(clusters):
        print(f"{cluster} (o{c}): {prettify(clusters[cluster], "s")}")

    # Given a budget B:
    # We generate all possible partitions for clusters into B buckets
    num_clusters = len(clusters.keys())
    partitions = [(p, partition) for p, partition in enumerate(stirling_partitions(n=num_clusters, k=budget))]

    # For each partition, we place all states from each cluster in the specified bucket to form an observation class
    keys = list(clusters.keys())
    for p, partition in partitions:
        obs_function = [-1]*tpmc_instance.size
        strategy_constraints = []
        for b, bucket in enumerate(partition):
            bucket_clusters = set()
            for cluster in bucket:
                # Assign states in the cluster to the bucket/observation class
                for state in clusters[keys[cluster]]:
                    obs_function[state] = b
                bucket_clusters.add(keys[cluster])

        print(f"\nPossible partition {p + 1}")
        print(f"Buckets/partition: {prettify(partition, "o")}")
        print(f"POMDP: {obs_function}")

        # TODO: We should use some knowledge of the optimal strategies
        #       when an observation function composes a single cluster
        result = solver.evaluate_pomdp(adapter, obs_function=obs_function, timeout_ms=20000)
        for i in range(5):
            time.sleep(1)
            print(f"Slept for {i+1}s...")
