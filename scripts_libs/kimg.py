'''
OBJECTIVE: Quickly / easily rename many image files for 
    photo archives

ASSUMPTIONS: 
    * user has pillow (PIL fork) installed (pip3 intall Pillow)
    * images are located in same folder where some operations are done
    * without user input, shall not overwrite an image when resizing
    * all tabs are soft (use spaces, not \t)

DEPRACATED INFO:
* assumption:user has pyexiv2 installed (http://tilloy.net/dev/pyexiv2/download.html)


KJG171112: BASED ON NEW DEVELOPMENT OF FUNCTION 'RECLIST', NEED TO 
COMPLETELY RETHINK THE FLOW / STRUCTURE OF YOUR FUNCTIONS. FUCK.

KJG181121: need to overhaul kimg in order to: 
1. make cross-platform
2. behave nicely with klib
3. use PIL
4. ensure all have triple-quote based description
5. figure out what's meant by kjg171112 statement



'''

# INITIALIZE MODULES #######################################
import klib
from klib import pad # want direct access w/o module
import PIL.Image as pil
import numpy as np
import os
# Ensure that using python3. don't want to use py2 anymore
assert klib.PYVERSION==3, "Must use python3. Exiting."

# from PIL import Image - done
# import os - done
# import time - ???
# import pyexiv2 - ???

# INITIALIZE FUNCTIONS #####################################

def gdm(img):
    # objective: get date modified
    # kjg181121: works
    import os
    return os.path.getmtime(img)
#
def gdc(img):
    # objective: get date created
    # kjg181121: works
    import os
    return os.path.getctime(img)
#
def gdt(img):
    #objective: get date taken (via PIL)
    # NOTE: THIS FAILS FOR PNG IMGS, perhaps due tag No.
    # kjg181121: works
    from PIL import Image	# compiled module from internet
    import time
    try:
        a= Image.open(img)._getexif()[36867] #gives string
        b='%Y:%m:%d %H:%M:%S' #string parser
        c=time.mktime(time.strptime(a,b)) 
        return c #format: seconds since epoch
    except KeyError:
        # reason: latest date will be after to gdm and gdc
        return time.time() #worst case, return current time
    except IOError:
        # reason: attempting to get data on non-JPG file
        print("FN 'gdt' WARNING, NON-JPG FILE:",img)
        return time.time() #user: use at own risk
    except TypeError:
        # reason: not entirely sure yet, but seems to be rare error
        #    ErrTxt: 'NoneType' object has no attribute '__getitem__'
        #   for now, will simply return current date, and hope that 
        #   functions 'gdm' or 'gdc' will capture earliest 
        #   date. (KJG170830)
        print("FN 'gdt' WARNING, missing attribute 'date taken':",img)
        return time.time()
#
def imgdate(seconds):
    # convert float seconds value to formatted string
    # kjg181121: works
    import time
    tstruct=time.localtime(seconds) #get 'time.struct_time' type
    return time.strftime("%Y%m%d_%H%M%S",tstruct)[2:] # drop 2 digits from year
#
def getdate(img):
    ''' Objective: return earliest img file made, in seconds.'''
    # kjg181121: works
    m=gdm(img) #date photo modified
    c=gdc(img) #date photo created
    t=gdt(img) #date photo taken (not always available)
    return min(m,c,t)
#
def getrange(jpgOnly=True,dateOnly=True,sub='.'):
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
    import time
    minDate=time.time()	# intitialize high
    maxDate=0			# initialize low
    startDir=os.getcwd() # store orig directory for return
    if(sub!='.'):
        # change to correct directory
        # 1. check directory exists
        # 2. go to directory
        # 3. begin operations
        # 4. (later) go back to current directory
        os.chdir(sub)
    if(jpgOnly==True):
        # using list comprehension technique here:
        mainList=[x for x in os.listdir('.') if (
        'jpg' in x or 'JPG' in x)]
    else:
        mainList=os.listdir('.')
    for iFile in mainList:
        a=getdate(iFile)
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
def getext(img):
    # objective: return extension (with period) of file
    # kjg181121: works
    return img.split('.')[-1]
#
def getlist(types=['jpg'],recursive=True):
    ''' Objective: return list of files desired to be 
        modified. Can search recursively or only in 
        the current folder. can also choose which types of files are returned in list
    '''
    # kjg181125: works
    import os
    from glob import glob
    # for each type, append to list
    
    # ensure types are valid
    if(type(types)==str): types=[types] # if given as string, correct it
    
    items=[]
    for itype in types: 
        if(recursive):
            [items.append(os.getcwd()+y[1:]) for x in os.walk('.') for y in glob(os.path.join(x[0], '*.'+itype))]
        # for each type, append the list of files that are present with the specified type
        else:
            [items.append(os.getcwd()+ifile[1:]) for ifile in glob('./*.jpg')]
    # now have list of files including their filepaths
    return items
