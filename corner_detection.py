import numpy as np
import cv2
import sys


img = cv2.imread("C:\\Users\\balmu\OneDrive\\Pictures\\Picture/algo.png")


img = cv2.resize(img,(0,0),fx= 5,fy=5)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,1000,0.1,1)

convert_int = np.int0(corners)

for corner in convert_int:
    x,y  = corner.ravel()
    circle = cv2.circle(img,(x,y),2,(255,0,0),-1)




cv2.imshow("image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()

