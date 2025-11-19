import numpy as np
from z3 import sat, unsat, unknown

from builders.ssp import LineTPMC
from dynamic_solvers.TPMCSolver import TPMCSolver
from dynamic_solvers.builders.POMDPSpec import POMDPAdapter


class SensorSelectionAgent:
    """Agent for sensor selection problem (SSP) with binary observations (0/1) using Bernoulli distribution."""

    def __init__(self, goal: int, n_states: int, lr: float = 0.05, init_strategy: str = "uniform", init_bias: float = 0.0):
        """
        Args:
            goal: Goal state index
            n_states: Number of states
            lr: Learning rate
            init_strategy: Initialization strategy - "uniform", "spatial_split", "distance_decay"
            init_bias: Initial logit bias for uniform strategy
        """
        self.n = n_states
        self.goal = goal
        self.lr = lr

        # theta[i] is the logit for P(obs=1) at state i
        self.theta = self._initialize_theta(init_strategy, init_bias)
        self.theta[goal] = 0  # Goal doesn't matter
        self.baseline = 0.0 # prevent random noise from destabilizing the update

    def _initialize_theta(self, strategy: str, init_bias: float) -> np.ndarray:
        """
        Initialize theta with spatial awareness.

        Strategies:
            - "uniform": All states get the same bias
            - "spatial_split": States on the same side of the goal get high correlation
            - "distance_decay": Sensor probability decreases with distance from goal
        """
        theta = np.zeros(self.n, dtype=float)

        if strategy == "uniform":
            # All states have the same initial bias
            theta[:] = init_bias

        elif strategy == "spatial_split":
            # States on left of goal biased toward sensors, right toward no-sensors
            # This encourages different strategies on each side
            for i in range(self.n):
                if i < self.goal:
                    theta[i] = 3  # Bias toward sensors on the left
                elif i > self.goal:
                    theta[i] = -3  # Bias against sensors on the right
                # Goal gets 0 (will be set outside)

        elif strategy == "distance_decay":
            # States closer to goal more likely to have sensors
            for i in range(self.n):
                if i != self.goal:
                    distance = abs(i - self.goal)
                    max_dist = max(self.goal, self.n - self.goal - 1)
                    # Closer → higher probability
                    normalized_dist = distance / max_dist
                    theta[i] = 2.0 * (1 - normalized_dist)  # Range [0, 2]

        else:
            raise ValueError(f"Unknown init_strategy: {strategy}")

        return theta

    def sigmoid(self, x):
        """Numerically stable sigmoid."""
        return np.where(x >= 0,
                       1 / (1 + np.exp(-x)),
                       np.exp(x) / (1 + np.exp(x)))

    def sample(self, budget: int | None = None, enforce_budget: bool = False):
        """
        Sample binary observation assignment Y.

        Args:
            budget: Maximum number of active sensors (obs=1)
            enforce_budget: If True, enforce exact budget via top-k selection

        Returns:
            Y: Observation assignment
            probs: Sampling probabilities
        """
        probs = self.sigmoid(self.theta)

        # Hard Constraint on Budget during Inference
        if enforce_budget and budget is not None:
            # Hard constraint: select top-k states by probability
            Y = [0] * self.n

            # Get indices sorted by probability (excluding goal)
            indices = [(i, probs[i]) for i in range(self.n) if i != self.goal]
            indices.sort(key=lambda x: x[1], reverse=True)

            # Activate top budget sensors
            for i in range(min(budget, len(indices))):
                state_idx = indices[i][0]
                Y[state_idx] = 1

            Y[self.goal] = -1
        else:
            # Soft constraint: sample independently
            Y = []
            for i in range(self.n):
                if i == self.goal:
                    Y.append(-1)
                else:
                    Y.append(1 if np.random.rand() < probs[i] else 0)

        return Y, probs

    def update(self, Y: list[int], probs: np.ndarray, reward: float):
        """REINFORCE update for Bernoulli distribution."""
        self.baseline = 0.9 * self.baseline + 0.1 * reward
        advantage = reward - self.baseline

        for i in range(self.n):
            if i == self.goal:
                continue

            # Gradient: (y - p) where y ∈ {0,1} is sample, p is probability
            grad = Y[i] - probs[i]
            self.theta[i] += self.lr * advantage * grad


def train(agent: SensorSelectionAgent, oracle: TPMCSolver, pomdp: POMDPAdapter,
          episodes: int = 200, budget: int | None = None, timeout: int = 10000,
            penalty_unsat: float = -50, penalty_timeout: float = -100,
          budget_penalty: float = 0.0):
    """
    Train SSP agent with oracle feedback.

    Args:
        budget: Target budget for sensor placement
        budget_penalty: Penalty per sensor over budget (0 = no penalty)
    """

    stats = {'sat': 0, 'unsat': 0, 'timeout': 0, 'best_reward': float('-inf'), 'best_Y': None}

    for ep in range(episodes):
        Y, probs = agent.sample()
        n_active = sum(1 for y in Y if y == 1)
        result = oracle.evaluate_pomdp(pomdp, Y, timeout)

        if result.result == sat:
            reward = float(result.reward.as_fraction())

            # Apply budget penalty if over budget
            if budget is not None and n_active > budget:
                reward -= budget_penalty * (n_active - budget) # Soft Constraint on Budget during Training

            stats['sat'] += 1
            if reward > stats['best_reward']:
                stats['best_reward'] = reward
                stats['best_Y'] = Y.copy()
        elif result.result == unsat:
            reward = penalty_unsat
            stats['unsat'] += 1
        else:
            reward = penalty_timeout
            stats['timeout'] += 1

        agent.update(Y, probs, reward)

        if ep % 10 == 0:
            print(f"EP {ep:03d} | R={reward:7.2f} | B={agent.baseline:7.2f} | "
                  f"SAT={stats['sat']:3d} UNSAT={stats['unsat']:2d} TO={stats['timeout']:2d} | "
                  f"Active={n_active}/{budget if budget else '?'}")

    return agent, stats

if __name__ == "__main__":
    budget = 29
    size = 61
    goal = 30
    tau = "31 / 2"
    threshold_q = "4"
    threshold = f"<= {tau} * {threshold_q}"
    tpmc = LineTPMC(budget, goal, size, determinism=False, verbose=False)
    context = tpmc.ctx
    pomdp = POMDPAdapter(tpmc)

    solver = TPMCSolver(context, verbose=True)
    solver.prepare_constraints(pomdp, threshold)

    agent = SensorSelectionAgent(goal, n_states=size, init_strategy="spatial_split")

    # Training: soft guidance toward budget
    trained_agent, stats = train(agent, solver, pomdp, episodes=40, budget=budget,
                                 timeout=10000, budget_penalty=0.5)

    # Inference: enforce exact budget via top-k
    final_Y, _ = trained_agent.sample(budget=budget, enforce_budget=True)
    n_active_final = sum(1 for y in final_Y if y == 1)

    print(f"\nBest Y: {stats['best_Y']}")
    print(f"Best reward: {stats['best_reward']}")
    print(f"Final inference Y has {n_active_final} active sensors (budget={budget})")
