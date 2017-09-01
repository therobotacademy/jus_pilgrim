#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32


# BEGIN CALLBACK
def callback(msg):
    print ""
    print "--------- luminosidad=", msg.data, "luxes"
# END CALLBACK


rospy.init_node('sharp_reader')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('sharp_data', Int32, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
