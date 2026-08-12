# Robot Obstacle Avoidance — A Progression

A series of ROS2 projects building up autonomous obstacle-avoidance behavior, starting simple and getting more capable at each stage. Rather than jumping straight to a "finished" navigation system, this repo shows the actual path: naive reactive avoidance first, then real physics, then smarter decision-making — with a working robot and working code at every step.

## Why

I wanted to learn ROS2 by building, not just reading. Each stage below was a real working system before I moved to the next one — nothing here is a stub or a plan, only the final stages are aspirational.

## Stages

| Stage | Environment | What it does | Status |
|---|---|---|---|
| [01 — Turtlesim Wall Avoider](./turtle_avoider) | `turtlesim` (2D, no physics) | A simulated turtle avoids the edges of its box by turning when it gets close to a boundary | ✅ Done |
| [02 — Gazebo Obstacle Avoider](./gazebo_avoider) | Gazebo (real 3D physics) + TurtleBot3 | A real simulated robot uses lidar to detect and avoid a physical obstacle in real time | ✅ Done |
| 03 — Smart Clearance Avoider | Gazebo + TurtleBot3 | Instead of always turning the same direction, the robot checks which side has more clearance and turns toward open space | 🔜 Planned |
| 04 — Nav2 Goal Navigation | Gazebo + Nav2 | Full path planning to a goal point using mapping (SLAM) instead of purely reactive avoidance | 🔜 Planned |

## What changed between stages so far

**Stage 1 → 2** was the big jump: from an abstract 2D point with a single (x, y) position, to a real robot with actual physics (momentum, collisions) reading an array of lidar distances instead of one coordinate. The core control pattern — subscribe to sensor data, decide, publish a velocity command — stayed the same; what changed was the sensor complexity and the realism of the simulation.

## Setup

Each stage folder has its own README with exact run instructions, since the environment setup differs (turtlesim needs nothing extra; Gazebo needs TurtleBot3 packages installed). General requirement across all stages: ROS2 Humble on Ubuntu 22.04.
