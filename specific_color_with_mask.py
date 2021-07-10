import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    error , image = video.read()

    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)   # to convert BGR image into HSV
    lower = np.array([70,0,0])                  # lower bound of the color for image to display /// in this case blue
    upper = np.array([130,255,255])               # upper bound of the color for  image to display

    mask = cv2.inRange(hsv,lower,upper)           # mask

    result = cv2.bitwise_and(image,image, mask = mask)



    cv2.imshow("image",result)
    cv2.imshow("mask",mask)

    if cv2.waitKey(1) == ord(" "):
        break


video.release()
cv2.destroyAllWindows()
