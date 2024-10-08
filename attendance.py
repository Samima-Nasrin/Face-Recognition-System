from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #===================variables===================
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_year = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_att_status = StringVar()


        #First image1
        img1 = Image.open("Images_FRS/main_nav.png")
        img1 = img1.resize((1500,130),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1500,height=130)

        #bg image4
        img4 = Image.open("Images_FRS/main_bg.png")
        img4 = img4.resize((1500,650),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1500,height=650)

        #title
        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT",font=("consolas",30,"bold"),bg="#a9ebb1",fg="white")
        title_lbl.place(x=-8,y=-10,width=1420,height=60)

        #frame
        main_frame = Frame(bg_img,bd=2, bg="#f0fcf7")
        main_frame.place(x=10,y=50,width=1320,height=500)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("roboto",11), bg="white")
        Left_frame.place(x=10,y=10,width=650,height=470)

        course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,font=("roboto",11))
        course_frame.place(x=5,y=5,width=635,height=410)

        #Labels and Entry
        #studentId
        studentId_label = Label(course_frame,text="Student Id",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        studentId_label.grid(row=0,column=2,padx=10,pady=20, sticky=W)

        studentID_entry = ttk.Entry(course_frame,width=20,font=("roboto",12,"bold"))
        studentID_entry.grid(row=0,column=3,padx=10, sticky=W)

        #Name
        studentname_label = Label(course_frame,text="Name",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        studentname_label.grid(row=0,column=0,padx=10,pady=10, sticky=W)

        studentName_entry = ttk.Entry(course_frame,width=20, textvariable=self.var_name,font=("roboto",12,"bold"))
        studentName_entry.grid(row=0,column=1,padx=10,pady=10, sticky=W)

        #Department
        dept_label = Label(course_frame,text="Department",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        dept_label.grid(row=1,column=0,padx=10,pady=10, sticky=W)

        dept_entry = ttk.Entry(course_frame,width=20,textvariable=self.var_dept,font=("roboto",12,"bold"))
        dept_entry.grid(row=1,column=1,padx=10,pady=10, sticky=W)

        #Year
        dept_label = Label(course_frame,text="Year",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        dept_label.grid(row=1,column=2,padx=10,pady=10, sticky=W)

        dept_entry = ttk.Entry(course_frame,width=20,textvariable=self.var_year,font=("roboto",12,"bold"))
        dept_entry.grid(row=1,column=3,padx=10,pady=10, sticky=W)

        #Date
        date_label = Label(course_frame,text="Date",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        date_label.grid(row=2,column=0,padx=10,pady=10, sticky=W)

        date_entry = ttk.Entry(course_frame,width=20,textvariable=self.var_date,font=("roboto",12,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=10, sticky=W)

        #Time
        time_label = Label(course_frame,text="Time",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        time_label.grid(row=2,column=2,padx=10,pady=20, sticky=W)

        time_entry = ttk.Entry(course_frame,width=20,textvariable=self.var_time,font=("roboto",12,"bold"))
        time_entry.grid(row=2,column=3,padx=10,pady=20, sticky=W)

        #Attendance
        attend_label = Label(course_frame,text="Attendance",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        attend_label.grid(row=3,column=0,padx=10, sticky=W)

        self.atten_status = ttk.Combobox(course_frame,font=("roboto",12),width=18,textvariable=self.var_att_status,state="read only")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=10,sticky=W)


        #buttons
        
        #button frame
        btn_frame = Frame(course_frame, bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=363,width=630,height=45)

        #Import button
        save_btn = Button(btn_frame,text="Import csv", command=self.importCsv, width=15, font=("roboto",12,"bold"),bg="#2bc870",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)

        #Export
        Update_btn = Button(btn_frame,text="Export csv", command=self.exportCsv, width=15, font=("roboto",12,"bold"),bg="#5389dc",fg="white",cursor="hand2")
        Update_btn.grid(row=0,column=1)

        #Update
        Delete_btn = Button(btn_frame,text="Update", width=15, font=("roboto",12,"bold"),bg="#ffa942",fg="white",cursor="hand2")
        Delete_btn.grid(row=0,column=2)

        #reset
        Reset_btn = Button(btn_frame,text="Reset", width=15, command=self.reset_data,font=("roboto",12,"bold"),bg="#f05346",fg="white",cursor="hand2")
        Reset_btn.grid(row=0,column=3)



        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Register",font=("roboto",11), bg="white")
        Right_frame.place(x=660,y=10,width=640,height=470)

        #==table===
        Table_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=5,width=630,height=410)


        #scroll bar
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(Table_frame,columns=("id", "name", "dept", "year", "date", "time", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Student Id")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("dept", text="Department")
        self.AttendanceReportTable.heading("year", text="Year")

        #FIX THIS
        self.AttendanceReportTable.heading("date", text="Time")
        self.AttendanceReportTable.heading("time", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance Status")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=110)
        self.AttendanceReportTable.column("name", width=110)
        self.AttendanceReportTable.column("dept", width=130)
        self.AttendanceReportTable.column("year", width=110)
        self.AttendanceReportTable.column("date", width=120)
        self.AttendanceReportTable.column("time", width=120)
        self.AttendanceReportTable.column("attendance", width=110)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        



    #=================fetch data==========================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    #=============import csv function==========
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #===========export csv function=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error", "No data found to export", parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Data exported to '"+os.path.basename(fln)+"' successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent = self.root)

    
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dept.set(rows[2])
        self.var_year.set(rows[3])
        self.var_date.set(rows[4])
        self.var_time.set(rows[5])
        self.var_att_status.set(rows[6])


    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_year.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_att_status.set("")





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()