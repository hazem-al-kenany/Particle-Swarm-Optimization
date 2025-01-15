# Particle Swarm Optimization (PSO) Simulation

This project implements a **Particle Swarm Optimization (PSO)** algorithm, a population-based optimization technique inspired by the social behavior of birds and fish. The objective is to minimize a function (distance from the origin) by iteratively updating agent positions and velocities based on individual and group performance.

---

## Features

### Particle Swarm Optimization Algorithm
- **Agents**:
  - Each agent has a position (`x, y`) and velocity.
  - Agents maintain their personal best position and value.
- **Global Best**:
  - Tracks the best position and value among all agents.
- **Velocity Update**:
  - Combines:
    - **Inertia**: Preserves a portion of the current velocity.
    - **Cognitive Component**: Moves towards the agent's personal best.
    - **Social Component**: Moves towards the global best.

### Objective Function
- Evaluates how "good" a position is:
  - Uses the Euclidean distance from the origin (`0,0`).

### Simulation
- **Initialization**:
  - Agents are randomly initialized in a search space (`-50 to 50`).
  - Velocities are initialized between `-1` and `1`.
- **Iterations**:
  - Agents iteratively update their positions and velocities for `100` iterations.
- **Output**:
  - Tracks the best global position and value.

---

## Code Structure

### Classes and Functions

#### **Agent**
- Represents an individual particle.
- Attributes:
  - `position`: Current position of the agent.
  - `velocity`: Current velocity of the agent.
  - `personal_best`: Best position found by the agent.
  - `personal_best_value`: Value of the objective function at `personal_best`.

#### **Objective Function**
- Function: `objective_function(position)`
- Returns the Euclidean distance of the position from the origin.

#### **Initialization**
- Function: `initialize_agents(num_agents, space_size)`
- Initializes agents with random positions and velocities.

#### **Velocity Update**
- Function: `update_velocity(agent, global_best, c1, c2)`
- Updates velocity based on inertia, cognitive, and social components.

#### **Position Update**
- Function: `update_position(agent)`
- Moves agents by updating their positions using the updated velocity.

#### **Simulation**
- Function: `run_simulation(agents, iterations)`
- Executes the optimization process:
  - Updates velocities and positions.
  - Tracks personal and global bests.

#### **Output**
- Function: `print_agent_positions(agents, global_best, title)`
- Prints agent positions and the global best.

---

## How to Run

### Prerequisites
- Python 3.7 or higher.

### Running the Simulation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-folder>
