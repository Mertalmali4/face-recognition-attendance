from retinaface import RetinaFace
from os.path import exists
from tkinter import*
import face_recognition
from functools import partial
import pymsgbox
import cv2
import face_recognition
import pickle
import pandas as pd
import os
import numpy as np

#window
tkWindow = Tk()  
tkWindow.geometry('300x350')  
tkWindow.title('Face Recognition Add Face')
tkWindow.iconbitmap("logo-renksiz.ico")
encode_list1=[]
def findEncodings(imagesList):
    encode_list1=[]
    for img in imagesList:
        resp = RetinaFace.detect_faces(img, threshold = 0.3)
        
            
        if 1==len(resp):
            for key in resp:
                identity = resp[key]
                facial_area=identity["facial_area"]
                #facial_area_location.append(((facial_area[3],facial_area[0]), (facial_area[1],facial_area[2])))
                
                
                image = cv2.imread(img)
                crop_img = image[facial_area[1]: facial_area[3], facial_area[0]: facial_area[2]]
                
                
                encode=face_recognition.face_encodings(crop_img)[0]
                encode_list1.append(encode)


    return encode_list1

#username label and text entry box
usernameLabel = Label(tkWindow, text="Please Enter Your\n School Number",font=15).place(x=70,y=70)
username=StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=100,y=130)

#password label and password entry box
encode_list=[]
encode_list_known=[]
def function1():
    user=username.get()
    if len(user)==9:
        tkWindow.destroy()
        pymsgbox.alert("Please Look The Camera And Press Ok Button")
        vid_cap=cv2.VideoCapture(0)
        ret, frame =vid_cap.read()
        resp = RetinaFace.detect_faces(frame, threshold = 0.3)
        
            
        if 1==len(resp):
            cv2.imshow("mert",frame)
            cv2.imwrite("dataset/" + str(user)+".jpg",frame)
            pymsgbox.alert("Your Face Added Successfully")
        else:
            pymsgbox.alert("No Face Found in the Photo")
            return 1;   

        
        
    else:
        pymsgbox.alert("Please Enter Again")


log=Button(tkWindow, text="ADD",command=function1).place(x=135,y=165,width=50,height=30)



mainloop()












