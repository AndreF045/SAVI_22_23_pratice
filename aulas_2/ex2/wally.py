
import cv2
import numpy as np


scene_img = cv2.imread("/home/andre/Pictures/scene.jpg")
wally_img = cv2.imread("/home/andre/Pictures/wally.png")

#para apresentar o resultado

result = cv2.matchTemplate(scene_img, wally_img, cv2.TM_CCOEFF_NORMED)

cv2.imshow("result", result)

cv2.destroyAllWindows()

#vai nos dar a melhor math localizaçao do wally
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.4

if max_val >= threshold:
    print('wally found!')

    
    wally_w = wally_img.shape[1]
    wally_h = wally_img.shape[0]

    # Calculate the bottom right corner of the rectangle to draw
    top_left = max_loc
    bottom_right = (top_left[0] + wally_w, top_left[1] + wally_h)

    
    cv2.rectangle(scene_img, top_left, bottom_right, 
                    color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

    cv2.imshow("esta aqui o wally", scene_img)
    cv2.waitKey()
    

else:
    print('wally not found.')