import cv2
import numpy as np

def sketch(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    #lap=cv2.Laplacian(blur,cv2.CV_64F)
    canny=cv2.Canny(blur,10,70)
    ret,mask=cv2.threshold(canny,1,255,cv2.THRESH_BINARY_INV)
    return mask

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()
    cv2.imshow("Live Sketch",sketch(frame))
    if cv2.waitKey(1)==13:
        break
cam.release()
cv2.destroyAllWindows()
