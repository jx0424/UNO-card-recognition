import cv2
import numpy as np

path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\B\b1.jpg'
img_colour = cv2.imread(path)   # open the saved image in colour
cv2.imshow('image', img_colour)

cropped = img_colour[260:400,260:395]
cv2.imshow('cropped', cropped)

cv2.waitKey(0)