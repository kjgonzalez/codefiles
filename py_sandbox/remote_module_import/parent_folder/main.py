'''
Author: Kris Gonzalez
Objective: demonstrate how import modules from both subfolders and parent
    folders
KJG190429: assume using python3
'''

import sys,os

# to import from remote folder:
path_mod1=os.path.abspath('../')
sys.path.append(path_mod1)
import module1
print('module 1 pyt:',module1.pyt1(3,4))


# to import from subfolder:
import subfolder.module2 as module2
print('module 2 pyt:',module2.pyt2([3,4]))
