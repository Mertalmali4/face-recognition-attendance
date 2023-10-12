from tkinter import *
import os
from PIL import ImageTk, Image
import datetime

x = datetime.datetime.now()

xl_name=("start "+"ExcelData/"+str(x.day)+"_"+str(x.month)+"_"+str(x.year)+".xlsx")

root=Tk()

root.configure(background="white")

def function1():
    
    os.system("python add_face.py")
    
def function2():
    
    os.system("python new_face_recognition_project.py")

def function3():

    os.system("python train.py")

def function4():

    os.system(xl_name)

root.iconbitmap("logo-renksiz.ico")


root.title("Face Recognition Attendance System")


Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Add New Face",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


Button(root,text="Recognize",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Train Dataset",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Excel Document",font=('times new roman',20),bg="#0D47A1",fg="white",command=function4).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="AI2X",font=("times new roman",20),fg="black",bg="white",height=2).grid(row=7,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

mainloop()