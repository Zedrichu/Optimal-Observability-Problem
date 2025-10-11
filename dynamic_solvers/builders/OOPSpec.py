from abc import ABC, abstractmethod
from typing import List, Optional, Callable
from io import StringIO

from rich.console import Console
from z3 import (Context, z3, Real, Q, Or, Sum, And, Not, Implies, Bool)

from dynamic_solvers.builders.worlds import World
from dynamic_solvers.utils import parse_threshold


class OOPSpec(World, ABC):
    def __init__(self, budget: int, goal: int,
                 determinism: bool, bool_encoding: bool,
                 ctx: Optional[Context] = None, verbose: bool = False):
        self.ctx = ctx or Context()  # Use provided context or create fresh one
        self.budget = budget
        self.goal = goal
        self.determinism = determinism
        self.bool_encoding = True
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
        if self.bool_encoding:
            if self.determinism:
                bellman_generator = self._compute_state_bellman_bool_det
                self.console.print(
                    "\n# Deterministic strategies with boolean encoding (both strategies and observations).")
            else:
                bellman_generator = self._compute_state_bellman_bool_rand
                self.console.print("\n# Randomised strategies with boolean encoding (observations only).")
        else:
            bellman_generator = self._compute_state_bellman_real
            self.console.print("\n# Strategy and observation variables encoded as reals.")
        equations = []
        for s in range(self.size):
            if s == self.goal:
                equations.append(self.ExpRew[s] == 0)
                continue

            # Decrement the state index after processing the goal state
            idx = s - 1 if s > self.goal else s
            equations.extend(bellman_generator(s, idx))

        self.console.print(equations)
        return equations

    @abstractmethod
    def _compute_state_bellman_bool_det(self, state: int, state_idx: int) -> List[z3.BoolRef]:
        raise NotImplementedError()

    @abstractmethod
    def _compute_state_bellman_bool_rand(self, state: int, state_idx: int) -> List[z3.BoolRef]:
        raise NotImplementedError()

    def _compute_state_bellman_real(self, state: int, state_idx: int) -> List[z3.BoolRef]:
        # Build action terms for each direction using a transition function
        terms = self.initialize_terms()
        for a in range(len(self.actions)):
            action_term = self.build_action_term(a, state_idx)
            next_state = self.navigate(state, a)
            destination_rew = self.build_destination_rew(next_state)
            terms.append(action_term * destination_rew)
        return [z3.BoolRef(self.ExpRew[state] == Sum(terms))]

    def initialize_terms(self):
        """ Initial term in Bellman sum for current state - reward of staying in place.
        Common format of Bellman equations used by default. [See base paper]"""
        return [1]

    def build_destination_rew(self, next_state: int) -> z3.ArithRef:
        """ Expected reward from the state the selected action leads to, to the goal.
        Common format of Bellman equations used by default. [See base paper]"""
        return self.ExpRew[next_state]

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
        """Dispatch to type-specific (encoding-specific) strategy constraints."""
        if self.bool_encoding and self.determinism:
            return self._build_boolean_strategy_constraints()
        else:
            return self._build_real_strategy_constraints()

    def _build_boolean_strategy_constraints(self) -> List[z3.BoolRef]:
        self.console.print("\n# Deterministic strategies (one-hot encoding or degenerate categorical distribution)."
                           "\n# Proper boolean encoding activated for strategy variables.")
        # At least 1 action is enabled from each observation
        constraints = [Or(*[self.X[o][a] for a in range(len(self.actions))], self.ctx)
                       for o in range(len(self.X))
        ]

        # At most 1 action can be enabled from each observation
        constraints.extend([
            Implies(
                self.X[o][a1],
                And(*[Not(self.X[o][a2], self.ctx) for a2 in range(len(self.actions)) if a1 != a2]),
                self.ctx)
            for o in range(len(self.X))
            for a1 in range(len(self.actions))
        ])

        self.console.print(constraints)
        return constraints

    def _build_real_strategy_constraints(self) -> List[z3.BoolRef]:
        # Randomized strategies (proper probability distributions)
        if self.determinism:
            self.console.print(
                '\n# Deterministic strategies (one-hot encoding or degenerate categorical distribution)\n')
        else:
            self.console.print('\n# Randomized strategies (proper probability distributions)')
        constraints = []
        # TODO!: Check for determinism first and apply binary constraints only (no need for range)
        for strategy in self.X:
            # Constrain the probability rates under proper distribution as observation groups
            # if not self.determinism:
            prob_range_constraints = [bound for rate in strategy
                                      for bound in [rate <= 1, rate >= 0]]
            constraints.extend(prob_range_constraints)

            # Strategies must be unitary (rates sum up to 1)
            constraints.append(Sum(strategy) == 1)

            if self.determinism: # One-hot encoding or degenerate categorical distribution
                categorical_constraints = [Or(rate == 0, rate == 1, self.ctx) for rate in strategy]
                constraints.extend(categorical_constraints)

        self.console.print(constraints)
        return constraints

    @abstractmethod
    def build_observation_constraints(self) -> List[z3.BoolRef]:
        raise NotImplementedError()

    @abstractmethod
    def collect_constraints(self, threshold: str) -> List[z3.BoolRef]:
        raise NotImplementedError()
