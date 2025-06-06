from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 


class register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register")

        #*****variables********
        self.var_firstnm=StringVar()
        self.var_lastnm=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securtityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        # background image
        imge = Image.open(
            r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\moon-lake-mountains-cold-night-nature-scenery-wallpaper-preview.jpg")
        imge = imge.resize((1530, 710), Image.LANCZOS)
        self.photoimge = ImageTk.PhotoImage(imge)

        bg_img2 = Label(self.root, image=self.photoimge)
        bg_img2.place(x=0, y=-50, width=1530, height=850)

        # left image
        imge1 = Image.open(
            r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\360_F_550617518_Eu3U6kTl3mODPvnfTMFHQ88z1y5KNfNQ.jpg")
        imge1 = imge1.resize((470, 550), Image.LANCZOS)
        self.photoimge1 = ImageTk.PhotoImage(imge1)

        bg_img1 = Label(self.root, image=self.photoimge1)
        bg_img1.place(x=50, y=100, width=470, height=550)

        # Main frame for the form
        main_frame = Frame(self.root, bg="white")
        main_frame.place(x=520, y=100, width=800, height=550)

        # Register label
        get_str1 = Label(main_frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="dark green", bg="white")
        get_str1.place(x=20, y=20)

        # First Name Label
        first_name_label = Label(main_frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white")
        first_name_label.place(x=50, y=100)

        # Entry widget for First Name
        frame_entry = ttk.Entry(main_frame,textvariable=self.var_firstnm, font=("times new roman", 15))
        frame_entry.place(x=50, y=130, width=250)

        #Last Name
        first_name_label = Label(main_frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white")
        first_name_label.place(x=370, y=100)

        # Entry widget for First Name
        frame_entry = ttk.Entry(main_frame,textvariable=self.var_lastnm, font=("times new roman", 15))
        frame_entry.place(x=370, y=130, width=250)
          
           
        #Contact No.
        first_name_label = Label(main_frame, text="Contact No.", font=(
            "times new roman", 15, "bold"), bg="white")
        first_name_label.place(x=50, y=170)

        # Entry widget for First Name
        frame_entry = ttk.Entry(main_frame,textvariable=self.var_contact, font=("times new roman", 15))
        frame_entry.place(x=50, y=200, width=250)

         #Email
        first_name_label = Label(main_frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white")
        first_name_label.place(x=370, y=170)

        # Entry widget for First Name
        frame_entry = ttk.Entry(main_frame,textvariable=self.var_email, font=("times new roman", 15))
        frame_entry.place(x=370, y=200, width=250)

        #Select Security Question
        first_name_label = Label(main_frame, text="Select Security Questions", font=(
            "times new roman", 15, "bold"), bg="white")
        first_name_label.place(x=50, y=240)

        self.combo_security_q=ttk.Combobox(main_frame,textvariable=self.var_securityQ,font=(
            "times new roman", 15, "bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your Date Of Birth","Your Best Friend Name","Your Favourite Song")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)


        #Security Answer
        first_name_label = Label(main_frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white")
        first_name_label.place(x=370, y=240)

        # Entry widget for First Name
        frame_entry = ttk.Entry(main_frame,textvariable=self.var_securtityA, font=("times new roman", 15))
        frame_entry.place(x=370, y=270, width=250)

        #Password
        first_name_label = Label(main_frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white")
        first_name_label.place(x=50, y=310)

        # Entry widget for First Name
        frame_entry = ttk.Entry(main_frame,textvariable=self.var_pass, font=("times new roman", 15))
        frame_entry.place(x=50, y=340, width=250)

        #Confirm PAssword

        first_name_label = Label(main_frame, text="Confirm password", font=(
            "times new roman", 15, "bold"), bg="white")
        first_name_label.place(x=370, y=310)

        # Entry widget for First Name
        frame_entry = ttk.Entry(main_frame,textvariable=self.var_confpass, font=("times new roman", 15))
        frame_entry.place(x=370, y=340, width=250)


        #***************checkButton*********
        self.var_check=IntVar()
        check_button=Checkbutton(main_frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=(
            "times new roman", 12, "bold"),onvalue=1,offvalue=0)
        check_button.place(x=50,y=380)

        #************Buttons***************

        img=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images (4).jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(main_frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)
          
        img2=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images (5).jpg")
        img2=img2.resize((200,50),Image.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(img2)
        b1=Button(main_frame,image=self.photoimage7,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)


        #****function******
    def register_data(self):
        if self.var_firstnm.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password And Confirm Password Must Be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms And Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="manish@902520",database="my_table")
            my_cursor=conn.cursor()
            query=("Select *from register where Email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                 self.var_firstnm.get(),
                 self.var_lastnm.get(),
                 self.var_contact.get(),
                 self.var_email.get(),
                 self.var_securityQ.get(),
                 self.var_securtityA.get(),
                 self.var_pass.get()   
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    




if __name__ == "__main__":
    root = Tk()
    obj = register(root)
    root.mainloop()
