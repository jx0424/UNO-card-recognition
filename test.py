import cv2
import numpy as np
import os
from os import listdir

# img_colour = cv2.imread(r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\b1.jpg')   # open the saved image in colour
# img = cv2.cvtColor(img_colour, cv2.COLOR_BGR2GRAY)   # convert to B/W
# img_sm = cv2.blur(img, (9,9))         # smoothing
# thr_value, img_th = cv2.threshold(img_sm, 150, 255, cv2.THRESH_BINARY)   # binarisation
# kernel = np.ones((3,3), np.uint8)
# img_close = cv2.morphologyEx(img_th, cv2.MORPH_OPEN, kernel)      # morphology correction
# img_canny = cv2.Canny(img_close, 100, 200)                          # edge detection
# contours, hierarchy = cv2.findContours(img_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   # extract contours on binarised image, not on canny
# #cv2.drawContours(img_colour, contours, -1, (0, 255, 0), 1)         # paint contours on top of original coloured mage
# #cv2.imshow('picture', img_colour)
# #cv2.imshow('edges', img_canny)
# # cv2.imshow('colour' ,img_colour)
# for i, c in enumerate(contours):         # loop through all the found contours
#     print(i, ':', hierarchy[0, i])          # display contour hierarchy
#     #print('length: ', len(c))               # display numbr of points in contour c
#     perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
#     print('perimeter: ', perimeter)               
#     epsilon = 0.02*perimeter    # parameter of polygon approximation: smaller values provide more vertices
#     vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
#     print('approx corners: ', vertex_approx, '\n')                    # number of vertices
#     ellipse = cv2.fitEllipse(c)
#     (xc,yc),(d1,d2), angle = ellipse
#     axes_ratio = round (d1/d2,  3)
#     print('axes ratio', axes_ratio, '\n')
#     cv2.drawContours(img_colour, [c], 0, (0, 255, 0), 3)   # paint contour c
#     cv2.putText(img_colour, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c
#     [x,y,w,h] = cv2.boundingRect(c)
#     #cv2.rectangle(img_colour, (x,y), (x+w,y+h), (255, 0, 0), 2)
#     cv2.ellipse(img_colour, ellipse, (0, 0, 255), 1)
#     sample =[perimeter, vertex_approx, axes_ratio]
# cv2.namedWindow('picture', cv2.WINDOW_NORMAL)
# cv2.imshow('picture',img_colour)

# key = cv2.waitKey(0)
# cv2.destroyAllWindows()

folder_dir = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images'
for images in os.listdir(folder_dir):
# check if the image ends with png
    if (images.endswith(".jpg")):
        print(images)

# directory_in_str = 'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images'
# directory = os.fsencode(directory_in_str)
    
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     if filename.endswith('.png'):
#         print(filename)