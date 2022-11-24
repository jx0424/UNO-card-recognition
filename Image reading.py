import cv2
import numpy as np

#Load in image from folder 
image = cv2.imread(r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\b0.jpg')
bilateral_image = cv2.bilateralFilter(image, 9 , 100, 100)
cv2.imshow('Bilateral image', bilateral_image)
blur_image = cv2.GaussianBlur(bilateral_image, (3,3), cv2.BORDER_CONSTANT)
cv2.imshow('blur',blur_image)
BW_image = cv2.cvtColor(blur_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Black and White', BW_image)
thr_value, threshed_image = cv2.threshold(BW_image, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('threshed image' ,threshed_image)

kernel = np.ones((9,9), np.uint8)
image_close = cv2.morphologyEx(threshed_image, cv2.MORPH_OPEN, kernel)      # morphology correction
img_canny = cv2.Canny(image_close, 50, 100) 

# canny_image = cv2.Canny (threshed_image, 100, 100)
# cv2.imshow('canny', canny_image)
contours, hierarchy = cv2.findContours(image_close, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours))

cv2.drawContours(image, contours, -1 , (0,255,0), 2)
cv2.imshow('contour image', image)







cv2.waitKey(0)


# #function to read image file from computer
# path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\b1.jpg'
# image = cv2.imread(path) #read image file in grayscale from folder through the assigned path
# #blurring the image to decrease noise
# #blur_image = cv2.GaussianBlur(image, (15,15), cv2.BORDER_DEFAULT)
# # blank_image = np.zeros(image.shape, dtype = 'uint8')
# # thresh_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 2) # compute a threshold value for each pixel, based on neighbourhood

# # canny_image = cv2.Canny(thresh_image, 125, 175)

# # #dilated_image = cv2.dilate(canny_image, (7,7), iterations=3)
# #bilateral = cv2.bilaterralFilter(img, 10 , 35, 25)
# # contour , hierachies = cv2.findContours(thresh_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# # print(len(contour))

# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow('rgb', rgb)
# # cv2.drawContours(blank_image, contour, -1, (0,0,255), 2)
# # cv2.imshow('Contours drawn', blank_image)
# #eroded_image = cv2.erode(dilated_image, (3,3), iterations= 1)

# cv2.imshow ('UNO Card', image) #display the image
# cv2.waitKey(0)
 
