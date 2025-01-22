"""
capture data from device, save to csv
"""

import argparse
import time
import serial

def t2str(val:float) -> str:
    subsec = val-int(val)
    return time.strftime("%H:%M:%S", time.localtime(val))+f"{subsec:0.3f}"[1:]

if(__name__ == '__main__'):
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--save', default=False, action='store_true', help='save data')
    p.add_argument('--per', default=60, type=float, help='save every N seconds')
    p.add_argument('--port', default='/dev/ttyACM0', help='serial port')
    p.add_argument('--windows',default=False,action='store_true',help="treat as windows code, not for rpi")
    p.add_argument('--info',default="",help="add additional info about run")
    
    args = p.parse_args()

    ARG_SAVE=args.save
    ARG_PORT=args.port
    ARG_WIN=args.windows
    ARG_PER=args.per
    ARG_INFO=args.info

    if(ARG_SAVE):
        fname = "data/rec"+time.strftime("%y%m%d_%H%M%S", time.localtime(time.time()))+f'{ARG_INFO}.csv'
        f = open(fname,'w')
        f.write("time_epoch,value\n")
        print(f"writing to: {fname}")
        if(not ARG_WIN):
            f.close()

    ser = serial.Serial(port=ARG_PORT,baudrate=9600,timeout=1)
    if(not ARG_WIN):
        ser.setDTR(False)
        time.sleep(1)
        ser.flushInput()
        ser.setDTR(True)
        time.sleep(2)

    print("Port opened")
    x = 0
    tsave=time.time()
    print("exiting")
    
    try:
        while(True):
            t=time.time()
            if(ARG_WIN):
                x = int(ser.readline().decode().strip())
                print(f"{t2str(t)}: {x}")
                if(ARG_SAVE): f.write(f"{t},{x}\n")

            else:
                x=ser.readall()
                try:
                    x = int(x)
                except Exception as e:
                    x = f"{x} (err)"

                print(f"{t2str(t)}: {x}")
                if(ARG_SAVE and t>=tsave):
                    f = open(fname,'a')
                    f.write(f"{t},{x}\n")
                    f.close()
                    tsave=t+ARG_PER
    except Exception as e:
        print(type(e),e)
        print('CTRL+C end')

    print('done, exiting')
    if(ARG_SAVE): f.close()
    ser.close()
# eof
