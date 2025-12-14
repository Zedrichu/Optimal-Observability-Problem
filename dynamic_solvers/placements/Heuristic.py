from placements.State import State


class Heuristic:
    def h(self, state: State):
        return self.f(self, state)

    @staticmethod
    def f(self, state: State):
        coverage = -sum(state.obs)
        distance = self._sum_sensor_dist(self, state)
        proximity = self._dist_to_goal(self, state)

        return coverage + distance + proximity

    @staticmethod
    def _sum_sensor_dist(self, state: State) -> int:
        sum = 0
        last_found_pos = -1
        for i in range(state.n):
            if last_found_pos == -1:
                if state.obs[i] == 1:
                    last_found_pos = i
            elif state.obs[i] == 1:
                # TODO: count distance between sensors or number of sensor offs between sensors?
                # i.e. i - last_found_pos vs i - last_found_pos - 1
                sum += i - last_found_pos - 1
                last_found_pos = i
        return sum

    @staticmethod
    def _dist_to_goal(self, state: State) -> int:
        left, right = state.goal - 1, state.goal + 1
        while left >= 0 or right < state.n:
            if left >= 0 and state.obs[left] == 1:
                return state.goal - left
            if right < state.n and state.obs[right] == 1:
                return right - state.goal
            left -= 1
            right += 1
        return -1
