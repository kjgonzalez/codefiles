'''
Kristian Gonzalez. 

THIS IS THE OFFICIAL LOCATION OF ALL PYTHON FUNCTIONS AND
CLASSES THAT ARE MADE FOR PERSONAL USE. ONLY FUNCTIONS THAT
ARE FULLY FUNCTIONAL OR STABLE MAY BE USED HERE. IF A 
FUNCTION IS NOT USABLE YET, EITHER SAVE IT ELSEWHERE OR 
SAVE IT HERE, COMMENTED OUT.


== Miscellaneous ===========================================
* all lines shall be at maximum 60 characters long. if 
    writing text, using hanging indent as shown in this 
    sentence
* create help text for all items written here. this is to 
    facilitate understanding and relearning things that may
    have been created too long ago to remember. 
* it's understood that this file is being shared between 2 
    computers AND dropbox AND a usb stick. trying to 
    maintain uniformity is fairly important. remember to 
    delete needless copies
* as of 181008, will now always use 4 spaces as the tab 
    delimiter. using a "hard tab" causes too many formatting
    headaches across different programs, platforms, etc.
'''

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
#
def clipin():
    ''' copy text from clipboard to a variable in python'''
    import Tkinter
    r=Tkinter.Tk()
    r.withdraw()
    a=r.clipboard_get()
    r.destroy()
    return a
#def clipin
def clipout(a):
    '''copy text from variable in python to clipboard '''
    import Tkinter
    r=Tkinter.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(a)
    r.destroy()
# def clipout
def ins(main,txt,loc):
    return main[:loc]+txt+main[loc:]
#ins
def iif(txt,criterion='',loc=0):
    ''' "iif": "Insert In Filenames". Insert specific text 
        into files in a folder, an optionally only affect
        files that have a specific text in them.
        general steps: 
        1. get list of files in working directory
        2. filter for files listed in criterion
        3. affect files in filtered list
        4. should be done.
    '''
    import os
    a=os.listdir(os.curdir)
    b=[]
    if(criterion!=''):
        for i in a:
            if(criterion in i):
                # print     i
                b.append(i)# filter files
        a=b # if criterion not blank, have new filtered list
    for i in a: #print i #modifyme
        os.rename(i,i[:loc]+txt+i[loc:])
#def iif
def ListAllSubfolders():
    import os
    a=[]
    b=os.getcwd();
    for dirpath, dirnames, filenames in os.walk('.'):
        a.append(dirpath.replace('.\\',b+'\\'))
    return a
#def ListAllSubfolders
def wordCount(arr):
    ''' Author: Kris Gonzalez
    Objective: Count number of words in a text 
        array in the clipboard.
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
# # # for whatever reason, decided to have some mathematical formulas here.
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
def area_c(diam):
    '''return area of circle, given diameter'''
    from math import pi
    return pi/4.0*diam**2
def circumference(diam):
    '''return circumference of circle, given diameter'''
    from math import pi
    return pi*diam
