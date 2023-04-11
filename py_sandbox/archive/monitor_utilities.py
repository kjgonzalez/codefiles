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

NOTE: as a rule, will trust memory_info().rss to be outputing truthful data, and will assume that
    the task manager is lazy and doesn't always know the latest state of a process
'''

import psutil,time, argparse
import numpy as np
out = 'C:/Users/kjg91/Downloads/out_monitor'

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

class UtilityMonitor:
    '''
    get values of computer performance

    todo: temperature
    todo: overall computer memory usage
    todo: overall pc process (CPU)
    todo: per-program memory ussage
    todo: per-program pc process
    todo: network usage
    '''
    def __init__(self):
        self._src_net = ''
        self._total_mem_MB = psutil.virtual_memory()[0]/1024**2
        self._mem_pid = None
        self._mem_name = None
    def init_network(self,source='Wi-Fi'):
        ''' determine source of internet. 'auto' = autodetermine '''
        self._src_net = source
        if (source == 'auto'):
            print('auto-determining source...')
            # find max(2norm(allSources))
            res = calculateRates(1, items)
            ind = np.argmax([np.linalg.norm(i[:2]) for i in res])
            self.src = items[ind]
    def init_cpu_targ(self,targ):
        ''' todo: look for specific process(es) to monitor '''
        pass
    def init_mem_targ(self,targ):
        ''' todo: look for specific process(es) to monitor '''
        self._mem_pid = targ
        self._mem_name = psutil.Process(targ).name()
    def init_temperature(self):
        ''' todo: initialize temperature monitor '''
        pass
    def mem_overall_MB(self):
        ''' return current overall memory usage as a percentage of total'''
        return round(psutil.virtual_memory().used/1024**2,2)

    def mem_snapshot_MB(self,pid=None,name=None):
        ''' todo: match either pid or name, and gather up all processes matching descrip'''
        if(name is not None): raise NotImplementedError()
        return round(psutil.Process(pid).memory_info().rss/1024**2,2 )
    def net_snapshot_bytes(self):
        ''' todo: return current up/down in bytes'''
        data = psutil.net_io_counters(pernic=True)[self._src_net]
        return np.array([time.time(), data.bytes_recv, data.bytes_sent], dtype=float)

    def get_meta(self):
        ''' return metadata of current collection '''
        meta = dict()
        meta['net_src'] = self._src_net
        meta['mem_iproc_PID'] = self._mem_pid
        meta['mem_iproc_name'] = self._mem_name
        meta['mem_total_MB'] = self._total_mem_MB
        return meta
    def get_data(self,collectiontime_ms=500) -> dict:
        '''
        1. take snapshot at point 1
        2. wait X seconds
        3. take snapshot at point 2
        4. calculate current usage
        '''
        dat = dict()
        net0 = self.net_snapshot_bytes()
        cpu_overall = psutil.cpu_percent(collectiontime_ms/1000)
        net1 = self.net_snapshot_bytes()

        up_Kbps = round((net1[2]-net0[2])/(net1[0]-net0[0])/1024*8,2)
        dn_Kbps = round((net1[1]-net0[1])/(net1[0]-net0[0])/1024*8,2)

        dat['net_up_Kbps'] = up_Kbps
        dat['net_dn_Kbps'] = dn_Kbps
        dat['mem_total_MB'] = self.mem_overall_MB()
        if(self._mem_pid is not None):
            dat['mem_iproc_MB'] = self.mem_snapshot_MB(pid=self._mem_pid)
        dat['cpu_total_pct'] = cpu_overall
        return dat


if(__name__=='__main__'):

    um = UtilityMonitor()
    um.init_network()
    um.init_mem_targ(7824)
    print(um.get_meta())
    for i in range(10):
        print(um.get_data())
        time.sleep(1)


    exit()
    # note: this program outputs KB/s (kilobytes)
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--list',default=False,action='store_true',help='lists available networks, then exits')
    p.add_argument('--src',type=str,default='auto',help='internet source to measure. "auto" = automatically detect active network')
    p.add_argument('--p',default=1.0,type=float,help='cycle period')
    p.add_argument('--n',default=-1,type=int,help='number of cycles to run. -1 means infinite.')
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
        raise Exception('invalid value of n used:',n)
