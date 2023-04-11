'''
kjgnote: at this point, want to test out having a decorator as a function that gets imported
'''
import functools

def stamper(pfunc):
    import time
    logstr='LOG: '+time.strftime('%Y%b%d-%H:%M:%S',time.localtime(time.time()))+'\n'
    @functools.wraps(pfunc)
    def wrapper_stamper(*args,**kwargs):
        pfunc(logstr,*args,**kwargs)
    return wrapper_stamper
