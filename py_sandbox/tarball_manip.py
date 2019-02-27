'''
Author: Kris Gonzalez
Objective: demonstrate how to read a single image from a tarball without
    creating an extracted copy. additionally, show how to generate a hash file
    that can be used as a checksum when downloading from a server
'''

import tarfile
import hashlib
import numpy as np
import PIL.Image as pil
import matplotlib.pyplot as plt
from klib import data as dat
import os


# create a tarball
tarname='tarball.tar.gz'
tar_out=tarfile.open(tarname,'w:gz')
tar_out.add(dat.jpgpath,os.path.basename(dat.jpgpath))
tar_out.add(dat.pngpath,os.path.basename(dat.pngpath))
# adding remote file as a same-folder file, don't always need 2nd arg
tar_out.close()


# manipulate a single object in a tar file
tar=tarfile.open('tarball.tar.gz')  # create tar object
allFiles=tar.getnames()             # get list of available files
print('files in tarball:',allFiles)
ifile=tar.extractfile(allFiles[0])  # choose desired file and "extractfile"
ipic=np.array(pil.open(ifile))      # can also use plt.imread
plt.imshow(ipic),plt.show()

# generate a hash file that can be used as a checksum
hash=hashlib.md5(open(tarname,'rb').read()).hexdigest()
print('hash / checksum:',hash)

# once complete, delete tarball (save on having so many binaries)
os.remove(tarname)
