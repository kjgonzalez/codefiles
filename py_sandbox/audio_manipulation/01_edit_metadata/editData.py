'''
DateCreated: 190507
Objective: be able to look at & edit metadata of a given song. ideally, would be
    cross-platform, but windows-only is fine.

Things to accomplish:
1. load a song file (mp3)
2. print out the relevant metadata
3. modify each metadata field, and then save the file again

kjgnote: using module eyeD3 to do this. following examples from:
https://eyed3.readthedocs.io/en/latest/
'''

import os,sys
import eyed3
fbase = '../00_raw_data/'
fname = "Dua Lipa - Electricity ft. Diplo Mark Ronson.mp3"
fpath=os.path.join(fbase,fname)

assert os.path.exists(fpath),'invalid: '+fpath
