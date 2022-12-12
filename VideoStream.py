# --------------------Library used
import cv2
import numpy as np
import pickle
import time 

#---------------------------HSV Ranges----------------------------
min_blue = np.array([87, 150, 80])
max_blue = np.array([117, 255, 255])
min_red = np.array([0, 50, 20])
max_red = np.array([10, 255, 255])
min_green = np.array([45, 100, 50])
max_green = np.array([75, 255, 255])
min_yellow = np.array([15, 90, 80])
max_yellow = np.array([40, 255, 255]) 




#-------------------------------- Video Stream Function----------------------------------
def VideoStream():
#--------Naming and Resizing window for the video stream    
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("frame", 700,700)
    #open up video camera
    vc = cv2.VideoCapture(0)
    #limit fps to 30 to reduce load
    vc.set(cv2.CAP_PROP_FPS , 30)
    #delay for 1 second to let camera "warm up"
    time.sleep(1)
    while vc.isOpened():
        #load ML model
        clf = pickle.load(open('ML_Model','rb'))
        #obtain the frames from video stream
        _, frame = vc.read()
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #---------------------------Mask generation----------------------
    #---------------Blue----------------------------
        blue_mask = cv2.inRange(frame_hsv, min_blue, max_blue)
        segmented_imgB = cv2.bitwise_and(frame,frame,mask=blue_mask)
        blue_card = np.sum(blue_mask)
    #---------------Green---------------------------
        green_mask = cv2.inRange(frame_hsv, min_green, max_green)
        segmented_imgG = cv2.bitwise_and(frame,frame,mask=green_mask)
        green_card = np.sum(green_mask)
    #---------------Red-----------------------------
        red_mask = cv2.inRange(frame_hsv, min_red, max_red)
        segmented_imgR = cv2.bitwise_and(frame,frame,mask=red_mask)
        red_card = np.sum(red_mask)
    #--------------Yellow--------------------------
        yellow_mask = cv2.inRange(frame_hsv, min_yellow, max_yellow)
        segmented_imgY = cv2.bitwise_and(frame,frame,mask=yellow_mask)
        yellow_card = np.sum(yellow_mask)
    #---------------------------------------------------------
        masks = [blue_mask,green_mask,red_mask,yellow_mask]
    #----------------------Frame Processing------------------------
        kernel = np.ones((3,3),np.uint8)
        blur_frame = cv2.GaussianBlur(frame, (7,7),0)
        gray_frame = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2GRAY)
        _, frame_th = cv2.threshold(gray_frame, 160 , 255, cv2.THRESH_BINARY)
        frame_close = cv2.morphologyEx(frame_th, cv2.MORPH_CLOSE, kernel)
        frame_open = cv2.morphologyEx(frame_close, cv2.MORPH_OPEN, kernel)
        #------------------find contours that are captured by camera
        contours,hierarchy = cv2.findContours(frame_open, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #loop through all contours and get the contour properties with constraints to get the contour that we desire.
        for i, c in enumerate(contours):         
            perimeter = cv2.arcLength(c, True)    
            epsilon = 0.1*perimeter    
            vertex_approx = len(cv2.approxPolyDP(c, epsilon, True))  
            area = cv2.contourArea(c)
            [x,y,w,h] = cv2.boundingRect(c)
            if area > 1200 and area < 3500 and len(c)>200 and len(c) < 400 :
                cv2.drawContours(frame , contours, -1, (0, 255, 0), 2)
                features = [len(c), perimeter, vertex_approx]
                features_array = (np.array(features)).reshape(1, -1)
                #Run the ML model with the data from video capture
                MLPrediction = clf.predict(features_array)
                #-----------------Colour detection from middle of window
                height, width, _ = frame.shape
                cx = int(width / 2)
                cy = int(height / 2)
                pixel_center = frame_hsv[cy, cx]
                hue_value = pixel_center[0]
                colour = "Undefined"
                if hue_value < 5:
                    colour = "Red"
                elif hue_value < 33:
                    colour = "Yellow"
                elif hue_value < 78:
                    colour = "Green"
                elif hue_value < 131:
                    colour = "Blue"
                else:
                    colour = "Red"
                #this pixel will get the hs
                pixel_center_bgr = frame[cy, cx]           
                text = colour + str(MLPrediction)
                b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
                #display the colour and display on the video stream 
                cv2.putText(frame, text, (c[0, 0, 0], c[0, 0, 1]-20), 0, 3, (b, g, r), 5)
                #plot this circle to help user to get the colour
                cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)                 
        cv2.imshow('frame', frame)
        #when ESC key is pressed, break through the loop and exit the program
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()
    vc.release()





