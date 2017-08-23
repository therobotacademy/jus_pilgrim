#!/usr/bin/python

# Change rotating wheel when reaching threshold distance to an object

import rospy
from std_msgs.msg import Int32

#Library of controller Maestro
import maestro as m
# Maestro channel assignment
izq = 4
dcho = 5
# Threshold distance: below, change rotation wheel
min_dist= 23.1 # Corresponding to an output of 250 from Sharp sensor



# BEGIN CALLBACK
def callback(msg):
    dist= msg.data

    if dist < min_dist:
        #Rotate around LEFT wheel
        wheel_moving= izq
        wheel_stopped= dcho
    else:
        #Rotate around RIGHT wheel
        wheel_moving= dcho
        wheel_stopped= izq

    s= m.Controller()
    s.setTarget(wheel_moving,1)
    s.setTarget(wheel_stopped,0)

    print "Distance= ", dist        
    print "Rotating around wheel ", wheel_moving
    print "Stopped wheel ", wheel_stopped
    print ""
# END CALLBACK


rospy.init_node('start_stop')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('sharp_data', Int32, callback)
# END SUBSCRIBER





rospy.spin()
# END ALL
