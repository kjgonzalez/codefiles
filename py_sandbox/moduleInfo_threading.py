'''
datecreated: 191001
objective: demonstrate basics of threading
'''

import time
import threading

def fn():
    print('starting thread')
    time.sleep(1)
    print('ending thread')

def fn2():
    print('main thread start')
    x=threading.Thread(target=fn,)
    print('before 2nd thread start')
    x.start()
    print('main finished')

if(__name__=='__main__'):
    fn2()

# eof

