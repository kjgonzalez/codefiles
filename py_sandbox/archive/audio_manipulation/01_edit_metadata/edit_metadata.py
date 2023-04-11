'''
DateCreated: 190507
Objective: be able to look at & edit metadata of a given song. ideally, would be
    cross-platform, but windows-only is fine.

Things to accomplish:
1. load a song file (mp3)
2. print out the relevant metadata
3. modify each metadata field, and then save the file again

kjg0507: tried eyeD3, didn't work. now moving to mutagen
https://stackoverflow.com/questions/8948/accessing-mp3-meta-data-with-python

update: ok, do we need to make a damn wrapper class that helps manage all this stuff?

update2: ok, made the damn class. this should be used as part of some sort of
    "kaudio" library.

update3: seems to get an error if a field is empty

update4: alright, things seem to be stable... going to bed now BYEEEE

kjg190622: copied to kaudio module.
'''

import os,sys
from shutil import copyfile
from kaudio import LoadMetaData
# from mutagen.id3 import ID3,TIT2,TPE1,TRCK,TALB,TDRC,TCON,COMM
#
# class LoadMetaData(object):
#     '''
#     Simplify  the process of reading and editing a song file's metadata. This
#         class is essentially a wrapper for the mutagen.id3 module, and also
#         limits the number of fields that are edited, specifically:
#             title / artist / artist / album / track / genre / year / comment
#     If a field is empty / missing, it is simply returned as ''
#     Example:
#         dat = LoadMetaData(filepath)
#         dat.list()
#         dat.get('title')
#         dat.set('artist','Tenacious D')
#         dat.set('comment','')
#         dat.save()
#     '''
#     def __init__(self,filepath):
#         assert os.path.exists(filepath),'Invalid:'+filepath
#         self.dat=ID3(filepath)
#         # replacing complicated tags with intuitive names
#         self.tags='title artist album track genre year comment'.split(' ')
#         self._tags = 'TIT2 TPE1 TALB TRCK TCON TDRC COMM::eng'.split(' ')
#         self._d=dict([self.tags[i],self._tags[i]] for i in range(len(self.tags)))
#
#     def get(self,property):
#         ''' Get value of given property. 1) check property is in tags 2) check
#             that property exists in object 3) return value. see self.tags for
#             valid properties.
#         '''
#         assert property in self.tags,'Invalid property "{}"'.format(property)
#         try:
#             return self.dat[self._d[property]].text[0]
#         except KeyError:
#             return ''
#
#     def set(self,property,value):
#         ''' Set value of given property. 1) Make sure value is valid. 2) check
#             that property is valid. 3) check that property exists. 4) either
#             modify or remove property. See self.tags for valid properties.
#         '''
#         if(type(value)!=str):
#             value = str(value)
#             print("WARNING: value type has been corrected to 'str'")
#
#         # ensure that property is valid
#         assert property in self.tags,'Invalid property "{}"'.format(property)
#
#         # check if property in object. if not, create it.
#         if(self._d[property] not in self.dat.keys()):
#             if(property=='title'):self.dat.add(TIT2(encoding=3,text=value))
#             elif(property=='artist'): self.dat.add(TPE1(encoding=3,text=value))
#             elif(property=='album'): self.dat.add(TALB(encoding=3,text=value))
#             elif(property=='track'): self.dat.add(TRCK(encoding=3,text=value))
#             elif(property=='genre'): self.dat.add(TCON(encoding=3,text=value))
#             elif(property=='year'): self.dat.add(TDRC(encoding=3,text=value))
#             elif(property=='comment'): self.dat.add(COMM(encoding=3,lang='eng',text=value))
#             else: raise Exception('Invalid property to add')
#         elif(value == ''):
#             # user wants to clear the tag, so remove from object
#             self.dat.pop(self._d[property])
#         else:
#             # simply modify the property
#             self.dat[self._d[property]].text[0] = value
#         return True
#
#     def list(self):
#         ''' debugging. quickly list out all values '''
#         for i in self.tags:
#             print(i,':',self.get(i))
#
#     def save(self):
#         ''' Write current state to same file. CAUTION: there is no overwrite
#             protection, so take care not to lose information.'''
#         self.dat.save()
#         return True

if(__name__ == '__main__'):
    # load up filepath
    fbase = '../00_raw_data/'
    fname = "Khalid - Better.mp3"
    fpath_orig=os.path.join(fbase,fname)
    assert os.path.exists(fpath_orig),'invalid: '+fpath_orig

    # first, create a copy to work on and edit
    fname2='COPY_'+fname.replace(' ','_')
    fpath=os.path.join(fbase,fname2)
    if(not os.path.exists(fpath)):
        copyfile(fpath_orig,fpath)

    # display metadata
    print('filepath:',fpath)
    dat = LoadMetaData(fpath)
    dat.list()
    # import ipdb; ipdb.set_trace()
    dat.save()
