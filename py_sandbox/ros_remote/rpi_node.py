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
st = klib.Stamper()
now = lambda :st.now().replace(':','') # dont want colons in filename

assert sys.version_info[0] == 3, "Please use python version 3"

def takephoto(src,savepath='.'):
    ''' given a source, take a photo, save it, and close the source. '''
    cap=cv2.VideoCapture(src)
    ret, frame = cap.read()
    cap.release()
    fpath = os.path.join(savepath,now())
    cv2.imwrite(fpath,frame)
    print('photo saved:',fpath)



if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--src',default=0,type=int,help='camera source')
    args=p.parse_args()


    takephoto(args.src)
