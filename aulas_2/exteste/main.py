from pickletools import uint8
import numpy as np
import cv2 


def main():
    print("hello world")

print("creating a new image")

#image = np.ndarray((240,320), dtype= np.uint8)
IMG = np.random.randint(0, high= 255, size=(240,320), dtype= np.uint8
)


#set image to gray

#image = image*0 +128
IMG += 128 

cv2.imshow("window", IMG)

cv2.waitKey(0)





if __name__ == "__main__":
    main()