'''
source:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
KJG191219: confirmed to work on rpi
'''
import numpy as np
import cv2
import sys,argparse
assert sys.version_info[0] == 3, "Please use python version 3"

p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument('--src',default=0,type=int,help='camera source')
p.add_argument('--avgprint',default=False,action='store_true',help='debug: print average pixel color')

args=p.parse_args()


cap = cv2.VideoCapture(args.src)
print('press "q" to exit')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if(args.avgprint):
        # print average color of frame
        print('mean BGR value:',frame.mean(0).mean(0).astype(int))

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
