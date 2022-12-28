import numpy as np
import cv2


#def main():

scene_img = cv2.imread("/home/andre/Desktop/Savi/SAVI_22_23_pratice/aulas_2/images/beach.jpg")
wally_img = cv2.imread("/home/andre/Pictures/wallly.png")

#para apresentar o resultado

result = cv2.matchTemplate(scene_img, wally_img, cv2.TM_CCOEFF_NORMED)

cv2.imshow("result", result)


cv2.destroyAllWindows()

#vai nos dar a melhor math localizaçao do wally
_, max_val, _, max_loc = cv2.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.1

if max_val >= threshold:
    print('wally found!')

    
    wally_w = wally_img.shape[1]
    wally_h = wally_img.shape[0]

    # Calculate the bottom right corner of the rectangle to draw
    top_left = max_loc
    bottom_right = (top_left[0] + wally_w, top_left[1] + wally_h)

    
    cv2.rectangle(scene_img, top_left, bottom_right, 
                    color=(255, 0, 0), thickness=2, lineType=cv2.LINE_4)

    cv2.imshow("esta aqui o wally", scene_img)
    cv2.waitKey()
    

else:
    print('wally not found.')





#if __name__ == "__main__":
#main()