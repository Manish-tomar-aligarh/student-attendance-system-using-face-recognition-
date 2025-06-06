import cv2
import mysql.connector
from tkinter import Tk

class FaceRecognition:
    def _init_(self, root):
        self.root = root
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        self.clf.read("classifier.xml")
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def get_student_data(self, student_id):
        try:
            conn = mysql.connector.connect(user='your_user', password='your_password',
                                           host='your_host', database='your_database')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Name, Roll, Dep, student_id FROM student WHERE Student_id=%s", (student_id,))
            result = my_cursor.fetchone()
            conn.close()
            if result:
                return {"Name": result[0], "Roll": result[1], "Dep": result[2], "ID": result[3]}
            else:
                return {"Name": "Unknown", "Roll": "Unknown", "Dep": "Unknown", "ID": "Unknown"}
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
            return {"Name": "Unknown", "Roll": "Unknown", "Dep": "Unknown", "ID": "Unknown"}

    def mark_attendance(self, i, r, n, d):
        # Your attendance marking code here
        pass

    def draw_boundary(self, img, scaleFactor=1.1, minNeighbors=10):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray_img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
        for (x, y, w, h) in faces:
            id, confidence = self.clf.predict(gray_img[y:y+h, x:x+w])
            if confidence < 77:  # Adjust this threshold as necessary
                student_data = self.get_student_data(id)
                cv2.putText(img, f"ID: {student_data['ID']}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Roll: {student_data['Roll']}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name: {student_data['Name']}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Dep: {student_data['Dep']}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                self.mark_attendance(student_data['ID'], student_data['Roll'], student_data['Name'], student_data['Dep'])
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

    def recognize(self, img):
        self.draw_boundary(img)
        return img

if __name__ == "_main_":
    root = Tk()
    app = FaceRecognition(root)
    
    video_cap = cv2.VideoCapture(0)
    while True:
        ret, img = video_cap.read()
        if not ret:
            print("Failed to capture video stream")
            break

        # Process every other frame to improve speed
        img = app.recognize(img)
        cv2.imshow("Welcome to Face Recognition", img)

        if cv2.waitKey(1) == 13:  # Press Enter to exit
            break

    video_cap.release()
    cv2.destroyAllWindows()
    root.mainloop()