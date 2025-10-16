'''
check range of last byte in ipaddr to get active ip addresses.

todo: instead of "ping", use something else (faster)
todo: threading
'''

import argparse
import subprocess
import time

def exists(ipaddr):
    return subprocess.run(
        f"ping {ipaddr} -n 1 -w 15",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        ).returncode == 0

def getname(ipaddr):
    xx = subprocess.run(f'nslookup {ipaddr}',stdout=subprocess.PIPE)
    for irow in xx.stdout.decode().split('\n'):
        if('Name' in irow):
            return irow.split(':')[-1].strip()
    return 'NAME_NOT_FOUND'

if(__name__ == '__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('ipbase',help='first 3 bytes of ip address (e.g. 1.2.3)')
    # todo: range, allow only checking between a-b (inclusive)
    args=p.parse_args()

    print("Starting...")
    t0=time.time()
    IPBASE = args.ipbase+'.'
    for i in range(256):
        iaddr = IPBASE+str(i)
        if(exists(iaddr)):
            name = getname(iaddr)
            print(f'{iaddr}: {name}')
    print(f"Done (duration={time.time()-t0:0.2f}s), exiting...")

# eof
