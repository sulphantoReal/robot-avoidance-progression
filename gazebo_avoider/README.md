# Stage 2 — Gazebo Obstacle Avoider

A real TurtleBot3 (Burger) in a physics-simulated Gazebo world, using lidar to detect and avoid obstacles in real time — the same reactive control pattern as Stage 1, but with real sensor data and real physics instead of an abstract 2D position.

## How it works

The node subscribes to `/scan` (a `LaserScan` message — an array of distance readings swept around the robot). It looks at a ~30-degree cone directly in front of the robot (the first and last 15 readings in the array, since index 0 corresponds to straight ahead), filters out invalid `0.0` readings, and checks the closest valid distance in that cone. If anything is within 0.5 meters, it stops and turns; otherwise it drives forward at a slow, safe speed.

## Run it

Requires ROS2 Humble + Gazebo (Classic) + TurtleBot3 packages (`ros-humble-turtlebot3`, `ros-humble-turtlebot3-simulations`) installed, and `TURTLEBOT3_MODEL=burger` set in your environment.

Terminal 1:
```bash
ros2 launch turtlebot3_gazebo empty_world.launch.py
```
Place an obstacle in the world using Gazebo's Insert panel. Terminal 2 (same package/build setup as Stage 1):
```bash
ros2 run <your_package_name> obstacle_avoider
```

## What I learned

- **Gazebo has two incompatible generations** (Classic vs. Ignition/Fortress) that can both be installed on the same machine, and ROS2 packages aren't always wired to the one you expect. I hit a `Service /spawn_entity unavailable` error because TurtleBot3's launch files targeted Gazebo Classic's `gazebo_ros` bridge while I assumed I was running Ignition. Learned to actually check which simulator a launch file expects rather than assuming based on which one I'd installed.
- **Lidar data isn't always clean.** Some readings come back as `0.0` instead of a real distance or infinity, which will silently break a naive "find the minimum distance" check if you don't filter for valid readings first.
- **Simulating physics is genuinely heavier than 2D simulation** — worth checking your machine is on AC power (not battery) before running Gazebo, since throttling can cause behavior that looks like a bug but is actually just reduced performance.
