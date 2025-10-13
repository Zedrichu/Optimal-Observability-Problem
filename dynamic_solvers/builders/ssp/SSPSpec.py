from abc import ABC
from itertools import chain
from typing import List, override

from z3 import z3, Real, Or, Sum

from dynamic_solvers.builders.OOPSpec import OOPSpec


class SSPSpec(OOPSpec, ABC):
    def declare_variables(self):
        # TODO! Use pre-computed dictionary for sensor mapping (especially with multiple goals)
        # O(1) lookup - minimal overhead, big readability gain
        # self.state_to_sensor = {state: idx for idx, state in enumerate(self.nongoal_states)}
        self.console.print("\n  ⚙️  Declaring variables...", justify="center")

        nongoal_states = [s for s in range(self.size) if s != self.goal]
        self.ExpRew = self.declare_expected_rewards()
        self.Y = self.declare_observation_function(nongoal_states)
        self.X = self.declare_strategy_mapping(nongoal_states)

    def declare_observation_function(self, sensor_states: List[int]) -> List[z3.ArithRef]:
        # Choice of observations on each non-goal state (state sensors)
        # e.g. `ys0 == 1` means that in state 0 the sensor is on, `ys0 == 0` - state sensor is off
        self.console.print("\n# Choice of observation on each non-goal state (state sensors that are on/off)")
        state_to_observation = [Real(f'ys{s}', self.ctx) for s in sensor_states]
        self.console.print(state_to_observation)
        return state_to_observation

    def declare_strategy_mapping(self, sensor_states: List[int]) -> List[List[z3.ArithRef]]:
        # Action rates of randomized strategies per state (when the sensor is on)
        self.console.print("\n# Action rates of randomized strategies per state (when sensor is on)")
        sensor_to_action = [[Real(f'xo{s}{act}', self.ctx) for act in self.actions] for s in sensor_states]

        # Default strategy variables per action (when no sensor is observed - unknown state)
        default_policy = [Real(f'x⊥{act}', self.ctx) for act in self.actions]
        sensor_to_action.append(default_policy)

        self.console.print(sensor_to_action)
        return sensor_to_action

    def build_action_term(self, action_idx: int, state_idx: int):
        return ((1 - self.Y[state_idx]) * self.X[-1][action_idx] +
                self.Y[state_idx] * self.X[state_idx][action_idx])

    @override
    def initialize_terms(self):
        """For SSP instances w/o determinism use adapted Bellman equation format."""
        if self.bellman_format == 'default':
            return [] if not self.determinism else [1]
        return super().initialize_terms()

    @override
    def build_destination_rew(self, next_state: int) -> z3.ArithRef:
        """For SSP instances w/o determinism adapt Bellman equations.
        Add reward of single transition (1) to the next state's expected reward towards the goal."""
        if self.bellman_format == 'default':
            return 1 + self.ExpRew[next_state] if not self.determinism else self.ExpRew[next_state]
        return super().build_destination_rew(next_state)

    def build_observation_constraints(self) -> List[z3.BoolRef]:
        # Observation function constraints - every state should be mapped to some observable class
        # For SSP, 2 observation classes exist: activated sensor or unknown
        self.console.print(f"\n# Observation function constraints - every state should be mapped to some observable class"
              f"\n# For SSP, 2 observation classes exist: activated sensor or unknown")
        constraints = [Or(sensor == 0, sensor == 1, self.ctx) for sensor in self.Y]
        self.console.print(constraints)
        return constraints

    def build_budget_constraint(self):
        # Budget constraint - total sensors used <= budget
        self.console.print("# Budget constraint - total no. of sensors activated <= budget")
        constraint = Sum(self.Y) == self.budget # TODO!: Check whether == or <= works better ? original mentions == budget
        self.console.print(constraint)
        return constraint

    def collect_constraints(self, threshold: str) -> List[z3.BoolRef]:
        self.console.print("\n  🛠️  Building constraints...", justify="center")

        builders = [
            lambda: [*self.build_fully_observable_constraints(), self.build_threshold_constraint(threshold)],
            lambda: self.build_bellman_equations(),
            lambda: [*self.build_strategy_constraints(), *self.build_observation_constraints()],
            lambda: [self.build_budget_constraint()],
        ]

        self.console.print("\nApplying order of constraints:")
        self.console.print(",".join(f"{i} <- {order}" for (i, order) in enumerate(self.order_constraints)))

        constraint_builders = [builders[i]() for i in self.order_constraints]
        # self.console.print("\nOrder of constraints after applying reordering:")
        # self.console.print(constraint_builders)

        # Flatten constraints for solver loading
        all_constraints = list(chain.from_iterable(constraint_builders))
        return all_constraints
