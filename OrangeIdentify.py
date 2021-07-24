import cv2 as cv
import numpy as np

img = cv.imread('Imagens/Laranja_3.jpg')
# cv.imshow('Laranjas', img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

h,s,v = cv.split(hsv)

# cv.imshow('H', h)
# cv.imshow('S', s)
# cv.imshow('V', v)

mask = cv.inRange(h, 1, 25)
# cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Final', masked)

cv.waitKey(0)