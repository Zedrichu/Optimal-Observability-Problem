import heapq

from placements.Heuristic import Heuristic


class Frontier:
    def __init__(self):
        self.pq = []
        self.heuristic = Heuristic()

    def add(self, state: State) -> None:
        heapq.heappush(self.pq, (self.heuristic.h(state), state))

    def next(self) -> State:
        return heapq.heappop(self.pq)[1]

    def is_empty(self) -> bool:
        return len(self.pq) == 0