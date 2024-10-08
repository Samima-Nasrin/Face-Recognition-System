from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from train import Train
from student import Student
from face_recognition import Face_Recognition
from developer import Developer
from help import Help
from attendance import Attendance
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #First image1
        img1 = Image.open("Images_FRS/main_nav.png")
        img1 = img1.resize((1500,250),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1500,height=250)

        #bg image4
        img4 = Image.open("Images_FRS/main_bg.png")
        img4 = img4.resize((1500,650),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1500,height=650)

        #title
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("consolas",30,"bold"),bg="#a9ebb1",fg="white")
        title_lbl.place(x=-8,y=-10,width=1420,height=60)

        #================time=========================================
        def time():
            string = strftime('%H:%M:%S ')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('roboto',14,'bold'),bg="#B4F0BA", fg="#9b5094")
        lbl.place(x=20,y=5,width=100,height=60)
        time()

        #Profile button5
        img5 = Image.open("Images_FRS/profile.png")
        img5 = img5.resize((130,130),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command=self.student_details, cursor="hand2", bg="white")
        b1.place(x=270,y=100,width=140,height=140)

        b1_1 = Button(bg_img,text="Profiles",command=self.student_details, cursor="hand2", font=("roboto",15,"bold"),bg="#5a5a5a",fg="white")
        b1_1.place(x=270,y=238,width=140,height=30)

        #Detect face button6
        img6 = Image.open("Images_FRS/detect.png")
        img6 = img6.resize((110,110),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,image=self.photoimg6,command=self.face_data, cursor="hand2", bg="white")
        b2.place(x=495,y=100,width=140,height=140)

        b2_1 = Button(bg_img,text="Face Detector",command=self.face_data, cursor="hand2", font=("roboto",15,"bold"),bg="#5a5a5a",fg="white")
        b2_1.place(x=495,y=238,width=140,height=30)

        #Attendance button7
        img7 = Image.open("Images_FRS/attendance.png")
        img7 = img7.resize((120,120),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data, bg="white")
        b3.place(x=720,y=100,width=140,height=140)

        b3_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data, font=("roboto",15,"bold"),bg="#5a5a5a",fg="white")
        b3_1.place(x=720,y=238,width=140,height=30)

        #Developer button12
        img12 = Image.open("Images_FRS/developer.png")
        img12 = img12.resize((110,110),Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b4 = Button(bg_img,image=self.photoimg12, command=self.developer_data,cursor="hand2", bg="white")
        b4.place(x=945,y=100,width=140,height=140)

        b4_1 = Button(bg_img,text="Developer", command=self.developer_data,cursor="hand2", font=("roboto",15,"bold"),bg="#5a5a5a",fg="white")
        b4_1.place(x=945,y=238,width=140,height=30)

        #Train data button8
        img8 = Image.open("Images_FRS/train.png")
        img8 = img8.resize((110,110),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img,image=self.photoimg8,command=self.train_data, cursor="hand2", bg="white")
        b5.place(x=270,y=300,width=140,height=140)

        b5_1 = Button(bg_img,text="Train Data",command=self.train_data, cursor="hand2", font=("roboto",15,"bold"),bg="#5a5a5a",fg="white")
        b5_1.place(x=270,y=438,width=140,height=30)

        #Photos button9
        img9 = Image.open("Images_FRS/photos.png")
        img9 = img9.resize((110,110),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img , bg="white")
        b6.place(x=495,y=300,width=140,height=140)

        b6_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img ,font=("roboto",15,"bold"),bg="#5a5a5a",fg="white")
        b6_1.place(x=495,y=438,width=140,height=30)

        #Help button10
        img10 = Image.open("Images_FRS/helpd.png")
        img10 = img10.resize((110,110),Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img,image=self.photoimg10,command=self.help_desk,cursor="hand2", bg="white")
        b7.place(x=720,y=300,width=140,height=140)

        b7_1 = Button(bg_img,text="Help Desk",command=self.help_desk,cursor="hand2", font=("roboto",15,"bold"),bg="#5a5a5a",fg="white")
        b7_1.place(x=720,y=438,width=140,height=30)

        #Exit button11
        img11 = Image.open("Images_FRS/exit.png")
        img11 = img11.resize((100,100),Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img,image=self.photoimg11,command=self.iExit,cursor="hand2", bg="white")
        b8.place(x=945,y=300,width=140,height=140)

        b8_1 = Button(bg_img,text="Exit",command=self.iExit,cursor="hand2", font=("roboto",15,"bold"),bg="#5a5a5a",fg="white")
        b8_1.place(x=945,y=438,width=140,height=30)
        


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    #=======function buttons======================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()