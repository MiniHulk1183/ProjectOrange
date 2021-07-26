import cv2 as cv
import numpy as np

img = cv.imread('Imagens/Laranja_1.jpg')
cv.imshow('Laranjas', img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lower = np.array([1, 50, 120])
upper = np.array([25, 255, 255])

mask = cv.inRange(hsv, lower, upper)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Final', masked)

cv.waitKey(0)