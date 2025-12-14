from Frontier import Frontier
from State import State
from Z3Executor import Z3Executor
from builders.POMDPSpec import POMDPAdapter


class GraphSearch:
    def __init__(self, n: int, adapter: POMDPAdapter, solver: Z3Executor):
        self.n = n
        self.set = set()
        self.frontier = Frontier()

        self.adapter = adapter
        self.solver = solver

    def search(self, initial_state: State) -> State | None:
        self.frontier.add(initial_state)
        self.set.add(initial_state)

        while not self.frontier.is_empty():
            state = self.frontier.next()
            if not self.is_valid(state):
                continue
            print(f"Exploring state: {state.obs}")
            if state.is_goal_state(self.solver, self.adapter):
                return state
            next_states = state.get_next_states()
            for next_state in next_states:
                if next_state not in self.set:
                    self.frontier.add(next_state)
                    self.set.add(next_state)
        return None

    def is_valid(self, state: State) -> bool:
        return (sum(state.obs) + 1) == self.adapter.budget