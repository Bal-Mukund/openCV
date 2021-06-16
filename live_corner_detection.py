import numpy as np
import cv2


# to open webcam
video = cv2.VideoCapture(0)

while True:
    error,image = video.read()

    gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray,1000,0.1,2)  # function to detect corner

    icorners = np.int0(corners)    # to convert float into integers


    for corner in icorners:

        x,y = corner.ravel()  # to obtain elements from double list

        cv2.circle(image,(x,y),2,(255,0,0),2)

# if you want to draw lines using these circles

    #for i in range(len(icorners)):
     #   for j in range(i + 1, len(icorners)):
      #      corner1 = tuple(icorners[i][0])
       #     corner2 = tuple(icorners[j][0])

        #    cv2.line(image, corner1, corner2, (0, 0, 255), 1)


    cv2.imshow("image",image)

    if cv2.waitKey(1) == ord(" "):  # to quit if spacebar is pressed
        break

video.release()  # to release webcam
cv2.destroyAllWindows()
