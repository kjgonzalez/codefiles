'''
Title: The kimg module
Author: Kristian Gonzalez
Objective: Quickly & easily edit many image files for photo archives

== CALLING THIS MODULE REMOTELY ============================
(see module klib.py)

== NOTES ===================================================
Assumptions include:
* user has pillow (PIL fork) installed (pip3 intall Pillow)
* user has piexif installed (pip3 install piexif (exif preservation)
* images are located in same folder where some operations are done
* without user input, shall not overwrite an image when resizing
* all tabs are soft (use spaces, not \t)
* will follow guidelines from klib, such as 80char line limit, assume python3,
    use hanging indent (like shown here), create help text, etc.
* kjgnote: in order to prevent damaging photos that are panoramas (images with
    high ratios), will try to prevent resizing images that have a ratio greater
    than 2.0. Empirically, the 2015 image set shows this is where there's a 
    higher probability of a photo being a panorama, and thus being hurt by the
    "maximum dimension" resizing rule.

* KJG181121: need to overhaul kimg in order to: 
    1. make cross-platform - done?
    2. behave nicely with klib - done?
    3. use PIL - done
    4. ensure all have triple-quote based description - in progress
    5. KJG171112: BASED ON NEW DEVELOPMENT OF FUNCTION 'RECLIST', NEED TO 
        COMPLETELY RETHINK THE FLOW / STRUCTURE OF YOUR FUNCTIONS. FUCK.
        kjg181127: not sure what #5 means

'''

# INITIALIZE MODULES #######################################
from klib import pad # want direct access w/o module
from klib import PYVERSION
from klib import dir
import PIL.Image as pil
import numpy as np
import os
# Ensure that using python3. don't want to use py2 anymore
assert PYVERSION==3, "Must use python3. Exiting."

# from PIL import Image - done
# import os - done
# import time - ???
# import pyexiv2 - ???

# INITIALIZE FUNCTIONS #####################################

def gdm(imgname):
    ''' Get date modified '''
    # kjg181121: works
    import os
    return os.path.getmtime(imgname)
#
def gdc(imgname):
    ''' Get date created '''
    # kjg181121: works
    import os
    return os.path.getctime(imgname)
#
def gdt(imgname):
    ''' Get date taken (via PIL). Note: this fails for PNG images '''
    # kjg181121: works
    from PIL import Image	# compiled module from internet
    import time
    try:
        a= Image.open(imgname)._getexif()[36867] #gives string
        b='%Y:%m:%d %H:%M:%S' #string parser
        c=time.mktime(time.strptime(a,b)) 
        return c #format: seconds since epoch
    except KeyError:
        # reason: latest date will be after to gdm and gdc
        return time.time() #worst case, return current time
    except IOError:
        # reason: attempting to get data on non-JPG file
        print("FN 'gdt' WARNING, NON-JPG FILE:",imgname)
        return time.time() #user: use at own risk
    except TypeError:
        # reason: not entirely sure yet, but seems to be rare error
        #    ErrTxt: 'NoneType' object has no attribute '__getitem__'
        #   for now, will simply return current date, and hope that 
        #   functions 'gdm' or 'gdc' will capture earliest 
        #   date. (KJG170830)
        print("FN 'gdt' WARNING, missing attribute 'date taken':",imgname)
        return time.time()
#
def imgdate(seconds):
    ''' Convert float seconds value to formatted string '''
    # kjg181121: works
    import time
    tstruct=time.localtime(seconds) #get 'time.struct_time' type
    return time.strftime("%Y%m%d_%H%M%S",tstruct)[2:] # drop 2 digits from year
#
def getdate(imgname):
    ''' Objective: return earliest img file made, in seconds.'''
    # kjg181121: works
    m=gdm(imgname) #date photo modified
    c=gdc(imgname) #date photo created
    t=gdt(imgname) #date photo taken (not always available)
    return min(m,c,t)
#
def getlist(types=['jpg','JPG'],recursive=True):
    ''' Objective: return list of files desired to be 
        modified. Can search recursively or only in 
        the current folder. can also choose which types of files are returned in list
    '''
    # kjg181125: works
    # ensure types argument is valid
    assert type(types)==list, "'types' argument must be a list of strings"
    items=[]
    for itype in set(types): # set(...) ensures unique values only
        items.extend(dir(rec=recursive,ext=itype))
    # now have list of files including their filepaths
    return items
#
def getrange(dateOnly=True,subfolder='.',types=['jpg','JPG']):
    ''' Objective: return in a string the min and max dates of
        the files / photos contained in a single folder (no 
        subfolders)
        Assumptions: 
            * can search jpg's only, or all files
            * EVENTUALLY: recursive search option
            * return string of format: YYMMDD_HHmmSS-YYMMDD_HHmmSS
            * if dateOnly=True, then give format YYMMDD-YYMMDD
    '''
    # kjg181121: kinda works, but maybe needs to be optimized
    import os
    assert os.path.exists(subfolder),"Error: path doesn't exist: "+subfolder
    import time
    minDate=time.time()  # intitialize high
    maxDate=0            # initialize low
    startDir=os.getcwd() # store orig directory for return
    if(subfolder!='.'):
        # change to correct directory
        # 1. check directory exists
        # 2. go to directory
        # 3. begin operations
        # 4. (later) go back to current directory
        os.chdir(subfolder)
    mainList=getlist(types=types,recursive=False)
    for ifile in mainList:
        a=getdate(ifile)
        if(a<minDate): minDate = a
        if(a>maxDate): maxDate = a
    # once complete, convert to dates and return that
    if(dateOnly==True): 
        # if only want dates (YYMMDD), then isolate for that
        a=imgdate(minDate)
        a=a[:a.find("_")]
        b=imgdate(maxDate)
        b=b[:b.find("_")]
        rangeStr=a+"-"+b
    else:
        rangeStr=imgdate(minDate)+"-"+imgdate(maxDate)
    os.chdir(startDir) # go back to orig directory (safeguard)
    return rangeStr
