"""
Shell & GUI -based image manipulation
k241031: moving old code to "_old" and starting fresh.
k241102: given power of exif data, will only use
some goals:
* GUI
* batch resize & rename
* folder rename
*

sources:
exif data tags: https://exiv2.org/tags.html
piexif library: https://pypi.org/project/piexif/
iterate on filesize: https://stackoverflow.com/questions/40587343/python-pil-find-the-size-of-image-without-writing-it-as-a-file

relevant tags:
305: Exif.Image.Software (note: should modify with "kimg_v1"
36867: Exif.Image.DateTimeOriginal

"""

import time
import os
import os.path as osp
from typing import Union, List
import io
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import PIL.Image as pil
import piexif as pex

KEY_DATETAKEN = pex.ExifIFD.DateTimeOriginal
KEY_SOFTWARE = pex.ImageIFD.Software
KEY_XPCOMMENT = pex.ImageIFD.XPComment
KEY_XPKEYWORDS = pex.ImageIFD.XPKeywords

IMG_MAXSIZE=2000 # k241031: standard maximum dimension for an image

def tags2xpkeywords(tags:List[str]):
    """
    Return a jpg-xpkeyword compatible tag format. the field ImageIFD.XPKeywords (40094)

    """
    res = []
    assert ';' not in ''.join(tags),"semicolon ';' not permitted in tags"
    for ichar in ';'.join(tags):
        res.append(ichar.encode()[0])
        res.append(0)
    res.append(0)
    res.append(0)
    return res


def get_date_taken(imgpath:str,as_str=False,strformat="%y%m%d_%H%M%S") ->Union[float,str]:
    """
    Given path to image, make best effort to determine date taken. Either return date taken as
      epoch or time string
    strformat: yymmdd_HHMMSS, e.g. 241031_025236

    """
    _created = os.path.getctime(imgpath)
    _modified = os.path.getmtime(imgpath)
    # get date from exif data
    _taken = time.time()
    try:
        exraw = pex.load(imgpath)
        exraw2 = exraw['Exif'][KEY_DATETAKEN].decode()
        _taken = time.mktime(time.strptime(exraw2, '%Y:%m:%d %H:%M:%S'))
    except Exception as e:
        pass # reluctantly doing it this way, as cannot anticipate all filetypes that can throw error
    _filename=time.time()
    # try:
    #     txt_name = osp.splitext(osp.basename(imgpath))[0]
    #     _filename = time.mktime(time.strptime(txt_name, '%y%m%d_%H%M%S'))
    # except Exception as e:
    #     pass
    s_epoch = min(_created,_modified,_taken,_filename)
    if(as_str):
        return time.strftime("%y%m%d_%H%M%S",time.localtime(s_epoch))
    return s_epoch

def epoch2exifstr(epochtime:float):
    ''' convert epoch data to exif string (string, not bytes) '''
    return time.strftime("%Y:%m:%d %H:%M:%S", time.localtime(epochtime))

