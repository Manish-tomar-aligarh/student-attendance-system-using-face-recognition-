from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("ALGERIAN", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\apple-logo-is-rendered-3d-sits-surface-covered-blue-water-droplets_14117-746054.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=50, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\Face Recognition.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
        f_lbl_bottom.place(x=650, y=55, width=950, height=700)

        # Button for face recognition
        b1 = Button(f_lbl_bottom, text="Face Recognition", cursor="hand2", font=("times new roman", 23, "bold"), bg="yellow", fg="red", command=self.face_recog)
        b1.place(x=160, y=620, width=600, height=40)


        #*****************Attendance***************
    

     

    def mark_attendance(self, i, r, n, d):
    # Open the file in read mode to check existing records
     with open("Manish.csv", "r") as f:
        myDataList = f.readlines()
        name_list = []
        for line in myDataList:
            entry = line.strip().split(",")
            name_list.append(entry[0])  # Assuming the first entry is the unique identifier like 'i'

    # Condition to check if the record already exists
     if i not in name_list:
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")

        # Open the file in append mode to add new record
        with open("Manish.csv", "a", newline="\n") as f:
            f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")






    # Face recognition function
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord=[]

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="manish@902520", database="face_recognizer")
                my_cursor = conn.cursor()


                try:
                    my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (id,))
                    p = my_cursor.fetchone()
                    p = "+".join(p)

                    my_cursor.execute("SELECT Roll FROM student WHERE Student_id=%s", (id,))
                    r = my_cursor.fetchone()
                    r = "+".join(r)

                    my_cursor.execute("SELECT Dep FROM student WHERE Student_id=%s", (id,))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    
                   


                    if confidence > 77:  # Adjust this value
                        cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(i,r,n,d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord=[x,y,w,y]  
                    return coord      

                except mysql.connector.Error as e:
                    print(f"Error fetching data: {e}")

                finally:
                    my_cursor.close()
                    conn.close()

        def recognize(img, clf, faceCascade):

            coord =draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
