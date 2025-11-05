from placements.Frontier import Frontier
from placements.State import State


class GraphSearch:
    def __init__(self, n: int):
        self.n = n
        self.set = set()
        self.frontier = Frontier()

    def search(self, initial_state: State) -> State | None:
        self.frontier.add(initial_state)
        self.set.add(initial_state)

        while not self.frontier.is_empty():
            state = self.frontier.next()
            if state.is_goal_state():
                return state
            next_states = state.get_next_states()
            for next_state in next_states:
                if next_state not in self.set:
                    self.frontier.add(next_state)
                    self.set.add(next_state)
        return None
