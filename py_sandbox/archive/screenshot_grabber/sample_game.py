'''
test out ocr on a game screenshot

'''

from PIL import Image as ima
from PIL import ImageGrab as igr
import matplotlib.pyplot as plt
import klib as klb
import pytesseract as ocr
import PIL.ImageOps as ops
import time
from sys import argv
# kjgnote: bbox arg is (x1,y1,x2,y2)

# screen = ima.open('game.png')
bb={}
bb['wood'] = (29, 5, 76,20)
bb['food'] = (109,5,153,20)
bb['gold'] = (199,5,230,20)
bb['stone']= (261,5,307,20)
bb['pop']  = (331,5,388,20)
bb['age']  = (959,9,1100,25)

# bb['time'] = (3,40,61,49)

screen = ima.open(argv[1]).convert()

j=1
Nrows = len(bb.keys())
for i in bb.keys():
    img=screen.crop(bb[i])
    img=img.convert('L') # no idea what happened ,but 'LA' and 'L' are different
    # print(type(img))
    img=ops.invert(img)
    print(i+':',ocr.image_to_string(img))
    plt.subplot(Nrows,1,j)
    plt.imshow(img)
    plt.ylabel(i)
    
    j+=1

plt.show()




