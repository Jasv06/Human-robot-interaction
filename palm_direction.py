import rospy
import numpy as np
import roslib
import time 
import sys
from std_msgs.msg import Float32
from geometry_msgs.msg import Point
from std_msgs.msg import Int32 

from human_robot_interaction.msg import *

x_basis_of_palm = [0,0,0]
y_basis_of_palm = [0,0,0]
z_basis_of_palm = [0,0,0]

def palm_direction_sensor(data):
	
	global x_basis_of_palm
	global y_basis_of_palm
	global z_basis_of_palm
	
	x_basis_of_palm[0] = data.x_basis[0]
	x_basis_of_palm[1] = data.x_basis[1]
	x_basis_of_palm[2] = data.x_basis[2]
	y_basis_of_palm[0] = data.y_basis[0]
	y_basis_of_palm[1] = data.y_basis[1]
	y_basis_of_palm[2] = data.y_basis[2]
	z_basis_of_palm[0] = data.z_basis[0]
	z_basis_of_palm[1] = data.z_basis[1]
	z_basis_of_palm[2] = data.z_basis[2]
	
def main():
	
	rospy.init_node('palm_direction')
	
	pub = rospy.Publisher('palm_direction_for_robot', up_or_down, queue_size = 1)
	
	r = rospy.Rate(10)
	
	print("Direction of palm node initialized!!")
	
	while not rospy.is_shutdown():
		
		palm_orientation = up_or_down()	
		
		palm_orientation.pointing_up = False 
		palm_orientation.pointing_down = False		
				       
		rospy.Subscriber("hand_orientation", orientation, palm_direction_sensor)
		
		x_orientation = x_basis_of_palm
		y_orientation = y_basis_of_palm
		z_orientation = z_basis_of_palm
		
		if y_orientation[1] < 0:
			palm_orientation.pointing_up = True 
			palm_orientation.pointing_down = False
			
		elif y_orientation[1] > 0:
			palm_orientation.pointing_up = False 
			palm_orientation.pointing_down = True 
		
		pub.publish(palm_orientation)
		r.sleep()
		
if __name__ == '__main__':
	main()
