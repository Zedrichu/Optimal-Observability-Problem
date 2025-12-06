from abc import ABC, abstractmethod
from typing import List

from direction import Direction


class World(ABC):
    size: int
    actions: List[str]
    goal: int
    clusters: dict[Direction, List[int]]

    @abstractmethod
    def navigate(self, state: int, action: int) -> int:
        raise NotImplementedError()

    @abstractmethod
    def dist(self, source: int, target: int) -> int:
        raise NotImplementedError()

    @abstractmethod
    def cluster(self) -> dict[Direction, List[int]]:
        raise NotImplementedError()


class Line(World):
    def __init__(self, length: int, goal: int):
        self.length = length

        self.size = length
        self.actions = ['l', 'r']

        self.goal = goal
        self.clusters = self.cluster()

    def navigate(self, state: int, action_idx: int) -> int:
        action = self.actions[action_idx]
        if action == 'l':
            return max(state - 1, 0)
        else:  # action == 'r'
            return min(state + 1, self.length - 1)

    def dist(self, source: int, target: int) -> int:
        return abs(source - target)

    def cluster(self) -> dict[Direction, List[int]]:
        clusters = {}

        for state in range(self.size):
            if state < self.goal:
                clusters.setdefault(Direction.E, []).append(state)
            elif state > self.goal:
                clusters.setdefault(Direction.W, []).append(state)
        return clusters


class Grid(World):
    def __init__(self, width: int, height: int, goal: int):
        self.width = width
        self.height = height

        self.size = width * height
        self.actions = ['l', 'r', 'u', 'd']

        self.goal = goal
        self.clusters = self.cluster()

    def navigate(self, state: int, action_idx: int) -> int:
        """Navigate in 2D grid based on action"""
        action = self.actions[action_idx]
        x = state % self.width
        y = state // self.width

        if action == 'l':  # left
            if x != 0:
                return state - 1
        elif action == 'r':  # right
            if x != self.width - 1:
                return state + 1
        elif action == 'u':  # up
            if y != 0:
                return state - self.width
        else:  # action == 'd' (down)
            if y != self.height - 1:
                return state + self.width
        return state

        # size_x = 4; size_y = 3; column = 11 % 4 = 3
        # 3 -> 3 % 4 == 3 -> (11 - 3) // 4 == 2
        # 5 -> 5 % 4 == 1 -> (3 - 1) + 6 // 4 = 2 + 1 = 3
        # size_x -> size_y |
        # 0 1 2 3          v  5 4 3 2
        # 4 5 6 7             4 3 2 1
        # 8 9 10 11           3 2 1 0

    def dist(self, source: int, target: int) -> int:
        """
        Compute Manhattan distances between each state and the goal state based on the grid topology.
        """
        # Grid-specific bounds calculation
        goal_column = target % self.width
        column = source % self.width
        goal_row = target // self.width
        row = source // self.width

        return abs(goal_column - column) + abs(goal_row - row)

    def cluster(self) -> dict[Direction, List[int]]:
        clusters = {}

        goal_x = self.goal % self.width
        goal_y = self.goal // self.width

        for state in range(self.size):
            state_x = state % self.width
            state_y = state // self.width
            if state_x < goal_x and state_y == goal_y:
                clusters.setdefault(Direction.E, []).append(state)
            elif state_x > goal_x and state_y == goal_y:
                clusters.setdefault(Direction.W, []).append(state)
            elif state_x == goal_x and state_y < goal_y:
                clusters.setdefault(Direction.S, []).append(state)
            elif state_x == goal_x and state_y > goal_y:
                clusters.setdefault(Direction.N, []).append(state)
            elif state_x < goal_x and state_y < goal_y:
                clusters.setdefault(Direction.SE, []).append(state)
            elif state_x > goal_x and state_y < goal_y:
                clusters.setdefault(Direction.SW, []).append(state)
            elif state_x < goal_x and state_y > goal_y:
                clusters.setdefault(Direction.NE, []).append(state)
            elif state_x > goal_x and state_y > goal_y:
                clusters.setdefault(Direction.NW, []).append(state)
        return clusters


class Maze(World):
    def __init__(self, width: int, depth: int, goal: int):
        if width % 2 == 0:
            raise ValueError('Width must be odd for maze generation')

        self.width = width
        self.depth = depth

        self.size = width + 3 * (depth - 1)
        self.actions = ['l', 'r', 'u', 'd']

        self.goal = goal
        self.clusters = self.cluster()

    def navigate(self, state: int, action_index: int) -> int:
        """Navigate in 2D maze based on action"""
        action = self.actions[action_index]
        if action == 'l':
            if 0 < state < self.width:
                return state - 1
        elif action == 'r':
            if 0 <= state < self.width - 1:
                return state + 1
        elif action == 'u':
            if state == self.width:
                return 0
            elif state == self.width + 1:
                return (self.width - 1) // 2
            elif state >= self.width + 2:
                return state - 3
        else:  # action == 'd'
            if state == 0:
                return self.width
            elif state == (self.width - 1) // 2:
                return self.width + 1
            elif self.width - 1 <= state < self.size - 3:
                return state + 3
        return state

    def dist(self, source: int, target: int) -> int:
        """
        Compute shortest-path distances between each state and the goal state based on the maze topology.
        """
        goal_column = target if target < self.width \
                             else (target - self.width) % 3 * (self.width // 2)
        goal_height = 0 if target < self.width \
                        else (target - self.width) // 3 + 1

        if source < self.width:
            return goal_height + abs(source - goal_column)
        else:
            column = (source - self.width) % 3 * (self.width // 2)
            row = (source - self.width) // 3 + 1
            diff = int(goal_column != column)
            return abs(column - goal_column) + abs(row - goal_height + 2 * goal_height * diff)

    def cluster(self) -> dict[Direction, List[int]]:
        clusters = {}

        goal_x = self.goal if self.goal < self.width \
            else (self.goal - self.width) % 3 * (self.width // 2)
        goal_y = 0 if self.goal < self.width \
            else (self.goal - self.width) // 3 + 1

        for state in range(self.size):
            state_x = state if state < self.width \
                else (state - self.width) % 3 * (self.width // 2)
            state_y = 0 if state < self.width \
                else (state - self.width) // 3 + 1

            if state_x < goal_x and state_y == 0:
                clusters.setdefault(Direction.E, []).append(state)
            elif state_x > goal_x and state_y == 0:
                clusters.setdefault(Direction.W, []).append(state)
            elif state_x == goal_x and state_y < goal_y:
                clusters.setdefault(Direction.S, []).append(state)
            elif (state_x != goal_x and state_y > 0) or (state_x == goal_x and state_y > goal_y):
                clusters.setdefault(Direction.N, []).append(state)
        return clusters
