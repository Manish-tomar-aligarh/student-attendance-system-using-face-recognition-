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

        # Load and resize images
        self.photoimg_top = ImageTk.PhotoImage(Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\apple-logo.jpg").resize((650, 700), Image.LANCZOS))
        self.photoimg_bottom = ImageTk.PhotoImage(Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Face Recognition.jpg").resize((950, 700), Image.LANCZOS))

        # Display images
        Label(self.root, image=self.photoimg_top).place(x=0, y=50, width=650, height=700)
        Label(self.root, image=self.photoimg_bottom).place(x=650, y=55, width=950, height=700)

        # Button for face recognition
        Button(self.root, text="Face Recognition", cursor="hand2", font=("times new roman", 23, "bold"), 
               bg="yellow", fg="red", command=self.face_recog).place(x=810, y=620, width=600, height=40)

    def mark_attendance(self, student_id, roll, name, department):
        """Mark attendance in a CSV file for unique student entries."""
        file_path = "Manish.csv"
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        with open(file_path, "r") as f:
            records = f.readlines()

        if not any(student_id in record for record in records):
            with open(file_path, "a", newline="\n") as f:
                f.write(f"\n{student_id},{roll},{name},{department},{time},{date},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
            """Detect faces, identify students, and draw boundaries."""
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Fetch details from database
                student_data = self.get_student_data(id) if confidence > 77 else None
                if student_data:
                    name, roll, department, student_id = student_data
                    self.display_student_info(img, x, y, name, roll, department, student_id)
                    self.mark_attendance(student_id, roll, name, department)
                else:
                    cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
            return img

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

    def get_student_data(self, student_id):
        """Fetch student data from the database."""
        conn = mysql.connector.connect(host="localhost", username="root", password="manish@902520", database="face_recognizer")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT Name, Roll, Dep, Student_id FROM student WHERE Student_id=%s", (student_id,))
            result = cursor.fetchone()
            return result if result else None
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()

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
