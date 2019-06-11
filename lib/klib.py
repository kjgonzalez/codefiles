'''
Title: The klib module
Author: Kristian Gonzalez

THIS IS THE OFFICIAL LOCATION OF ALL PYTHON FUNCTIONS AND CLASSES THAT ARE MADE
    FOR PERSONAL USE. ONLY FUNCTIONS THAT ARE FULLY FUNCTIONAL OR STABLE MAY BE
    USED HERE. IF A FUNCTION IS NOT USABLE YET, EITHER SAVE IT ELSEWHERE OR
    SAVE IT HERE, COMMENTED OUT.

== CALLING THIS MODULE REMOTELY ============================
In Linux:
1. open ~/.bashrc
2. add line (adapting to local computer):
    export PYTHONPATH="/home/user/.../codefiles/scripts_libs:$PYTHONPATH"
3. reload bash or source

In Windows:
1. START > search "path" > "edit the system environment variables"
2. click "Environment Variables..."
3. find "PYTHONPATH" in user variables, or create new variable
4. add new value (adapting to local computer):
    C:\...\codefiles\scripts_libs
5. reopen Command Line

== NOTES ===================================================
* as of 181016, this module and all contained members will assume python 3.x
    environment. functionality may break when used in python 2.x
* as of 181016, all lines shall be at maximum 80 characters long. if writing
    text, using hanging indent as shown in this sentence
* create help text for all items written here. this is to facilitate
    understanding and relearning things that may have been created too long ago
    to remember.
* it's understood that this file is being shared across multiple platforms.
    Thus, trying to maintain uniformity is important. Remember to delete
    needless copies / simplify the method of maintaining a single source
* as of 181008, will now always use 4 spaces as the tab
    delimiter. using a "hard tab" causes too many formatting
    headaches across different programs, platforms, etc.
* because the following is useful but too compact to put into a function,
    here's how to sort a numpy array by i'th column: a[a[:,i].argsort()], and
    backwards: a[a[:,i].argsort()[::-1]]
* REJECTED: will import all necessary modules at top instead of within each function /
    class. this makes more sense from a usability perspective, and avoids
    unecessarily importing each time a call is made.
* will return to putting modules within each function. this increases
    portability because not every function can be used across every platform.
    thus, don't want to shut out entire module to a single platform because of
    this. only the most global and standard of modules are imported globally,
    INCLUDING numpy. from current perspective, serious computing would require
    this module at the very least.
* as of 190321, will put classes after inits, before functions
'''

# INITIALIZATIONS ==============================================================
import os,sys,time # only "standard" modules are imported here
import numpy as np
from glob import glob
import functools # not sure if this is standard
# import PIL.Image as pil # not standard, must remove
# import tkinter # not standard across versions #kjgnote: may not be that useful anymore
# import winsound # kjg190227: this is not cross platform, leave in-function


# FIRST, BEFORE ALL ELSE, CHECK VERSIONS OF OS AND PYTHON
def __getSysInfo__():
    ''' Get local computer info. Generally, should keep software OS and version
        independent, but this may not always be possible. Also, avoiding
        importing sys or other modules to pylib.
    Returns:
        * OSVERSION (linux[0]/win[1]/mac[2]?)
        * PYVERSION (2/3)
    '''
    if('linux' in sys.platform):
        osver = 0
    elif('win' in sys.platform):
        osver = 1
    else:
        osver = 2
    return (osver,sys.version_info.major)
# def __getSysInfo__
(OSVERSION,PYVERSION) = __getSysInfo__()

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

class Stamper:
    ''' wrapper for time function under following assumptions:
        * don't care about sub-second precision
        * want human-readable timestamp
        * want easy conversion b/t string and float of timestamp
    Example usage:
    stamp=Stamper()
    stamp.now
        OUT: "2019Mar21-13:11:23"
    stamp.toseconds(stamp.now())
        OUT: 1553170283.0
    stamp.tostamp(stamp.toseconds(stamp.now()))
        OUT: "2019Mar21-13:11:23"
    '''
    def __init__(self):
        self._tsf="%Y%b%d-%H:%M:%S" # time stamp format
    def now(self):
        ''' Return current time in string. note: decimal value is truncated, not
            rounded.
        '''
        return time.strftime(self._tsf,time.localtime(time.time()))
    def toseconds(self,ts_str):
        ''' convert string timestamp to epoch seconds '''
        return time.mktime(time.strptime(ts_str,self._tsf))
    def tostamp(self,ts_float):
        ''' convert epoch seconds to string timestamp '''
        return time.strftime(self._tsf,time.localtime(ts_float))
# class Stamper

class Stopwatch:
    ''' Stopwatch: Basic class that logs a time when it's created. Can also
        restart timer with function call "start", and can get the elapsed time
        with function "lap". Note that all values are in seconds.

        Example:
        from klib import Stopwatch
        sw=Stopwatch()
        (some code)
        print(sw.lap())
            OUT: 5.2087955
    '''
    def __init__(self):
        self.t1=time.time()
    def start(self):
        self.t1=time.time()
    def lap(self):
        return time.time()-self.t1

