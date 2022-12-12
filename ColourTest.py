import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

img = cv2.imread(path)   # open the saved image in
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#---------------Blue----------------------------
blue_mask = cv2.inRange(img_hsv, min_blue, max_blue)
blue_card = np.sum(blue_mask)

#---------------Green---------------------------
green_mask = cv2.inRange(img_hsv, min_green, max_green)
green_card = np.sum(green_mask)

#---------------Red-----------------------------
red_mask = cv2.inRange(img_hsv, min_red, max_red)
red_card = np.sum(red_mask)

#--------------Yellow--------------------------
yellow_mask = cv2.inRange(img_hsv, min_yellow, max_yellow)
yellow_card = np.sum(yellow_mask)



if blue_card > 1000:
    cv2.putText(image, "Blue" + str(MLPrediction) , (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))
if green_card > 1000:
    cv2.putText(image, "Green" + str(MLPrediction) , (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0))
if red_card > 1000:
    cv2.putText(image, "Red" + str(MLPrediction) , (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))
if yellow_card > 1000:
    cv2.putText(image, "Yellow"  + str(MLPrediction) , (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))

