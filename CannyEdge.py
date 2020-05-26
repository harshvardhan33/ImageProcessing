# Run the code on google colab

import numpy as np 
import cv2
from google.colab.patches import cv2_imshow

img1 = cv2.imread("building.jpg")
grayImage = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImageBlur = cv2.blur(grayImage,(3,3))
edgedImage = cv2.Canny(grayImageBlur, 100, 300, 3)
cv2_imshow(edgedImage)
