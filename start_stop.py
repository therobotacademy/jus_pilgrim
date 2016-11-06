#!/usr/bin/python

# Change rotating wheel when reaching threshold distance to an object

import rospy
from std_msgs.msg import Int32

# Maestro channel assignment
izq = 4
dcho = 5
# Threshold distance: below, change rotation wheel
min_dist= 23.1 # Corresponding to an output of 250 from Sharp sensor

# BEGIN CALLBACK
def callback(msg):
    global dist
    dist= msg.data
# END CALLBACK

dist= 50 #Anything to start

# Used for rospy.Rate (should equal or muliple of rate in 'control' node)
cycle = 0.5
rospy.init_node('start_stop')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('sharp_data', Int32, callback)
# END SUBSCRIBER
############################################
# BEGIN PUB: left and right servos speed set
write_left = rospy.Publisher('speed_left', Int32,queue_size=10)
write_right = rospy.Publisher('speed_right', Int32,queue_size=10)
# END PUB
############################################

# BEGIN LOOP
rate = rospy.Rate(1/cycle)

while not rospy.is_shutdown():
    if dist < min_dist:
        #Rotate around LEFT wheel
        wheel_moving= izq
        wheel_stopped= dcho
        write_left.publish(-1)
        write_right.publish(0)
    else:
        #Rotate around RIGHT wheel
        wheel_moving= dcho
        wheel_stopped= izq
        write_left.publish(0)
        write_right.publish(1)

    print "Distance= ", dist        
    print "Rotating around wheel ", wheel_moving
    print "Stopped wheel ", wheel_stopped
    print ""
    rate.sleep()
# END LOOP
# END ALL