def rename_resize(filepath:str,maxdim=2000,maxsz_kb=800.0,modify_exif=False,qual_initial=95):
    """
    Rename and resize image while keeping relevant metadata intact. minimize file read/writes, so
      will check conditions a multiple times

    General Steps:
    1. get date taken
    3. if name & dims already appropriate, exit
    2. rename file
    3. resize file
    4. modify exif as needed
    5. save with exif

    INPUT:
      filepath: path to single image file
      maxdim: maximum allowable dimension (height or width)
      maxsz_kb: maximum allowable filesize (in kilobytes)
      modify_exif: if exif data should be modified (update date taken, say modified by klib_v1)
    OUTPUT:
      Return status value when complete:
        0: success
        1+: failure, somehow
    """
    earliestdate_float = get_date_taken(filepath)
    earliestdate = time.strftime("%y%m%d_%H%M%S",time.localtime(earliestdate_float))
    basename = osp.splitext(osp.basename(filepath))[0]
    try:
        exif = pex.load(filepath)
    except Exception as e:
        exif = None
    fsize_kb = osp.getsize(filepath)/1024
    img = pil.open(filepath)
    dsize = max(img.size)
    must_resize = (dsize>maxdim) or (fsize_kb>maxsz_kb)
    must_rename = earliestdate!=basename
    is_compressible=osp.splitext(filepath)[1].lower() in ['.jpg','.jpeg']
    qual = qual_initial if(is_compressible) else 100

    fpath2 = osp.join(os.path.dirname(filepath), earliestdate + osp.splitext(filepath)[1])
    # avoid overwriting an existing file with same name
    if(osp.exists(fpath2)):
        tmp = fpath2
        i=0
        while(os.path.exists(tmp)):
            i+=1
            tmp = f"_{i}".join(osp.splitext(fpath2))
        fpath2 = tmp

    if(not must_rename and not must_resize):
        return 1 # nothing was changed
    elif(must_rename and not must_resize):
        try:
            img.close()
            os.rename(filepath,fpath2)
        except PermissionError as e:
            print(e)
            print('pause')
        return 0
    # otherwise, must resize

    if(exif is not None):
        if(modify_exif):
            exif['0th'][pex.ImageIFD.Software] += "+klib_v1".encode()
            exif['Exif'][KEY_DATETAKEN] = epoch2exifstr(earliestdate_float)
        exif_bytes = pex.dump(exif)
    else:
        exif_bytes=b''

    newmax = min(maxdim,dsize)
    newdims = [int(i*newmax/dsize) for i in img.size]
    img = img.resize(newdims)

    def img2bytes(img_,exifbytes_,qual_) ->(io.BytesIO,float):
        bytes_ = io.BytesIO()
        img_.save(bytes_,exif=exifbytes_,quality=qual_,format='jpeg')
        sz_kb=bytes_.tell()/1024
        bytes_.seek(0,0)
        return bytes_,sz_kb

    filebytes_, newsize = img2bytes(img, exif_bytes, qual)
    fnameout = fpath2 if (must_rename) else filepath

    if(is_compressible):
        # check how large file would be, save when under required maxfilesize

        while(newsize>maxsz_kb and qual>30):
            qual-=5
            filebytes_, newsize = img2bytes(img, exif_bytes, qual)
            # with io.BytesIO() as filebytes:
            #     img.save(filebytes,exif=exif_bytes,quality=qual,format='jpeg')
            #     newsize = filebytes.tell()/1024
            # should_iterate = newsize>maxsz_kb and qual>30
            # if(should_iterate): qual-=5 # should always start at 95%

    print(f'{osp.basename(fnameout)} {qual}')
    fout = open(fnameout,'wb')
    fout.write(filebytes_.read())
    fout.close()
    img.close()
    if(must_rename):
        img.close()
        os.remove(filepath)
    return 0

def rename_folder(folderpath:str,as_prefix=True):
    """
    Find earliest/latest date in folder, generate new folder name
    todo: impelment recursive
    """
    epochs = []
    for ifile in os.listdir(folderpath):
        epochs.append(get_date_taken(os.path.join(folderpath,ifile)))
    d0=min(epochs)
    d1=max(epochs)
    mmdd0 = time.strftime("%m%d",time.localtime(d0))
    mmdd1 = time.strftime("%m%d",time.localtime(d1))
    newname = f"{mmdd0}-{mmdd1}"
    if(as_prefix):
        folderpath2 = f"/{newname} ".join(osp.split(folderpath))
    else:
        folderpath2 = osp.join(osp.split(folderpath)[0],newname)
    os.rename(folderpath,folderpath2)
    print(f"old folder: {folderpath}")
    print(f"new folder: {folderpath2}")
    return 0


class EasyExif:
    """ all-in-one place to process an exif file """
    def __init__(self,filepath:str):
        self.ex = pex.load(filepath)
        #self.keywords = # todo

    def datetimeoriginal(self,as_epoch=False,valstr:str=None,
                         valepoch:Union[float,int]=None) ->Union[None,str,float]:
        # user just wants to get value
        if(valstr is None and valepoch is None):
            try:
                val_str = self.ex['Exif'][pex.ExifIFD.DateTimeOriginal].decode()
                if(as_epoch):
                    return time.mktime(time.strptime(val_str,'%Y:%m:%d %H:%M:%S'))
                else:
                    return val_str
            except KeyError as e:
                print(f"EasyExif: {e}")
                return None
        elif(valstr is not None):
            # todo: check that string is compatible
            # _taken = time.mktime(time.strptime(exraw2, '%Y:%m:%d %H:%M:%S'))
            test = time.mktime(time.strptime(valstr,'%Y:%m:%d %H:%M:%S'))
            self.ex['Exif'][pex.ExifIFD.DateTimeOriginal] = valstr.encode()
        elif(valepoch is not None):
            res = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(valepoch))
            self.ex['Exif'][pex.ExifIFD.DateTimeOriginal] = res.encode()

    def dump(self) -> bytes:
        # todo: organize all keywords here
        return pex.dump(self.ex)



