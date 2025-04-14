#https://soft-matter.github.io/trackpy/v0.6.4/tutorial/walkthrough.html
#import graphing/data processing libraries

#check documentation for particle identification accuracy parameters !
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#import image processing/particle tracking libraries
import cv2
import trackpy as tp

# Path to your video file
video_path = 'path/to/video.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# List to store frames
frames = []
# Read frames one by one
while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Convert frame to greyscale
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(grey_frame)

cap.release()


#locate markers in the first frame
# arguments = img, particle size (pixels), search for bright(T)/dark(F) features
marker = tp.locate(frames[0], 11, invert=True)
#add adtl parameters as needed to filter all markers

#show dataframe of located particles
marker.head()

#show 1st image frame with particles located
tp.annotate(marker, frames[0])

#locate markers in all the frames
markers = tp.batch(frames[:], 11, invert=True)
#tp.quiet()

#track specific particles across frames
# arguments = particles, pixel displacement range/frame, max # of undetected frames
positions = tp.link(markers, 5, memory=3 )

#view located marker data across video time
positions.head() 

#filter marker trajectories 
# arguments = trajectories, present for more than # of frames
positions_filtered = tp.filter_stubs(positions, 25)

#plot marker trajectories over space
plt.figure()
tp.plot_traj(positions_filtered)

#can add more graphs to evaluate marker motion
#can store dataframes with PandasHDFStore