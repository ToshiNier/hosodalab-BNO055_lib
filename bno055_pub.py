#!/usr/bin/python

import rospy
from std_msgs.msg import Float32MultiArray
from adafruit_bno055_controller import *
from xl_config import *

# def main():
#     bno_controller = AdafruitBno055Controller()
#     x,y,z = bno_controller.gravity()
#     print x,y,z
    

# if __name__ == "__main__":
#     main()

def bno055_pub():
    rospy.init_node('bno055_pub', anonymous=True)
    pub = rospy.Publisher('bno055_state', Float32MultiArray)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        bno_controller  =  = AdafruitBno055Controller()
        x,y,z = bno_controller.gravity()
        gravity_str = "gravity is = %f, %f, %f" %x,%y,%z
        rospy.loginfo(gravity_str)
        pub.publish([x,y,z])
        rate.sleep()

if __name__ == '__main__':
    try:
        bno055_pub()
    except rospy.ROSInterruptException:
        pass
