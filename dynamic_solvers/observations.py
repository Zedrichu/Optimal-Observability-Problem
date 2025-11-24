from typing import List, Iterable

from builders.worlds import Line, Maze


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
    maze = Maze(5, 3, 6)
    print(f"\nMaze Clusters (goal = s{maze.goal}):")
    for c, cluster in enumerate(maze.clusters):
        print(f"{cluster} (o{c}): {prettify(maze.clusters[cluster], "s")}")
    print()

    # Suppose we are given a budget B
    B = 3
    num_clusters = len(maze.clusters.keys())

    # We generate all possible partitions for clusters into B buckets
    partitions = [(p, partition) for p, partition in enumerate(stirling_partitions(n=num_clusters, k=B))]

    # For each partition, we place all states from each cluster in the specified bucket to form an observation class
    keys = list(maze.clusters.keys())
    for _, partition in partitions:
        obs_function = []
        for bucket in partition:
            observation_class = []
            for cluster in bucket:
                observation_class.extend(maze.clusters[keys[cluster]])
            obs_function.append(observation_class)
        print()
        print(prettify(partition, "o"))
        print(prettify(obs_function, "s"))
