from pickletools import uint8
import numpy as np
import cv2 


def main():
    
    img = cv2.imread("/home/andre/Desktop/Savi/SAVI_22_23_pratice/aulas_2/images/lake.jpg")
    
    h,w,_ = img.shape
    dark = img.shape[::]
    dark[:,int(w/2):] = (img[:,int(w/2):]*0.5).astype(np.uint8)

    ind = np.int(grey.shape[1]/2)       # get width/2 value of the image for indexing
    img_grey[:,0:ind,0] = grey[:,0:ind]      # make blue component value equal to gray image
    img_grey[:,0:ind,1] = grey[:,0:ind]      # make green component value equal to gray image
    img_grey[:,0:ind,2] = grey[:,0:ind]      # make red component value equal to gray image

    cv2.imshow("lake", img)
    cv2.imshow("half drak", dark)
    cv2.waitKey(0)




if __name__ == "__main__":
    main()