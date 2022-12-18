cmake_minimum_required(VERSION 3.0.2)
project(human_robot_interaction)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
  message_generation
)

 add_message_files(
   FILES
   JointGroupCommand.msg
   JointSingleCommand.msg
   handstatus.msg
   orientation.msg
   up_or_down.msg
)

generate_messages(
  DEPENDENCIES
   geometry_msgs 
   std_msgs
 )

catkin_package(
  CATKIN_DEPENDS geometry_msgs roscpp rospy std_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/demonstrator_hold_hand/hand_life_demonstrator.py scripts/demonstrator_hold_hand/hand_status_demonstrator.py scripts/demonstrator_hold_hand/LeapListener_demonstrator.py scripts/demonstrator_hold_hand/Leap_server_demonstrator.py scripts/demonstrator_hold_hand/robot_control_demonstrator.py
scripts/Industrial_like_robot/hand_life_industrial.py scripts/Industrial_like_robot/hand_status_industrial.py scripts/Industrial_like_robot/LeapListener_industrial.py scripts/Industrial_like_robot/Leap_server_industrial.py scripts/Industrial_like_robot/robot_control_industrial.py scripts/Industrial_like_robot/hand_rate_of_change.py scripts/Industrial_like_robot/palm_direction.py scripts/Industrial_like_robot/robot_control_industrial_2.py scripts/Industrial_like_robot/robot_control_industrial_3.py scripts/Industrial_like_robot/robot_control_industrial_4.py
DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
