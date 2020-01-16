'''
date: 200115
objective: transmit video from rpi to computer


general steps: 
1. take a picture with webcam, make sure it's transmitting properly
'''

import cv2
import numpy as np
import sys,argparse,time,os
import klib
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

st = klib.Stamper()
now = lambda :st.now().replace(':','') # dont want colons in filename

assert sys.version_info[0] == 3, "Please use python version 3"

def takephoto(src,savepath='.'):
    ''' given a source, take a photo, save it, and close the source. '''
    cap=cv2.VideoCapture(src)
    ret, frame = cap.read()
    cap.release()
    fpath = os.path.join(savepath,now()+'.jpg')
    cv2.imwrite(fpath,frame)
    print('photo saved:',fpath)

def temp_talker():
    ''' keeping only as debugging tool '''
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # default:10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def imgout():
    ''' publish images (aka video stream). can be checked with rviz '''
    pub = rospy.Publisher('campub', Image, queue_size=10) # topic here
    rospy.init_node('campub', anonymous=True) # publisher here
    rate = rospy.Rate(1) # default:10hz
    bridge=CvBridge()
    while not rospy.is_shutdown():
        ret,frame = cap.read()
        avgpixel = frame.mean(0).mean(0).astype(int)
        print('avg value (BGR):',avgpixel)
        rosimg=bridge.cv2_to_imgmsg(frame) # ,"bgr8"
        try:
            pub.publish(rosimg)
        except CvBridgeError as e:
            print(e)
        #rate.sleep() # may need to use when debugging

if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--src',default=0,type=int,help='camera source')
    args=p.parse_args()
    cap = cv2.VideoCapture(args.src)
    
    try:
        imgout() # this function goes into internal while loop
    except rospy.ROSInterruptException:
        pass
    cap.release()