#
def imgrename(img,appendOldName=False):
    ''' objective: handle the messiness of renaming an image
        file and ensuring that it doesn't have the same name
        as an image taken in the same YYMMDD_HHmmSS as
        another photo. Exif data is preserved. Specific to 
        calling this function, you can append the old file 
        name to the new file (imgdate) value that is 
        generated, such as if wanting to keep a video's 
        original name.
    '''
    # kjg181125: works, but may ONLY work in windows!!!
    import os
    newname=imgdate(getdate(img))	#get new name for img
    if(appendOldName==True):
        # append imgdate value with old 
        #	filename (except extension)
        newname = newname + '_'+img[:img.find('.')]
    #adding in special section in case function being used 
    #	to modify a file remotely
    if('\\' in img):
        #get path to file (using some replace magic)
        c=img.count('\\')	#want to replace last '\\'
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
	'''
	from PIL import Image
	import piexif # LEARN HOW TO USE THIS!!!
    # kjg181125: FIXME!!! here
	
	im=Image.open(imgname)	#open image file object
	# before doing anything else, check if img too small
	if(im.size[0]<maxsize and im.size[1]<maxsize):
		return 'NoChnge:'+imgname
	
	# before modifying image, get exif properties
	si=pyexiv2.ImageMetadata(imgname)
	si.read()
	
	if(overwrite==False):
		#do not want to overwrite image; make new file
		i=imgname.split('.')
		imgname=i[0]+'_edit'+'.'+i[1]
	#otherwise, imgname will remain the same and overwrite
	
	#next, set new image dimensions
	i=im.size # (w,h)
	if(i[0]>i[1]):	#if w > h
		w2=maxsize
		h2=int(float(w2)/float(i[0])*i[1])
	else:			# w<=h
		h2=maxsize
		w2=int(float(h2)/float(i[1])*i[0])
	
	#resize and save image
	im.resize((w2,h2),Image.ANTIALIAS).save(imgname)
	
	# transfer over exif properties before done with file
	di=pyexiv2.ImageMetadata(imgname)
	di.read()
	si.copy(di)
	di['Exif.Photo.PixelXDimension'] = w2
	di['Exif.Photo.PixelYDimension'] = h2
	di.write() # have now saved metadata
	return 'Resized:'+imgname
#
# def renredall(maxsize=2000,overwrite=False):
	# ''' objective: in current folder, rename all jpg's
		# and resize them to desired amount as well as choose
		# whether or not to overwrite files
		# NOTE: only targets jpg files. ignores all others.
		# '''
	# import os
	# for i in os.listdir('.'):
		# if('jpg' in i or 'JPG' in i):
			# imgrename(i)
	# for i in os.listdir('.'):
		# if('jpg' in i or 'JPG' in i):
			# imgreduce(i,maxsize,overwrite)
	# print 'done'
# #
# def recrenredall(overwrite,maxsize=2000):
	# ''' Objective: in current and all subfolders, rename
		# all jpg's and resize them to desired amount as well
		# as choose whether or not to overwrite files. Because
		# of high risk of error without proper input, require
		# 'overwrite' field to be filled out.
		# 'overwrite=True' >> overwrite old files
		# NOTE: only targets jpg files, ignores all others.
	# '''
	# import os
	# # first, rename all files to proper convention
	# os.system('dir /s /b "*jpg" > delme')
	# f=file('delme')
	# a=[]
	# for i in f:
		# if('jpg' in i or 'JPG' in i):
			# a.append(i[:-1])
	# f.close()
	# for i in a:
		# imgrename(i)
	# # after renaming, must get new list for resizing
	# os.system('dir /s /b "*jpg" > delme')
	# f=file('delme')
	# a=[]
	# for i in f:
		# if('jpg' in i or 'JPG' in i):
			# a.append(i[:-1])
	# f.close()
	# counter=1
	# for i in a:
		# print imgreduce(i,maxsize,overwrite),'('+str(counter)+'/'+str(len(a))+')'
		# counter=counter+1
	# # once complete renaming, resizing: delete txt file
	# os.system('del delme')
	# print 'done'
# #
# def renSubfolder(SubfolderName,JPGONLY=True,DATEONLY=False):
	# ''' Objective: Rename a SUBFOLDER of current directory 
	# by going in, looking at each img's mod dates (this
	# uses function 'getdate', doesn't depend on 
	# filename), then determining min / max. optional 
	# YYMMDD data. arguments are if only look at 
	# imgs, use only.
	# '''
	
	# import os
	# a=SubfolderName
	# #try:
	# os.chdir(a)
	# b=getrange(jpgOnly=JPGONLY,dateOnly=DATEONLY)
	# os.chdir('..')
	# os.rename(a,b)
# #



