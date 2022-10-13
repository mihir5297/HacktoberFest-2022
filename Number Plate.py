# Project 3
# NUMBER PLATE DETECTION

import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_russian_plate_number.xml")
minArea = 500
# color = (85,255,0)
color = (0,0,0)
img = cv2.imread('Resources/Car.jpg')
imgNew = cv2.resize(img, (520,640))
imgGray = cv2.cvtColor(imgNew, cv2.COLOR_BGR2GRAY)

numberplates = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in numberplates:
    area = w*h
    if area > minArea:
        cv2.rectangle(imgNew,(x,y),(x+w, y+h),(255,0,0),2)
        cv2.putText(imgNew, "Number Plate", (x,y+80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.1, color, 2)
        imgRoi = imgNew[y:y+h, x:x+w]
        imgPlate = cv2.resize(imgRoi,(340,220))
        cv2.imshow("Number Plate", imgPlate)


cv2.imshow('Car', imgNew)
cv2.waitKey(0)