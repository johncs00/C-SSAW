import csv
import cv2
import pytesseract as pt
import numpy as np
from io import StringIO

imageFile = 'stop.jpg'
img = cv2.imread(imageFile)
# img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshold = cv2.bitwise_not(cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5011, 1))
cv2.imshow('step1', threshold)
boxArr = pt.image_to_boxes(threshold, config='psm 1')
# print(boxArr)
# To read the coordinates
boxes = []
f = StringIO(boxArr)
reader = csv.reader(f, delimiter = ' ')
for row in reader:
    if(len(row)==6):
        boxes.append(row)

# print(boxes)
# # Draw the bounding box
img = threshold
# cv2.imshow('input',img)
h, w = img.shape
for b in boxes:
    cv2.rectangle(img,(int(b[1]),h-int(b[2])),(int(b[3]),h-int(b[4])),(100,np.random.randint(255),np.random.randint(255)),1)
cv2.imshow('output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Problem: The rectangles are too big or something.
