'''
objective: approximate a drawn circle's correctness

general steps:
1. load image
2. collect points of circle
3. get "average radius"
4. get error array, then average error
5. DONE


'''

# initializations
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pil
import PIL.ImageDraw as idr
pyt = np.linalg.norm # note: takes in a single vector
def err(estimate,trueval):
    return (estimate-trueval)/trueval
from sys import argv
imgname=argv[1]

# img=plt.imread(imgname)

img=pil.open(imgname).convert('L') # open as grayscale
img_np=np.array(img) # just a (H,W) img, one layer
pts=np.column_stack(np.where(img_np<0.5)) # returns [[rows],[cols]]
# print('No. points:',len(pts))

pcenter=np.mean(pts,0) # '0' means avg along row (1st dimension)

radii=np.array([pyt(pcenter-ip) for ip in pts]) # get radial distance of each point to pc
# print('radii:',type(radii),len(radii),'count')
r_avg=np.mean(radii)
# print('average:',r_avg)

errors=np.array([abs(err(ir,r_avg)) for ir in radii])
err_avg=np.mean(errors)
err_med=np.median(errors)
print("average error: {:.3f}".format(err_avg))
# visualize this with plotting a circle

# get point, flip values, convert to int, convert to tuple
p1=tuple(np.flip(pcenter-r_avg).astype('int'))
p2=tuple(np.flip(pcenter+r_avg).astype('int'))
bbox=list(p1)+list(p2)

# def custom ellipse fn to get a width
def ellipse2(imgdraw,bbox,outline=(255,255,255),fill=None,width=1):
    ''' custom ellipse function. see rectangle2 in pil_manip_notes.py'''
    x1=bbox[0]
    y1=bbox[1]
    x2=bbox[2]
    y2=bbox[3]
    for i in range(width):
        for j in range(width):
            imgdraw.ellipse(((x1+i,y1+j),(x2+i,y2+j)),outline=outline,fill=fill)

img2=img.convert('RGB')
img_draw=idr.Draw(img2)
ellipse2(img_draw,bbox,outline=(255,0,0),width=3)
plt.imshow(img2)
plt.title("Average Error: {:.4f}".format(err_avg))
plt.show()








# eof
