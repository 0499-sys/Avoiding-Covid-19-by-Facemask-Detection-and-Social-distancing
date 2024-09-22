from keras.models import load_model
import cv2,os
import numpy as np
import tkinter
#from tkinter import messagebox
import smtplib
#import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import Image as im 
from PIL import Image
import imagehash 

email = 'nnrsproject2019@gmail.com'
password1 = 'nnrs@123'


from pygame import mixer
mixer.init()
sound = mixer.Sound('alarm.wav')

# Initialize tkinter
root = tkinter.Tk()
root.withdraw()

# Load trained DL model
model = load_model('face_mask_detection.h5')

# Classifier to detect face
face_det_classifier = cv2.CascadeClassifier('F:\Academics MSU\SEM 8\Project\haarcascade\haarcascade_frontalface_default.xml')

# Capture Video
vid_source = cv2.VideoCapture(0)

# dict containing details of wearing mask and colour of the rectangle
text_dict = {0:'Mask' , 1:'No Mask'}
rect_color_dict = {0:(0,255,0) , 1:(0,0,255)}

SUBJECT = 'Subject'
TEXT = 'Someone without mask is been caught'

flag = 0

while(True):
    ret,img = vid_source.read()
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_det_classifier.detectMultiScale(grayscale_img,1.3,5)
    
    for(x,y,w,h) in faces :
        face_img = grayscale_img[y:y+w , x:x+w]
        resized_img = cv2.resize(face_img,(100,100))
        
        normalized_img = resized_img/255.0
        reshaped_img =  np.reshape(normalized_img, (1,100,100,1))
        result=model.predict(reshaped_img)
        
        label=np.argmax(result,axis=1)[0]
        
        cv2.rectangle(img,(x,y),(x+w,y+h),rect_color_dict[label],2)
        cv2.rectangle(img,(x,y-40),(x+w,y),rect_color_dict[label],-1)
        cv2.putText(img, text_dict[label], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0),2)
        
        if(label==1):
            #sound.play()
            if(flag==0):
                flag=1
                cv2.imwrite("base.jpg",resized_img)
                data_img = open('base.jpg','rb').read()
                #print(data_img)
                #data_img = im.fromarray(img)
                     
                msg = MIMEMultipart()
                msg['Subject'] = 'subject'
                msg['From'] = 'nnrsproject2019@gmail.com'
                From = msg['From']
                msg['To'] = 'nnrsproject2019@gmail.com'
                To = msg['To']
                text = MIMEText("Below person is Wanted....$5,00,000 ka inaaam !!!!!!")
                msg.attach(text)
                #image = MIMEImage(data_img, name=os.path.basename('img.jpg'))
                #print(image)
                #msg.attach(data_img)
            
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(email, password1)
                s.sendmail(From, To, msg.as_string())
                s.quit()
                #messagebox.showwarning("Warning","Access Denied. Please wear Mask")
        
            else:
                cv2.imwrite("compare.jpg",resized_img)
                hash = imagehash.average_hash(Image.open('base.jpg'))
                otherhash = imagehash.average_hash(Image.open('compare.jpg'))
             
                x = hash - otherhash
                
                if(x > 10):
                    flag = 0 
                    
                    #cv2.imwrite("base.jpg",resized_img)
                    data_img = open('base.jpg','rb').read()
                    #print(data_img)
                    #data_img = im.fromarray(img)
                         
                    msg = MIMEMultipart()
                    msg['Subject'] = 'subject'
                    msg['From'] = 'nnrsproject2019@gmail.com'
                    From = msg['From']
                    msg['To'] = 'nnrsproject2019@gmail.com'
                    To = msg['To']
                    text = MIMEText("Below person is Wanted....$5,00,000 ka inaaam !!!!!!")
                    msg.attach(text)
                    #image = MIMEImage(data_img, name=os.path.basename('img.jpg'))
                    #print(image)
                    #msg.attach(data_img)
                
                    s = smtplib.SMTP("smtp.gmail.com", 587)
                    s.ehlo()
                    s.starttls()
                    s.ehlo()
                    s.login(email, password1)
                    s.sendmail(From, To, msg.as_string())
                    s.quit()
                    #messagebox.showwarning("Warning","Access Denied. Please wear Mask")
        else:
             sound.stop()   
             pass
             break
    
    cv2.imshow('Live',img)
    key=cv2.waitKey(1)
    
    if(key==27):
        break
    
cv2.destroyAllWindows()
vid_source.release()
