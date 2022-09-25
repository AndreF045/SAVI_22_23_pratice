from cgitb import grey
import cv2 as cv
import sys
import numpy as np

img = cv.imread("/home/andre/Pictures/man.jpg")
cv.imshow("este é o shek", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("shrek grey", grey)


k = cv.waitKey(0)