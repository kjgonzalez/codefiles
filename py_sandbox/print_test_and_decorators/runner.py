'''
Objective: wrap the print function with a 1. timestamp and a 2. dual output to file
just testing how well text output saves stuff
'''

text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ac sollicitudin odio, sed sagittis elit. Proin id urna.
'''
import time
import builtins
import functools
import remote_mod
#foutkjg=open('res.txt','w')
#def stamp():
    #import time
    #return 'LOG: '+time.strftime('%Y%b%d-%H%M%S',time.localtime(time.time()))+'\n'



def andsavetofile(pfunc):
    # kjgnote: file manip object must already exist
    @functools.wraps(pfunc)
    def wrapper_astf(*args,**kwargs):
        pfunc(*args,**kwargs,file=foutkjg)
        pfunc(*args,**kwargs)
    return wrapper_astf


foutkjg=open('delme.txt','w')
# kjgnote: it seems like the order of these two wrappers doesn't matter. either way, both files end up with a timestamp
@andsavetofile
@remote_mod.stamper
def print(*args,**kwargs):
    builtins.print(*args,**kwargs)


# old, method1
#def stamp():
    #return 'LOG: '+time.strftime('%Y%b%d-%H%M%S',time.localtime(time.time()))
#def addfout(printfunc):
    #def wrapper(*args,**kwargs):
        #printfunc(stamp(),file=foutkjg)
        #printfunc(*args,**kwargs,file=foutkjg)
        #printfunc(stamp())
        #printfunc(*args,**kwargs)
    #return wrapper

#print=addfout(print)



for i in range(int(100)):
    print(i,text)
    time.sleep(1)
print('done')



# want to create two decorators: 1. augment print function with a timestamp 2. augment print function with dual write to screen and to file

#first, for write to screen:
