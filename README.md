# robotiq_3f_ros_pkg

[![](https://github.com/Nishida-Lab/robotiq_3f_ros_pkg/workflows/CI/badge.svg)](https://github.com/Nishida-Lab/robotiq_3f_ros_pkg/actions)

## Description
ROS wrapper package that provides functions related to 3-Finger Gripper control of robotiq package(https://github.com/ros-industrial/robotiq) as ROS service

## Install
```
$ cd your_ws/src
$ git clone https://github.com/davidmartinez13/robotiq.git
$ git clone https://github.com/davidmartinez13/robotiq_3f_ros_pkg.git
$ cd ..
$ rosdep install -iry --from-paths src
$ catkin build
```

## Available ROS services
```
/robotiq_3f_gripper/activate
/robotiq_3f_gripper/reset
/robotiq_3f_gripper/open_hand
/robotiq_3f_gripper/close_hand
/robotiq_3f_gripper/set_mode
/robotiq_3f_gripper/set_position
/robotiq_3f_gripper/set_speed
/robotiq_3f_gripper/set_torque
/robotiq_3f_gripper/get_mode
/robotiq_3f_gripper/get_position
/robotiq_3f_gripper/get_speed
/robotiq_3f_gripper/get_torque
```

## Available gripper mode
- basic
- pinch
- wide
- scissor

## Usage
Spawn simplified robotiq in gazebo:
```
roslaunch robotiq_3f_gazebo spawn_robotiq_3f_gripper.launch
```
Control the gripper with ros services:
- If not on sim, launch the listener:
    ```
    roslaunch robotiq_3f_driver listener.launch ip_address:=192.168.1.11
    ```

- If in sim, load macro gripper:
    ```
    roslaunch robotiq_3f_gripper_articulated_gazebo robotiq_gripper_empty_world_macro.launch
    ```
    Then launch the listener for sim:
    ```
    roslaunch robotiq_3f_driver listener_sim.launch
    ```
    Both ways the ROS services and gripper will be activated.

Try sending some commands as:

```
rosservice call /robotiq_3f_gripper/activate
rosservice call /robotiq_3f_gripper/set_mode wide
rosservice call /robotiq_3f_gripper/set_position 200
rosservice call /robotiq_3f_gripper/set_position 150
rosservice call /robotiq_3f_gripper/set_position 0
```

## CI
Replace the repository specific keywords in the above link as follows:
- `<your_repo>` -> `robotiq_3f_ros_pkg`
- `<your_pkg>` -> `robotiq_3f_control`, `robotiq_3f_description`, `robotiq_3f_driver`, `robotiq_3f_gazebo`, `robotiq_3f_srvs`
- `<your_rosinstall_dir>` -> `.`
