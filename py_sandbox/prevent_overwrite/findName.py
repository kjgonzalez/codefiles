'''
date: 190611
objective: create function that avoids overwriting a filename if it already exists
'''
# initializations
import os,sys

# check if file exists already
fpath = 'test.txt'


def findName(filename):
    ''' find valid new name for file if file already exists '''
    if(not os.path.exists(filename)):
        return filename
    path = os.path.dirname(filename) # no separator at end
    _name = os.path.basename(filename)
    if('.' in _name):
        name,ext = _name.split('.')
    else:
        name,ext = _name,''
    # try creating a valid filename
    i=0
    valid=False
    while(not valid):
        i+=1 # 2nd file should start with 1, etc
        name2=os.path.join(path,'{}_{}.{}'.format(name,i,ext))
        valid=not os.path.exists(name2) # True = name available
    return name2

fpath2=findName(fpath)
print('new:',fpath2)
f=open(fpath2,'w')
f.close()

# original:
#print('exists?',os.path.exists(fpath))
#path = os.path.dirname(fpath) # no separator at end
#_name = os.path.basename(fpath)
#if('.' in _name):
#    name,ext = _name.split('.')
#else:
#    name,ext = _name,''
#
#print(path,name,ext)
#
## try creating a valid filename
#i=1
#name2=os.path.join(path,'{}_{}.{}'.format(name,i,ext))
#
#print('new: ',name2)
#print(os.path.exists(name2))


