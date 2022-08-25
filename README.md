# Human Robot Interaction(HRI)
![](Images/IMG_6493.JPG)
## What is HRI? 
Human Robot Interaction(HRI) is the field of studies dedicated to the understanding and evaluation of robotic systems for the use by or with humans. This interaction involves the communication or direct involvement with someone or something. In our case this refers to the constant communication between the robot and the human via messages. Among the different types of interactions we can find visual interaction, touch interaction or sound interaction. 

Consequently, this project aims to develop different concepts for the cooperation between an industrial-like robot and a human operator. For this purpose, the sensor systems LeapMotion and Astra are used to determine the motion of the human operator. The motion is provided directly in a skeleton model. Thus the robot(ReactorX-150) acquires the ability to interact in the smoothest possible way.

## Requierments
You should have [Ubuntu 20.04](https://releases.ubuntu.com/20.04/), [ROS Noetic](http://wiki.ros.org/noetic), [Leap Motion SDK](https://developer.leapmotion.com/tracking-software-download), [Python 2](https://www.python.org/downloads/release/python-272/), and [Python 3](https://www.python.org/downloads/) installed on your device.
## Features

## Documentation and Enviornment setup
The documentation of this repository can be found [here](). This documentation includes a description of the sensors and the robot arm which were used to develop and test the industrial-like interaction.

For more information on how to perfom the correct installation of the requierments mentioned before and the correct environemtal setup please refer to [Chapter 5 subsection 1]() from the documentation.
## Installation
**1.** Go to the source folder of your catkin workspace.
```bash 
cd ~/catkin_ws/src
git clone https://github.com/Jasv06/human_robot_interaction.git
cd ~/catkin_ws
catkin_make
```
**2.** Source your current catkin workspace.
```bash 
source ~/catkin_ws/devel/setup.bash
```
