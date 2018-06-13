
import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def bno055_lis():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('bno055_lis', anonymous=True)

    rospy.Subscriber('bno055_state', Float32MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    bno055_lis()
