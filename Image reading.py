import cv2
import numpy as np

#Load in image from folder 
image = cv2.imread(r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\y1.jpg')

try:
    bilateral_image = cv2.bilateralFilter(image, 9 , 100, 100)
    cv2.imshow('Bilateral image', bilateral_image)
    blur_image = cv2.GaussianBlur(bilateral_image, (3,3), cv2.BORDER_CONSTANT)
    cv2.imshow('blur',blur_image)
    BW_image = cv2.cvtColor(blur_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Black and White', BW_image)
    thr_value, threshed_image = cv2.threshold(BW_image, 165, 255, cv2.THRESH_BINARY)
    cv2.imshow('threshed image' ,threshed_image)
    kernel = np.ones((5,5), np.uint8)
    image_close = cv2.morphologyEx(threshed_image, cv2.MORPH_OPEN, kernel)      # morphology correction
    image_open = cv2.morphologyEx(image_close, cv2.MORPH_CLOSE, kernel)
    #img_canny = cv2.Canny(image_close, 50, 100) 

    # canny_image = cv2.Canny (threshed_image, 100, 100)
    #cv2.imshow('canny', img_canny)
    contours, hierarchy = cv2.findContours(image_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    cv2.drawContours(image, contours, -1 , (0,255,0), 2)
    cv2.imshow('contour image', image)

#cv2.waitKey(0)
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
                    #cv2.ellipse(image, ellipse, (0, 0, 255), 1)
                    #cropped = image[250:410,260:395]
                    #cv2.imshow('cropped', cropped) 
                    cv2.imshow('contours',image)
                    sample = [perimeter, vertex_approx, axes_ratio]
except: 
    #bilateral_image = cv2.bilateralFilter(image, 9 , 100, 100)
    #cv2.imshow('Bilateral image', bilateral_image)
    BW_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.blur(BW_image ,(5,5))
    cv2.imshow('blur',blur_image)
   
    cv2.imshow('Black and White', BW_image)
    th, threshed_image = cv2.threshold(blur_image,140,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('threshed image' ,threshed_image)
    kernel = np.ones((5,5), np.uint8)
    #image_close = cv2.morphologyEx(threshed_image, cv2.MORPH_OPEN, kernel)      # morphology correction
    #image_open = cv2.morphologyEx(image_close, cv2.MORPH_CLOSE, kernel)
    #img_canny = cv2.Canny(image_close, 50, 100) 

    # canny_image = cv2.Canny (threshed_image, 100, 100)
    #cv2.imshow('canny', img_canny)
    contours, hierarchy = cv2.findContours(threshed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    cv2.drawContours(image, contours, -1 , (0,255,0), 2)
    cv2.imshow('contour image', image)

#cv2.waitKey(0)
    # for i, c in enumerate(contours):         # loop through all the found contours
    #                 print(i, ':', hierarchy[0, i])          # display contour hierarchy
    #                 #print('length: ', len(c))               # display numbr of points in contour c
    #                 perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
    #                 print('perimeter: ', perimeter)               
    #                 epsilon = 0.006*perimeter    # parameter of polygon approximation: smaller values provide more vertices
    #                 vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
    #                 print('approx corners: ', vertex_approx, '\n')                    # number of vertices
    #                 ellipse = cv2.fitEllipse(c)
    #                 (xc,yc),(d1,d2), angle = ellipse
    #                 axes_ratio = round (d1/d2,  3)
    #                 print('axes ratio', axes_ratio, '\n')
    #                 cv2.drawContours(image, [c], 0, (0, 255, 0), 3)   # paint contour c
    #                 cv2.putText(image, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c    
    #                 [x,y,w,h] = cv2.boundingRect(c)
    #                 cv2.rectangle(image, (x,y), (x+w,y+h), (255, 0, 0), 2)
    #                 #cv2.ellipse(image, ellipse, (0, 0, 255), 1)
    #                 #cropped = image[250:410,260:395]
    #                 #cv2.imshow('cropped', cropped) 
    #                 cv2.imshow('contours',image)
    #                 sample = [perimeter, vertex_approx, axes_ratio]
#     #other image processing for other colour
#         # for i, c in enumerate(contours):         # loop through all the found contours
#         #             print(i, ':', hierarchy[0, i])          # display contour hierarchy
#         #             #print('length: ', len(c))               # display numbr of points in contour c
#         #             perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
#         #             print('perimeter: ', perimeter)               
#         #             epsilon = 0.006*perimeter    # parameter of polygon approximation: smaller values provide more vertices
#         #             vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
#         #             print('approx corners: ', vertex_approx, '\n')                    # number of vertices
#         #             ellipse = cv2.fitEllipse(c)
#         #             (xc,yc),(d1,d2), angle = ellipse
#         #             axes_ratio = round (d1/d2,  3)
#         #             print('axes ratio', axes_ratio, '\n')
#         #             cv2.drawContours(image, [c], 0, (0, 255, 0), 3)   # paint contour c
#         #             cv2.putText(image, str(i), (c[0, 0, 0]+20, c[0, 0, 1]+30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))    # identify contour c    
#         #             [x,y,w,h] = cv2.boundingRect(c)
#         #             cv2.rectangle(image, (x,y), (x+w,y+h), (255, 0, 0), 2)
#         #             #cv2.ellipse(image, ellipse, (0, 0, 255), 1)
#         #             #cropped = image[250:410,260:395]
#         #             #cv2.imshow('cropped', cropped) 
#         #             cv2.imshow('contours',image)
#         #             sample = [perimeter, vertex_approx, axes_ratio]
    
cv2.waitKey(0)

#if perimeter > asdasdas and 





