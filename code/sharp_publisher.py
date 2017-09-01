#!/usr/bin/env python
# BEGIN ALL
# BEGIN SHEBANG
#!/usr/bin/env python
# END SHEBANG

# Publisher of the distance data of the Sharp sensor of JUS

# BEGIN IMPORT
import rospy
#Library of controller Maestro
import maestro as m
# END IMPORT

# BEGIN STD_MSGS
from std_msgs.msg import Int32
# END STD_MSGS

# Maestro channel assignment
sharp=1
# Sharp equation coefficients: dist(cm)= a / (Output-b) - c
coefV_a_Luxes=1.58
# Used for rospy.Rate (should equal or muliple of rate in 'control' node)
cycle = 0.7

rospy.init_node('sharp_node')

# BEGIN PUB
pub = rospy.Publisher('sharp_data', Int32,queue_size=10)
# END PUB

# BEGIN LOOP
s= m.Controller()
rate = rospy.Rate(1/cycle)

while not rospy.is_shutdown():
        Output=s.getPosition(sharp)
        lux=coefV_a_Luxes*Output
        pub.publish(lux)
        rate.sleep()
# END LOOP
# END ALL
