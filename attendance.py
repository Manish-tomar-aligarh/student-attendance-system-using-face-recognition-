from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog






mydata=[]
class attendance:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("Face Recognition System") 


       #***********Varialbles**************
       self.var_atten_id=StringVar()
       self.var_atten_roll=StringVar()
       self.var_atten_name=StringVar()
       self.var_atten_dep=StringVar()
       self.var_atten_time=StringVar()
       self.var_atten_date=StringVar()
       self.var_atten_attendance=StringVar()

       img=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\chatbot.jpg")
       img=img.resize((800,200),Image.LANCZOS)
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=800,height=200)
       

       img1=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images23.jpg")
       img1=img1.resize((800,200),Image.LANCZOS)
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root,image=self.photoimg1)
       f_lbl.place(x=800,y=0,width=800,height=200)

       #Background image
       img3=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\face.jpg")
       img3=img3.resize((1530,710),Image.LANCZOS)
       self.photoimg3=ImageTk.PhotoImage(img3)

       bg_img=Label(self.root,image=self.photoimg3)
       bg_img.place(x=0,y=130,width=1530,height=710)

       title_lbl=Label(bg_img,text="Attendance Management System",font=("ALGERIAN",35,"bold"),bg="yellow",fg="black")
       title_lbl.place(x=0,y=0,width=1530,height=45)

       main_frame=Frame(bg_img,bd=2,bg="white")
       main_frame.place(x=20,y=50,width=1480,height=600)

       #left frame
       Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
       Left_frame.place(x=10,y=10,width=760,height=580)

       img_left=Image.open(r"C:\Users\MANIS\OneDrive\Desktop\Student Attendance System Using Face Recognition\Images\images17.jpg")
       img_left=img_left.resize((760,130),Image.LANCZOS)
       self.photoimg_left=ImageTk.PhotoImage(img_left)

       f_lbl=Label(Left_frame,image=self.photoimg_left)
       f_lbl.place(x=0,y=0,width=760,height=130)


       left_inseide_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
       left_inseide_frame.place(x=3,y=135,width=750,height=370)

       #*Labels And Entry********

        #attendance
       attendanceID_label=Label(left_inseide_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
       attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

       attendanceID_entry=ttk.Entry(left_inseide_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
       attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


       #Roll
       
       roll_label=Label(left_inseide_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
       roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

       roll_entry=ttk.Entry(left_inseide_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
       roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

       #Name

       Name_label=Label(left_inseide_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
       Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

       Name_entry=ttk.Entry(left_inseide_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
       Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Department
       Department_label=Label(left_inseide_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
       Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

       Department_entry=ttk.Entry(left_inseide_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
       Department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
       Time_label=Label(left_inseide_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
       Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

       Time_entry=ttk.Entry(left_inseide_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
       Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
         
         #Date
       Date_label=Label(left_inseide_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
       Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

       Date_entry=ttk.Entry(left_inseide_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
       Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendaNCE
       attendance1_label=Label(left_inseide_frame,text="Attendance Status:",font=("comicsansns",12,"bold"),bg="white")
       attendance1_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

       self.atten_status=ttk.Combobox(left_inseide_frame,width=20,textvariable=self.var_atten_attendance,font="comiscnsns 11 bold", state="readonly")
       self.atten_status["values"]=("Status","Present","Absent")
       self.atten_status.grid(row=3,column=1,pady=8)
       self.atten_status.current(0)



       #button frame
       btn_frame=Frame(left_inseide_frame,bd=2,relief=RIDGE,bg="white")
       btn_frame.place(x=0,y=300,width=745,height=45)

       save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
       save_btn.grid(row=0,column=0)

       
       update_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
       update_btn.grid(row=0,column=1)

       
       delete_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
       delete_btn.grid(row=0,column=2)

       
       reset_btn=Button(btn_frame,text="Reset",width=20,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
       reset_btn.grid(row=0,column=3)

       






       #right frame
       Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student attendance Details",font=("times new roman",12,"bold"))
       Right_frame.place(x=780,y=10,width=660,height=580)

       table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
       table_frame.place(x=5,y=5,width=650,height=540)


       #********Scroll Bar table***********
       scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

       self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       scroll_x.config(command=self.AttendanceReportTable.xview)
       scroll_y.config(command=self.AttendanceReportTable.yview)


       self.AttendanceReportTable.heading("id",text="Attendance ID")
       self.AttendanceReportTable.heading("roll",text="Roll")
       self.AttendanceReportTable.heading("name",text="Name")
       self.AttendanceReportTable.heading("department",text="Department")
       self.AttendanceReportTable.heading("time",text="Time")
       self.AttendanceReportTable.heading("date",text="Date")
       self.AttendanceReportTable.heading("attendance",text="Attendance")

       self.AttendanceReportTable["show"]="headings"
       self.AttendanceReportTable.column("id",width=100)
       self.AttendanceReportTable.column("roll",width=100)
       self.AttendanceReportTable.column("name",width=100)
       self.AttendanceReportTable.column("department",width=100)
       self.AttendanceReportTable.column("time",width=100)
       self.AttendanceReportTable.column("date",width=100)
       self.AttendanceReportTable.column("attendance",width=100)


       self.AttendanceReportTable.pack(fill=BOTH,expand=1)

       self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #****************fetch data*********

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
   

   #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 

  #export csv

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported To"+os.path.basename(fln)+"Successfully") 
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 

    def get_cursor(self, event=""):
    # Assuming you're using a treeview or similar widget to get the selected row
     cursor_row = self.AttendanceReportTable.focus()  # Modify according to your widget
     content = self.AttendanceReportTable.item(cursor_row)
     rows = content.get('values')

    # Check if rows is not empty and has the required number of elements
     if rows:
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
     else:
        print("No data selected")  # Handle empty case gracefully
 


    def reset_data(self):
        
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("") 
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("") 
          
        



 



if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()