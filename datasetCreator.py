import numpy as np
import cv2
#create haar cascade classifier
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#start webcam
cap = cv2.VideoCapture(0)
#ask user for the id of the face it wants to store in dataset
id = raw_input('enter user id: ')
samplenum = 0
while(True):
	#capture webcam image
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect faces in the image
    faces = detector.detectMultiScale(gray, 1.3, 5)
    #store the faces in the dataset and include the user id in the filepath
    if(len(faces)!=0):
        for (x,y,w,h) in faces:
            samplenum = samplenum + 1
            cv2.imwrite("dataSet/User."+str(id)+"."+str(samplenum)+".jpg",gray[y:y+h,x:x+w])
            #draw a rectangle around the detected face
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.waitKey(100)
    cv2.imshow('face',img)
    cv2.waitKey(1)
    #we take 301 sample images
    if(samplenum > 300) :
        break   
cap.release()
cv2.destroyAllWindows()
