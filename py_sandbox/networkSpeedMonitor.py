'''
Author: Kris Gonzalez
Date Created: 180509
Objective: make simple python script to monitor network download / upload speed

note: in the future, may care about which network
    connection am looking at. for now, will stick to
    ethernet.

possible network connections at sample house:
0 : Ethernet
1 : Ethernet 3
2 : Local Area Connection* 1
3 : Local Area Connection* 2
4 : Ethernet 2
5 : Wi-Fi
6 : Loopback Pseudo-Interface 1



# ISSUES:
please check whether data is in BYTES or BITS
'''

import psutil,time, argparse
import numpy as np

def getData(source='Ethernet'):
    ''' take a snapshot and get absolute values for time, download, upload'''
    data = psutil.net_io_counters(pernic=True)[source]
    return np.array([time.time(),data.bytes_recv,data.bytes_sent],dtype=float)
    # return(float(time.time()),float(data.bytes_recv),float(data.bytes_sent))

def calculateRate(dt,source):
    ''' given a waiting time (dt [s]), calculate download / upload rates (in Kbps) '''
    dat0 = getData(source)
    time.sleep(dt)
    dat1 = getData(source)

    res=dat1-dat0
    rateDn=res[1]/res[0]
    rateUp=res[2]/res[0]
    return (res[1:]/res[0]/1024.).round(2)

def testSources(dt,sourcesList):
    ''' for each given source, return upload / download rate (in Kbps) '''

    for isrc in sourcesList:
        pass
    pass

ans=    calculateRate(1,'Wi-Fi')
import ipdb; ipdb.set_trace()

if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--list',default=False,action='store_true',help='lists available networks, then exits')
    p.add_argument('--src',type=str,default='auto',help='internet source to measure. "auto" = automatically detect active network')
    p.add_argument('--p',default=1.0,type=int,help='cycle period')
    p.add_argument('--n',default=10,type=int,help='number of cycles to run. -1 means infinite.')
    args=p.parse_args()
    src=args.src
    s=args.p
    n=args.n

    items=list(psutil.net_io_counters(pernic=True).keys())
    if(args.list):
        # list available sources, then exit
        print('available connections (use either number or name as source):')
        [print(j,':',i) for j,i in enumerate(items)]
        print('\nExiting...')
        exit()

    if(args.src=='auto'):
        print('auto-determining source')

        exit()
# A: want to be able to auto-determine source
# B: wanna be able to use number OR source name

    # if user gave number, convert to string
    if(src.isdigit()):
        src=items[int(src)]
    print('src:',src)
    print('period:',s)
    print('Ntimes:',n)
    print('')
if(n==-1):
    # run infinite times
    while(True):
        print(calculateRate(s,src))
if(n>0):
    # run n times
    for i in range(n):
        print(calculateRate(s,src))
else:
    raise Error('invalid value of n used:',n)
