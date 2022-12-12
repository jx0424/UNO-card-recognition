#-------------Library used
import cv2
import numpy as np
import matplotlib.pyplot as plt 
import os
import ML_Trainer
import VideoStream
from tkinter import *

#-----------------------GUI-------------------------
root = Tk()
#------set the window to be 400x400
root.geometry('400x400')
#set title to Python Machine Learning
root.title("Python Machine Learning")
left_frame = Frame(root, width=100, height=50)
#------------Buttons for functions calling---------
# Create a button for Machine Learning Trainder
btn = Button(root, text = "Machine Learning Trainer", command=ML_Trainer.ML_trainer)
btn.pack()
# create button for Video stream
btn2 = Button(root, text= 'Video Stream', command = VideoStream.VideoStream )
btn2.pack()

root.mainloop()
