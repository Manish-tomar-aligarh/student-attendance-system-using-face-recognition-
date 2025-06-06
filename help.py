from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class help:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("Face Recognition System")


       title_lbl=Label(self.root,text="Help Desk",font=("ALGERIAN",35,"bold"),bg="yellow",fg="red")
       title_lbl.place(x=0,y=0,width=1530,height=45)



       img_top=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\apple-logo-is-rendered-3d-sits-surface-covered-blue-water-droplets_14117-746054.jpg")
       img_top=img_top.resize((1530,720),Image.LANCZOS)
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl=Label(self.root,image=self.photoimg_top)
       f_lbl.place(x=0,y=50,width=1530,height=720)


       dev_label=Label(f_lbl,text="Email:- manishtomar08082006@gmail.com",font=("times new roman",20,"bold"),bg="red",fg="white")
       dev_label.place(x=500,y=300)






if __name__ == "__main__":
    root=Tk()
    obj=help(root)
    root.mainloop() 