import cv2
import numpy as np
import matplotlib.pyplot as plt

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

path = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images\b0.jpg'
img = cv2.imread(path)   # open the saved image in
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img_crop =  img[285:320,245:300,:]  #img[250:430,210:460,:] #
# colour_histogram(img_crop,'rgb')
# img_crop_HSV = cv2.cvtColor(img_crop, cv2.COLOR_BGR2HSV);
# colour_histogram(img_crop_HSV,'hsv')
# cv2.imshow('cropped',img_crop)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

min_blue = np.array([105,220,250])
max_blue = np.array([110,255,255])
#check hsv values for red green and yellow
min_red = np.array([105,220,250])
max_red = np.array([110,255,255])
min_green = np.array([105,220,250])
max_green = np.array([110,255,255])
min_yellow = np.array([105,220,250])
max_yellow = np.array([110,255,255])
colour_list = [[min_blue , max_blue],[min_red , max_red],[min_green , max_green],[min_yellow , max_yellow]]


for colour , min_colour, max_colour in colour_list:#the list is a list of min max colour array.
    mask = cv2.inRange(img_hsv, min_blue, max_blue)
    segmented_img = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('seg', segmented_img)
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.drawContours (img, contours, -1, (0,0,255), 3)
    #if contours:
        #return data_asdasda 
    #else: continue the loop

#if segmented_img
cv2.imshow('test', output)
cv2.waitKey(0)