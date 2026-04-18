'''
when slicer exports gcode, it embeds the byte data of the image. want to be able to parse this and display.
'''

import argparse
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import PIL.Image as pil

def getPngDataFromGcode(filepath:str) -> bytes:
    ''' return byte data from Prusa-Slicer-generated gcode '''
    fin = open(filepath,'r')
    _raw = ''
    done=False
    linecount=0
    in_png=False
    shape = []
    while(not done):
        iline = fin.readline()
        linecount += 1
        if(iline==''):
            done=True
            linecount-=1
        elif('thumbnail begin' in iline):
            in_png = True  # in thumbnail region, but 0th line is simply shape info
            continue
        elif('thumbnail end' in iline):
            in_png = False
            done=True
        if(not in_png): continue
        # in png, collect data
        _raw +=iline[2:-1]
    parsed = base64.b64decode(_raw)
    return parsed


if(__name__ == '__main__'):
    ap=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument('path',help='target file')
    ap.add_argument('--mpl',default=False,action='store_true',help='use matplotlib instead of pure Pillow')
    args=ap.parse_args()
    rawdata:bytes = getPngDataFromGcode(args.path)
    print('loaded:',args.path)
    if(args.mpl):
        p:plt.Axes
        f,p=plt.subplots()
        p.imshow(pil.open(BytesIO(rawdata)))
        p.set_axis_off()
        f.tight_layout()
        plt.show()
    else:
        pil.open(BytesIO(rawdata)).show()
# eof
