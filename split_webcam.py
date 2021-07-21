import numpy as np
import cv2

video = cv2.VideoCapture(0)

while True:

    error , image = video.read()

    width = int(video.get(3))
    height = int(video.get(4))

    vector_image = np.zeros(image.shape,np.uint8)

    crop_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    vector_image[:height //2  , :width // 2] = crop_image
    vector_image[height // 2 : ,:width // 2] = crop_image
    vector_image[height // 2: ,width // 2 :] = crop_image
    vector_image[:height // 2 ,width // 2 :] = crop_image

    cv2.imshow("Image",vector_image)

    if cv2.waitKey(1) == ord(" "):
        break

video.release()
cv2.destroyAllWindows()
