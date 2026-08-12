# Stage 1 — Turtlesim Wall Avoider

The starting point: a simulated turtle in ROS2's built-in 2D simulator that avoids the walls of its box by continuously checking its position and turning when it gets close to an edge.

## How it works

The node subscribes to `/turtle1/pose`, which gives the turtle's current `x` and `y` coordinates on every update. If either coordinate is near the boundary of the box (turtlesim's world is roughly 0–11 on both axes), it publishes a `Twist` command that turns the turtle while creeping forward slightly — the slight forward motion is what actually moves it out of the danger zone; turning alone doesn't change position, only heading, so a pure "stop and spin" version got stuck oscillating at the wall.

This is a reactive, closed-loop system: sense → decide → act, running continuously.

## Run it

```bash
ros2 run turtlesim turtlesim_node
```
In a second terminal, place `wall_avoider.py` in a ROS2 package's Python module folder (`ament_python` build type, depends on `rclpy` and `geometry_msgs`), register it in `setup.py` under `console_scripts`, build with `colcon build`, then:
```bash
ros2 run <your_package_name> wall_avoider
```

## What I learned

The wall-detection condition alone wasn't enough — checking "am I near a wall" and then only turning (no forward motion) meant the turtle could satisfy that condition forever without ever escaping it, since spinning in place doesn't change x/y. Adding a small forward speed during the turn fixed it. Small thing, but a good reminder that a robot's *state* (position) and its *actions* (turning) aren't the same thing, and a control loop needs to actually change the state to escape a condition based on it.
