'''
date: 200116
objective: receive image messages and display from publisher
'''




import cv2
import numpy as np
import sys,argparse,time,os
import klib
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
bridge = CvBridge()
st = klib.Stamper()
now = lambda :st.now().replace(':','') # dont want colons in filename

assert sys.version_info[0] == 3, "Please use python version 3"
flag_first = True

CVIMG = None

def cb_string(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
def listener():
    ''' keeping function here purely for debugging '''
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, cb_string)
    rospy.spin()

def cb_img(data):
    global CVIMG
    if(True):
        flag_first=False
        # print('i heard something',time.time())
        CVIMG = bridge.imgmsg_to_cv2(data)
        print(time.time(),CVIMG.shape)
    #CVIMG = bridge.imgmsg_to_cv2(data) # may need to use data.data

def imgin():
    ''' keeping function here purely for debugging '''
    rospy.Subscriber(args.topic, Image, cb_img)
    rospy.init_node('camsub', anonymous=True)
    rospy.spin()

if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--topic',type=str,default='camera',help='name of topic')
    args=p.parse_args()
    # imgin()

    #while(type(CVIMG)==type(None)):
        #time.sleep(1) # wait for ros image to be updated
        #print('waiting...')
    rospy.Subscriber(args.topic, Image, cb_img)
    rospy.init_node('camsub', anonymous=True)
    
    while(True):
        cv2.imshow('frame',CVIMG)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
