# RL-Based Sensor Selection Summary for POMDP/TPMC Framework

This document summarizes the architecture, goals, and implementation plan for integrating a reinforcement learning (RL) module into a POMDP/TPMC-based optimization pipeline for learning observation assignments (sensor placements). It provides all context necessary for an automated coding assistant to contribute effectively to the project.

---

## 1. Problem Setting

We work with a parametric POMDP/TPMC modeling framework where:

- The system dynamics, rewards, and state-transition constraints are encoded symbolically.
- The **observation function** is **not fixed** and depends on a vector **Y** specifying sensor placement or observation assignments.
- For any fixed vector **Y**, the induced POMDP is fully defined.

The key components:

- **Y**: Sensor/observation assignment vector (often binary or integer per state).
- **X**: Action-level strategy variables synthesized by the oracle.
- **Rewards**: Computed from the POMDP once Y and X are fixed.

We use an SMT-based oracle (Z3) to compute the **optimal MinExpRew** for the POMDP induced by a specific Y.

---

## 2. Oracle Interface

The oracle exposes a function:

```
def evaluate_pomdp(self, pomdp_adapter, obs_function: list[int], timeout_ms: int) -> ResultOOP:
    """
    Evaluate a POMDP with a specific observation function via push/pop.
    Adds Bellman constraints induced by Y and solves for the optimal reward.
    """
```

This function returns:

- The POMDP optimal strategy for that Y
- The optimal reward
- Solve performance metrics

The oracle is expensive but exact, making it suitable for RL-as-black-box evaluation.

---

## 3. Goal: Learn Y via Reinforcement Learning

We want:

- An RL module that searches over Y-space
- Uses the oracle as a reward function (returning MinExpRew = minimum expected steps to goal)
- Learns sensor configurations Y that **minimize MinExpRew** (fewer steps to reach goal)
- Optionally supports transfer to modified world layouts or goals

The RL operates **above** the oracle and does not interact with the POMDP step-by-step.

**Note**: The oracle returns a positive value (expected number of steps with +1 reward per step). We perform **gradient descent** to minimize this value.

---

## 3A. Alternative Architecture: Two-Learner System with POMDP Simulation

### Motivation

The current architecture uses the SMT oracle as a black-box reward function. While exact, this has limitations:
- **Expensive evaluation**: SMT solving can take seconds to minutes per Y
- **Limited exploration**: Only 40-200 Y samples feasible per training run
- **No intermediate data**: Oracle returns only final optimal reward, no trajectory information

We have a **POMDP simulation environment** (`LinePOMDPEnv`, `GridPOMDPEnv`, `MazePOMDPEnv`) that can provide:
- Fast experience collection (1000s of environment steps/second)
- Trajectory data for richer learning signals
- Support for policy learning algorithms

### Two-Learner Architecture

```
┌────────────────────────────────────────────────────┐
│  Meta-Learner (Observation Function Optimizer)     │
│  - Samples Y ~ π_θ(Y) (same as current)            │
│  - Updates θ to minimize expected steps            │
└──────────────┬─────────────────────────────────────┘
               │ Y (observation function)
               ↓
┌────────────────────────────────────────────────────┐
│  Policy Learner (Strategy Optimizer)               │
│  - Given fixed Y, learns policy π(a|o)             │
│  - Trains in POMDP simulation environment          │
│  - Returns: average steps to goal over N trials    │
└────────────────────────────────────────────────────┘
```

**Bi-level Optimization:**
- **Inner loop**: For fixed Y, learn optimal policy π*(Y) via RL in simulation
- **Outer loop**: Optimize Y to minimize E[steps | π*(Y)]

### Implementation Outline

**Policy Learner Component:**
```python
class PolicyLearner:
    """Learns optimal policy for a fixed observation function."""

    def __init__(self, env_config, algorithm='PPO'):
        self.algorithm = algorithm  # PPO, DQN, A2C, etc.

    def train_and_evaluate(self, Y, n_episodes=100, n_trials=10):
        """
        Train policy for observation function Y.

        Returns:
            avg_steps: Average steps to goal (reward for meta-learner)
        """
        env = create_env(obs_function=Y, **env_config)
        policy = create_policy()

        # Train policy for n_episodes
        for ep in range(n_episodes):
            trajectory = rollout(env, policy)
            policy.update(trajectory)

        # Evaluate trained policy
        avg_steps = evaluate(policy, env, n_trials)
        return avg_steps
```

**Modified Meta-Learner Training:**
```python
def train_meta_learner(meta_agent, policy_learner, episodes=200):
    for ep in range(episodes):
        Y, probs = meta_agent.sample()

        # CHANGE: Use policy learner instead of oracle
        avg_steps = policy_learner.train_and_evaluate(Y)
        reward = avg_steps  # Minimize steps

        # Same REINFORCE update as before
        meta_agent.update(Y, probs, reward)
```

### Advantages

| Aspect | Oracle-Based | Two-Learner (Simulation) |
|--------|--------------|--------------------------|
| Y evaluations/sec | ~0.1-1 | ~10-100 |
| Total Y explored | 40-200 | 1000s+ |
| Policy quality | Optimal (exact) | Approximate (learned) |
| Scalability | Poor (timeout issues) | Good |
| Data richness | Single reward value | Full trajectories |

### Hybrid Approach (Recommended)

Combine both methods for best results:

