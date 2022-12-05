import cv2
import numpy as np
import os
from os import listdir

##-----------------------------Contour for wild card--------------------------------------------
# folder_dir = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images'
# for images in os.listdr(folder_dir):
#     if images.
path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\kW.jpg'
image = cv2.imread(path)
#bilateral_image = cv2.bilateralFilter(image, 11 , 70,70)
#cv2.imshow('Bilateral image', bilateral_image)
BW_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.blur(BW_image ,(7,7))
cv2.imshow('blur',blur_image)
cv2.imshow('Black and White', BW_image)
th, threshed_image = cv2.threshold(blur_image, 165, 255,cv2.THRESH_BINARY)
cv2.imshow('threshed image' ,threshed_image)
kernel = np.ones((3,3), np.uint8)
image_close = cv2.morphologyEx(threshed_image, cv2.MORPH_OPEN, kernel)      # morphology correction
    #image_open = cv2.morphologyEx(image_close, cv2.MORPH_CLOSE, kernel)
    #img_canny = cv2.Canny(image_close, 50, 100) 

    # canny_image = cv2.Canny (threshed_image, 100, 100)
    #cv2.imshow('canny', img_canny)
contours, hierarchy = cv2.findContours(image_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv2.drawContours(image, contours, -1 , (0,255,0), 2)
cv2.imshow('contour image', image)

for i, c in enumerate(contours):         # loop through all the found contours
    print(i, ':', hierarchy[0, i])          # display contour hierarchy
    #print('length: ', len(c))               # display numbr of points in contour c
    perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
    print('perimeter: ', perimeter)               
    epsilon = 0.006*perimeter    # parameter of polygon approximation: smaller values provide more vertices
    vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
    print('approx corners: ', vertex_approx, '\n')                    # number of vertices
    ellipse = cv2.fitEllipse(c)
    (xc,yc),(d1,d2), angle = ellipse
    axes_ratio = round (d1/d2,  3)
    print('axes ratio', axes_ratio, '\n')
    cv2.drawContours(image, [c], 0, (0, 255, 0), 3)   # paint contour c
    cv2.putText(image, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c     
    [x,y,w,h] = cv2.boundingRect(c)
    cv2.rectangle(image, (x,y), (x+w,y+h), (255, 0, 0), 2)
    #cv2.ellipse(img_colour, ellipse, (0, 0, 255), 1)
    cv2.imshow('contours',image)
    sample =[perimeter, vertex_approx, axes_ratio]
print(len(contours))

# #green cards contour
# path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\gR.jpg'
# img_colour = cv2.imread(path)   # open the saved image in colour
# img = cv2.cvtColor(img_colour, cv2.COLOR_BGR2GRAY)   # convert to B/W
# img_sm = cv2.blur(img, (9,9))         # smoothing
# thr_value, img_th = cv2.threshold(img_sm, 160, 255, cv2.THRESH_BINARY)   # binarisation
# kernel = np.ones((3,3), np.uint8)
# img_close = cv2.morphologyEx(img_th, cv2.MORPH_OPEN, kernel)      # morphology correction
# img_canny = cv2.Canny(img_close, 100, 200)  
# cv2.imshow('colour',img_colour)
# cv2.imshow('canny', img_canny)
# cv2.imshow('sm', img_sm)
# cv2.imshow('close', img_close)                        # edge detection
# contours, hierarchy = cv2.findContours(img_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)   # extract contours on binarised image, not on canny
# print(len(contours))

# #yellow cards contour
# path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\yR.jpg'
# img_colour = cv2.imread(path)   # open the saved image in colour
# img = cv2.cvtColor(img_colour, cv2.COLOR_BGR2GRAY)   # convert to B/W
# img_sm = cv2.blur(img, (9,9))         # smoothing
# thr_value, img_th = cv2.threshold(img_sm, 160, 255, cv2.THRESH_BINARY)   # binarisation
# kernel = np.ones((3,3), np.uint8)
# img_close = cv2.morphologyEx(img_th, cv2.MORPH_OPEN, kernel)      # morphology correction
# img_canny = cv2.Canny(img_close, 100, 200)  
# cv2.imshow('colour',img_colour)
# cv2.imshow('canny', img_canny)
# cv2.imshow('sm', img_sm)
# cv2.imshow('close', img_close)                        # edge detection
# contours, hierarchy = cv2.findContours(img_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)   # extract contours on binarised image, not on canny
# print(len(contours))

# #red cards contour
# path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\rR.jpg'
# img_colour = cv2.imread(path)   # open the saved image in colour
# img = cv2.cvtColor(img_colour, cv2.COLOR_BGR2GRAY)   # convert to B/W
# img_sm = cv2.blur(img, (9,9))         # smoothing
# thr_value, img_th = cv2.threshold(img_sm, 160, 255, cv2.THRESH_BINARY)   # binarisation
# kernel = np.ones((3,3), np.uint8)
# img_close = cv2.morphologyEx(img_th, cv2.MORPH_OPEN, kernel)      # morphology correction
# img_canny = cv2.Canny(img_close, 100, 200)  
# cv2.imshow('colour',img_colour)
# cv2.imshow('canny', img_canny)
# cv2.imshow('sm', img_sm)
# cv2.imshow('close', img_close)                        # edge detection
# contours, hierarchy = cv2.findContours(img_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)   # extract contours on binarised image, not on canny
# for i, c in enumerate(contours):         # loop through all the found contours
#             print(i, ':', hierarchy[0, i])          # display contour hierarchy
#             #print('length: ', len(c))               # display numbr of points in contour c
#             perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
#             print('perimeter: ', perimeter)               
#             epsilon = 0.006*perimeter    # parameter of polygon approximation: smaller values provide more vertices
#             vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
#             print('approx corners: ', vertex_approx, '\n')                    # number of vertices
#             ellipse = cv2.fitEllipse(c)
#             (xc,yc),(d1,d2), angle = ellipse
#             axes_ratio = round (d1/d2,  3)
#             print('axes ratio', axes_ratio, '\n')
#             cv2.drawContours(img_colour, [c], 0, (0, 255, 0), 3)   # paint contour c
#             cv2.putText(img_colour, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c     
#             #[x,y,w,h] = cv2.boundingRect(c)
#             #cv2.rectangle(img_colour, (x,y), (x+w,y+h), (255, 0, 0), 2)
#             cv2.ellipse(img_colour, ellipse, (0, 0, 255), 1)

# print(len(contours))

# #wild cards contour
# path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\kE.jpg'
# img_colour = cv2.imread(path)   # open the saved image in colour
# img = cv2.cvtColor(img_colour, cv2.COLOR_BGR2GRAY)   # convert to B/W
# img_sm = cv2.blur(img, (3,3))         # smoothing
# #img_th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,35,9)
# #img_sm = cv2.GaussianBlur(img,(9,9), cv2.BORDER_CONSTANT)
# #ret3,img_th = cv2.threshold(img_sm,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# #thr_value, img_th = cv2.threshold(img_sm, 180, 255, )   # binarisation
# kernel = np.ones((3,3), np.uint8)
# img_close = cv2.morphologyEx(img_sm , cv2.MORPH_OPEN, kernel)      # morphology correction
# img_canny = cv2.Canny(img_close, 100, 200)  
# cv2.imshow('colour',img_colour)
# cv2.imshow('canny', img_canny)
# #cv2.imshow('sm', img_sm)
# cv2.imshow('close', img_close)                        # edge detection
# contours, hierarchy = cv2.findContours(img_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)   # extract contours on binarised image, not on canny

# for i, c in enumerate(contours):         # loop through all the found contours
#             print(i, ':', hierarchy[0, i])          # display contour hierarchy
#             #print('length: ', len(c))               # display numbr of points in contour c
#             perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
#             print('perimeter: ', perimeter)               
#             epsilon = 0.006*perimeter    # parameter of polygon approximation: smaller values provide more vertices
#             vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
#             print('approx corners: ', vertex_approx, '\n')                    # number of vertices
#             ellipse = cv2.fitEllipse(c)
#             (xc,yc),(d1,d2), angle = ellipse
#             axes_ratio = round (d1/d2,  3)
#             print('axes ratio', axes_ratio, '\n')
#             cv2.drawContours(img_colour, [c], 0, (0, 255, 0), 3)   # paint contour c
#             cv2.putText(img_colour, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c     
#             #[x,y,w,h] = cv2.boundingRect(c)
#             #cv2.rectangle(img_colour, (x,y), (x+w,y+h), (255, 0, 0), 2)
#             cv2.ellipse(img_colour, ellipse, (0, 0, 255), 1)

# print(len(contours))








# #cv2.drawContours(img_colour, contours, -1, (0, 255, 0), 1)         # paint contours on top of original coloured mage
# #cv2.imshow('picture', img_colour)
# #cv2.imshow('edges', img_canny)
# # cv2.imshow('colour' ,img_colour)
        
# for i, c in enumerate(contours):         # loop through all the found contours
#     print(i, ':', hierarchy[0, i])          # display contour hierarchy
#             #print('length: ', len(c))               # display numbr of points in contour c
#     perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
#     print('perimeter: ', perimeter)               
#     epsilon = 0.1*perimeter    # parameter of polygon approximation: smaller values provide more vertices
#     vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
#     print('approx corners: ', vertex_approx, '\n')                    # number of vertices
#     ellipse = cv2.fitEllipse(c)
#     (xc,yc),(d1,d2), angle = ellipse
#     axes_ratio = round (d1/d2,  3)
#     print('axes ratio', axes_ratio, '\n')
#     cv2.drawContours(img_colour, [c], 0, (0, 255, 0), 3)   # paint contour c
#     cv2.putText(img_colour, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c     
#             #[x,y,w,h] = cv2.boundingRect(c)
#             #cv2.rectangle(img_colour, (x,y), (x+w,y+h), (255, 0, 0), 2)
#     cv2.ellipse(img_colour, ellipse, (0, 0, 255), 1)
#     cv2.imshow('image',img_colour)

#     sample =[perimeter, vertex_approx, axes_ratio]    
cv2.waitKey(0)