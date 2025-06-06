from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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
        data_path = "data/"
        images, labels = [], []

        try:
            # Retrieve all image paths
            image_paths = [os.path.join(data_path, f) for f in os.listdir(data_path) if f.endswith(".jpg")]

            for image_path in image_paths:
                try:
                    # Extract ID from filename assuming format like `user.<name>.<id>.jpg`
                    parts = os.path.split(image_path)[1].split('.')
                    if len(parts) >= 3 and parts[2].isdigit():  # Adjust to use parts[2] for the ID
                        id = int(parts[2])
                    else:
                        print(f"Skipping file {image_path} due to incorrect format.")
                        continue

                    # Read and convert image to grayscale
                    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    if img is None:
                        print(f"Image {image_path} could not be read.")
                        continue

                    # Append the processed data to the lists
                    images.append(img)
                    labels.append(id)

                except ValueError as e:
                    print(f"Error processing file {image_path}: {e}")

            # If no images are loaded, display an error message
            if not images:
                messagebox.showerror("Error", "No valid images found in the dataset.")
                return

            # Train the recognizer model
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.train(images, np.array(labels))

            # Save the trained model
            model_path = "classifier.xml"
            recognizer.write(model_path)
            messagebox.showinfo("Result", "Training completed successfully and model saved.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
