'''
Author: Kris Gonzalez
Date Created: 180509
Objective: make simple python script to monitor network download / upload speed

NOTES:
* download / upload values are in KB/s (kilobytes/second)
* cycle time isn't exactly the value given, closer to about 2% longer
* possible network connections at sample house:
    0 : Ethernet
    1 : Ethernet 3
    2 : Local Area Connection* 1
    3 : Local Area Connection* 2
    4 : Ethernet 2
    5 : Wi-Fi
    6 : Loopback Pseudo-Interface 1

'''

import psutil,time, argparse
import numpy as np

def getData(source='Ethernet'):
    ''' take a snapshot and get absolute values for time, download, upload'''
    data = psutil.net_io_counters(pernic=True)[source]
    return np.array([time.time(),data.bytes_recv,data.bytes_sent],dtype=float)
    # return(float(time.time()),float(data.bytes_recv),float(data.bytes_sent))

def calculateRates(dt,sourceList):
    ''' given a waiting time (dt [s]), calculate download / upload rates (in Kbps) '''
    dat0=[]
    dat1=[]
    res=[]
    for isrc in sourceList:
        dat0 += [getData(isrc)]
    time.sleep(dt)
    for i,isrc in enumerate(sourceList):
        temp = getData(isrc)-dat0[i]
        # iDownUp=(temp[1:]/temp[0]/1024.).round(2)
        iDownUp=(temp[1:]/1024./temp[0]).round(2)
        res.append([*iDownUp,isrc])
    res=np.array(res,dtype=object)
    return res

def calculateOne(dt,source):
    ''' determine data of single source '''
    temp=calculateRates(dt,[source])[0,:2]
    return list(temp)

if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--list',default=False,action='store_true',help='lists available networks, then exits')
    p.add_argument('--src',type=str,default='auto',help='internet source to measure. "auto" = automatically detect active network')
    p.add_argument('--p',default=1.0,type=float,help='cycle period')
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
        print('auto-determining source...')
        # find max(2norm(allSources))
        res = calculateRates(1,items)
        ind=np.argmax([np.linalg.norm(i[:2]) for i in res])
        src=items[ind]

    # if user gave number, convert to string
    if(src.isdigit()):
        src=items[int(src)]
    print('src:',src)
    print('period:',s)
    print('Ntimes:',n)
    print('')
    print('Down  Up')

    if(n==-1):
        # run infinite times
        while(True):
            print( *calculateOne(s,src) ) # single source
    if(n>0):
        # run n times
        for i in range(n):
            print( *calculateOne(s,src) ) # single source
    else:
        raise Error('invalid value of n used:',n)
