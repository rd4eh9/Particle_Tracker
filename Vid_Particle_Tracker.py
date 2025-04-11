# use this tracker algorithm https://github.com/lushank1/Marker_detection_and_tracking 
# Steps:
#import images into array --> parse from video
#identify particles
#find center of particle
#track change in xyz for each particle over time

import cv2
from tracker import*

#import video into frames

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
    frames.append(frame)

cap.release()

print(f"Total frames extracted: {len(frames)}")

 # how to access elements BGR blue = image[50, 100, 0]

markers = []

# use existing particle tracking library + replace this code
#iterate through all frames
for frame in range(frames):
    height, width, channels = frame.shape
    #iterate through all pixels
    for y in range(height):
        for x in range(width):
            blue, green, red = frame[y, x]
            if #nearby pixels exceed threshold value for marker color:
                #find every marker centroid + save in array/list
                markers.append([y,x])
        
#map distance b/w centroid in each frame (+ output equation?)

#look into openCV tracker library 

