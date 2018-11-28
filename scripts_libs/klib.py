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
'''

# FIRST, BEFORE ALL ELSE, CHECK VERSIONS OF OS AND PYTHON
def __getSysInfo__():
    ''' Get local computer info. Generally, should keep software OS and version
        independent, but this may not always be possible. Also, avoiding
        importing sys or other modules to pylib.
    Returns:
        * OSVERSION (linux[0]/win[1]/mac[2]?)
        * PYVERSION (2/3)
    '''
    import sys
    if('linux' in sys.platform):
        osver = 0
    elif('win' in sys.platform):
        osver = 1
    else:
        osver = 2
    return (osver,sys.version_info.major)

(OSVERSION,PYVERSION) = __getSysInfo__()


def getallsubfolders():
    ''' Simple command to get all subfolders in a given folder. index 0 is the 
        current folder.
    '''
    import os
    from glob import glob
    subfolders=[os.getcwd()+y[1:] 
            for x in os.walk('.') 
                for y in glob(os.path.join(x[0]))]
    return subfolders

# create a function that will make a noise when done
def ringbell(duration=0.15,freq=1300):
    ''' Objective: play a noise when called
    
    NOTE: this function requires sox to be installed on linux system!
    '''
    if(OSVERSION==0):
        # using linux
        import os
        msg=os.system('play --no-show-progress --null --channels 1 synth {} sine {}'.format(duration,freq))
        if(msg!=0):
            raise Exception("Program 'sox' not installed. Sound could not play")
    elif(OSVERSION==1):
        raise Exception ("Not implemented yet, please verify below code")
        import winsound
        winsound.Beep(freq,duration)
# def ringbell

def timestamper(pfunc):
    ''' intended to wrap a print function or similar, which prepends text to be 
        printed with a timestamp, which looks like:
        LOG: YYMMDD-HHmmSS
    '''
    import time
    import functools
    logstr='LOG: '+time.strftime('%Y%b%d-%H:%M:%S',time.localtime(time.time()))+'\n'
    @functools.wraps(pfunc)
    def wrapper_stamper(*args,**kwargs):
        pfunc(logstr,*args,**kwargs)
    return wrapper_stamper





class Stopwatch:
    ''' Stopwatch: Basic class that logs a time when it's created. Can also 
        restart timer with function call "tik", and can get the elapsed time
        with function "tok". Designed to be a bit similar to matlab functions.
        Note that all values are in seconds.
        
        Example: 
        >> from klib import Stopwatch as st
        >> a=st()
        >> (some code)
        >> print(a.tok())
        OUT: 5.2087955
    '''
    def tik(self):
        self.t1=self.time.time()
    def tok(self):
        return self.time.time()-self.t1
    def __init__(self):
        import time
        self.time=time
        self.tik()
# class Stopwatch

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
        import numpy as np
        names=np.array([list(z.keys())],dtype='object').transpose()
        nums=np.array([list(z.values())],dtype='object').transpose()
    return np.column_stack((names,nums))
# def listContents

def pad(text,strLen,char=' ',side='L'):
    ''' Objective: provide easy, powerful padding tool for
        text. vars:
        'text': the text to pad
        'strLen': maximum length of final string
        'char': padding character, default ' '
        'side': side to pad, default left. options: L, R
    '''
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
    import Tkinter
    r=Tkinter.Tk()
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
    import os
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
    import os
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

def pyt(arr):
    ''' pyt(array) = pythagorean of items in list
    Assumptions:
        All items in list are double or integer numbers
        Return number as float
    '''
    b=0
    for i in arr: b=b+i*i
    return b**0.5
#def pyt

def avg(arr):
    ''' avg(array) = average items in list
    Assumptions:
        All items in list are double or integer numbres
        return number as float
    '''
    b=0.0
    for i in arr: b = b+float(i)
    return b/float(len(arr))
#def avg
