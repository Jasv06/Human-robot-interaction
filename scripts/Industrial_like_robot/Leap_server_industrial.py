import socket
import sys
import numpy as np
import rospy
import time 
from std_msgs.msg import Float32
from geometry_msgs.msg import Point
from std_msgs.msg import Int32
import struct
from human_robot_interaction.msg import * 

localIP = "127.0.0.1"
Port = 57410

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((localIP, Port))
  
print("Do Ctrl+c to exit the program !!")
print("####### Server is listening and publishing #######")
   
def leap_data():
  
  rospy.init_node('Leap_data', anonymous = False)  
  
  """Number of hands"""
  pub_number_of_hands = rospy.Publisher('HandNumber', Float32, queue_size = 1)
  
  """Hand state"""
  pub_hand_state = rospy.Publisher('hand_state', Float32, queue_size = 1)
  
  
  """hand publishers"""
  pub_hand_id = rospy.Publisher('hand_id', Float32, queue_size = 1)
  pub_palm_position_stable = rospy.Publisher('hand_position_stable', Point, queue_size = 1)
  pub_life_of_hand = rospy.Publisher('life_of_hand', Float32, queue_size = 1)
  pub_hand_orientation = rospy.Publisher('hand_orientation', orientation, queue_size = 1)
  pub_hand_rate_of_change = rospy.Publisher('hand_rate_of_change', Point, queue_size = 1)
  
  rate = rospy.Rate(50)
  
  while not rospy.is_shutdown():
  
     coordinates = Point() 
     rate_of_change = Point()
     orientation_of_hand = orientation()
    
     data, address = s.recvfrom(4096)
          
     data = struct.unpack('<21f', data)      
     
     number_of_hand_in_frame = data[0]
     
     strength = data[1]
     
     hand_identifier = data[2]
          
     coordinates.x = data[3]*0.001
     coordinates.y = data[4]*0.001
     coordinates.z = data[5]*0.001
     
     life_of_hand_in_sensor = data[6]
     
     palm_direction = data[7]
     
     rate_of_change.x = data[8]
     rate_of_change.y = data[9]
     rate_of_change.z = data[10]
     
     orientation_of_hand.x_basis[0] = data[11]
     orientation_of_hand.x_basis[1] = data[12]
     orientation_of_hand.x_basis[2] = data[13]
     
     orientation_of_hand.y_basis[0] = data[14]
     orientation_of_hand.y_basis[1] = data[15]
     orientation_of_hand.y_basis[2] = data[16]
     
     orientation_of_hand.z_basis[0] = data[17]
     orientation_of_hand.z_basis[1] = data[18]
     orientation_of_hand.z_basis[2] = data[19]
     
     pub_number_of_hands.publish(number_of_hand_in_frame)
     pub_hand_state.publish(strength)
     pub_hand_id.publish(hand_identifier)
     pub_palm_position_stable.publish(coordinates)
     pub_life_of_hand.publish(life_of_hand_in_sensor)
     pub_hand_orientation.publish(orientation_of_hand)
     pub_hand_rate_of_change.publish(rate_of_change)
     
     rate.sleep()
     
if __name__ == '__main__':
     try:
       leap_data()
     except rospy.ROSInterruptException:
       rospy.signal_shutdown("Programm being shutdown!")

