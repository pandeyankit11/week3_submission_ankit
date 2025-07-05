# Week 3 Submission – Ankit Pandey (kratos_ankit)

This repository contains the ROS 2 nodes and custom interfaces for the Week 3 assignment on Electronics and Controls.

## Package Structure

- ROS 2 Package Name: `kratos_ankit`
- Interface Package: `kratos_ankit_interfaces`



##  Question-wise File Mapping

###  Question 1: Hello World Publisher & Subscriber

- `q1_publisher.py` – Publishes "Hello World!" to `/new` at 15 Hz.
- `q1_subscriber.py` – Subscribes to `/new` and prints received messages.

###  Question 2: Signal S1, S2 Switching System

- `q2_publisher.py` – Publishes `'green'` for 10 seconds, then `'red'` on `/s1`.
- `q2_controller.py` – Subscribes to `/s1` and publishes opposite color to `/s2`.

###  Question 3: Mars Rover Status Monitoring

- Custom Message: `RoverStatus.msg` (in `kratos_ankit_interfaces/msg`)
- `q3_publisher.py` – Publishes combined data: velocity (`Twist`), position (`Pose`), battery, distance, and time.
- `q3_subscriber.py` – Subscribes to `/rover_status` and prints each field.

###  Question 4: Digital Clock System

- `q4_pub1.py` – Publishes count on `/second` at 1 Hz.
- `q4_pub2.py` – Increments `/minute` and `/hour` based on `/second`.
-  `q4_sub1.py` – Subscribes to `/second`.
- `q4_sub2.py` – Subscribes to all three and publishes final time `HH:MM:SS` on `/clock`.



##  Bonus Question: ROS 2 Action – Robotic Arm Controller

- Custom Action: `MoveArm.action` (in `kratos_ankit_interfaces/action`)
- `q5_action_client.py` – Implements a server that moves the arm 1° per second toward a target.
- `q5_action_client.py` – Sends goal angle and receives feedback/result from server.



##  RQT Graph – Question 4

> ![RQT Graph - Q4](rqt_graph_q4.png)
// I was unable to minimise the graph , therefore only half graph is visible.

The RQT graph above shows the pub-sub relationships between `/second`, `/minute`, `/hour`, and `/clock`.



##  Notes

- All code is written in **Python** but uses `ament_cmake` as the build system.
- The package builds cleanly using `colcon build` and runs via `ros2 run`.
- Topics are properly named and logged for testing in `rqt_graph` and `ros2 topic echo`.



##  How to Build & Run

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
