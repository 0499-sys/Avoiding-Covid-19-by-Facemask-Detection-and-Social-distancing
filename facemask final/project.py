from keras.models import load_model
import cv2
import numpy as np
import tkinter
from tkinter import messagebox
#import smtplib


from pygame import mixer
mixer.init()
sound = mixer.Sound('beep-01a.wav')

# Initialize tkinter
root = tkinter.Tk()
root.withdraw()


model = load_model('model-080.model')

face_clsfr=cv2.CascadeClassifier('F:\Academics MSU\SEM 8\Project\haarcascade\haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)


labels_dict={0:'MASK',1:'NO MASK'}
color_dict={0:(0,255,0),1:(0,0,255)}
  

while(True):

    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_clsfr.detectMultiScale(gray,1.3,5)  

    for (x,y,w,h) in faces:
    
        face_img=gray[y:y+w,x:x+w]
        resized=cv2.resize(face_img,(100,100))
        normalized=resized/255.0
        reshaped=np.reshape(normalized,(1,100,100,1))
        result=model.predict(reshaped)

        label=np.argmax(result,axis=1)[0]
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),color_dict[label],4)
        cv2.rectangle(frame,(x,y-40),(x+w,y),color_dict[label],4)
        cv2.putText(frame, labels_dict[label], (x, y-10),cv2.FONT_ITALIC, 1,(255,255,255),4)
        
        if(labels_dict[label] =='MASK'):
            #sound.stop()
            print("No Beep")
           
        elif(labels_dict[label] =='NO MASK'):    
            #sound.play()
            #messagebox.showwarning("Warning","Access Denied. Please wear Mask")
            print("Beep") 
        
    cv2.imshow('Mask Detection App',frame)
    key=cv2.waitKey(1)
    
    if(key==27):
        break
cap.release()
cv2.destroyAllWindows()