from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class developer:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("Face Recognition System") 



       title_lbl=Label(self.root,text="Developer",font=("ALGERIAN",35,"bold"),bg="yellow",fg="red")
       title_lbl.place(x=0,y=0,width=1530,height=45)



       img_top=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\apple-logo-is-rendered-3d-sits-surface-covered-blue-water-droplets_14117-746054.jpg")
       img_top=img_top.resize((1530,720),Image.LANCZOS)
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl=Label(self.root,image=self.photoimg_top)
       f_lbl.place(x=0,y=50,width=1530,height=720)

        #frame
       main_frame=Frame( f_lbl,bd=2,bg="white")
       main_frame.place(x=1000,y=0,width=500,height=600)

       img_top1=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\IMG-20230426-WA0000.jpg")
       img_top1=img_top1.resize((200,200),Image.LANCZOS)
       self.photoimg_top1=ImageTk.PhotoImage(img_top1)

       f_lbl=Label(main_frame,image=self.photoimg_top1,bg="red")
       f_lbl.place(x=300,y=0,width=200,height=200)

        #Developer info
       dev_label=Label(main_frame,text="Hello My Name is:- Manish Tomar",font=("times new roman",14,"bold"),bg="white")
       dev_label.place(x=0,y=5)

       dev_label=Label(main_frame,text="Roll No:- 2301090100072",font=("times new roman",14,"bold"),bg="white")
       dev_label.place(x=0,y=40)

       dev_label=Label(main_frame,text="B.tech CS 2nd year student",font=("times new roman",14,"bold"),bg="white")
       dev_label.place(x=0,y=75)

       dev_label=Label(main_frame,text="Section :- A",font=("times new roman",14,"bold"),bg="white")
       dev_label.place(x=0,y=110)

       dev_label=Label(main_frame,text="Teacher Name :- Richa Upraity",font=("times new roman",14,"bold"),bg="white")
       dev_label.place(x=0,y=145)


       img_top2=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\apple-logo-is-rendered-3d-sits-surface-covered-blue-water-droplets_14117-746054.jpg")
       img_top2=img_top2.resize((500,400),Image.LANCZOS)
       self.photoimg_top2=ImageTk.PhotoImage(img_top2)

       f_lbl=Label(main_frame,image=self.photoimg_top2)
       f_lbl.place(x=0,y=210,width=500,height=400)

       






if __name__ == "__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()