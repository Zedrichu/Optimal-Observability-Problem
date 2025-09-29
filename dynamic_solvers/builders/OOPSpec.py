from abc import ABC, abstractmethod
from typing import List, Optional
from io import StringIO

from rich.console import Console
from z3 import (Context, z3, Real, Q, Or, Sum)

from dynamic_solvers.builders.worlds import World
from dynamic_solvers.utils import parse_threshold


class OOPSpec(World, ABC):
    def __init__(self, budget: int, goal: int, determinism: bool,
                 ctx: Optional[Context] = None, verbose: bool = False):
        self.ctx = ctx or Context()  # Use provided context or create fresh one
        self.budget = budget
        self.goal = goal
        self.determinism = determinism
        self.verbose = verbose

        self.ExpRew = None  # Expected reward variables
        self.Y = None       # Observation function variables
        self.X = None       # Strategy mapping variables (action rates)

        self.exp_rew_evaluator = None

        self.console = Console(quiet=not verbose, record=True)

    @abstractmethod
    def declare_variables(self):
        raise NotImplementedError()

    @abstractmethod
    def declare_observation_function(self, observable_states: List[z3.ArithRef]) -> List[z3.ArithRef]:
        raise NotImplementedError()

    @abstractmethod
    def declare_strategy_mapping(self, *args) -> List[List[z3.ArithRef]]:
        raise NotImplementedError()

    def declare_expected_rewards(self) -> List[z3.ArithRef]:
        # Expected cost/reward of reaching the goal from each corresponding state.
        self.console.print("\n# Expected cost/reward of reaching the goal from each corresponding state.")
        expected_rewards = [Real(f'pi{s}', self.ctx) for s in range(self.size)]
        # self.console.print(f"[ pi<x>, x ∈ ℕ, 0 <= x < {self.goal} ]")
        self.console.print(expected_rewards)
        return expected_rewards

    def build_fully_observable_constraints(self) -> List[bool]:
        """
        Build basic POMDP constraints - a POMDP instance cannot perform better than the fully observable variant.
        """
        self.console.print('\n# A POMDP instance cannot perform better than the fully observable variant')
        constraints = [self.ExpRew[s] >= self.dist(s, self.goal) for s in range(self.size)]

        self.console.print(constraints)
        return constraints

    def build_bellman_equations(self) -> List[z3.BoolRef]:
        # Bellman equations for expected rewards in each world's state
        self.console.print("\n# Bellman equations for expected rewards in each world's state")

        equations = []
        for s in range(self.size):
            if s == self.goal:
                equations.append(self.ExpRew[s] == 0)
                continue

            # Build action terms for each direction using a transition function
            terms = self.initialize_terms()
            for a in range(len(self.actions)):
                # Decrement the state index after processing the goal state
                idx = s - 1 if s > self.goal else s

                action_term = self.build_action_term(a, idx)
                next_state = self.navigate(s, a)
                destination_rew = self.build_destination_rew(next_state)
                terms.append(action_term * destination_rew)
            equations.append(self.ExpRew[s] == Sum(terms))

        self.console.print(equations)
        return equations

    def initialize_terms(self):
        """
        Common format of Bellman equations used with deterministic strategies.
        Otherwise, use the adapted shape of Bellman equations as previously done.
        """
        return [1] if self.determinism else []

    def build_destination_rew(self, next_state: int) -> z3.ArithRef:
        """
        Common format of Bellman equations used with deterministic strategies.
        Otherwise, use the adapted shape of Bellman equations as previously done.
        """
        return self.ExpRew[next_state] if self.determinism else 1 + self.ExpRew[next_state]

    @abstractmethod
    def build_action_term(self, action_idx: int, state_idx: int) -> z3.ArithRef:
        raise NotImplementedError()

    def build_threshold_constraint(self, threshold: str) -> bool:
        # Agent dropped in the world under uniform distribution
        # Check if the minimal expected cost is below some threshold
        self.console.print(f"\n# Agent dropped uniformly in the world"
              f"\n# Objective: check if the minimal expected cost is below some threshold `{threshold}`")

        # Generate the sum of expected reward variables for non-target states (uniform distribution)
        sumExpRew = Sum([self.ExpRew[s] for s in range(self.size) if s != self.goal])
        terms, sign = parse_threshold(threshold)

        self.exp_rew_evaluator = sumExpRew * Q(1, self.size - 1, self.ctx)

        thr = Q(terms[0], terms[1], self.ctx) if len(terms) > 1 else terms[0]
        constraint = sign(sumExpRew * Q(1, self.size - 1, self.ctx), thr)

        self.console.print(constraint)
        return constraint

    def build_strategy_constraints(self) -> List[z3.BoolRef]:
        # Randomized strategies (proper probability distributions)
        self.console.print('\n# Randomized strategies (proper probability distributions)')
        constraints = []
        for strategy in self.X:
            for rate in strategy:
                constraints.append(rate <= 1)
                constraints.append(rate >= 0)
        # # TODO!: Test if the sum constraint per strategy can be put together, rather than batching all at the end
        # for strategy in self.X:
            constraints.append(Sum(strategy) == 1)

        # TODO!: Check for determinism first and apply binary constraints only (no need for range)
        if self.determinism:
            self.console.print('# Deterministic strategies activated (one-hot encoding or degenerate categorical distribution)\n')
            for strategy in self.X:
                for rate in strategy:
                    constraints.append(Or(rate == 0, rate == 1, self.ctx))

        self.console.print(constraints)
        return constraints

    @abstractmethod
    def build_observation_constraints(self) -> List[z3.BoolRef]:
        raise NotImplementedError()

    @abstractmethod
    def collect_constraints(self, threshold: str) -> List[z3.BoolRef]:
        raise NotImplementedError()
