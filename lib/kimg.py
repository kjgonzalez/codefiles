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

TODO: make a simple separation program that can takes an entire folder of files and separates them by how many hours
    are between chronologically ordered photos. use as an auto-folderize program

TODO: make a function that takes in a jpg and creates a pdf with preconfigured settings. e.g. imgToPDF(imgpath,newname,settings)
'''

# INITIALIZE MODULES #######################################
from klib import PYVERSION, getlist
import PIL.Image as pil
import time
import os
from typing import Union
assert PYVERSION == 3, "Must use python3. Exiting."

# INITIALIZE FUNCTIONS #####################################

def gdm(imgname):
    ''' Get date modified '''
    # kjg181121: works
    import os
    return os.path.getmtime(imgname)

def gdc(imgname):
    ''' Get date created '''
    # kjg181121: works
    import os
    return os.path.getctime(imgname)

def gdt(imgname):
    ''' Get date taken (via PIL). Note: this fails for PNG images '''
    # kjg181121: works
    from PIL import Image    # compiled module from internet
    try:
        with Image.open(imgname) as f:
            a = f._getexif()[36867] #gives string
            f.close()
        b = '%Y:%m:%d %H:%M:%S' #string parser
        c = time.mktime(time.strptime(a,b))
        return c # format: seconds since epoch
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

def imgdate(seconds):
    ''' Convert float seconds value to formatted string '''
    # kjg181121: works
    import time
    tstruct=time.localtime(seconds) #get 'time.struct_time' type
    return time.strftime("%Y%m%d_%H%M%S",tstruct)[2:] # drop 2 digits from year

def getdate(imgname):
    ''' Objective: return earliest img file made, in seconds.'''
    # kjg181121: works
    m=gdm(imgname) #date photo modified
    c=gdc(imgname) #date photo created
    t=gdt(imgname) #date photo taken (not always available)
    return min(m,c,t)

def getrange(subfolder='.', date_only=True, recursive=True, exts:str= 'jpg-JPG'):
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
    assert os.path.exists(subfolder),"Error: path doesn't exist: {}".format(subfolder)
    min_date = time.time()  # intitialize high
    max_date = 0            # initialize low
    main_list = getlist(subfolder,recursive=recursive,exts=exts)
    for ifile in main_list:
        idate = getdate(ifile)
        if(idate < min_date): min_date = idate
        if(idate > max_date): max_date = idate
    # once complete, convert to dates and return that
    if(date_only):
        # if only want dates (YYMMDD), then isolate for that
        idate = imgdate(min_date)
        idate = idate[:idate.find("_")]
        idate2 = imgdate(max_date)
        idate2 = idate2[:idate2.find("_")]
        range_str = idate+"-"+idate2
    else:
        range_str = imgdate(min_date)+"-"+imgdate(max_date)
    return range_str

def getext(imgname):
    ''' Return extension (with period) of file '''
    # kjg181121: works
    return os.path.splitext(imgname)[1][1:]

def imgrename(imgname, append=False):
    ''' Objective: handle the messiness of renaming an image
        file and ensuring that it doesn't have the same name
        as an image taken in the same YYMMDD_HHmmSS as
        another photo. Exif data is preserved. Specific to 
        calling this function, you can append the old file 
        name to the new file (imgdate) value that is 
        generated, such as if wanting to keep a video's 
        original name.
    '''
    newname = imgdate(getdate(imgname))   # get new name for img
    path,oldname = os.path.split(imgname)
    ext = getext(imgname)
    if(append):
        newname = newname + '_'+imgname[:imgname.find('.')]

    # ensure that have unique filename and not overwriting
    i = 0
    while(i < 100):
        testname = os.path.join(path,newname)+\
                   ('_'+str(i) if(i>0) else '') + \
                   '.'+ext
        if(os.path.exists(testname)): i += 1
        else:
            os.rename(imgname,testname)
            return os.path.abspath(testname)

def imgreduce(imgname,maxsize=2000,overwrite=False):
    '''Objective: reduce image size, and by default save 
        to new file name. if file is smaller than
        maxsize, image will not be modified at all.
        defaults: maxsize = 2000, overwrite=False
    ** kjgnote: need to double check if this function truly working, as
        well as being cross-platform.
    '''
    import piexif
    # kjg181127: works
    im = pil.open(imgname)
    # before doing anything else, check if img too small
    if(im.size[0] < maxsize and im.size[1] < maxsize):
        return 'NoChange:'+imgname
    
    # before modifying image, try getting exif properties
    flag_hasexif=True
    try:
        exif = piexif.load(im.info['exif'])
        flag_hasexif=True
    except KeyError:
        print("FN 'imgreduce' WARNING: MISSING EXIF DATA:",imgname)
        flag_hasexif=False
    if(not overwrite):
        i = os.path.splitext(imgname)
        imgname = i[0]+'_edit'+i[1]

    # next, set new image dimensions
    i = im.size # (w,h)
    if(i[0] > i[1]):  #if w > h
        w2 = maxsize
        h2 = int(float(w2)/float(i[0])*i[1])
    else:           # w<=h
        h2 = maxsize
        w2 = int(float(h2)/float(i[1])*i[0])
    #resize and save image, with exif data
    if(flag_hasexif):
        exif_byte = piexif.dump(exif) # perhaps can do sooner
        im.resize((w2,h2),pil.ANTIALIAS).save(imgname,exif=exif_byte)
    else:
        im.resize((w2,h2),pil.ANTIALIAS).save(imgname)
    im.close()

def renfolder(path,exts='jpg-JPG',append=False):
    ''' Objective: Rename a SUBFOLDER of current directory 
    by going in, looking at each img's mod dates (this
    uses function 'getdate', doesn't depend on 
    filename), then determining min / max. optional 
    YYMMDD data. arguments are if only look at 
    imgs, use only.
    INPUTS:
        * path: subfolder to rename
        * exts: extensions
        * append: keep old name as suffix
    '''
    assert os.path.isdir(path), "Invalid path: {}".format(path)
    assert path != '.', "Cannot rename working directory"
    path = os.path.abspath(path)
    base,oldname = os.path.split(path)
    newname = os.path.join(base,getrange(path,exts=exts))
    if(append):
        newname = newname+' '+oldname
    os.rename(path,newname)
    print("FN 'renSubfolder': renamed '{}' to '{}'".format(path,newname))

def renred(path, maxsize=2000,overwrite=False,recursive=False):
    ''' For each jpg in path, resize and rename.
        NOTE: only targets jpg files. ignores all others.
        '''
    for ifile in getlist(path,recursive=recursive,exts='jpg-JPG'):
        imgreduce(ifile,maxsize=maxsize,overwrite=overwrite)
        imgrename(ifile)

def img2pdf(path,resolution:Union[str,int,float]=100):
    '''
    Convert an image to pdf.
    INPUTS:
        * path: path to image file
        * resolution: typically a number. can also give 'a4' and program will attempt to auto-resize based on width
    NOTE: A4 dimensions are (210,297) mm, (8.268,11.693) inches
    '''
    x: pil.Image = pil.open(path).convert('RGB')
    basepath,_fname = os.path.split(path)
    newpath = os.path.join(basepath,os.path.splitext(_fname)[0]+'.pdf')
    if(resolution == 'a4'):
        # try to set resolution to A4 dimensions (in inches)
        resolution = x.size[0]/8.268
    x.save(newpath, resolution=resolution)  # default resolution seems to be 72 dpi

def reformat(file:str,newtype:str='webp',oldtypes:str='jpg-JPG-png-PNG'):
    ''' Reformat arg file as newtype.
    INPUTS:
        * file: filepath (to file), 'here'= files in current folder, 'rec'=current and subfolders
        * newtype: desired type. acceptable: jpg, png, webp
        * oldtypes: dash-separated types to look for. default: 'jpg-JPG-png-PNG'
    OUTPUT: (new files)
    '''
    # determine desired file(s)
    files = []
    if(os.path.isfile(file)):
        files.append(file)
    elif(file == 'here'):
        files = getlist('.',exts=oldtypes)
    elif(file == 'rec'):
        files = getlist('.',recursive=True,exts=oldtypes)
    else: raise Exception('arg file must be valid file, ')

    assert newtype in ['jpg','png','webp']
    for ifile in files:
        base = os.path.splitext(ifile)[0]
        print('next:',ifile)
        if(('.png' in ifile or '.PNG' in ifile) and (newtype in ['png','webp'])):
            pil.open(ifile).convert('RGBA').save(base+'.'+newtype)
        else:
            pil.open(ifile).convert('RGB').save(base + '.' + newtype)
    print('done')

if(__name__ == '__main__'):
    import argparse

    actions = dict()
    actions['renameFolder'] = 'rename folder to reflect range of files inside, i.e. "YYMMDD-YYMMDD"'
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,description='Potential arguments:'+str(list(actions.keys())))
    p.add_argument('usage',type=str,help='desired operation')
    p.add_argument('--args',nargs='+',required=False)
    args=p.parse_args()
    action = args.usage
    others = args.args
    # want to implement some basic modification abilities to this lib. will add as needed
    if(action == 'renameFolder'):
        # want to rename folder to reflect range of images / videos inside
        print("this action")
        targFolder = others[0]
        assert os.path.isdir(targFolder,),"argument needs to be target folder. exiting."
        renfolder(targFolder)

    else: print("Error, desired action not recognized. fix or add. exiting.")
    
    
    
    
    
    

