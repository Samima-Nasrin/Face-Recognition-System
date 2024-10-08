from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #First image1
        img1 = Image.open("Images_FRS/dev_navv.png")
        img1 = img1.resize((1400,170),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1400,height=170)


        #bg image4
        img4 = Image.open("Images_FRS/dev_bg.jpg")
        img4 = img4.resize((1450,560),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=170,width=1450,height=560)

        title_lbl = Label(bg_img,text="DEVELOPER",font=("consolas",33,"bold"),bg="#aea0bc",fg="white")
        title_lbl.place(x=-5,y=-5,width=1400,height=55)

        #frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=30,y=60,width=460,height=450)

        #text
        dev_label = Label(main_frame, text="Developed with <3 by Samima Nasrin,\n buy her a coffee :) ", font=("consolas",16,"bold"), fg="#3c4533")
        dev_label.place(x=20,y=50)

        dev_label = Label(main_frame, text="nasrinsamima7044@gmail.com ", font=("roboto",14,"bold"), bg="#e5be59", fg="#3c4533")
        dev_label.place(x=60,y=370)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()