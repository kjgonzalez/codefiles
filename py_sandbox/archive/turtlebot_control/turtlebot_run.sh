#!/bin/sh
# Author: Kris Gonzalez
# DateCreated: 180528
# Objective: shorthand for turtlebot simulation environment. use AFTER roscore!
export TURTLEBOT_GAZEBO_WORLD_FILE=/usr/share/gazebo-7/worlds/empty.world
# launch turtlebot base environment
roslaunch turtlebot_gazebo turtlebot_world.launch