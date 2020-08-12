# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:55:45 2020

@author: varsha
"""


import cv2
import numpy as np
import time


cap = cv2.VideoCapture(0)
# give the camera to warm up 
time.sleep(3)
count = 0 
background=0
for i in range(30):
    ret,background = cap.read()
    if ret == False :
        continue
        
# flipping of the frame 
background = np.flip(background,axis=1)

# we are reading from video 
while(cap.isOpened()):
    ret, img = cap.read()
    if not ret : 
        break
    count = count + 1
	# Flipping the image (Can be uncommented if needed)
    img = np.flip(img,axis=1)
	
	# Converting image to HSV color space.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	#value = (35, 35)
	
	#blurred = cv2.GaussianBlur(hsv, value,0)
	
	# Defining lower range for red color detection.
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
	
	# Defining upper range for red color detection
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
	
	# Addition of the two masks to generate the final mask.
    mask = mask1+mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8),iterations = 2)
	
	# Replacing pixels corresponding to cloak with the background pixels.
    img[np.where(mask==255)] = background[np.where(mask==255)]
    cv2.imshow('Display',img)
    k = cv2.waitKey(10)
    if k == 27:
        break