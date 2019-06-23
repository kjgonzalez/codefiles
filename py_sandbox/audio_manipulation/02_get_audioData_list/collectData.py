'''
objective: collect metadata for each song in music folder (recursively)
'''

import os
import klib as k
from kaudio import LoadMetaData as LMD

music_path = 'D:/Music2/'

allFiles=k.dir(music_path,rec=True)
print('number of files:',len(allFiles))
print('example:',allFiles[0])
print('data:')
LMD(allFiles[0]).list()
import ipdb; ipdb.set_trace()
