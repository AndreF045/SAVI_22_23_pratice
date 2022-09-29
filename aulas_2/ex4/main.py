import numpy as np
import cv2



    
scene_img = cv2.imread("/home/andre/Pictures/scene.jpg")
wally_img = cv2.imread("/home/andre/Pictures/wally.png")

H,W,_ = scene_img.shape
scene_gray = cv2.cvtColor(scene_img,cv2.COLOR_BGR2GRAY) #imagem em  gray



#para apresentar o resultado

result = cv2.matchTemplate(scene_img, wally_img, cv2.TM_CCOEFF_NORMED)

cv2.imshow("result", result)

cv2.destroyAllWindows()

#vai nos dar a melhor math localizaçao do wally
_, max_val, _, max_loc = cv2.minMaxLoc(result)

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

image_gui = scene_img * 0

#mask =np.zeros((wally_h,wally_w)).astype(np.uint8)
#for pt in zip(*loc[::-1]):
    #   cv2.rectangle(mask, top_left, bottom_right,255, -1)

    
wally_w = wally_img.shape[1]
wally_h = wally_img.shape[0]

    # Calculate the bottom right corner of the rectangle to draw
top_left = max_loc
bottom_right = (top_left[0] + wally_w, top_left[1] + wally_h)
    

    
mask =np.zeros((H,W)).astype(np.uint8)

cv2.rectangle(mask, top_left, bottom_right,255, -1)


mask_bool = mask.astype(bool)
image_gui[mask_bool]= scene_img[mask_bool]

negate_mask = np.logical_not(mask_bool)

merged_3 = cv2.merge([scene_gray,scene_gray,scene_gray])
image_gui[negate_mask] = merged_3[negate_mask]


cv2.imshow("esta aqui o wally", scene_img)
cv2.imshow("gui", image_gui)
cv2.waitKey()
    




