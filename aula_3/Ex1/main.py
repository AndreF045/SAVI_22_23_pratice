import cv2
import numpy as np



def main():
    cap = cv2.VideoCapture('/home/andre/Videos/traffic.mp4')

    #deteçao de objetos da camara estatica
    object_detector = cv2.createBackgroundSubtractorMOG2()

    while True:

        ret,frame = cap.read()

        mask = object_detector.apply(frame)

        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)

    
        if cv2.waitKey(30) == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    




if __name__== "__main__":
    main()