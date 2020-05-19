# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:09:41 2020

@author: harshvardhan
"""

import numpy as np
import cv2

img = cv2.imread('lena_face.jpg',0)
width = img.shape[0]
height = img.shape[1]

pixels = []
for i in range(width):
    for j in range(height):
         pixels.append(np.binary_repr(img[i][j] ,width=8))  
         

         

eight_bit_img = (np.array([int(i[0]) for i in pixels],dtype = np.uint8) * 128).reshape(width,height)
seven_bit_img = (np.array([int(i[1]) for i in pixels],dtype = np.uint8) * 64).reshape(width,height)
six_bit_img = (np.array([int(i[2]) for i in pixels],dtype = np.uint8) * 32).reshape(width,height)
five_bit_img = (np.array([int(i[3]) for i in pixels],dtype = np.uint8) * 16).reshape(width,height)
four_bit_img = (np.array([int(i[4]) for i in pixels],dtype = np.uint8) * 8).reshape(width,height)
three_bit_img = (np.array([int(i[5]) for i in pixels],dtype = np.uint8) * 4).reshape(width,height)
two_bit_img = (np.array([int(i[6]) for i in pixels],dtype = np.uint8) * 2).reshape(width,height)
one_bit_img = (np.array([int(i[7]) for i in pixels],dtype = np.uint8) * 1).reshape(width,height)


a = eight_bit_img+seven_bit_img+six_bit_img+five_bit_img+four_bit_img
cv2.imshow("Removing Three Least Significant Bits", a)
cv2.imwrite("LSB_remove.jpg",a)
b = five_bit_img+four_bit_img+three_bit_img+two_bit_img+one_bit_img
cv2.imshow("Removing Three Most Significant Bits", b)
cv2.imwrite("MSB_remove.jpg",b)

cv2.imshow('8bit',eight_bit_img)
cv2.imshow('7bit',seven_bit_img)
cv2.imshow('6bit',six_bit_img)
cv2.imshow('5bit',five_bit_img)
cv2.imshow('4bit',four_bit_img)
cv2.imshow('3bit',three_bit_img)
cv2.imshow('2bit',two_bit_img)
cv2.imshow('1bit',one_bit_img)


cv2.imwrite('8bit.jpg',eight_bit_img)
cv2.imwrite('7bit.jpg',seven_bit_img)
cv2.imwrite('6bit.jpg',six_bit_img)
cv2.imwrite('5bit.jpg',five_bit_img)
cv2.imwrite('4bit.jpg',four_bit_img)
cv2.imwrite('3bit.jpg',three_bit_img)
cv2.imwrite('2bit.jpg',two_bit_img)
cv2.imwrite('1bit.jpg',one_bit_img)

cv2.waitKey(0) 
cv2.destroyAllWindows()