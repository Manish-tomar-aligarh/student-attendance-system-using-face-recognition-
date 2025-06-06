from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title
        title_lbl = Label(self.root, text="Train Data Set", font=("ALGERIAN", 35, "bold"), bg="yellow", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\train data4.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1530, height=325)

        # Train Button
        b1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                    font=("times new roman", 25, "bold"), bg="black", fg="white")
        b1.place(x=0, y=380, width=1530, height=60)

        # Bottom Image
        img_bottom = Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images12.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        # Path to the dataset
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:  # Iterating over 'path'
            try:
                img = Image.open(image).convert('L')  # Open image in grayscale
                imageNp = np.array(img, 'uint8')  # Convert to NumPy array

                filename = os.path.basename(image)  # Extract file name
                parts = filename.split('.')  # Split by '.'

                # Validate file format and extract ID
                if len(parts) >= 3 and parts[-2].isdigit():  # Check valid ID
                    id = int(parts[-2])
                else:
                    print(f"Skipping file with invalid format: {filename}")
                    continue

                faces.append(imageNp)
                ids.append(id)

                cv2.imshow("Training", imageNp)  # Display image
                cv2.waitKey(1) == 13  # Wait for key press

            except Exception as e:
                print(f"Error processing file {image}: {e}")

        ids = np.array(ids)  # Convert 'ids' to NumPy array

        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
