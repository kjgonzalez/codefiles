'''
given a pdf file of images, resize it to be a smaller filesize by reducing image resolution
'''

import os
import argparse
import time
from io import BytesIO
import tempfile
import fitz
from PIL import Image as pil


def get_pdf_bytes(filepath,dpi):
    imgpages = []
    doc = fitz.open(FILE)
    tmp = BytesIO()
    dirtmp = tempfile.TemporaryDirectory()
    for pgnum in range(len(doc)):
        page = doc[pgnum]
        pix = page.get_pixmap(dpi=dpi)
        ipath = os.path.join(dirtmp.name,f'pg{pgnum}.png')
        pix.save(ipath)
        img = pil.open(ipath).convert("RGB")

        imgpages.append(img)
    if(len(imgpages)>1):
        imgpages[0].save(tmp,save_all=True,append_images=imgpages[1:],format='pdf')
    else:
        imgpages[0].save(tmp, save_all=True,format='pdf')
    return tmp

def is_right_size(val:float,target:float):
    return target*0.9 < val < target

if(__name__ == '__main__'):
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('file',help='path to target pdf')
    p.add_argument('--mbmax',default=2.0,type=float,help='pdf MB size')
    p.add_argument('--dpi0',default=50,type=int,help='lower limit for bisection')
    p.add_argument('--dpi1',default=500,type=int,help='upper limit for bisection')
    args = p.parse_args()
    FILE = args.file
    FPATHOUT = os.path.splitext(FILE)[0]+'_out.pdf'
    MBMAX = args.mbmax
    t0=time.time()
    print(f'file: {FILE}')
    counter = 0

    # lower limit
    x0=args.dpi0
    b0 = get_pdf_bytes(FILE,x0)
    y0 = len(b0.getbuffer())/1024/1024
    counter+=1
    print(f'{counter} dpi={x0} MB={y0:0.4f}')
    if(is_right_size(y0,MBMAX)):
        open(FPATHOUT,'wb').write(b0.getbuffer())
        print(f'done in {time.time() - t0:0.3f} s')
        exit()

    # upper limit
    x1=args.dpi1
    b1 = get_pdf_bytes(FILE,x1)
    y1 = len(b1.getbuffer()) / 1024 / 1024
    counter+=1
    print(f'{counter} dpi={x1} MB={y1:0.4f}')
    if (is_right_size(y1, MBMAX)):
        open(FPATHOUT,'wb').write(b1.getbuffer())
        print(f'done in {time.time() - t0:0.3f} s')
        exit()

    yc=MBMAX*2
    while(not is_right_size(yc,MBMAX)):
        xc = int(round((x0 + x1) / 2, -1))
        bc = get_pdf_bytes(FILE,xc)
        yc = len(bc.getbuffer())/1024/1024
        if((yc-MBMAX)>0): x1=xc # too big
        else: x0 = xc
        counter+=1
        print(f'{counter} dpi={xc} MB={yc:0.4f}')
    print(f'done. {counter} attempts')

    open(FPATHOUT,'wb').write(bc.getbuffer())

    print(f'done in {time.time()-t0:0.3f} s')