# class Stopwatch

class DataHelp(object):
    ''' Call this object when want to use a binary such as an image. This saves
        space and effort on binaries on the repo without having to constantly
        copy/paste new data in.
        KJG190320: uses non-standard module, may not work on all platforms.
    '''
    def __init__(self):
        self.basedir=os.path.dirname(__file__) # get abs path to lib
        pass

    @property
    def jpgpath(self):
        ''' Absolute path to jpg file. path should be cross-platform '''
        path=os.path.abspath(os.path.join(self.basedir,'data','baby.jpg'))
        assert os.path.exists(path),'error,missing file: '+path
        return path

    @property
    def jpgimg(self):
        ''' Return jpg image as 3-channel numpy array, [0-255] uint8. This is
            "success baby" image.
        '''
        import PIL.Image as pil
        return np.array(pil.open(self.jpgpath))

    @property
    def pngpath(self):
        ''' Absolute path to png file. should be cross-platform '''
        path=os.path.abspath(os.path.join(self.basedir,'data','cvlogo.png'))
        assert os.path.exists(path),'error,missing file: '+path
        return path

    @property
    def pngimg(self):
        ''' Return png image as 4-channel numppy array, [0-255] uint8. This is
            open cv logo image.
        '''
        import PIL.Image as pil
        return np.array(pil.open(self.pngpath))
data=DataHelp()
# class Data

def antiOverwrite(filename):
    ''' Given a filename, check if it already exists, and if so, find a unique
        filename in same folder, with similar name.
    INPUT: filename: string, proposed filename and path
    OUTPUT: name2: string, available, unused filename and path.
    '''
    if(not os.path.exists(filename)):
        return filename
    path = os.path.dirname(filename) # no separator at end
    _name = os.path.basename(filename)
    if('.' in _name):
        name,ext = _name.split('.')
    else:
        name,ext = _name,'' # in case file has no extension
    # try creating a valid filename
    i=0
    valid=False
    while(not valid):
        i+=1 # 2nd file should start with 1, etc
        name2=os.path.join(path,'{}_{}.{}'.format(name,i,ext))
        valid=not os.path.exists(name2) # True = name available
    return name2

def getlist(rec=False,files=True,ext=''):
    ''' This function is implemented as alias for "dir". Use THAT function. '''
    return dir(rec,files,ext)

def dir(rec=False,files=True,ext=''):
    '''
    Objective: Emulate ls / dir command to be cross platform and return as a
        list. Can choose to run recursively, only show folders or show all
        files (of specific types) and folders. if recursive = False and
        files=False, would just show current working directory. filetypes will
        show all filetypes by default, but can be specific ones as well.
    Inputs:
        * rec: Recursive check. Default: False (no recursion)
        * files: Show only files or folders. Default: True (files only)
        * ext: Which filetypes to return. Default: '' (any)
    Output:
        * <list>: filepaths
    '''
    isf=os.path.isfile
    opj=os.path.join
    abp=os.path.abspath
    paths=os.walk('.') if rec else '.' # where to check, if recursive
    ext='.'+ext if ext!='' else ext # if not default, prefix '.'

    # for each directory, for each file/folder, append to list
    all = [ipath for base in paths for ipath in glob(opj(abp(base[0]),'*'))]
    if(files):
        # only want files back. if ext='', return all incl w/o ext.
        sub=[ipath for ipath in all if (isf(ipath) and (ext in ipath))]
        return sub
    else:
        sub=[ipath for ipath in all if not isf(ipath)]
        return sub
# def dir

def ping(ip_address='www.google.com'):
    ''' check that an internet connection works'''
    s=Stamper();now=s.now
    while(not os.system('ping {} -c 1'.format(ip_address))==0):
        print(now())
        time.sleep(5)
    # ringbell() # kjg190320: perhaps not necessary?
    time.sleep(0.01)
    # ringbell() # perhaps not necessary?
    print('checker: connection works!')
# def ping

def ringbell(duration=0.15,freq=1300):
    ''' Objective: play a noise when called

    NOTE: this function requires sox to be installed on linux system!
    NOTE: not verified on windows
    '''
    if(OSVERSION==0):
        # using linux
        msg=os.system('play --no-show-progress --null --channels 1 synth {} sine {}'.format(duration,freq))
        if(msg!=0):
            raise Exception("Program 'sox' not installed. Sound could not play")
    elif(OSVERSION==1):
        raise Exception ("Not implemented yet, please verify below code")
        import winsound # must leave this here, would not work on other platforms.
        winsound.Beep(freq,duration)
# def ringbell

