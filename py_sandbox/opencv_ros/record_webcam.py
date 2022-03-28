'''
record from given webcam at a given framerate
'''

import time
import argparse
import cv2
import numpy as np

def changeResolution(feed,newheight=10000,newwidth=10000):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, newheight)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,newwidth)
    return 0

class TimeCorrection:
    '''
    Dynamically fix time offset error from lack of interrupt
        routine. this is rudimentary PI-controller
    '''
    def __init__(self,desPer,arrsize=20):
        self.des = desPer
        self.err = np.zeros(arrsize)
        self.ind = 0
        self.errsum=0
    def update(self,val):
        e = val-self.des
        self.err[self.ind] = e # error is how much more time than reference was used
        self.errsum += e
        self.ind = self.ind+1 if(self.ind < len(self.err)-1) else 0
    @property
    def correction(self):
        return self.err.mean()*2+self.errsum*.2


if(__name__ == '__main__'):
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--src',default=0,help='camera source')
    p.add_argument('--rate',default=1,help='desired FPS (max 60)')
    p.add_argument('--out',default='../data/output.avi',help='filepath')
    p.add_argument('--maxtime',default=-1,help='maximum seconds to record, "-1" = never stop')
    args = p.parse_args()
    
    _src = int(args.src)
    _rate = int(args.rate)
    _per = 1000/float(_rate) # value in milliseconds
    _fpath = args.out
    _tmax = float(args.maxtime)+.1 # small correction for camera delay

    cap = cv2.VideoCapture(_src)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    _resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    cap.set(cv2.CAP_PROP_FPS,60) # assume using hd camera
    out = cv2.VideoWriter(_fpath,fourcc=fourcc, fps=_rate,frameSize=_resolution)

    print('starting...')
    tstart = time.time()
    t0 = time.time() # get milliseconds
    flag_record = True
    nframes = 0 # frames written
    tc = TimeCorrection(_per)
    while(cap.isOpened() and (flag_record)):
        flag_record = True if((time.time()-tstart < _tmax) or _tmax < 0) else False
        t1 = (time.time()-t0)*1000 # get elapsed milliseconds
        if(t1 >= _per-tc.correction):
            tc.update(t1)
            t0 = time.time()
            out.write(frame)
            nframes += 1
            print('frames written: {} | elapsed: {:2.3f} | dt: {:2.3f} | err:{:2.3f}'.format(
                nframes,time.time()-tstart,t1,tc.correction))
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    cv2.destroyAllWindows()
    print('done')
# eof
