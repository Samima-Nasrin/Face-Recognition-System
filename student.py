from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=======================variables===========================
        self.var_dept = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_passing = StringVar()
        self.var_name = StringVar()
        self.var_id = StringVar()
        self.var_section = StringVar()
        self.var_group = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()



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
        title_lbl = Label(bg_img,text="STUDENT DETAILS",font=("consolas",30,"bold"),bg="#a9ebb1",fg="white")
        title_lbl.place(x=-8,y=-10,width=1420,height=60)

        #frame
        main_frame = Frame(bg_img,bd=2, bg="#f0fcf7")
        main_frame.place(x=10,y=50,width=1320,height=500)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("roboto",11), bg="white")
        Left_frame.place(x=10,y=10,width=650,height=470)

        #======course =============
        course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("roboto",11))
        course_frame.place(x=5,y=5,width=635,height=120)

        #department
        dept_label = Label(course_frame,text="Department",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        dept_label.grid(row=0,column=0,padx=10)

        dept_combo = ttk.Combobox(course_frame,textvariable=self.var_dept, font=("roboto",12),width=17,state="read only")
        dept_combo["values"] = ("Select Department", "Computer Science and Engineering", "Information Technology", "Electronics & Communication Engineering", "Electrical Engineering")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=3,pady=10)

        #year
        year_label = Label(course_frame,text="Year",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        year_label.grid(row=0,column=2,padx=10, sticky=W)

        year_combo = ttk.Combobox(course_frame,textvariable=self.var_year,font=("roboto",12),width=17,state="read only")
        year_combo["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)

        #semster
        sem_label = Label(course_frame,text="Semester",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        sem_label.grid(row=1,column=0,padx=10, sticky=W)

        sem_combo = ttk.Combobox(course_frame,textvariable=self.var_sem,font=("roboto",12),width=17,state="read only")
        sem_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)

        #Passing year
        passing_label = Label(course_frame,text="Passing year",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        passing_label.grid(row=1,column=2,padx=10, sticky=W)

        passing_combo = ttk.Combobox(course_frame,textvariable=self.var_passing,font=("roboto",12),width=17,state="read only")
        passing_combo["values"] = ("Select Paasing year", "2024", "2025", "2026", "2027", "2028")
        passing_combo.current(0)
        passing_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)

        #=====Class student ======
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Info",font=("roboto",11))
        class_student_frame.place(x=1,y=130,width=640,height=310)

        #Name
        studentname_label = Label(class_student_frame,text="Name",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        studentname_label.grid(row=0,column=0,padx=10, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("roboto",12,"bold"))
        studentName_entry.grid(row=0,column=1,padx=10, sticky=W)

        #studentId
        studentId_label = Label(class_student_frame,text="Student Id",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        studentId_label.grid(row=0,column=2,padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("roboto",12,"bold"))
        studentID_entry.grid(row=0,column=3,padx=10, sticky=W)

        #section
        section_label = Label(class_student_frame,text="Section",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        section_label.grid(row=1,column=0,padx=10, pady=10, sticky=W)

        section_entry = ttk.Entry(class_student_frame,textvariable=self.var_section,width=20,font=("roboto",12,"bold"))
        section_entry.grid(row=1,column=1,padx=10,pady=10, sticky=W)

        #group
        group_label = Label(class_student_frame,text="Group",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        group_label.grid(row=1,column=2,padx=10, pady=10, sticky=W)

        group_entry = ttk.Entry(class_student_frame,textvariable=self.var_group,width=20,font=("roboto",12,"bold"))
        group_entry.grid(row=1,column=3,padx=10,pady=10, sticky=W)

        #emial
        email_label = Label(class_student_frame,text="Email address",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        email_label.grid(row=2,column=0,padx=10, pady=10, sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("roboto",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=10, sticky=W)

        #phone
        phone_label = Label(class_student_frame,text="Phone number",font=("roboto",12,"bold"),bg="white", fg="#4f4f4f")
        phone_label.grid(row=3,column=0,padx=10, pady=10, sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("roboto",12,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,pady=10, sticky=W)

        #radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take a Photo",value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        #radio buttons2
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No photo sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #button frame
        btn_frame = Frame(class_student_frame, bd=2,relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=205,width=630,height=45)

        #save button
        save_btn = Button(btn_frame,text="Save",command=self.add_data, width=15, font=("roboto",12,"bold"),bg="#36d47c",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)

        #update
        Update_btn = Button(btn_frame,text="Update", command=self.update_data, width=15, font=("roboto",12,"bold"),bg="#9f87e9",fg="white",cursor="hand2")
        Update_btn.grid(row=0,column=1)

        #delete
        Delete_btn = Button(btn_frame,text="Delete", command=self.delete_data, width=15, font=("roboto",12,"bold"),bg="#f05346",fg="white",cursor="hand2")
        Delete_btn.grid(row=0,column=2)

        #reset
        Reset_btn = Button(btn_frame,text="Reset", command=self.reset_data, width=15, font=("roboto",12,"bold"),bg="#ffa942",fg="white",cursor="hand2")
        Reset_btn.grid(row=0,column=3)

        #button frame1
        btn_frame1 = Frame(class_student_frame, bd=2,relief=RIDGE, bg="white")
        btn_frame1.place(x=0,y=250,width=630,height=45)

        #photo 
        photo_btn = Button(btn_frame1,text="Take a Photo",command=self.generate_dataset, width=31, font=("roboto",12,"bold"),bg="#55a2ff",fg="white",cursor="hand2")
        photo_btn.grid(row=0,column=0)

        #update photo
        update_photo_btn = Button(btn_frame1,text="Update Photo", width=31, font=("roboto",12,"bold"),bg="#55a2ff",fg="white",cursor="hand2")
        update_photo_btn.grid(row=0,column=1)


        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student List",font=("roboto",11), bg="white")
        Right_frame.place(x=660,y=10,width=640,height=470)

        #====search system=====
        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("roboto",11))
        Search_frame.place(x=5,y=5,width=630,height=70)

        #search by
        search_label = Label(Search_frame,text="Search By",font=("roboto",11,"bold"),bg="white", fg="#4f4f4f")
        search_label.grid(row=0,column=0,padx=10,pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame,font=("roboto",12),width=15,state="read only")
        search_combo["values"] = ("Select", "Rollno", "Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

        #search bar
        search_entry = ttk.Entry(Search_frame,width=20,font=("roboto",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10, sticky=W)

        #search
        search_btn = Button(Search_frame,text="Search", width=8, font=("roboto",10,"bold"),bg="#55a2ff",fg="white")
        search_btn.grid(row=0,column=3)

        #show all
        showAll_btn = Button(Search_frame,text="Show All", width=8, font=("roboto",10,"bold"),bg="#55a2ff",fg="white")
        showAll_btn.grid(row=0,column=4)

        #==table===
        Table_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=78,width=630,height=365)


        #scroll bar
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        
        self.student_table = ttk.Treeview(Table_frame,columns=("Dept", "Year", "Sem", "Passing", "Name", "Id", "Section", "Group", "Email", "Phone", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dept", text="Department")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Passing", text="Passing Year")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Id", text="Id")
        self.student_table.heading("Section", text="Section")
        self.student_table.heading("Group", text="Group")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone No.")
        self.student_table.heading("Photo",text="Photo Sample")
        self.student_table["show"] = "headings"

        self.student_table.column("Dept", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Passing", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Id", width=100)
        self.student_table.column("Section", width=100)
        self.student_table.column("Group", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        

    #==========function declaration=================

    def add_data(self):
        if self.var_dept.get() == "Select Department" or self.var_name == "" or self.var_section == "" or self.var_id == "" or self.var_group == "" or self.var_email == "" or self.var_phone == "" or self.var_sem.get() == "Select Semester" or self.var_year.get() == "Select Year" or self.var_passing.get() == "Select Passing Year":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password=".", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dept.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_passing.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_section.get(),
                                                                                                    self.var_group.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_radio1.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


    #===============fetch data======================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password=".", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)

            conn.commit()
        conn.close()


    #=============get cursor==================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dept.set(data[0]),
        self.var_year.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_passing.set(data[3]),
        self.var_name.set(data[4]),
        self.var_id.set(data[5]),
        self.var_section.set(data[6]),
        self.var_group.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_radio1.set(data[10])

    #update function
    def update_data(self):
        if self.var_dept.get() == "Select Department" or self.var_name == "" or self.var_section == "" or self.var_id == "" or self.var_group == "" or self.var_email == "" or self.var_phone == "" or self.var_sem.get() == "Select Semester" or self.var_year.get() == "Select Year" or self.var_passing.get() == "Select Passing Year":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)

        else:
            try:
                Upadate = messagebox.askyesno("Update", "Do you want to update details?", parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password=".", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""UPDATE student SET Dept=%s, Year=%s, Sem=%s, Passing=%s, Name=%s, Section=%s, `GroupNo`=%s, Email=%s, Phone=%s, PhotoSample=%s WHERE Id=%s""", (self.var_dept.get(), self.var_year.get(),self.var_sem.get(),self.var_passing.get(),self.var_name.get(),self.var_section.get(),self.var_group.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get(),self.var_id.get()))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success", "Details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent = self.root)


    #delete function
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password=".", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="DELETE FROM student WHERE Id=%s"
                    val =(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent = self.root)


    #reset function
    def reset_data(self):
        self.var_dept.set("Select Department") 
        self.var_name.set("")
        self.var_section.set("")
        self.var_id.set("")
        self.var_group.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_sem.set("Select Semester")
        self.var_year.set("Select Year")
        self.var_passing.set("Select Passing Year")



    #=====================Generate data set or Take photo samples==============================
    def generate_dataset(self):
        if self.var_dept.get() == "Select Department" or self.var_name == "" or self.var_section == "" or self.var_id == "" or self.var_group == "" or self.var_email == "" or self.var_phone == "" or self.var_sem.get() == "Select Semester" or self.var_year.get() == "Select Year" or self.var_passing.get() == "Select Passing Year":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password=".", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                idx = 0
                for x in myresult:
                    idx+=1
                my_cursor.execute("""UPDATE student SET Dept=%s, Year=%s, Sem=%s, Passing=%s, Name=%s, Section=%s, `GroupNo`=%s, Email=%s, Phone=%s, PhotoSample=%s WHERE Id=%s""", (self.var_dept.get(), self.var_year.get(),self.var_sem.get(),self.var_passing.get(),self.var_name.get(),self.var_section.get(),self.var_group.get(),self.var_email.get(),self.var_phone.get(),self.var_radio1.get(),self.var_id.get()==idx+1))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #===========Load predefned data on face frontals from opencv===============

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(idx)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed successfully", parent=self.root)


            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent = self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()