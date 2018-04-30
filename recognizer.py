import cv2
import numpy as np

#create face recognizer object and load the training data into it
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('recognizer/trainer.yml')
#create the face detector using opencv's training data
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
#open webcam
cam = cv2.VideoCapture(0)
#set font
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    #read webcam frames 
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #detect faces
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        #predict what ID is being recognized
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        # update the ID based on the prediction to reflect the name associated with the ID
        if(conf > 50):
            if(Id==1):
                Id="Mike : confidence is " + str(conf)
            elif(Id==2):
                Id="Trump : confidence is " + str(conf)
            elif(Id==3):
                Id="Morgan Freeman: confidence is " + str(conf)
            elif(Id==4):
                Id="Leo: confidence is " + str(conf)
        else:
            Id="I don't know this person : confidence is " + str(conf)
        #write the name of the person in the square surrounding their face
        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, (255,255,255))
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
