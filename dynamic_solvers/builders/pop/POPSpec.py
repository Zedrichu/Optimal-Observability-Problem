from abc import ABC
from itertools import chain
from typing import List

from z3 import z3, Real, Or, Sum

from dynamic_solvers.builders.OOPSpec import OOPSpec


class POPSpec(OOPSpec, ABC):
    def declare_variables(self):
        self.console.print("\n  ⚙️  Declaring variables...", justify="center")
        observable_states = [s for s in range(self.size) if s != self.goal]

        self.ExpRew = self.declare_expected_rewards()
        self.Y = self.declare_observation_function(observable_states)
        self.X = self.declare_strategy_mapping()

    def declare_observation_function(self, observable_states: List[int]) -> List[List[z3.ArithRef]]:
        # Choice of observations on the states (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)
        self.console.print("\n# Choice of observations (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)")
        state_to_observation = [[Real(f'ys{s}o{o+1}', self.ctx)
                                    for o in range(self.budget)]
                                    for s in observable_states]
        self.console.print(state_to_observation)
        return state_to_observation

    def declare_strategy_mapping(self) -> List[List[z3.ArithRef]]:
        # Rates of randomized strategies
        self.console.print("\n# Rates of randomized strategies")
        observation_to_action = [[Real(f'xo{o+1}{act}', self.ctx)
                                    for act in self.actions]
                                    for o in range(self.budget)]
        self.console.print(observation_to_action)
        return observation_to_action

    def build_action_term(self, action_idx: int, state_idx: int):
        return Sum([self.Y[state_idx][o] * self.X[o][action_idx]
                    for o in range(self.budget)])

    def build_observation_constraints(self) -> List[z3.BoolRef]:
        # Observation function constraints - every state should be mapped to some observable class
        self.console.print("\n# Observation function constraints - every state should be mapped to some observable class")
        constraints = []
        for state_obs in self.Y:
            constraints.extend([Or(obs == 0, obs == 1, self.ctx) for obs in state_obs])

        self.console.print('# Every state should be mapped to exactly one equivalence class')
        constraints.extend([Sum(state_obs) == 1 for state_obs in self.Y])

        self.console.print(constraints)
        return constraints

    def collect_constraints(self, threshold: str, determinism: bool) -> List[z3.BoolRef]:
        self.console.print("\n  🛠️  Building constraints...", justify="center")

        constraint_builders = [
            self.build_fully_observable_constraints(),
            self.build_bellman_equations(),
            [self.build_threshold_constraint(threshold)],
            self.build_strategy_constraints(determinism),
            self.build_observation_constraints(),
        ]

        # Flatten constraints for solver loading
        all_constraints = list(chain.from_iterable(constraint_builders))
        return all_constraints
