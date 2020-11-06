import numpy as np
import cv2
import time


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera tidak dapat diakses")
    exit()
    
exitt = False
while (exitt == False):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'Face Detection',(15, 50),font, 1,(0, 255, 255), 2)

    if len(faces) == 0:
        teks = "Wajah Terdeteksi = " + "0"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, teks, (10, 470), font, 1, (0, 255, 255), 2)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]


        teks = "Wajah Terdeteksi = " + str(len(faces))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, teks, (10, 470), font, 1, (0, 255, 255), 2)

      
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       exitt = True
       break

cap.release()
cv2.destroyAllWindows()


 