def listContents(arr,ReturnAsNPArr=False):
    ''' Take in a string list and return a dict or numpy array of
    the unique values and the number of times they appear.
    '''
    z=dict()
    for irow in arr:
        if(irow in z.keys()):
            z[irow]+=1 #irow already seen, incremnt counter
        else:
            z[irow]=1 # irow never seen, create key and set to 1
    if(ReturnAsNPArr==False):
        return z
    else:
        names=np.array([list(z.keys())],dtype='object').transpose()
        nums=np.array([list(z.values())],dtype='object').transpose()
    return np.column_stack((names,nums))
# def listContents

def pad(text,strLen,char=' ',side='L'):
    ''' Objective: provide easy, powerful padding tool for
        text. vars:
        'text': the text to pad. if not a string, will try to convert
        'strLen': maximum length of final string
        'char': padding character, default ' '
        'side': side to pad, default left. options: L, R
    '''
    text=str(text) if type(text)!=str else text
    if(len(text)<strLen):
        if(side=='R'):
            return pad(text+char,strLen,char,side)
        else:
            return pad(char+text,strLen,char,side)
    else:
        return text
# def pad

def clipin():
    ''' copy text from clipboard to a variable in python'''
    import tkinter
    r=tkinter.Tk()
    r.withdraw()
    a=r.clipboard_get()
    r.destroy()
    return a
#def clipin

def clipout(a):
    '''copy text from variable in python to clipboard
    KJGNOTE: not functioning correctly in python3 (ubuntu side)
    '''
    import tkinter
    r=tkinter.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(a)
    r.destroy()
# def clipout

def InsStr(main,txt,loc):
    ''' InsertString. Insert a given string exactly at the location given.
    Ex:
    >> InsStr("this is a test","not ",8)
        'this is not a test'
    '''
    return main[:loc]+txt+main[loc:]
#InsStr

def InsInFilenames(txt,criterion='',loc=0):
    ''' Insert In Filenames. Batch string insert into filenames. Insert
        specific text into filenames of files in a folder, an optionally only
        affect files that have a specific text in them.
    General steps:
        1. get list of files in working directory
        2. filter for files listed in criterion
        3. affect files in filtered list
        4. done.
    '''
    a=os.listdir(os.curdir)
    b=[]
    if(criterion!=''):
        for i in a:
            if(criterion in i):
                b.append(i)# filter files
        a=b # if criterion not blank, have new filtered list
    for i in a:
        os.rename(i,i[:loc]+txt+i[loc:])
#def InsInFilenames

def ListAllSubfolders():
    ''' Objective: list all subfolders in a directory
    '''
    a=[]
    b=os.getcwd();
    for dirpath, dirnames, filenames in os.walk('.'):
        a.append(dirpath.replace('.\\',b+'\\'))
    return a
#def ListAllSubfolders

def wordCount(arr):
    ''' Objective: Count number of words in a text array.
    Assumptions:
        separate words are separated by spaces, so
            just need to split string by spaces.
        input data is either string or array of strings
    '''
    n=0
    if(type('a')==type(arr)):
        # arr is a string
        n=n+len(arr.split())
    else:
        #assume arr is a list
        for i in arr:
            n=n+len(i.split())
        #forloop
    #if-typecheck
    return n
# def wordCount

def getprimes(integer):
    assert type(integer)==int, "Given value needs to be an integer"
    curr=int(integer+0)
    div=2
    d={}
    while(curr!=1):
        if(curr%div==0):
            d[div]=d[div]+1 if(div in d.keys()) else 1
            curr=curr/div
        else:
            div+=1
    return d
# def getprimes

def pyt(arr):
    ''' pyt(array) = pythagorean of items in list
    Assumptions:
        All items in list are double or integer numbers
        Return number as float
    '''
    b=sum([i*i for i in arr])
    return b**0.5
#def pyt



def scale(arr,xlim=(None,None),ylim=(0.01,0.99) ):
    ''' return a linearly scaled output of original array. follows simple
        interpolation for each element in the array. xmin and xmax are the
        min/max values of the original array. note: this is used instead of name
        "map", as this is already taken.
    INPUTS:
        arr: original array. e.g. 3x3 array
        ymin: minimum value for scaled output, default=0.01
        ymax: maximum value for scaled output, default=0.99
    OUTPUT:
        yarray: scaled array with same shape.
    '''

    # allow user to set input limits as well (if scalar, etc)
    xmin= np.min(arr) if(xlim[0]==None) else float(xlim[0])
    xmax= np.max(arr) if(xlim[1]==None) else float(xlim[1])
    ymin=ylim[0]
    ymax=ylim[1]
    return (ymax-ymin)/(xmax-xmin)*(np.array(arr)-xmin)+ymin

def md5_hash(filename):
    ''' return the md5 checksum of a file '''
    import hashlib as hl
    with open(filename,'rb') as f:
        return hl.md5(f.read()).hexdigest()


# eof
