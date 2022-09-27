from pickletools import uint8
import numpy as np
import cv2 


def main():
    
    img = cv2.imread("/home/andre/Desktop/Savi/SAVI_22_23_pratice/aulas_2/images/lake.jpg")
    #grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #ind = np.int(grey.shape[1]/2)       # get width/2 value of the image for indexing
    #img[:,0:ind,0] = grey[:,0:ind]      # make blue component value equal to gray image
    #img[:,0:ind,1] = grey[:,0:ind]      # make green component value equal to gray image
    #img[:,0:ind,2] = grey[:,0:ind]      # make red component value equal to gray image

    cv2.imshow("lake", img)
    cv2.waitKey(0)




if __name__ == "__main__":
    main()