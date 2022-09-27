from pickletools import uint8
import numpy as np
import cv2 as cv


def main():
    print("hello world")

print("creating a new image")

#image = np.ndarray((240,320), dtype= np.uint8)
image = np.random.randint(0, high= 255, size=(240,320), dtype= np.uint8
)


#set image to gray

#image = image*0 +128
image += 128 

cv.imshow("window", image)

cv.waitKey(0)





if __name__ == "__main__":
    main()