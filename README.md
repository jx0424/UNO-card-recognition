Project Title:
PDE 3433 Assignment 2 - Computer Vision

Project Description:
The code consist of 3 parts:
1. ML_Trainer.py - This piece of code will process the images in the file named "images" and it will build a machine learning model from scratch using the RandomForest classifier. It will also display the accuracy percentage of the given data.
2. GUI.py - This piece of code is mainly to build a very simple GUI with working buttons of buttons for ML_trainer and VideoStream.
3. VideoStream.py - This piece of code is used to start up the video capture function from opencv and process the frame provided by a external camera and use the machine learning model to identify the UNO cards.

Library Used in all the program:
opencv - use for image processing and contour extraction
os - to iterate through the images in a folder
numpy - to deal with arrays for image processing
pickle - to save and load the trained machine learning model
sklearn - the main library used for building the machine learning model
tkinter - use to build the simple gui
time - use to let the code count time, used in VideoStream.py to "warm up" the camera.

Challenges faced during the assignment:
1. The contours of all cards are easily detectable excpect for yellow card.
2. For video streaming, the code wasnt able to recognise all the card but was able to recognise "1", "7", "3" perfectly. The main reason this could happen is maybe because of the features that were introduced to the machine learning model (wasnt precise enough) or the camera wasnt able to extract good contours from video stream
3. Due to the lighting in my room, the contours obtain from the video stream are always inconsistant and causes the recognition process to reduce in performance by a lot.

Future Improvements:
1. Make the accuracy percentage of the machine learning model higher, preferably above 80/90% to ensure that it can better recognise the ALL the cards.
2. Shorten the code to make it less intensive and more responsive.
3. Make a more robust/neat GUI.
4. Find out the optimal threshold for general lighting of the environment.

How to use the codes:
1. Make sure that you have all the codes(ML_Trainer.py, GUI.py,VideoStream.py) and the image folder in one folder.
2. Run the GUI.py and click on "Machine Learning Trainer" and it should display the accuracy of the machine learning model.
3. Click on "Video Stream" to initiate camera and the machine learning model to recognise the cards.

