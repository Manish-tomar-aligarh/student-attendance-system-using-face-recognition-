from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("Face Recognition System") 



       #********variables*****
       self.var_dep=StringVar()
       self.var_course=StringVar()
       self.var_year=StringVar()
       self.var_semeseter=StringVar()
       self.var_std_id=StringVar()
       self.var_div=StringVar()
       self.var_roll=StringVar()
       self.var_gender=StringVar()
       self.var_dob=StringVar()
       self.var_email=StringVar()
       self.var_phone=StringVar()
       self.var_address=StringVar()
       self.var_teacher=StringVar()
       self.var_std_name=StringVar()





       img=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images7.jpg")
       img=img.resize((500,130),Image.LANCZOS)
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=500,height=130)
       

       img1=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images8.jpg")
       img1=img1.resize((500,130),Image.LANCZOS)
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root,image=self.photoimg1)
       f_lbl.place(x=500,y=0,width=500,height=130)


       img2=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images12.jpg")
       img2=img2.resize((500,130),Image.LANCZOS)
       self.photoimg2=ImageTk.PhotoImage(img2)

       f_lbl=Label(self.root,image=self.photoimg2)
       f_lbl.place(x=1000,y=0,width=550,height=130)


          #Background image
       img3=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\face.jpg")
       img3=img3.resize((1530,710),Image.LANCZOS)
       self.photoimg3=ImageTk.PhotoImage(img3)

       bg_img=Label(self.root,image=self.photoimg3)
       bg_img.place(x=0,y=130,width=1530,height=710)


       title_lbl=Label(bg_img,text="Student Management System",font=("ALGERIAN",35,"bold"),bg="yellow",fg="black")
       title_lbl.place(x=0,y=0,width=1530,height=45)

       main_frame=Frame(bg_img,bd=2,bg="white")
       main_frame.place(x=20,y=50,width=1480,height=600)

       #left label frame
       Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
       Left_frame.place(x=10,y=10,width=760,height=580)

       img_left=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images19.jpg")
       img_left=img_left.resize((760,130),Image.LANCZOS)
       self.photoimg_left=ImageTk.PhotoImage(img_left)

       f_lbl=Label(Left_frame,image=self.photoimg_left)
       f_lbl.place(x=0,y=0,width=760,height=130)
       #Current course
       Current_Course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
       Current_Course_frame.place(x=5,y=135,width=750,height=150)

       #Department

       dep_label=Label(Current_Course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
       dep_label.grid(row=0,column=0,padx=10)

       dep_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
       dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","Electrical")
       dep_combo.current(0)
       dep_combo.grid(row=0,column=1,padx=2,pady=10)

       #Course
       Course_label=Label(Current_Course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
       Course_label.grid(row=0,column=2,padx=10,sticky=W)

       Course_Combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
       Course_Combo["values"]=("Select Course","FE","SE","TE","BE")
       Course_Combo.current(0)
       Course_Combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

       #year
       year_label=Label(Current_Course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
       year_label.grid(row=1,column=0,padx=10,sticky=W)

       year_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
       year_combo["values"]=("Select Year","2023-24","2024-25","2025--26","2026-27")
       year_combo.current(0)
       year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

       #Semester

       semester_label=Label(Current_Course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
       semester_label.grid(row=1,column=2,padx=10,sticky=W)

       semester_combo=ttk.Combobox(Current_Course_frame,textvariable=self.var_semeseter,font=("times new roman",12,"bold"),state="readonly",width=20)
       semester_combo["values"]=("Select Semester","Sem:-1","Sem:-2")
       semester_combo.current(0)
       semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


         #Class Student Information
       class_studentframe=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
       class_studentframe.place(x=5,y=290,width=750,height=260)
       

       #student id
       studentid_label=Label(class_studentframe,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
       studentid_label.grid(row=0,column=0,padx=10,sticky=W)

       student_entry=ttk.Entry(class_studentframe,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
       student_entry.grid(row=0,column=1,padx=10,sticky=W)

       #Student name
       studentName_label=Label(class_studentframe,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
       studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

       studentName_entry=ttk.Entry(class_studentframe,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
       studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
      

      #Class Division

       class_div_label=Label(class_studentframe,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
       class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

      


       division_combo=ttk.Combobox(class_studentframe,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=15)
       division_combo["values"]=("A","B","C")
       division_combo.current(0)
       division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)




         #Roll no
       roll_no_label=Label(class_studentframe,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
       roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

       roll_no__entry=ttk.Entry(class_studentframe,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
       roll_no__entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)



         #Gender
       gender_label=Label(class_studentframe,text="Gender",font=("times new roman",12,"bold"),bg="white")
       gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

       gender_combo=ttk.Combobox(class_studentframe,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=15)
       gender_combo["values"]=("Male","Female","other")
       gender_combo.current(0)
       gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)




         #DOB
       dob_label=Label(class_studentframe,text="DOB:",font=("times new roman",12,"bold"),bg="white")
       dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

       dob_entry=ttk.Entry(class_studentframe,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
       dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


         #Email
       Email_label=Label(class_studentframe,text="Email:",font=("times new roman",12,"bold"),bg="white")
       Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

       Email_entry=ttk.Entry(class_studentframe,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
       Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)




         #phone no
       phone_label=Label(class_studentframe,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
       phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

       phone_entry=ttk.Entry(class_studentframe,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
       phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)



         #Address
       address_label=Label(class_studentframe,text="Address:",font=("times new roman",12,"bold"),bg="white")
       address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

       address_entry=ttk.Entry(class_studentframe,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
       address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)




         #Teacher name
       teacher_label=Label(class_studentframe,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
       teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

       teacher_entry=ttk.Entry(class_studentframe,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
       teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


       #radio buttons1

       self.var_radio1=StringVar()
       radiobt1=ttk.Radiobutton(class_studentframe,variable=self.var_radio1,text="Take a Photo Sample",value="yes")
       radiobt1.grid(row=6,column=0)

          #radio buttons2

       self.var_radio2=StringVar()
       radiobt2=ttk.Radiobutton(class_studentframe,variable=self.var_radio1,text="No Photo Sample",value="no")
       radiobt2.grid(row=6,column=1)

       #button frame
       btn_frame=Frame(class_studentframe,bd=2,relief=RIDGE,bg="white")
       btn_frame.place(x=0,y=200,width=745,height=45)

       save_btn=Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
       save_btn.grid(row=0,column=0)

       
       update_btn=Button(btn_frame,text="Update",command=self.update_data,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
       update_btn.grid(row=0,column=1)

       
       delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
       delete_btn.grid(row=0,column=2)

       
       reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
       reset_btn.grid(row=0,column=3)


       
       take_phot_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
       take_phot_btn.grid(row=0,column=4)

       
       update_btn=Button(btn_frame,text="Update Photo Sample",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
       update_btn.grid(row=0,column=5)

       




         #Right label frame
       Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
       Right_frame.place(x=780,y=10,width=660,height=580)


       img_right=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images17.jpg")
       img_right=img_right.resize((760,130),Image.LANCZOS)
       self.photoimg_right=ImageTk.PhotoImage(img_right)

       f_lbl=Label(Right_frame,image=self.photoimg_right)
       f_lbl.place(x=0,y=0,width=760,height=130)

       #search System

       search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
       search_frame.place(x=3,y=135,width=650,height=70)



       search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
       search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

       search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
       search_combo["values"]=("Select ","Roll_No","Phone_No")
       search_combo.current(0)
       search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

       search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
       search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


       search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
       search_btn.grid(row=0,column=3,padx=4)

       
       showall_btn=Button(search_frame,text="Show All",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
       showall_btn.grid(row=0,column=4,padx=4)

       #tabkle frame
       table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE )
       table_frame.place(x=5,y=210,width=650,height=350)

       scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

       self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command=self.student_table.xview)
       scroll_y.config(command=self.student_table.yview)

       self.student_table.heading("dep",text="Department")
       self.student_table.heading("course",text="Course")
       self.student_table.heading("year",text="Year")
       self.student_table.heading("sem",text="Semester")
       self.student_table.heading("id",text="StudentId")
       self.student_table.heading("name",text="Name")
       self.student_table.heading("div",text="Division")
       self.student_table.heading("roll",text="Roll")
       self.student_table.heading("gender",text="Gender")
       self.student_table.heading("dob",text="DOB")
       self.student_table.heading("email",text="Email")
       self.student_table.heading("phone",text="Phone")
       self.student_table.heading("address",text="Address")
       self.student_table.heading("teacher",text="Teacher")
       self.student_table.heading("photo",text="PhotoSampleStatus")
       self.student_table["show"]="headings"

       self.student_table.column("dep",width=100)
       self.student_table.column("course",width=100)
       self.student_table.column("year",width=100)
       self.student_table.column("sem",width=100)
       self.student_table.column("id",width=100)
       self.student_table.column("name",width=100)
       self.student_table.column("div",width=100)
       self.student_table.column("roll",width=100)
       self.student_table.column("gender",width=100)
       self.student_table.column("dob",width=100)
       self.student_table.column("email",width=100)
       self.student_table.column("phone",width=100)
       self.student_table.column("address",width=100)
       self.student_table.column("teacher",width=100)
       self.student_table.column("photo",width=150)

       self.student_table.pack(fill=BOTH,expand=1)
       self.student_table.bind("<ButtonRelease>",self.get_cursor)
       self.fetch_data()


       #********function declaration***********

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
              try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="manish@902520",database="face_recognizer")
                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semeseter.get(),
                                                                    self.var_std_id.get(),
                                                                    self.var_std_name.get(),
                                                                    self.var_div.get(),
                                                                    self.var_roll.get(),
                                                                    self.var_gender.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_email.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_address.get(),
                                                                    self.var_teacher.get(),
                                                                    self.var_radio1.get()

                                                                ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
              except Exception as es:
                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

                 #*****fetch data*******
    def fetch_data(self): 
      conn=mysql.connector.connect(host="localhost",username="root",password="manish@902520",database="face_recognizer")
      my_cursor=conn.cursor()    
      my_cursor.execute("select * from student")
      data=my_cursor.fetchall()

      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)

        conn.commit()
      conn.close()  



      #*****get cursor*****
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"] 


       self.var_dep.set(data[0]),
       self.var_course.set(data[1]),
       self.var_year.set(data[2]),
       self.var_semeseter.set(data[3]),
       self.var_std_id.set(data[4]),
       self.var_std_name.set(data[5]),
       self.var_div.set(data[6]),
       self.var_roll.set(data[7]),
       self.var_gender.set(data[8]),
       self.var_dob.set(data[9]),
       self.var_email.set(data[10]),
       self.var_phone.set(data[11]),
       self.var_address.set(data[12]),
       self.var_teacher.set(data[13]),
       self.var_radio1.set(data[14])


       #update



    def update_data(self):
     if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=self.root)
     else:
        try:
            update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
            if update>0:
                # Establish MySQL connection
                conn = mysql.connector.connect(host="localhost", username="root", password="manish@902520", database="face_recognizer")
                my_cursor = conn.cursor()
                
                # Execute the update query with the correct syntax
                my_cursor.execute("""
                    UPDATE student 
                    SET Dep=%s, course=%s, Year=%s, semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, 
                        Dob=%s, Email=%s, Phone=%s, Address=%s, teacher=%s, `Photo Sample`=%s 
                    WHERE Student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semeseter.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                
                # Commit the changes and display success message
                
            else:
                if not update:
                    return
            messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()   
                
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




             #delerte function
    def delete_data(self):
     if self.var_std_id.get() == "":
        messagebox.showerror("Error", "Student ID is required to delete a record", parent=self.root)
     else:
        try:
            # Ask for confirmation before deleting
            delete = messagebox.askyesno("Delete", "Are you sure you want to delete this student's record?", parent=self.root)
            if delete>0:
                # Establish MySQL connection
                conn = mysql.connector.connect(host="localhost", username="root", password="manish@902520", database="face_recognizer")
                my_cursor = conn.cursor()
                sql="delete from student where student_id=%s"
                val=(self.var_std_id.get(),)
                my_cursor.execute(sql,val)
            else:
                if not delete:
                   return    
            conn.commit()
            self.fetch_data()
            conn.close() 
            messagebox.showinfo("Success", "Student record has been successfully deleted", parent=self.root)   
                
                
             
            
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



            #reset**********
    def reset_data(self):
    # Reset each field to its default value
     self.var_dep.set("Select Department")
     self.var_course.set("Select Course")
     self.var_year.set("Select Year")
     self.var_semeseter.set("Select Semester")
     self.var_std_name.set("")
     self.var_std_id.set("")
     self.var_div.set("Select Division")
     self.var_roll.set("")
     self.var_gender.set("Male")  # Assuming "Male" is the default value
     self.var_dob.set("")
     self.var_email.set("")
     self.var_phone.set("")
     self.var_address.set("")
     self.var_teacher.set("")
     self.var_radio1.set("")  # Assuming this is for photo sample radio button (e.g., 'Yes' or 'No')





     #*******generate dataset or take a sample ******************

    

    

    def generate_dataset(self):
    # Ensure all fields are filled
     if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All Fields are required", parent=self.root)
     else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="manish@902520", database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from student") 
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                id+=1  

            my_cursor.execute("""
                    UPDATE student 
                    SET Dep=%s, course=%s, Year=%s, semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, 
                        Dob=%s, Email=%s, Phone=%s, Address=%s, teacher=%s, `Photo Sample`=%s 
                    WHERE Student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semeseter.get(),  # Correct spelling to semester
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                    ))     
                

                
               

            conn.commit()
            self.fetch_data()  # Refresh the data display
            self.reset_data()  # Reset the form fields
            conn.close()

            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                      face_cropped= img[y:y+h, x:x+w]
                      return face_cropped
                    
            cap = cv2.VideoCapture(0) 
            img_id=0
            while True:
              ret,frame_my=cap.read()
              if face_cropped(frame_my) is not None:
                img_id+=1      
                face=cv2.resize(face_cropped(frame_my),(450,450))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                cv2.imshow("Croped Face",face)

              if cv2.waitKey(1)==13 or int(img_id)==100:
                break  
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets completed!!!")        
              

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Database error occurred: {str(e)}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
       
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()