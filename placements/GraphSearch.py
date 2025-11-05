from placements.Frontier import Frontier
from placements.State import State


class GraphSearch:
    def __init__(self, n: int):
        self.n = n
        self.set = set()
        self.frontier = Frontier()

    def search(self, initial_state: State):
        self.frontier.add(initial_state)
        self.set.add(initial_state)

        while not self.frontier.is_empty():
            state = self.frontier.next()
            print(f"\nExpanded state: {state} ({sum(state.bits)})")
            if state.is_goal_state():
                return state
            next_states = state.get_next_states()
            print("Generated the next states:")
            for next_state in next_states:
                if next_state not in self.set:
                    self.frontier.add(next_state)
                    self.set.add(next_state)
            line = input()

        return -1





if __name__ == "__main__":
    n = 15
    sensors = {0,1,2,3,4,5,6}
    bits = bytearray([int(i in sensors) for i in range(n)])

    placement = State(n=n, goal=7, bits=bits, g=0, parent=None)

    gs = GraphSearch(n)
    gs.search(placement)
