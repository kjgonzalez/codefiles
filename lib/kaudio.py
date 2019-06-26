'''
central location for audio manipulation library.

requires mutagen to be installed (see pypi mutagen)

kjg190622: check if LoadMetaData works with AAC or non mp3 files.
kjg190623: gonna need to make a custom library for m4a files, in order to
    convert without issue
'''
import os,sys
from shutil import copyfile

from mutagen.id3 import ID3,TIT2,TPE1,TRCK,TALB,TDRC,TCON,COMM # mp3 metadata
from mutagen.mp4 import MP4 # m4a and mp4 metadata
from pydub import AudioSegment # for file conversion


class MetaMP3(object):
    '''
    Simplify the process of reading and editing a song file's metadata. This
        class is essentially a wrapper for the mutagen.id3 module, and also
        limits the number of fields that are edited, specifically:
            title / artist / artist / album / track / genre / year / comment
    If a field is empty / missing, it is simply returned as ''
    Example:
        dat = LoadMetaData(filepath)
        dat.list()
        dat.get('title')
        dat.set('artist','Tenacious D')
        dat.set('comment','')
        dat.save()
    '''
    def __init__(self,filepath):
        assert os.path.exists(filepath),'Invalid:'+filepath
        assert ('.mp3' in filepath or '.MP3' in filepath),'Not an mp3 format'
        self.dat=ID3(filepath)
        # replacing complicated tags with intuitive names
        self.tags='title artist album track genre year comment'.split(' ')
        self._tags = 'TIT2 TPE1 TALB TRCK TCON TDRC COMM::eng'.split(' ')
        self._d=dict([self.tags[i],self._tags[i]] for i in range(len(self.tags)))

    def get(self,property):
        ''' Get value of given property. 1) check property is in tags 2) check
            that property exists in object 3) return value. see self.tags for
            valid properties.
        '''
        assert property in self.tags,'Invalid property "{}"'.format(property)
        try:
            return str(self.dat[self._d[property]].text[0]) # year doesn't come back as string
        except KeyError:
            return ''

    def set(self,property,value):
        ''' Set value of given property. 1) Make sure value is valid. 2) check
            that property is valid. 3) check that property exists. 4) either
            modify or remove property. See self.tags for valid properties.
        '''
        if(type(value)!=str):
            value = str(value)
            print("WARNING: value type of "+property+" has been corrected to 'str'")

        # ensure that property is valid
        assert property in self.tags,'Invalid property "{}"'.format(property)

        # check if property in object. if not, create it.
        if(self._d[property] not in self.dat.keys()):
            # property doesn't already exist in metadata
            if(property=='title'):self.dat.add(TIT2(encoding=3,text=value))
            elif(property=='artist'): self.dat.add(TPE1(encoding=3,text=value))
            elif(property=='album'): self.dat.add(TALB(encoding=3,text=value))
            elif(property=='track'): self.dat.add(TRCK(encoding=3,text=value))
            elif(property=='genre'): self.dat.add(TCON(encoding=3,text=value))
            elif(property=='year'): self.dat.add(TDRC(encoding=3,text=str(value)))
            elif(property=='comment'): self.dat.add(COMM(encoding=3,lang='eng',text=value))
            else: raise Exception('Invalid property to add')
        elif(value == ''):
            # user wants to clear the tag, so remove from object
            self.dat.pop(self._d[property])
        elif(property=='year'):
            # having issues with year value. will specifically use 'add'
            self.dat.add(TDRC(encoding=3,text=str(value)))
        else:
            # simply modify the property
            self.dat[self._d[property]].text[0] = value
        return True

    def getAllData(self):
        ''' debugging. quickly list out all values '''
        res = dict()
        for itag in self.tags:
            res[itag] = self.get(itag)
        return res

    def save(self):
        ''' Write current state to same file. CAUTION: there is no overwrite
            protection, so take care not to lose information.'''
        self.dat.save()
        return True

class MetaM4A(object):
    '''
    Simplify the process of reading and editing a song file's metadata. This
        class is essentially a wrapper for the mutagen.mp4 module, and also
        limits the number of fields that are edited, specifically:
            title / artist / artist / album / track / genre / year / comment
    If a field is empty / missing, it is simply returned as ''
    For the mp4 / m4a format, this class does NOT save or modify data, it only
        retrieves what is available from the original file. all non-mp3 files
        are to be converted when possible.
    KJG190623: there's a known issue that length / bitrate metadata seem to be
        removed when converting from m4a to mp3, but upon copying the file,
        properties are restored. This is still being debugged.

    Example:
        dat = MetaM4A(filepath)
        dat.get('title')
'''
    def __init__(self,filepath):
        # kjgnote: track number is returned as a tuple
        # kjgnote: year comes out as a whole datestring
        # need to be able to handle not having a field if it's not available
        assert os.path.exists(filepath),'Invalid:'+filepath
        assert ('.m4a' in filepath or '.M4A' in filepath),'Not an m4a format'
        self.dat=MP4(filepath)
        self.tags= 'title artist album track genre year comment'.split(' ')
        self._tags= '\xa9nam \xa9ART \xa9alb trkn \xa9gen \xa9day \xa9cmt'.split(' ')
        self._d=dict([self.tags[i],self._tags[i]] for i in range(len(self.tags)))
    def get(self,property):
        ''' Get value of given property. 1) check property is in tags 2) check
            that property exists in object 3) return value. see self.tags for
            valid properties. NOTE: each m4a property comes back as a list, and
            may even have unique formatting. will handle.
        '''
        assert property in self.tags,'Invalid property "{}"'.format(property)
        try:
            raw=self.dat[self._d[property]][0]
        except KeyError:
            return ''
        # if property exists, get correct formatting
        if(property=='track'):
            return str(raw[0])
        elif(property=='year'):
            return raw[:4]
        else:
            return raw

class Converter(object):
    '''
    Object to convert a given set of files, one at a time. Created as an object
        instead of as a function to save on loading / unloading of memory. By
        default, will try to save metadata.

    General steps:
    1. load meta data, save somewhere
    2. convert file
    3. add in old metadata
    Example:
        CONV = Converter()
        CONV.to_mp3(filepath) # conversion is saved to same location, with metadata
    '''
    def __init__(self):
        print('converter loaded')

    def getmeta(self,filename):
        ''' Return a dictionary of all relevant properties. For the moment, will
            assume that converting from m4a to mp3
        '''
        metadata = {}
        dat = MetaM4A(filename)
        for itag in dat.tags:
            metadata[itag] = dat.get(itag)
        return metadata

    def convert(self,filename):
        assert 'm4a' in filename,'Not m4a file, please retry.'
        metadata = self.getmeta(filename)
        orig = AudioSegment.from_file(filename,format='m4a')
        newname = filename[:-3]+'mp3'
        orig.export(newname,format='mp3')
        dat=MetaMP3(newname)
        for iprop in metadata.keys():
            dat.set(iprop,metadata[iprop])
        dat.save()
        print('converted:',filename)
