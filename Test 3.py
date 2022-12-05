import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\b0.jpg'
img = cv2.imread(path)   # open the saved image in
img_blur = cv2.blur(img, (7,7))
img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)
min_blue = np.array([105,230,250])
max_blue = np.array([115,255,255])
mask = cv2.inRange(img_hsv, min_blue, max_blue)
segmented_img = cv2.bitwise_and(img,img,mask=mask)
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours (segmented_img, contours, -1, (0,0,255), 3)
cv2.imshow('mask', output)
# thr_value, img_th = cv2.threshold(img_colour_th, 160, 255, cv2.THRESH_OTSU)
# kernel = np.ones((3,3),np.uint8)
# img_open = cv2.morphologyEx(img_colour_th, cv2.MORPH_OPEN, kernel)
# img_close = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel)
# #img_canny = cv2.Canny(img_colour_th, 50,100)
# contours, hierarchy = cv2.findContours(img_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contours,-1,(0,255,0),2)
# cv2.imshow('th1', img)

# cv2.imshow('th', img_th)
# print(len(contours))

# #thr_hsv2bgr = cv2.cvtColor(img_colour_th, cv2.COLOR_HSV2BGR)
# #gray_img = cv2.cvtColor(thr_hsv2bgr, cv2.COLOR_BGR2GRAY)
# #thr , img_th = cv2.threshold(gray_img, 150 ,255, cv2.THRESH_BINARY)



# def colour_histogram(image, space):
#     if space == 'rgb':
#         labels = ['Blue', 'Green', 'Red']
#     elif space == 'hsv':
#         labels = ['Hue', 'Saturation', 'Value']
#     else:
#         labels = ['Component 1', 'Component 2', 'Component 3']

#     fig, ax = plt.subplots(1, 3, figsize=(15, 5))

#     for h in range(3):
#         ax[h].hist(image[:,:,h].ravel(),256,[0,256])
#         ax[h].set_title(labels[h])
        
#     plt.show()


# cv2.waitKey(0)
# for i, c in enumerate(contours):        # loop through all the found contours
#     print(i, ':', hierarchy[0, i])
#     print('length', len(c))
#     perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
#     print('perimeter: ', perimeter)  
#     [x,y,w,h] = cv2.boundingRect(contours[0])
#     cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)
#     cropped_HSV = img_hsv[y:y+h, x:x+w, :]
#     cv2.imshow('cropped hsv', cropped_HSV)
#     colour_histogram(cropped_HSV, 'hsv')
    
#     epsilon = 0.06*perimeter    # parameter of polygon approximation: smaller values provide more vertices
#     vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
#     print('approx corners: ', vertex_approx, '\n')                    # number of vertices
#     ellipse = cv2.fitEllipse(c)
#     (xc,yc),(d1,d2), angle = ellipse
#     axes_ratio = round (d1/d2,  3)
#     print('axes ratio', axes_ratio, '\n')
#     cv2.drawContours(img, [c], 0, (0, 255, 0), 3)   # paint contour c
#     cv2.putText(img, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c    
#     #[x,y,w,h] = cv2.boundingRect(c)
#     cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
#     cv2.ellipse(img, ellipse, (0, 0, 255), 1)
#     cv2.imshow('contours',img)
#     sample = [perimeter, vertex_approx, axes_ratio]
# cv2.waitKey(0)

# #     kernel = np.ones((5,5),np.uint8)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