**Phase 1 - Exploration (80% of training):**
- Use policy learner for fast Y evaluation
- Sample many observation functions
- Build cache of top-k best Y candidates

**Phase 2 - Exploitation (20% of training):**
- Re-evaluate top-k Y with oracle (exact)
- Fine-tune θ around validated regions
- Use oracle for final Y selection

**Benefits:**
- Fast exploration via simulation
- Exact evaluation via oracle
- Best of both worlds

### Considerations

**Challenges:**
1. Policy learning noise → Use multiple trials, stable algorithms (PPO)
2. Expensive per-Y evaluation → Parallel training, transfer learning
3. Policy ≠ optimal → Use oracle for validation

**When to Use:**
- **Oracle only**: Small state spaces, need provable optimality
- **Simulation only**: Large state spaces, oracle times out
- **Hybrid**: Medium instances, balance speed and accuracy

---

## 4. Minimal RL Approach (Naive REINFORCE)

We parameterize a policy over Y. Two versions are supported:

### **4.1 Binary Observation Assignments (0/1)**
- Each sensor decision `Y[i]` follows a Bernoulli distribution with probability `p[i] = sigmoid(theta[i])`.
- `theta` is a real-valued parameter vector.
- Sampling is done independently per position.
- This is useful for simple ON/OFF sensor placement.

### **4.2 Multi-Class Observation Assignments (1..8)**
For richer observation functions, each position selects one of several possible observation classes:

- `Y[i]` ∈ {1, 2, ..., 8}
- Each state i has 8 logits: `theta[i, 1..8]`
- These logits define a categorical distribution via a softmax:

```
p[i,k] = exp(theta[i,k]) / sum_j exp(theta[i,j])
```

- Sampling: `Y[i] = sample from Categorical(p[i,1..8])`
- `Y` is passed directly to the oracle as the observation assignment.

### **REINFORCE Update (Binary or Multi-Class) - MINIMIZATION**
After receiving reward R(Y):

- **Binary case (gradient descent for minimization):**
```
grad = (Y - probs)
advantage = R(Y) - baseline
theta -= lr * advantage * grad  # Note: MINUS sign for minimization
```

- **Multi-class case (gradient descent for minimization):**
```
onehot = indicator_vector(Y[i])
grad = onehot - probs[i]
advantage = R(Y) - baseline
theta[i] -= lr * advantage * grad  # Note: MINUS sign for minimization
```

In both cases:
- `baseline` is a running average of rewards to reduce variance
- The **negative sign** implements gradient descent to **minimize** the expected reward (number of steps)

---

## 5. Minimal Prototype Workflow

1. Initialize parameter vector `theta` of size N (number of sensor positions).
2. For each iteration:
   - Sample Y from Bernoulli(theta)
   - Call oracle.evaluate\_pomdp(Y)
   - Update `theta` with REINFORCE
3. After many iterations, the probabilities converge to a near-optimal Y.

This minimal setup requires less than 100 lines of code.

---

## 6. Practical Enhancements

To improve stability and efficiency:

### 6.1. Caching

Oracle calls are expensive. Memoize `(Y → reward)` pairs.

### 6.2. Batch Sampling

Sample multiple Y's per iteration to reduce variance.

### 6.3. Budget Constraints

If exactly K sensors must be active:

- Sample Bernoulli(Y) then project to the top-K probabilities.

### 6.4. Timeout Handling

If solver times out or returns unsat:

- Assign a default penalty reward (large positive value for minimization)
- The penalty should be worse than any valid solution to discourage infeasible configurations
- Skip or partially update theta based on the penalty

### 6.5. Logging

Track:

- Rewards
- Oracle solve times
- Y distributions

---

## 7. Generalization Across Worlds (Advanced)

To reuse learnings when:

- World dimensions change
- Goal states change

We can:

### 7.1. Parameterize Theta by Features

Replace:

- `theta[i]` = free parameter With:
- `theta[i] = f(features_at_state_i)`

This enables transfer across different environment layouts.

### 7.2. Learn a Surrogate Reward Model

Train neural surrogate:

```
R_hat(Y) ~ R(Y)
```

To reduce oracle calls and support Bayesian optimization.

### 7.3. Meta-Learning

Use MAML or similar to produce an initialization that quickly adapts to new worlds.

---

## 8. Mapping to RL Theory

Relevant RL concepts:

- **Policy gradients (3.4)**: Used to optimize theta
- **Baselines (3.5)**: Reduce variance
- **POMDPs (5.2)**: Explain how Y affects belief updates
- **Observability (2.3)**: Y defines the observation function
- **Model-based RL (4.1)**: Oracle is an exact model
- **Hybrid learning (4.2)**: Mix model/learning for efficiency

---

## 9. Summary of What the Agent Must Implement

### Minimal Requirements:

- Policy class for sampling Y from theta
- REINFORCE update
- Oracle call wrapper
- Caching
- Training loop

### Optional Extensions:

- Budget constraints
- Batch updates
- Feature-based theta
- Reward surrogate
- Meta-learning

---

## 10. Deliverables for a Coding Agent

A Claude code agent should be able to:

- Implement the minimal RL framework
- Integrate it with the existing oracle
- Create an experimentation script
- Add caching and logging
- (Optionally) implement budget and batching
- Provide hooks for future surrogate or meta-learning modules

---

This summary provides all the necessary context, constraints, architecture, and requirements for building an RL-driven sensor selection system for POMDP observation assignment learning.

