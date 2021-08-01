import cv2

n=0
m=0
face_mask = cv2.CascadeClassifier('jari.xml')
#face_mask = cv2.CascadeClassifier('buritan.xml')
#face_mask1 = cv2.CascadeClassifier('buritan.xml')
#img1 = cv2.imread('test5.jpeg')
#img = cv2.resize(img1,(240,300))
#cap = cv2.VideoCapture('test1.mp4')
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.0.12:8080/video')

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX
 
    cv2.rectangle(img,(100,100),(200,140),(255,0,0),2)
    cv2.putText(img, 'Lampu',(100,100-14), font,1.5,(128,127,255),3)
    a=0
    n=0
    m=0
    o=0
    face = face_mask.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
        a=a+1
        n=1
        m=x
        o=y
#        cv2.putText(img, 'Haluan',(x,y-14), font,1.5,(255,0,255),3)

 #   face1 = face_mask1.detectMultiScale(gray,1.1,4)
 #   for(x,y,w,h) in face1:
 #       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 #       cv2.putText(img, 'Buritan',(x,y-14), font,1,(255,0,0),3)

        #print('x=',x)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color=img[y:y+h, x:x+w]
        #cv2.putText(img, 'Using Mask',(55,280), font,0.5,(255,0,0))
    #cv2.putText(img, 'Without Mask',(20,200), font,0.5,(255,255,255))
    #if n==0:
    font = cv2.FONT_HERSHEY_SIMPLEX
    print(a)
    if o > 90 and o < 120:
        if m > 100 and m < 170:
             cv2.putText(img, 'On',(105,100+30), font,1,(255,255,255),2) 
    else:
         cv2.putText(img, 'Off',(105,100+30), font,1.2,(255,255,0),2) 
        

#        cv2.putText(img, 'Kapal detected',(40,30), font,2.5,(0,255,255),10)

    cv2.imshow('test',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    #print('n=',n)
    #print('m=',m)
    #cv2.waitKey()
cap.release()
cv2.destroyAllWindows()

