import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    bol, frame = cap.read()
    frame = cv2.flip(frame,1)
    blor = cv2.GaussianBlur(frame,(5,5),0)
    colSpace = cv2.cvtColor(blor,cv2.COLOR_BGR2HSV)

    #color code for lime-green, change according to your color selection
    lb = np.array([20,106,103],dtype = np.uint8)
    ub = np.array([42,255,255],dtype = np.uint8)
    mask = cv2.inRange(colSpace,lb,ub)
    out = frame.copy()

    #finding the contours
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for i in contours:
        area = cv2.contourArea(i) #finding the area of the contours so that we will draw only those contours whose area is above a certain threshold
        if area > 500:
            cv2.drawContours(out,contours,-1,(100,255,0),3)
    
    cv2.imshow('frame',out)
    cv2.imshow('green',mask)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()