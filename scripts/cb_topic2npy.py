#!usr/bin/env python3
'''ros utils'''
import rospy
from sensor_msgs.msg import Image, CameraInfo, NavSatFix
from geometry_msgs.msg import Vector3Stamped
from nav_msgs.msg import Odometry
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
import csv
import sys

# file_path = '/home/ncslaber/110-1/210906_loopClosure/'
file_path = '/home/ncslaber/110-1/210922_EKF-fusion-test/zigzag_bag/'

def msg2CV(msg):
    bridge = CvBridge()
    try:
        image = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        return image
    except CvBridgeError as e:
        print(e)
        return

class Synchronize:
    def __init__(self):
        self.msgColor = None
        self.msgDepth = None
        self.msgIMU = None
        self.msgGPS = None
        self.msgOdom = None

        self.flagColor = False
        self.flagDepth = False
        self.flagSaved = False
        self.flagIMU = False
        self.flagGPS = False
        self.flagOdom = False

        self.file_index = 0
        self.timestamp = 0

        self.listDepth = []
        self.listColor = []
        self.listPose = []
        
    def colorIn(self, color):
        self.msgColor = color
        self.flagColor = True
    def depthIn(self, depth):
        self.msgDepth = depth
        self.timestampSecs = depth.header.stamp.secs 
        self.timestampNSecs = depth.header.stamp.nsecs
        self.flagDepth = True
    def imuIn(self, yaw_degree):
        self.msgIMU = yaw_degree
        self.flagIMU = True
    def gpsIn(self, lat_lon):
        self.msgGPS = lat_lon
        self.flagGPS = True
    def odomIn(self, xyz):
        self.msgOdom = xyz
        self.flagOdom = True
        
    def save(self):
        if (self.flagDepth and self.flagColor and self.flagIMU and self.flagGPS) == True:
            self.imgColor = msg2CV(self.msgColor)
            self.imgDepth = msg2CV(self.msgDepth)
            
            np.save(file_path + "depth/" + str(self.file_index), self.imgDepth) # 1tree, 2tree, 2trees
            np.save(file_path + "color/" + str(self.file_index), self.imgColor)
            
            yaw_rad = self.msgIMU/180*np.pi
            with open(file_path + 'cb_pose.csv', 'a') as csvfile: # or w
                writer = csv.writer(csvfile)
                writer.writerow([self.msgGPS.latitude, self.msgGPS.longitude, yaw_rad]) 
            # np.save(file_path + "poseXYT/" + str(self.timestampSecs%1000)+'-'+str(int(self.timestampNSecs/1e6)), np.array([self.msgGPS.latitude, self.msgGPS.longitude, yaw_rad]))
            with open(file_path + 'index_timestamp.csv', 'a') as fp: # or w
                writer = csv.writer(fp)
                writer.writerow([self.file_index, str(self.timestampSecs)+'.'+str(self.timestampNSecs)] )

            print("saved!")
            self.flagSaved = True
            self.file_index += 1

                        
        else: 
            print("haven't receive one of them!")

synchronizer = Synchronize()
def cbDepth(msg):
    print("receive depth!")
    synchronizer.depthIn(msg)
    synchronizer.save()

def cbColor(msg):
    print("receive color!")
    synchronizer.colorIn(msg)

def cbIMU(msg):
    # if synchronizer_pose.flagSaved == False:
    synchronizer.imuIn(msg.vector.z) 
    
def cbOdom(msg):
    synchronizer.odomIn(msg.pose.pose.position) 
    
def cbGPS(msg):
   synchronizer.gpsIn(msg) 

if __name__ == "__main__":
    print("Python version: ",sys.version)
    rospy.init_node("depthHandler", anonymous=True)
    subDepth = rospy.Subscriber("/camera/depth/image_rect_raw", Image, cbDepth)
    subColor = rospy.Subscriber("/camera/color/image_raw", Image, cbColor)
    subIMU = rospy.Subscriber("/imu_filter/rpy/filtered", Vector3Stamped, cbIMU)
    subGPS = rospy.Subscriber("/outdoor_waypoint_nav/gps/filtered", NavSatFix, cbGPS)
    # subOdom = rospy.Subscriber("/outdoor_waypoint_nav/odometry/filtered_map", Odometry, cbOdom)

    print("successfully initialized!")
    

    rospy.spin()
