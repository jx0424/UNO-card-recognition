import cv2
import numpy as np

img_colour = cv2.imread(r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\b0.jpg')   # open the saved image in colour
img = cv2.cvtColor(img_colour, cv2.COLOR_BGR2GRAY)   # convert to B/W
img_sm = cv2.blur(img, (5, 5))         # smoothing
thr_value, img_th = cv2.threshold(img_sm, 0, 255, cv2.THRESH_OTSU)   # binarisation
kernel = np.ones((5, 5), np.uint8)
img_close = cv2.morphologyEx(img_th, cv2.MORPH_OPEN, kernel)      # morphology correction
img_canny = cv2.Canny(img_close, 50, 100)                          # edge detection
contours, hierarchy = cv2.findContours(img_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)   # extract contours on binarised image, not on canny
cv2.drawContours(img_colour, contours, -1, (0, 255, 0), 1)         # paint contours on top of original coloured mage
cv2.imshow('picture', img_colour)
cv2.imshow('edges', img_canny)

for i, c in enumerate(contours):         # loop through all the found contours
    print(i, ':', hierarchy[0, i])          # display contour hierarchy
    print('length: ', len(c))               # display numbr of points in contour c
    perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
    print('perimeter: ', perimeter)               
    epsilon = 0.02*perimeter    # parameter of polygon approximation: smaller values provide more vertices
    vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
    print('approx corners: ', vertex_approx, '\n')                    # number of vertices
    cv2.drawContours(img, [c], 0, (0, 255, 0), 3)   # paint contour c
    cv2.putText(img, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c
    [x,y,w,h] = cv2.boundingRect(c)
    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
    sample =[perimeter, vertex_approx]
cv2.namedWindow('picture', cv2.WINDOW_NORMAL)
cv2.imshow('picture',img)
key = cv2.waitKey(0)

cv2.destroyAllWindows()
print(len(contours))
