from abc import ABC
from itertools import chain
from typing import List, override

from z3 import z3, Real, Or, Sum, Bool, Implies, And, Not

from dynamic_solvers.builders.OOPSpec import OOPSpec
from dynamic_solvers.utils import init_var_type


class POPSpec(OOPSpec, ABC):
    def declare_variables(self):
        self.console.print("\n  ⚙️  Declaring variables...", justify="center")
        observable_states = [s for s in range(self.size) if s != self.goal]

        self.ExpRew = self.declare_expected_rewards()
        self.Y = self.declare_observation_function(observable_states)
        self.X = self.declare_strategy_mapping()

    def declare_observation_function(self, observable_states: List[int]) -> List[List[z3.ArithRef]]:
        # Choice of observations on the states (e.g. `ys0o1 = 1` means that in state 0, observable 1 is observed)
        self.console.print("\n# Choice of observations (e.g. `ys0o1 = 1` means that in state 0, observable 1 is observed)")

        # Initialize variables based on encoding mode w/ dynamic constructor (Late-binding Factory Pattern)
        initializer = init_var_type(self.bool_encoding)
        state_to_observation = [[initializer(f'ys{s}o{o+1}', self.ctx)
                                    for o in range(self.budget)]
                                    for s in observable_states]

        self.console.print(state_to_observation)
        return state_to_observation

    def declare_strategy_mapping(self) -> List[List[z3.ArithRef]]:
        # Action rates of observation-based strategies (e.g. `xo1a = 1` means for observation 1, action `a` is taken)
        self.console.print("\n# Action rates of observation-based strategies "
                           "(e.g. `xo1a = p` means for observation 1, action `a` is taken with probability `p`).")

        # Parametric late-bound factory based on encoding mode
        initializer = init_var_type(self.bool_encoding and self.determinism)
        observation_to_action = [[initializer(f'xo{o+1}{act}', self.ctx)
                                    for act in self.actions]
                                    for o in range(self.budget)]

        self.console.print(observation_to_action)
        return observation_to_action

    def _compute_state_bellman_bool_det(self, state: int, state_idx: int) -> List[z3.BoolRef]:
        return [
            Implies(
                And(self.Y[state_idx][o], self.X[o][a], self.ctx),
                self.ExpRew[state] == 1 + self.ExpRew[self.navigate(state, a)],
                self.ctx)
            for o in range(self.budget)
            for a in range(len(self.actions))
        ]

    def _compute_state_bellman_bool_rand(self, state: int, state_idx: int) -> List[z3.BoolRef]:
        return [
            Implies(
                self.Y[state_idx][o],
                self.ExpRew[state] == 1 + Sum([self.ExpRew[self.navigate(state, a)] * self.X[o][a]
                                           for a in range(len(self.actions))]),
                self.ctx)
            for o in range(self.budget)
        ]

    def build_action_term(self, action_idx: int, state_idx: int):
        return Sum([self.Y[state_idx][o] * self.X[o][action_idx]
                    for o in range(self.budget)])

    def build_observation_constraints(self) -> List[z3.BoolRef]:
        # Observation function constraints - every state should be mapped to some observable class
        self.console.print("\n# Observation function constraints - every state should be mapped to some observable class")
        constraints = []
        for state_obs in self.Y:
            if self.bool_encoding:
                constraints.extend([Or(*state_obs, self.ctx)])
            else:
                constraints.extend([Or(obs == 0, obs == 1, self.ctx) for obs in state_obs])

        self.console.print('# Every state should be mapped to exactly one equivalence class')
        if self.bool_encoding:
            constraints.extend([
                Implies(
                    self.Y[s][o1],
                    And(*[Not(self.Y[s][o2], self.ctx) for o2 in range(self.budget) if o2 != o1], self.ctx),
                    self.ctx)
                for s in range(len(self.Y))
                for o1 in range(self.budget)
            ])
        else:
            # TODO: Can sum over booleans but must use 1.0 (z3.Real) instead of 1 (z3.Int)
            constraints.extend([Sum(state_obs) == 1 for state_obs in self.Y])

        self.console.print(constraints)
        return constraints

    def collect_constraints(self, threshold: str) -> List[z3.BoolRef]:
        self.console.print("\n  🛠️  Building constraints...", justify="center")

        t = Real('t', self.ctx)
        constraint_builders = [
            self.build_fully_observable_constraints(),
            self.build_bellman_equations(),
            [self.build_threshold_constraint(threshold)],
            self.build_strategy_constraints(),
            # [t <= 1, t >= 0],
            self.build_observation_constraints(),
        ]

        # Flatten constraints for solver loading
        all_constraints = list(chain.from_iterable(constraint_builders))
        return all_constraints
