
import cv2 as cv
import numpy as np


scene_img = cv.imread("/home/andre/Pictures/scene.jpg", 0)
wally_img = cv.imread("/home/andre/Pictures/wally.png", 0)

#para apresentar o resultado
scenee_img = cv.imread("/home/andre/Pictures/scene.jpg", cv.IMREAD_UNCHANGED)
#cv.imshow("scene", scene_img)

result = cv.matchTemplate(scene_img, wally_img, cv.TM_CCOEFF_NORMED)

cv.imshow("result", result)

#cv.waitKey()
cv.destroyAllWindows()

#vai nos dar a melhor math localizaçao do wally
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.4

if max_val >= threshold:
    print('wally.')

    
    wally_w = wally_img.shape[1]
    wally_h = wally_img.shape[0]

    # Calculate the bottom right corner of the rectangle to draw
    top_left = max_loc
    bottom_right = (top_left[0] + wally_w, top_left[1] + wally_h)

    
    cv.rectangle(scenee_img, top_left, bottom_right, 
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow("esta aqui o wally", scenee_img)
    cv.waitKey()
    

else:
    print('wally not found.')