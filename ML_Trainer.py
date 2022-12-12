#-----------------------------Library used-----------------------------------
import cv2
import numpy as np
import os
from os import listdir
import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#------------Image file processing-------------------------------------------------
data_y = []
data_x = []
#-----------------interate though every images in the image folder--------------------------
folder_dir = r'C:\Users\brend\OneDrive - Middlesex University\Documents\GitHub\UNO-card-recognition\images'
for images in os.listdir(folder_dir):    
    if images.endswith(".jpg"):
        path = os.path.join(folder_dir, images)
        image = cv2.imread(path)
        img_cropped = image[270:390, 270:395]
        blur_image = cv2.blur(img_cropped, (9,9), 0)
        BW_image = cv2.cvtColor(blur_image, cv2.COLOR_BGR2GRAY)
        thr_value, threshed_image = cv2.threshold(BW_image, 160, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3,3), np.uint8)
        image_close = cv2.morphologyEx(threshed_image, cv2.MORPH_CLOSE, kernel)
        image_open = cv2.morphologyEx(image_close, cv2.MORPH_OPEN, kernel)
        contours, hierarchy = cv2.findContours(image_open, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        for i, c in enumerate(contours):         # loop through all the found contours
            perimeter = cv2.arcLength(c, True)     # perimeter of contour c (curved length)
            epsilon = 0.006*perimeter    # parameter of polygon approximation: smaller values provide more vertices
            vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))     # approximate with polygon
            area = cv2.contourArea(c)
            cv2.drawContours(img_cropped, [c], 0, (0, 255, 0), 3)   # paint contour c
            [x,y,w,h] = cv2.boundingRect(c)
            cv2.rectangle(image, (x,y), (x+w,y+h), (255, 0, 0), 2)
            features = [perimeter, vertex_approx, len(c)]
            if area > 1200 and area < 3500 and len(c)>150 and len(c) < 400:
                data_x.append(features)
                pattern_label = images[1]
                data_y.append(pattern_label)

#----------------------------Machine Learning Model Generator---------------------
X = data_x
y = data_y
def ML_trainer():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5,shuffle = True)
    classifier = RandomForestClassifier()
    classifier.fit(X_train, y_train)
    y_predict = classifier.predict(X_test)
#Compare the test and train value to generate accuracy of ML model
    score = sum(y_predict == y_test)/len(y_test)
    print(score*100, '%')
    classifier_file = open('ML_Model', 'ab')
# Save ML model  
    pickle.dump(classifier, classifier_file)    
    classifier_file.close()
