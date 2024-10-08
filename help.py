import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
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
        title_lbl = Label(bg_img,text="ASK HELP",font=("consolas",30,"bold"),bg="#a9ebb1",fg="white")
        title_lbl.place(x=-8,y=-10,width=1420,height=60)
        
        







if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()