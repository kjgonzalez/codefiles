"""
capture data from device, save to csv
"""

import argparse
import time
import serial
import msvcrt

def t2str(val:float) -> str:
    subsec = val-int(val)
    return time.strftime("%H:%M:%S", time.localtime(val))+f"{subsec:0.3f}"[1:]

if(__name__ == '__main__'):
    # p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # p.add_argument('--save', default=False, action='store_true', help='save data')
    # p.add_argument('--port', default='COM5', help='serial port')
    # args = p.parse_args()
    #
    # ARG_SAVE=args.save
    # ARG_PORT=args.port
    #
    #
    # if(ARG_SAVE):
    #     fname = "data/"+time.strftime("%y%m%d_%H%M%S", time.localtime(time.time()))+'.csv'
    #     f = open(fname,'w')
    #     print(f"writing to: {fname}")
    #
    #
    # ser = serial.Serial(port=ARG_PORT,baudrate=9600)
    # print("Port opened")
    # key=0
    # flag_done=False
    # while(not flag_done):
    #     if(msvcrt.kbhit()):
    #         if(msvcrt.getch()==b'q'):
    #             flag_done=True
    #
    #     t=time.time()
    #     x=int(ser.readline().decode())
    #     print(f"{t2str(t)}: {x}")
    #     if(ARG_SAVE): f.write(f"{t},{x}\n")
    #
    # print('done, exiting')
    # if(ARG_SAVE): f.close()
    # ser.close()
    try:
        assert False,"wrong"
    except Exception as e:
        print(type(e),e)

# eof
