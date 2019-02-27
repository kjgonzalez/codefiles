'''
objective: want to practice PIL library a bit and get familiar with some of what's possible. the main goals for this are to:

* load an image
* flip / rotate an image
* convert image to grayscale
* resize an image
* crop an image
* draw on image (text and rectangle)
* take a screenshot # NOT POSSIBLE WITH PIL IN UBUNTU
* display an image
'''

import klib
if(klib.PYVERSION!=3):
    raise Exception('must use python3. exiting.')

import os
import time
import matplotlib.pyplot as plt
import PIL.ImageDraw as idr
from PIL import ImageFont
import PIL.Image as pil
import numpy as np



# load an image
img=pil.open(klib.data.jpgpath)
print('path:',klib.data.jpgpath)
print('w,h:',img.size) # returns shape as a tuple in (width,height) format

import ipdb; ipdb.set_trace()
# flip / rotate / transpose an image
img2=img.transpose(pil.FLIP_LEFT_RIGHT)
plt.imshow(img2)
#plt.show(block=False);time.sleep(0.5);plt.close()

img2=img.transpose(pil.ROTATE_90)
plt.imshow(img2)
#plt.show(block=False);time.sleep(0.5);plt.close()


# convert to grayscale
img3=img.convert('L') # KJGNOTE: L means "luma" (greyscale), A means alpha (transparency?)
plt.imshow(img3)
#plt.show(block=False);time.sleep(0.5);plt.close()

## save an image
#img3.save('out.png')

# resize an image
img2=img.resize((int(img.size[0]/2),int(img.size[1]/2)))
plt.imshow(img2)
#plt.show(block=False);time.sleep(1);plt.close()

# crop an image
img2=img.crop((70,30,200,200)) #pixx format, (x1,y1,x2,y2)
plt.imshow(img2)
#plt.show(block=False);time.sleep(1);plt.close()

# convert betwene pil and numpy
img_arr=np.array(img2)
img_pil=pil.fromarray(img_arr) # ensure that data is 0-255 uint8!

# draw stuff on image
def rectangle2(imgdraw,bbox,outline=(255,255,255),fill=None,width=1):
    ''' KJG custom modification to PIL ImageDraw method.
    * bbox: tuple of pixx values, (x1,y1,x2,y2)
    * outline: tuple of RGB integers, (R,G,B) [default=(255,255,255)
    * fill: tuple of RGB integers, (R,G,b) [default=None]
    * width: integer scalar, w [default=1]
    '''
    x1=bbox[0]
    y1=bbox[1]
    x2=bbox[2]
    y2=bbox[3]
    for i in range(width):
        for j in range(width):
            imgdraw.rectangle(((x1+i,y1+j),(x2+i,y2+j)),outline=outline,fill=fill)
        #imgdraw.rectangle(((30,30),(200,200)))
    return imgdraw



img2=img.convert('RGB')
img2d=idr.Draw(img2) # note: create dual image pair, with one being 'canvas' and other being 'composite'
#img2d.rectangle(((30, 30),(200,200)))

if(klib.OSVERSION==0):
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 20)
elif(klib.OSVERSION==1):
    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\arial.ttf', 20)

img2d.text((10,10),'hello world',font=fnt,fill=(255,0,0))
rectangle2(img2d,(70,30,200,200),outline="red",width=5)
plt.title("Close with 'q' or X out of window")
plt.imshow(img2)
plt.show()



#eof
