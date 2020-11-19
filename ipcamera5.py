# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:37:22 2020

@author: harshvardhan
"""

import cv2 
video = cv2.VideoCapture(0) 
address = "http://192.168.29.112:8080/video" 
video.open(address)
if (video.isOpened() == False):  
    print("Error reading video file")  
frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 
size = (frame_width, frame_height) 
result = cv2.VideoWriter('ycrcb.avi',cv2.VideoWriter_fourcc(*'MJPG'), 10, size) 
while(True): 
    ret, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb) 
    if ret == True:  
        result.write(frame) 
        cv2.imshow('Frame', frame) 
        if cv2.waitKey(1) & 0xFF == ord('s'): 
            break
    else: 
        break

video.release() 
result.release() 

# Closes all the frames 
cv2.destroyAllWindows() 
   
print("The video was successfully saved") 