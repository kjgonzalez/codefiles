'''
logger class and example. NOTE: this class has been copied / moved to klib
'''

import os
class Logger:
    '''
    Simple log class to save all output from 'print' functions (top-level only)

    NOTES:
    * perhaps in future, implement overwite check (and boolean argument)
    '''

    def __init__(self,logpath='logfile.txt',overwrite=True):
        # initialize and open file here, when class is declared
        # if(os.path.exists(logpath) and not overwrite):
        #     # don't want to overwrite already-existing file
        #     dirname=os.path.dirname(logpath)
        #     _name=os.path.basename(logpath)
        #     if('.' in _name):
        #         name,ext = _name.split('.')
        #     else:
        #         name=_name
        #         ext=''
        #     maxit=1000
        #     it=0
        #
        #     # need original name
        #
        #     while(it<maxit):
        #         it+=1
        self.logpath = logpath
        self.fout = open(self.logpath,'w')
        from builtins import print as _print
        self._print = _print

    def print(self,*argv,**kwargs):
        end = kwargs['end'] if('end' in kwargs.keys()) else '\n'
        sep = kwargs['sep'] if('sep' in kwargs.keys()) else ' '
        oneline=sep.join([str(iarg) for iarg in argv])
        self._print(*argv,**kwargs)
        self.fout.write(oneline+end)
    def close(self):
        self.fout.close()

if(__name__=='__main__'):
    from builtins import print as _print
    import numpy as np
    #
    # _print = print # leave ability to use normal print
    # log = Logger()
    from klib import Logger
    print('imported from klib')
    log=Logger()


    print = log.print

    print('test 1')
    print('test','2')
    print('test',3)
    print('this is test',3,'in a series')
    print('test 4: ',[1,2,3,4])
    print('test 5:\n',np.random.rand(3,3))

    print('test',end=' ')
    print('6')

    print('test',7,'la','la',sep='-')
    log.close()

    _print('deleting file')
    os.remove(log.logpath)
