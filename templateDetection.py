# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 09:49:16 2020

@author: harshvardhan
"""

import cv2
import numpy as np

img = cv2.imread('number_plate.jpg')
greyimg =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('plate.jpg', 0)
width = template.shape[0]
height = template.shape[1]
match = cv2.matchTemplate(greyimg, template, cv2.TM_CCOEFF_NORMED)
locations = np.where(match >= 0.8) 
color = (0,255,0)
for i in zip(*locations[::-1]):    
    cv2.rectangle(img, i, (i[0] + height, i[1] + width), color, 0)


cv2.imshow('Template Found', img)
cv2.imwrite("Final.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()