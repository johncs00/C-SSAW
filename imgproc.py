#Image processing module for river gauges
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import pytesseract as pyt

def nothing(x):
    pass

def auto_canny(image, sigma=0.25): #taken from pyimagesearch
	# compute the median of the single channel pixel intensities
	v = np.median(image)

	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv.Canny(image, lower, upper)

	# return the edged image
	return edged

img = cv.imread('sample/Staff-gage-2.jpg', 0)
edges = cv.Canny(img,175,250)
autoedges = auto_canny(img)
print(pyt.image_to_string(img))
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0,255,0), 3)


plt.subplot(131),plt.imshow(img,cmap = 'BrBG_r')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(autoedges,cmap = 'gray')
plt.title('Auto Image'), plt.xticks([]), plt.yticks([])
plt.show()


#TODO Load as picture into the processing system

#TODO Find features of the image (gauge ticks, where the water is, etc.)

#TODO Use features to get a distance from the water to the first numbered tick

#TODO Invert the measurement to find the actual river height (from the bottom)
