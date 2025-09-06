import gc
from logging import Logger
from typing import List
from z3 import (Solver, Context,
                z3, set_option, sat, unsat,
                Real, Q, Or)

class LineSSPChain:
    """
    Z3 API solver for "Line" instances in the SSP problem with benchmarking

    Part of the OOP problem suites.
    """

    def __init__(self, budget: int, goal: int, size: int, det: int):
        self.budget = budget
        self.goal = goal
        self.size = size
        self.det = det

        self.actions = ['l', 'r']

        self.exp_rew = None
        self.obs_fun = None
        self.strategy = None

        self.ctx = None
        self.solver = None

        self.evaluator = None
        self.logger = Logger("LinePOPChain")

        self.reset()

    def reset(self):
        """Reset for fresh solving context"""
        gc.collect() # Clean memory before starting
        self.ctx = Context()
        self.solver = Solver(ctx=self.ctx)

    def compute_expected_rewards(self) -> List[z3.ArithRef | None]:
        # Expected cost/reward of reaching the goal from each corresponding state.
        print("# Expected cost/reward of reaching the goal from each corresponding state.")
        expected_rewards = [Real(f'pi{s}', self.ctx) for s in range(self.size)]
        print(expected_rewards)
        return expected_rewards

    def create_observation_maps(self, goal) -> List[List[z3.ArithRef | None]]:
        # Choice of observations on each non-goal state (state sensors)
        # e.g. `ys0 == 1` means that in state 0 the sensor is on, `ys0 == 0` - state sensor is off
        print("# Choice of observation on each non-goal state (state sensors that are on/off)")
        sensor_states = [s for s in range(self.size) if s != goal]

        state_to_observation = [ Real(f'ys{s}', self.ctx) for s in sensor_states]
        print(state_to_observation)
        return state_to_observation