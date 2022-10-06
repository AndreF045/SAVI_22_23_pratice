
import cv2
import numpy as np



def main():
    cap = cv2.VideoCapture('/home/andre/Videos/traffic.mp4')

    #deteçao de objetos da camara estatica
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=35)

    while True:

        ret,frame = cap.read()
        height, width, _ = frame.shape
        print(height, width)

        #extrat region of the image
        roi = frame[100:700, 300:1100]

#object detection
        mask = object_detector.apply(roi)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:

            #calculate area and remove small elements
            area = cv2.contourArea(cnt)
            if area > 8000:
                #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
                x, y, h, w = cv2.boundingRect(cnt)
                cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)


        
        #cv2.imshow("roi", roi)
        cv2.imshow("frame", frame)
        #cv2.imshow("mask", mask)

    
        if cv2.waitKey(30) == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    




if __name__== "__main__":
    main()