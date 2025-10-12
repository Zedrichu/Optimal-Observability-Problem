from abc import ABC, abstractmethod
from typing import List
import re


class World(ABC):
    size: int
    actions: List[str]

    @abstractmethod
    def navigate(self, state: int, action: int) -> int:
        raise NotImplementedError()

    @abstractmethod
    def dist(self, source: int, target: int) -> int:
        raise NotImplementedError()


class Line(World):
    def __init__(self, length: int):
        self.length = length

        self.size = length
        self.actions = ['l', 'r']

    def navigate(self, state: int, action_idx: int) -> int:
        action = self.actions[action_idx]
        if action == 'l':
            return max(state - 1, 0)
        else:  # action == 'r'
            return min(state + 1, self.length - 1)

    def dist(self, source: int, target: int) -> int:
        return abs(source - target)


class Grid(World):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.size = width * height
        self.actions = ['l', 'r', 'u', 'd']

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
        return abs(goal_column - column) + (abs(target - source) // self.width)


class Maze(World):
    def __init__(self, width: int, depth: int):
        if width % 2 == 0:
            raise ValueError('Width must be odd for maze generation')

        self.width = width
        self.depth = depth

        self.size = width + 3 * (depth - 1)
        self.actions = ['l', 'r', 'u', 'd']

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
