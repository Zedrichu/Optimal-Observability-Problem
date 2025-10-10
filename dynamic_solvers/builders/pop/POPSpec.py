from abc import ABC
from itertools import chain
from typing import List, override

from z3 import z3, Real, Or, Sum, Bool, Implies, And, Not

from dynamic_solvers.builders.OOPSpec import OOPSpec


class POPSpec(OOPSpec, ABC):
    def declare_variables(self):
        self.console.print("\n  ⚙️  Declaring variables...", justify="center")
        observable_states = [s for s in range(self.size) if s != self.goal]

        self.ExpRew = self.declare_expected_rewards()
        self.Y = self.declare_observation_function(observable_states)
        self.X = self.declare_strategy_mapping()

    def declare_observation_function(self, observable_states: List[int]) -> List[List[z3.ArithRef]]:
        if self.bool_encoding:
            # Choice of observations on the states (e.g. ys0o1 = True means that in state 0, observable 1 is observed)
            self.console.print("\n# Choice of observations (e.g. ys0o1 = True means that in state 0, observable 1 is observed)")
            state_to_observation = [[Bool(f'ys{s}o{o + 1}', self.ctx)
                                     for o in range(self.budget)]
                                    for s in observable_states]
            self.console.print(state_to_observation)
            return state_to_observation

        # Choice of observations on the states (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)
        self.console.print("\n# Choice of observations (e.g. ys0o1 = 1 means that in state 0, observable 1 is observed)")
        state_to_observation = [[Real(f'ys{s}o{o+1}', self.ctx)
                                    for o in range(self.budget)]
                                    for s in observable_states]
        self.console.print(state_to_observation)
        return state_to_observation

    def declare_strategy_mapping(self) -> List[List[z3.ArithRef]]:
        if self.bool_encoding and self.determinism:
            # Deterministic strategies (e.g. xo1a = True means that for observation 1, action a is taken)
            self.console.print("\n# Deterministic strategies (e.g. xo1a = True means that for observation 1, action a is taken)")
            observation_to_action = [[Bool(f'xo{o+1}{act}', self.ctx)
                                        for act in self.actions]
                                        for o in range(self.budget)]
            self.console.print(observation_to_action)
            return observation_to_action

        # Rates of randomized strategies
        self.console.print("\n# Rates of randomized strategies")
        observation_to_action = [[Real(f'xo{o+1}{act}', self.ctx)
                                    for act in self.actions]
                                    for o in range(self.budget)]
        self.console.print(observation_to_action)
        return observation_to_action

    @override
    def build_bellman_equations(self) -> List[z3.BoolRef]:
        if self.bool_encoding:
            # Bellman equations for expected rewards in each world's state
            self.console.print("\n# Bellman equations for expected rewards in each world's state")
            equations = []
            for s in range(self.size):
                if s == self.goal:
                    equations.append(self.ExpRew[s] == 0)
                    continue

                # Decrement the state index after processing the goal state
                state_idx = s if s < self.goal else s - 1
                for o in range(self.budget):
                    if self.determinism:
                        equations.extend([
                            Implies(
                                And(self.Y[state_idx][o], self.X[o][a], self.ctx),
                                self.ExpRew[s] == 1 + self.ExpRew[self.navigate(s, a)],
                                self.ctx)
                            for a in range(len(self.actions))
                        ])
                    else:
                        equations.extend([
                            Implies(
                                self.Y[state_idx][o],
                                self.ExpRew[s] == 1 + Sum([self.ExpRew[self.navigate(s, a)] * self.X[o][a]
                                                            for a in range(len(self.actions))]),
                                self.ctx)
                        ])
            self.console.print(equations)
            return equations
        return super().build_bellman_equations()

    def build_action_term(self, action_idx: int, state_idx: int):
        return Sum([self.Y[state_idx][o] * self.X[o][action_idx]
                    for o in range(self.budget)])

    @override
    def build_strategy_constraints(self) -> List[z3.BoolRef]:
        if self.bool_encoding and self.determinism:
            self.console.print('# Deterministic strategies activated using Boolean encoding (one-hot encoding or degenerate categorical distribution)\n')
            constraints = []
            constraints.extend([
                Or(*[self.X[o][a] for a in range(len(self.actions))], self.ctx)
                for o in range(self.budget)
            ])

            for o in range(self.budget):
                for a1 in range(len(self.actions)):
                    constraints.extend([
                        Implies(
                            self.X[o][a1],
                            And(*[Not(self.X[o][a2], self.ctx) for a2 in range(len(self.actions)) if a2 != a1] , self.ctx),
                            self.ctx)
                    ])
            self.console.print(constraints)
            return constraints
        return super().build_strategy_constraints()

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
