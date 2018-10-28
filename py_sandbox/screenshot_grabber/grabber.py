'''
objective: test out ImageGrab sub-module from PIL library. may only be windows/mac based as of 181027, but will investigate later.

general steps: grab a screenshot, crop to desired area, try to run OCR on it
'''

from PIL import Image as ima
from PIL import ImageGrab as igr
import matplotlib.pyplot as plt
import klib as klb
import pytesseract as ocr
import PIL.ImageOps as ops
import time

# # go from img in memory to ocr:
# img=ima.fromarray(arr)
# ocrstr=pytesseract.image_to_string(img)

if(False):
    temp=igr.grab()
    plt.imshow(temp)
    plt.show()
    exit()


# first, grab screenshot
# kjgnote: bbox arg is (x1,y1,x2,y2)
bdim=(472,245,578,275) # "module"
bdim=(528,326,623,388) # trying to cap ss only
bdim=(426,327,620,389) # trying to cap mm:ss
bdim=(544,425,617,463) # cap "clear"
bdim=( 16, 68,144, 91) # "this is a test"


while(True):
    t0=time.time()
    img=igr.grab(bbox=bdim)
    # img=img.convert('LA')
    print(ocr.image_to_string(img),time.time()-t0)
