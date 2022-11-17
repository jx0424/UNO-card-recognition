import cv2
import numpy as np

#function to read image files from computer
#image_read(user_choice):
    #card = user choice
##uno_cards = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,bR,bS,bT,,g0,g1,g2,g3,g4,g5,g6,g7,g8,g9,gR,gS,gT,]
##print("Choice of UNO card:
##      
##user_choice = input("Please enter the card of choice you want the program to identify: ")
##print(user_choice)
##
#image = cv2.imread(r'C:\Users\brend\OneDrive - Middlesex University\Desktop\images\b3.jpg')
#cv2.imshow('picture',image)
##                    
##    

#function to read image file from computer
path = r'C:\Users\brend\OneDrive - Middlesex University\Desktop\images\b2.jpg'
image = cv2.imread(path ,0) #read image file in grayscale from folder through the assigned path
#blurring the image to decrease noise
blur_image = cv2.GaussianBlur(image, (15,15), cv2.BORDER_DEFAULT)

thresh_image = cv2.adaptiveThreshold(blur_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 2) # compute a threshold value for each pixel, based on neighbourhood

canny_image = cv2.Canny(thresh_image, 125, 175)

dilated_image = cv2.dilate(canny_image, (7,7), iterations=3)

#eroded_image = cv2.erode(dilated_image, (3,3), iterations= 1)

cv2.imshow ('UNO Card', eroded_image) #display the image
cv2.waitKey(0)
 
