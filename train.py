from retinaface import RetinaFace
from os.path import exists
from tkinter import*
import face_recognition
import pymsgbox
import cv2
import face_recognition
import pickle
import pandas as pd
import os
import numpy as np





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




folder_path="dataset"
mode_path_list=os.listdir(folder_path)
img_List=[]
student_Id=[]
for path in mode_path_list:
            
    img_List.append(("dataset/"+path))
    #img_List.append(cv2.imread(os.path.join(folder_path,path)))        
    student_Id.append(os.path.splitext(path)[0])
            

print("Encoding Started...")

encode_list_known=findEncodings(img_List)

encode_list_known_with_Id=[encode_list_known,student_Id]
        
print("Encoding Complete")
        
file=open("data/EncodeFile.p","wb")
pickle.dump(encode_list_known_with_Id,file)
file.close()
print("File Saved")
        
pymsgbox.alert("All Faces Encoded Successfully")

'''
imag="dataset/111111111.jpg"
f = cv2.imread(imag)
     
# convert to numpy array
imager = np.asarray(bytearray(f))
print(imager)
# RGB to Grayscale
imager = cv2.imdecode(imager, 0)
      
# display image
cv2.imshow("output", imager)
'''
