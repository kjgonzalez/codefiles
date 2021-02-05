'''
Track memory usage of a specific process by name or PID

help information: python memtrack.py --help
NOTE: this program requires 'psutil', which requires
    either a python environment or to be installed before usage.
'''

import psutil
import argparse
import time
import os
from pprint import pprint

def tstamp():
    return time.strftime("%Y%m%dT%H%M%S",time.localtime(time.time()))

def mem_as_bytes(pid=None,name=None):
    membytes = 0
    if(pid is not None):
        try:
            membytes = psutil.Process(pid).memory_full_info().uss
        except psutil.NoSuchProcess:
            membytes=0
    elif(name is not None):
        for iproc in psutil.process_iter():
            if(name in iproc.name()): membytes += iproc.memory_full_info().uss
    else:
        raise Exception('no process info given, need PID or name')
    return membytes


if(__name__ == '__main__'):
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                description='only give one parameter, pid or name')
    p.add_argument('--pid',type=int,
                   help='PID of process to track. this takes priority over name parameter')
    p.add_argument('--name',default='python',
                   help='Name of process. any process matching the name is included & added together')
    p.add_argument('--dir',default='no',
                   help='Directory to save data to. ')
    p.add_argument('--timeout',default=3600,type=int,
                   help='Maximum time (in seconds) to run this program. Negative value indicates run forever')
    p.add_argument('--period',default=5,type=int,
                   help='collect data every N seconds')
    args = p.parse_args()

    timeout = int(args.timeout)
    period = int(args.period)
    print('args: ',end='')
    pprint(args)
    assert timeout != 0, "Timeout cannot be zero"
    assert period > 0, "Period must be greater than zero"

    src = ''
    if(args.pid is not None): src = 'pid:{}'.format(args.pid)
    elif(args.name is not None): src = 'name:{}'.format(args.name)
    else: raise Exception('Missing parameter either PID or name')

    fname = os.path.join(os.path.abspath(args.dir),tstamp()+'.csv')
    if(args.dir != 'no'):
        print('will save to file:',fname)
        with open(fname,'a') as f:
            f = open(fname,'a')
            out = 'Time, Process_{} [KB]\n'.format(src)
            f.write(out)
    print(out,end='')
    t0 = time.time()
    finished=False
    while(not finished):
        out = '{},{}\n'.format(tstamp(), int(mem_as_bytes(args.pid,args.name)/1024))
        if(args.dir != 'no'):
            with open(fname,'a') as f:
                f.write(out)
        print(out,end='')
        time.sleep(period)
        if(timeout < 0): continue
        elif(time.time()-t0 > timeout): finished = True