class GuiKImg:
    """ GUI interface for functions """
    @staticmethod
    def makeplace(elem,row,col):
        elem.grid(row=row,column=col) # need more later
        return elem

    def __init__(self):
        self.R = tk.Tk()
        self.R.title('KIMG GUI')
        self.R.resizable(False, False)
        mp = self.makeplace
        self.frm_main = mp(tk.Frame(self.R),0,0)
        self.btn_batch_rsz_rnm:tk.Button = mp(tk.Button(self.R,text='Batch Resize & Rename',width=30,command=self.cbBatchResizeRename),0,0)
        self.btn_fldrname:tk.Button = mp(tk.Button(self.R,text='Folder Rename',width=30,command=self.cbFolderRename),1,0)
        self.btn_findcopies:tk.Button = mp(tk.Button(self.R,text='Find Duplicate Images',width=30,command=self.cbFindDuplicateImages,state='disabled'),2,0)
        self.btn_moverszrnm:tk.Button = mp(tk.Button(self.R,text='Move All R/R Images',width=30,command=self.cbMoveAllResizedRenamedImages,state='disabled'),3,0)

        # non-GUI items
        self.types_allowed=['.jpg','.png','.jpeg']
        self._prevfldrrename=''
        print('GUI kimg ready')

    def cbBatchResizeRename(self):
        """
        rename & resize all images in a given folder
        General steps:
        1. select folder
        2. get list of files to modify (n files in folder. m will be modified. continue?)
            a. add file if maxdim > 2000
            b. add file if size>1MB
        3. for each relevant image, rename, resize and resave metadata
            a. rename file to yymmdd_HHMMSS format
            b. open file, load exif data
            c. resize, save img and exif data


        options:
        * disable overwrite?
        * create files in new folder?
        * recursive?

        # todo: call out every time an unknown extension is encountered
        # todo: keep relevant metadata the same
        """
        print('resize & rename') # todo

        path = fd.askdirectory(title="Select Folder",)
        if(path == ''): return
        print('path:',path)
        files = []
        for ifile in os.listdir(path):
            if(osp.splitext(ifile)[1].lower() in self.types_allowed):
                files.append(osp.join(path,ifile))
        print(f"{len(files)} applicable files found")
        _s = 's' if(len(files)>1) else ''
        ans = mb.askyesno("Rename & Resize",f"{len(files)} file{_s} found. Continue with rename & resize?")
        if(not ans): return

        nchanged=0
        for ifile in files:
            res = rename_resize(ifile)
            if(res==0): nchanged+=1

        print(f"{len(files)} files found. {nchanged} files changed")

    def cbFolderRename(self):
        """
        Get oldest and newest images in a folder, suggest rename to cover range as prefix
        expected format: MMD0-MMD1 OriginalFolderName

        """
        print('rename folder') # todo
        path = fd.askdirectory(title="Select Folder",initialdir=self._prevfldrrename)
        if(path == ''): return
        print('path:',path)
        files = []
        for ifile in os.listdir(path):
            if(osp.splitext(ifile)[1].lower() in self.types_allowed):
                files.append(osp.join(path,ifile))
        #print(f"{len(files)} applicable files found")
        _s = 's' if(len(files)>1) else ''
        ans = mb.askyesno("Folder Rename",f"{len(files)} file{_s} found. Continue with folder rename?")
        if(not ans): return
        self._prevfldrrename = osp.dirname(path)
        rename_folder(path)




    def cbFindDuplicateImages(self):
        ''' Find images that are the same or extremely similar '''
        print('find duplicate images') # todo

    def cbMoveAllResizedRenamedImages(self):
        '''
        Given a folder, move all images that are already correctly named & resized to "ready"
          folder
        '''
        print("move all resized & renamed images")


    def run(self):
        self.R.mainloop() # vital for each and every tkinter function


if(__name__=='__main__'):
    GuiKImg().run()

    # fpath = 'tests/data/tmp.png'
    # rename_resize(fpath)

    print('done')


    #
    # rename_folder("E:/photos/2017/HamburgSilvester/testing")

    # get_date_taken("E:/photos/2017/0315 Brunch With Laurel/170129_133648.JPG")
    # val = get_date_taken("E:/photos/2017/HamburgSilvester/testing/170711_183323.jpg",True)
    # res = rename_resize("E:/photos/2017/HamburgSilvester/testing/blah.jpg")
    # print(res)

    # res1 = get_date_taken("E:/photos/2017/0315 Brunch With Laurel/170129_133648.JPG")
    # res2 = get_date_taken("E:/photos/2017/0315 Brunch With Laurel/170129_133648.JPG",as_str=True)
    # print(res1)
    # print(res2)
    # print()
