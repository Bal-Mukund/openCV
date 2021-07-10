import cv2

def nothing(x):  #quite does nothing
    pass

img = cv2.imread("C:\\Users\\balmu\\OneDrive\\Pictures\\cartoon.jpg")  #path of the image
img = cv2.resize(img,None,fx=0.1,fy=0.1)

# creating a trackbar
cv2.namedWindow("cartoon")
cv2.createTrackbar("trackbar","cartoon",1,255,nothing)

while True:
    value = cv2.getTrackbarPos("trackbar","cartoon")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)      # BGR to gray
    gray_blur = cv2.medianBlur(gray,9)               # bluring gray image


    color_blur = cv2.bilateralFilter(img,9,value,value)   #bluring color image

    # finding edge of the image
    edge = cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,value)
    # merging edge and blur image
    carton = cv2.bitwise_and(color_blur,color_blur,mask=edge)

    # showing all the images
    cv2.imshow("image",img)
    cv2.imshow("cartoon",carton)

    key = cv2.waitKey(100)
    if key == ord(" "):
        break

cv2.destroyAllWindows()
