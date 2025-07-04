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

        # Top image
        img_top = Image.open(r"C:\path\to\your\image1.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=50, width=650, height=700)

        # Bottom image
        img_bottom = Image.open(r"C:\path\to\your\image2.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
        f_lbl_bottom.place(x=650, y=55, width=950, height=700)

        # Button for face recognition
        b1 = Button(f_lbl_bottom, text="Face Recognition", cursor="hand2", font=("times new roman", 23, "bold"), bg="yellow", fg="red", command=self.face_recog)
        b1.place(x=160, y=620, width=600, height=40)

    def mark_attendance(self, i, r, n, d):
        with open("Manish.csv", "r") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]

        if i not in name_list:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            with open("Manish.csv", "a", newline="\n") as f:
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, clf, min_confidence=78):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=8, minSize=(80, 80))

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Database connection
                conn = mysql.connector.connect(host="localhost", username="root", password="yourpassword", database="face_recognizer")
                my_cursor = conn.cursor()
                try:
                    my_cursor.execute("SELECT Name, Roll, Dep, Student_id FROM student WHERE Student_id=%s", (id,))
                    record = my_cursor.fetchone()
                    if record and confidence > min_confidence:
                        n, r, d, i = record
                        # Displaying user details on screen
                        cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                        cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                        cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                        self.mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                except mysql.connector.Error as e:
                    print(f"Database Error: {e}")
                finally:
                    my_cursor.close()
                    conn.close()

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, clf)
            return img

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture video.")
                break
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
