import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage.restoration import inpaint
from skimage import color
import time

'''

KJGNOTE: from documentation:
mask : (M[, N[, …, P]]) ndarray

Array of pixels to be inpainted. Have to be the same shape as one of the 
    ‘image’ channels. Unknown pixels have to be represented with 1, known 
    pixels - with 0.

'''




image_orig = data.astronaut()[0:200, 0:200]

# Create mask with three defect regions: left, middle, right respectively
mask = np.zeros(image_orig.shape[:-1])
mask[20:60, 0:20] = 1
mask[160:180, 70:155] = 1
mask[30:60, 170:195] = 1

# Defect image over the same region in each color channel
image_defect = image_orig.copy()
for layer in range(image_defect.shape[-1]):
    image_defect[np.where(mask)] = 0

# at this moment, want to convert image to grayscale for inpaint testing
img_defect_gray=color.rgb2gray(image_defect)

t0=time.time()
image_result = inpaint.inpaint_biharmonic(image_defect, mask, multichannel=True)
tf=time.time()-t0

t0=time.time()
img_res_2 = inpaint.inpaint_biharmonic(img_defect_gray, mask, multichannel=False) 
tf2=time.time()-t0
#exit()

print('elapsed time, color: ',tf)
print('elapsed time, gray : ',tf2)
fig, axes = plt.subplots(ncols=2, nrows=2)
ax = axes.ravel()
# returns numpy vector of subplot objects, going left-to-right, top-to-bottom

ax[0].set_title('Original image')
ax[0].imshow(image_orig)

ax[1].set_title('Defected image')
ax[1].imshow(image_defect)

ax[2].set_title('Inpainted image')
ax[2].imshow(image_result)

ax[3].set_title('Inpainted grayscale')
ax[3].imshow(img_res_2,cmap='gray')

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()
