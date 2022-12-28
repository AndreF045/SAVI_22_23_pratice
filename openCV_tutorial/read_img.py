#read image

import cv2 as cv
import sys

img = cv.imread("/home/andre/Pictures/man.jpeg")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("este é o shek", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("man.png", img)

    

