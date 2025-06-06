from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import  numpy as np


class train:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("Face Recognition System")




       title_lbl=Label(self.root,text="Train Data Set",font=("ALGERIAN",35,"bold"),bg="yellow",fg="black")
       title_lbl.place(x=0,y=0,width=1530,height=45)



       img_top=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\train data4.jpg")
       img_top=img_top.resize((1530,325),Image.LANCZOS)
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl=Label(self.root,image=self.photoimg_top)
       f_lbl.place(x=0,y=50,width=1530,height=325)

       
       #button

       b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="black",fg="white")
       b1.place(x=0,y=380,width=1530,height=60)



       img_bottom=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images12.jpg")
       img_bottom=img_bottom.resize((1530,325),Image.LANCZOS)
       self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)


       f_lbl=Label(self.root,image=self.photoimg_bottom)
       f_lbl.place(x=0,y=440,width=1530,height=325)

    import os

    def train_classifier(self):
    # Path to the dataset
     data_path = "data/"
    
    try:
        images = [os.path.join(data_path, f) for f in os.listdir(data_path) if f.endswith(".jpg")]
        
        for image in images:
            try:
                # Split the filename to get the ID
                parts = os.path.split(image)[1].split('.')
                
                if len(parts) >= 3 and parts[1].isdigit():
                    id = int(parts[1])
                else:
                    print(f"Skipping file {image} due to incorrect format.")
                    continue
                
                # Process the image here (your existing code)
                
            except ValueError as e:
                print(f"Error processing file {image}: {e}")
        
        # Rest of your training code...

    except Exception as e:
        print(f"An error occurred: {e}")





       

 

 






           
if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()