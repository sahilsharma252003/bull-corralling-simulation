# 🤖 Robotic Agent Simulation for Bull Corralling

This project simulates a robotic agent tasked with corralling a bull into a target cell within a 13x13 grid, navigating obstacles and accounting for adversarial behavior. The approach models the environment as a finite Markov Decision Process with an absorbing state and computes the optimal expected number of rounds using value iteration.

---

## 🎯 Objective

To simulate and solve a dynamic multi-agent environment where a robot must guide a bull into a fixed target position under probabilistic conditions and movement constraints.

---

## 🧠 Theoretical Framework

- **Finite State Space**: 161 × 161 = 25,921 valid game states (excluding obstacles, overlaps)
- **Absorbing State**: Target cell (7,7) ends the game once the bull arrives
- **Robot Advantage**:
  - Moves in 8 directions (including diagonals)
  - Always moves before the bull
- **Bull Behavior**:
  - Moves in 4 directions (orthogonal only)
  - Moves randomly if robot is far
  - Moves toward robot if within 5x5 proximity

---

## 🧪 Methodology

- **Algorithm**: Value Iteration with convergence threshold (ε = 0.01)
- **Initialization**:
  - T*(target, any_robot_pos) = 0
  - T* = ∞ for all other state pairs
- **Update Rule**:
  T*(posB, posC) = 1 + min over robot_moves [average of T*(new_bull, new_robot)]

- **Heuristic**:
  - Admissible and consistent Manhattan distance used for estimating lower bounds of T*

---

## 🧾 Files

- `bull_corralling_simulation.py`: Full simulation code
- `CS440 - Assignment 3 (final).pdf`: Complete theoretical breakdown, analysis, and proof of convergence

---

## 📊 Results

- **Starting State**:
  - Bull at (1,12)
  - Robot at (12,0)
- **Expected Time**: ≈ 18.11 rounds to successfully corral the bull to the target (7,7)

---

## 💡 Insights

- The robot can always win in finite time from any position due to the finite state space and the probabilistic movement model
- Obstacles near the target limit the robot’s mobility, creating a high-risk endgame
- A well-positioned robot can influence the bull while avoiding being trapped or “crushed”

---

## 📄 License

For academic and research purposes. Created by Sahil Sharma and Rahul Sankaralingam.
