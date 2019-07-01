'''
objective: collect metadata for each song in music folder (recursively)
'''

import os, argparse
import klib as k
from kaudio import MetaMP3 as M

p=argparse.ArgumentParser()
p.add_argument('--musicDir',type=str,default='.',help='location to analyze')
p.add_argument('--saveDir',type=str,default='.',help='where to save results')
p.add_argument('--logName',type=str,default='data.csv',help='name of results file')
args=p.parse_args()
# music_path = 'D:/Music2/'




allFiles=k.dir(args.musicDir,rec=True,ext='mp3')
print('number of files:',len(allFiles))
# print('example:',allFiles[0])
# print('data:')

filename = os.path.join(args.saveDir,args.logName)
f = open(filename,'w')

tags = M(allFiles[0]).tags

tags2 = ['fname']+tags
# print(';'.join(tags2))
f.write(';'.join(tags2)+'\n')

for ifile in allFiles:
    info2=[M(ifile).getAllData()[itag] for itag in tags]
    info3=';'.join([ifile]+info2)
    print('file:',ifile)
    f.write(info3+'\n')
print('done')