#
def getext(imgname):
    ''' Return extension (with period) of file '''
    # kjg181121: works
    return imgname.split('.')[-1]
#
def imgrename(imgname,appendOldName=False):
    ''' objective: handle the messiness of renaming an image
        file and ensuring that it doesn't have the same name
        as an image taken in the same YYMMDD_HHmmSS as
        another photo. Exif data is preserved. Specific to 
        calling this function, you can append the old file 
        name to the new file (imgdate) value that is 
        generated, such as if wanting to keep a video's 
        original name.
    '''
    # kjg181125: works, but ONLY works in windows!!!
    # kjg181213: FIX THIS SECTION!!!! 
    ''' fix this section!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
    import os
    newname=imgdate(getdate(imgname))	#get new name for img
    if(appendOldName==True):
        # append imgdate value with old 
        #   filename (except extension)
        newname = newname + '_'+imgname[:imgname.find('.')]
    #adding in special section in case function being used 
    #   to modify a file remotely
    if('\\' in img):
        #get path to file (using some replace magic)
        c=img.count('\\')   #want to replace last '\\'
        path=img.replace('\\','/').replace('/','\\',c-1)
        path=path.split('/')[0]+'\\' #use '/' as splitter
        newname=path+newname #prefix filename w/ path
    
    ext='.'+getext(img)			#ensure have proper ext
    i=0	#counter for maximum number of attempts
    validname=False	#flag for knowing if have valid name
    while(validname==False and i<100):
    # want to ensure filename is unique
        try:
            validname=True	# assume attempt will be success
            if(i==0):		# first attempt
                os.rename(img,newname+ext)	#simple rename
            else:			# not first attempt
                os.rename(img,newname+'_'+str(i)+ext)
        except WindowsError: # error windows gives if ...
            validname=False	#  try to name two files same
            i=i+1	# reset flag and increment counter
#
def imgreduce(imgname,maxsize=2000,overwrite=False):
    '''Objective: reduce image size, and by default save 
        to new file name. if file is smaller than
        maxsize, image will not be modified at all.
        defaults: maxsize = 2000, overwrite=False
	** kjgnote: need to double check if this function truly working, as 
		well as being cross-platform.
    '''
    from PIL import Image
    import piexif # LEARN HOW TO USE THIS!!!
    # kjg181127: works
    im=Image.open(imgname)	#open image file object
    # before doing anything else, check if img too small
    if(im.size[0]<maxsize and im.size[1]<maxsize):
        return 'NoChnge:'+imgname
    
    # before modifying image, try getting exif properties
    flag_hasexif=True
    try:
        exif=piexif.load(im.info['exif'])
        flag_hasexif=True
    except KeyError:
        print("FN 'imgreduce' WARNING: MISSING EXIF DATA:",imgname)
        flag_hasexif=False
    if(overwrite==False):
        #do not want to overwrite image; make new file
        i=imgname.split('.')
        imgname=i[0]+'_edit'+'.'+i[1]
    #otherwise, imgname will remain the same and overwrite
    
    #next, set new image dimensions
    i=im.size # (w,h)
    if(i[0]>i[1]):  #if w > h
        w2=maxsize
        h2=int(float(w2)/float(i[0])*i[1])
    else:           # w<=h
        h2=maxsize
        w2=int(float(h2)/float(i[1])*i[0])
    #resize and save image, with exif data
    if(flag_hasexif):
        exif_byte=piexif.dump(exif) # perhaps can do sooner
        im.resize((w2,h2),Image.ANTIALIAS).save(imgname,exif=exif_byte)
    else:
        im.resize((w2,h2),Image.ANTIALIAS).save(imgname)
#
def renred(maxsize=2000,overwrite=False,recursive=False):
    ''' Objective: rename and resize all images from filename list given
        and resize them to desired amount as well as choose
        whether or not to overwrite files
        NOTE: only targets jpg files. ignores all others.
        '''
    for ifile in getlist(recursive=recursive):
        print('Renaming:',ifile)
        imgrename(ifile)
    for ifile in getlist(recursive=recursive):
        print('Resizing:',ifile)
        imgreduce(ifile,maxsize,overwrite)
    print("FN 'renred': Done")
#
def renSubfolder(SubfolderName,JPGONLY=True,DATEONLY=False):
    ''' Objective: Rename a SUBFOLDER of current directory 
    by going in, looking at each img's mod dates (this
    uses function 'getdate', doesn't depend on 
    filename), then determining min / max. optional 
    YYMMDD data. arguments are if only look at 
    imgs, use only.
    '''
    n1=SubfolderName
    n2=getrange(jpgOnly=JPGONLY,dateOnly=DATEONLY,subfolder=SubfolderName)
    #try:
    os.rename(n1,n2)
    print("FN 'renSubfolder': renamed '{}' to '{}'".format(n1,n2))
#



