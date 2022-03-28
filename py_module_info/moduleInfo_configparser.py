'''
date: 200429
objective: check out configparser module, which allows one to read from an ini file
src1: https://docs.python.org/3/library/configparser.html
src2: https://docs.python.org/3/library/configparser.html#mapping-protocol-access

KJG200430: ini files aren't really that appealing to use. in fact, it might be best to use other
    filetypes to store your data
'''

import configparser
from pprint import pprint
dat = configparser.ConfigParser()
dat.read('../data/simpsons.ini')
pprint(dat)

# print out structure & information listed
for isec in dat:
    print('SEC:',isec)
    for ival in dat[isec]:
        print('  {}: {}'.format( ival,dat[isec][ival] ))

# can get values in a specific type
x = dat[isec]
y = x[ival]
y2 = x.getfloat(ival)

print('{}: {}'.format( y,type(y) ))
print('{}: {}'.format( y2, type(y2) ))