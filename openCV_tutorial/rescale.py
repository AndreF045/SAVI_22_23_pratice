
import numpy as np
import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cap = cv.VideoCapture('/home/andre/Videos/dogss.mp4')
while cap.isOpened():

    ret, frame = cap.read()

    frame_resize = rescaleFrame(frame)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #caso queira o video a cinza, trocar frame por gray(variavel em cima)
    cv.imshow('dog', frame)
    cv.imshow("dog resize", frame_resize)
    if cv.waitKey(5) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()