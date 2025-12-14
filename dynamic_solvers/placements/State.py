from z3 import sat

from Z3Executor import Z3Executor
from builders.POMDPSpec import POMDPAdapter


class State:
    def __init__(self, n: int, goal: int, obs: list[int], g: int, parent = None):
        super().__init__()
        self.n = n
        self.obs = obs
        self.goal = goal

        self.parent = parent
        self.g = g

        self._str = ""
        self._hash = None

    def get_next_states(self) -> list[int]:
        next_states = []
        seen = set()

        zeros = [i for i, v in enumerate(self.obs) if v == 0 and i != self.goal]
        ones = [i for i, v in enumerate(self.obs) if v == 1 and i != self.goal]

        for i in zeros:
            # We do not place sensors past the goal state
            if i > self.goal:
                continue
            for j in ones:
                if i == j:
                    continue
                obs = self.obs[:]
                obs[i] = 1
                obs[j] = 0
                obs_key = tuple(obs)
                if obs_key in seen:
                    continue
                seen.add(obs_key)
                next_states.append(State(n=self.n, goal=self.goal, obs=obs, g=self.g + 1, parent=self))
        return next_states

    def is_goal_state(self, solver: Z3Executor, adapter: POMDPAdapter) -> bool:
        strategy_constraints = adapter.infer_ssp_strategy_constraints(self.obs)
        result = solver.evaluate_pomdp(adapter, self.obs, 5000, strategy_constraints)
        # TODO: Caveat: what if unknown?
        return result.result == sat

    def __str__(self):
        if self._str:
            return self._str
        else:
            self._str = ''.join(str(bit) for bit in self.obs)
        return self._str

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        if self.n != other.n:
            return False
        for i in range(self.n):
            if self.obs[i] != other.obs[i]:
                return False
        return True

    def __hash__(self):
        if self._hash:
            return self._hash
        else:
            self._hash = int(''.join(str(bit) for bit in self.obs if bit != -1), 2)
        return self._hash

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()