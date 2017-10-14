import numpy as np
import cv2

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
# Load an color image in grayscale
img = cv2.imread('test.jpg',1)

#read in image and make it grey
gray = cv2.imread('test.jpg',0)
#Blur the image
blur = cv2.GaussianBlur(gray,(9,9),0)
#set the threshold and make all pixels either black or white
ret,thresh = cv2.threshold(blur,175,255,cv2.THRESH_BINARY_INV)
#Find th ecountours around the balck parts
contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
#draw the countours on original image
maxCont=contours[0]
prevBest=contours[0]
for cont in contours:
	if (cv2.contourArea(cont)>cv2.contourArea(maxCont)):
		prevBest=maxCont
		maxCont=cont

cv2.drawContours(img, [prevBest], 0, (0,255,0), 3)
cv2.imshow('dst_rt',img)
cv2.waitKey(0)
cv2.destroyAllWindows()