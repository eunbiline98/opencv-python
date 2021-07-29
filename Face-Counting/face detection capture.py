import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('C:/Users/Eunbiline_98/Documents/python source code download/image processing/penumpang_3.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
faces = face_cascade.detectMultiScale(grayImage)

 
if len(faces) == 0:
    print ("No faces found")

else:
    print (faces)
    print (faces.shape)
 
 
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
 
    cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
    cv2.putText(image, "penumpang detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
 
    cv2.imshow('deteksi penumpang',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
