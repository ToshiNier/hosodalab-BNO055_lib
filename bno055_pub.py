#!/usr/bin/python

import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension
from adafruit_bno055_controller import *
from xl_config import *

def bno055_pub():
    rospy.init_node('bno055_pub', anonymous=True)
    pub = rospy.Publisher('bno055_state', Float32MultiArray,queue_size=1)
    rate = rospy.Rate(10) # 10hz
    bno_controller = AdafruitBno055Controller()
    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "height"
    mat.layout.dim[1].label = "width"
    mat.layout.dim[0].size = 3
    mat.layout.dim[1].size = 1
    mat.layout.dim[0].stride = 3*1 #note dim[0] stride is just size of image
    mat.layout.dim[1].stride = 1
    mat.layout.data_offset = 0
    mat.data = [0]*3
    while not rospy.is_shutdown():
        x,y,z = bno_controller.gravity()
        gravity_str = "gravity is{}".format([x,y,z]) 
        rospy.loginfo(gravity_str)
        mat.data[0] = x
        mat.data[1] = y
        mat.data[2] = z
        pub.publish(mat)
        rate.sleep()

if __name__ == '__main__':
    try:
        bno055_pub()
    except rospy.ROSInterruptException:
        pass
