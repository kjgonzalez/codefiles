import cv2
import numpy as np

# image is expected be in RGB color space
def select_rgb_blue(image): 
    lower = np.uint8([128, 32,   2])    # Lower threshold (BLUE, GREEN, RED)
    upper = np.uint8([210, 81, 9])      # Upper threshold (BLUE, GREEN, RED)
    masked = cv2.inRange(image, lower, upper)    # Threashold the image, all in the threshold is white, all other black
    return masked
    
# image is expected be in RGB color space
def select_rgb_yellow(image): 
    lower = np.uint8([1, 161,   208])    # Lower threshold (BLUE, GREEN, RED)
    upper = np.uint8([59, 227, 244])     # Upper threshold (BLUE, GREEN, RED)
    masked = cv2.inRange(image, lower, upper)    # Threashold the image, all in the threshold is white, all other black
    return masked

def combine_images(blue_img, yellow_img):   # Combine the two images into one image
	# combine the mask
	masked = cv2.bitwise_or(blue_img, yellow_img)
	return masked

img = cv2.imread('cones.png',-1)    # Read the image into img as a color image (-1)

res_blue = select_rgb_blue(img)
cv2.imshow('Image Blue',res_blue)   # Show the image
cv2.waitKey(0)                      # Wait for user input

res_yellow = select_rgb_yellow(img)
cv2.imshow('Image Yellow',res_yellow)   # Show the image
cv2.waitKey(0)                          # Wait for user input

res = combine_images(res_blue, res_yellow)  
cv2.imshow('Image Resulting',res)           # Show the image
cv2.waitKey(0)                              # Wait for user input
cv2.destroyAllWindows()                     # Destroy all generated windows