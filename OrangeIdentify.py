import cv2 as cv
import numpy as np

img = cv.imread('Imagens/Laranja_1.jpg')
# cv.imshow('Laranjas', img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

h, s, v = cv.split(hsv)

cv.imshow('H', h)
cv.imshow('S', s)
cv.imshow('V', v)

cv.waitKey(0)
