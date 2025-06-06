from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
import tkinter
from student1 import Student
import os 
from train import Train
from face_recognition import FaceRecognition
from attendance import attendance
from Developer import developer
from help import help
import os
os.path.join(os.path.dirname(os.__file__), 'Scripts')



class Face_Recognition_System:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("Face Recognition System") 
      
       img=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images5.jpg")
       img=img.resize((500,130),Image.LANCZOS)
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=500,height=130)
       

       img1=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images 2.jpg")
       img1=img1.resize((500,130),Image.LANCZOS)
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root,image=self.photoimg1)
       f_lbl.place(x=500,y=0,width=500,height=130)


       img2=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images5.jpg")
       img2=img2.resize((500,130),Image.LANCZOS)
       self.photoimg2=ImageTk.PhotoImage(img2)

       f_lbl=Label(self.root,image=self.photoimg2)
       f_lbl.place(x=1000,y=0,width=550,height=130)

       #Background image
       img3=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\face.jpg")
       img3=img3.resize((1530,710),Image.LANCZOS)
       self.photoimg3=ImageTk.PhotoImage(img3)

       bg_img=Label(self.root,image=self.photoimg3)
       bg_img.place(x=0,y=130,width=1530,height=710)




       title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("ALGERIAN",35,"bold"),bg="white",fg="dark red")
       title_lbl.place(x=0,y=0,width=1530,height=45)

       #************time********************
              #************time********************
       def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

       # Create the lbl widget once, outside of the time() function
       lbl = Label(title_lbl, font=("times new roman", 14, "bold"), background="white", foreground="blue")
       lbl.place(x=0, y=0, width=110, height=50)

       # Call the time function to start the clock
       time()


       
       #student button
       img4=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\Student detail.jpg")
       img4=img4.resize((220,220),Image.LANCZOS)
       self.photoimg4=ImageTk.PhotoImage(img4)

       b=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
       b.place(x=100,y=80,width=220,height=220)

       b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=100,y=280,width=220,height=40)


       #detect face
       img6=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\face recognition.jpg")
       img6=img6.resize((220,220),Image.LANCZOS)
       self.photoimg6=ImageTk.PhotoImage(img6)

       b=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
       b.place(x=400,y=80,width=220,height=220)

       b1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=400,y=280,width=220,height=40)


       #attendance1 
       img7=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\attendance.jpg")
       img7=img7.resize((220,220),Image.LANCZOS)
       self.photoimg7=ImageTk.PhotoImage(img7)

       b=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
       b.place(x=700,y=80,width=220,height=220)

       b1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=700,y=280,width=220,height=40)


       
       #aHelp 
       img8=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images4.jpg")
       img8=img8.resize((220,220),Image.LANCZOS)
       self.photoimg8=ImageTk.PhotoImage(img8)

       b=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
       b.place(x=1000,y=80,width=220,height=220)

       b1=Button(bg_img,text="Help",cursor="hand2",command=self.help_data,font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=1000,y=280,width=220,height=40)


        #Train data
       img9=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\train data.jpg")
       img9=img9.resize((220,220),Image.LANCZOS)
       self.photoimg9=ImageTk.PhotoImage(img9)

       b=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
       b.place(x=100,y=400,width=220,height=220)

       b1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=100,y=600,width=220,height=40)


        #Photos
       img10=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\photos.jpg")
       img10=img10.resize((220,220),Image.LANCZOS)
       self.photoimg10=ImageTk.PhotoImage(img10)

       b=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
       b.place(x=400,y=400,width=220,height=220)

       b1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=400,y=600,width=220,height=40)



        #Developer
       img11=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\IMG-20230426-WA0000.jpg")
       img11=img11.resize((220,220),Image.LANCZOS)
       self.photoimg11=ImageTk.PhotoImage(img11)

       b=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.dev_data)
       b.place(x=700,y=400,width=220,height=220)

       b1=Button(bg_img,text="Developer",cursor="hand2",command=self.dev_data,font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=700,y=600,width=220,height=40)



       
        #Exit
       img12=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\exit.png")
       img12=img12.resize((220,220),Image.LANCZOS)
       self.photoimg12=ImageTk.PhotoImage(img12)

       b=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
       b.place(x=1000,y=400,width=220,height=220)

       b1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=1000,y=600,width=220,height=40)

    def open_img(self):
        os.startfile("Data")


    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
       if self.iExit >0:
          self.root.destroy()
       else:
          return


       #**********Function button****************

    def student_details(self):
    # Add the functionality you want here
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)
 

    def train_data(self):
    # Add the functionality you want here
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)


       
    def face_data(self):
    # Add the functionality you want here
       self.new_window=Toplevel(self.root)
       self.app=FaceRecognition(self.new_window)

   
    def attendance_data(self):
    # Add the functionality you want here
       self.new_window=Toplevel(self.root)
       self.app=attendance(self.new_window)

    def dev_data(self):
    # Add the functionality you want here
       self.new_window=Toplevel(self.root)
       self.app=developer(self.new_window)


    def help_data(self):
    # Add the functionality you want here
       self.new_window=Toplevel(self.root)
       self.app=help(self.new_window) 
       
 
        
 
        





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()