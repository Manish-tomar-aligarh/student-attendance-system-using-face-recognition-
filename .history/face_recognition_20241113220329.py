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
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
            """Detect faces, identify students, and draw boundaries."""
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                student_id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                if confidence > 75:  # Adjust confidence threshold
                    name, roll, department, student_id = self.get_student_data(student_id)
                    self.display_student_info(img, x, y, name, roll, department, student_id)
                    self.mark_attendance(student_id, roll, name, department)
                else:
                    cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

        def recognize(img, clf, faceCascade):
            """Recognize face from live video feed."""
            return draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), clf)

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            frame = recognize(frame, clf, faceCascade)
            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def display_student_info(self, img, x, y, name, roll, department, student_id):
        """Display student information on the screen."""
        cv2.putText(img, f"ID: {student_id}", (x, y - 70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(img, f"Roll: {roll}", (x, y - 45), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(img, f"Name: {name}", (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(img, f"Dep: {department}", (x, y + 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
