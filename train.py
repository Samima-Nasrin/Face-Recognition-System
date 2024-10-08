#Samima Nasrin 17-08-2024
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("roboto",35,"bold"),bg="#d6d6d6",fg="#0b0909")
        title_lbl.place(x=0,y=0,width=1400,height=45)

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
        title_lbl = Label(bg_img,text="TRAIN DATA",font=("consolas",30,"bold"),bg="#a9ebb1",fg="white")
        title_lbl.place(x=-8,y=-10,width=1420,height=60)

        #text
        dev_label = Label(bg_img, text="Train the system to recognize faces by uploading a set of photos. This process will analyze and store the facial features from the images, allowing \n the system to accurately identify individuals during attendance checks. Please ensure that the photos you upload or click photos while creating       \n profile are clear and well-lit for the best results. Click 'Train Data' to start training the data for further analysis                                                         ", font=("poppins",13), fg="#3c4533", bg="#f3f8ff")
        dev_label.place(x=100,y=130, width=1150, height=130)

        #button
        b1_1 = Button(bg_img,text="Train Data >", command=self.tarin_classifier, cursor="hand2", font=("roboto",15,"bold"),bg="#548ADC",fg="white")
        b1_1.place(x=100,y=300,width=1150,height=50)


    def tarin_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #Gray scale image 
            imageNp = np.array(img,'uint8')
            ID = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(ID)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        #============train the classifier and save===========
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows
        messagebox.showinfo("Result", "Training datasets completed", parent=self.root)








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()