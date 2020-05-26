import numpy as np 
import cv2
import math
from google.colab.patches import cv2_imshow

img2 = cv2.imread("car1.jpg")
gray= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) 
dst = cv2.Canny(gray, 50, 150, apertureSize= 3)
lines = cv2.HoughLines(dst, 1, np.pi / 180,35)
# Draw the lines
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(img2, pt1, pt2, (0,255,0), 1)

# Draw The circles
img2_temp = cv2.medianBlur(gray,5)
circles = cv2.HoughCircles(img2_temp,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img2,(i[0],i[1]),i[2],(0,255,0),2)

cv2_imshow(img2)