from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="FACE DETECTOR",font=("roboto",35,"bold"),bg="#d6d6d6",fg="#0b0909")
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
        title_lbl = Label(bg_img,text="FACE DETECTION",font=("consolas",30,"bold"),bg="#a9ebb1",fg="white")
        title_lbl.place(x=-8,y=-10,width=1420,height=60)

        #text
        dev_label = Label(bg_img, text="Activate the camera to detect and verify your identity. The system will determine if you belong to the class or if you are an unknown face.            \n Upon successful detection, your information will be displayed. Ensure your face is fully visible and unobstructed for accurate identification.           \n Click on 'Detect Face' to start. Press 'Enter' to turn off webcam.                                                                                                                         ", font=("poppins",13), fg="#3c4533", bg="#f3f8ff")
        dev_label.place(x=100,y=130, width=1150, height=130)

        #button
        b1_1 = Button(bg_img,text="Detect Face >", command=self.face_recog, cursor="hand2", font=("roboto",15,"bold"),bg="#548ADC",fg="white")
        b1_1.place(x=100,y=300,width=1150,height=50)



    #================attendance=======================
    def mark_attendance(self, id, n, d, yr):
        with open("attendanceList.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            
            if((id not in name_list) and (n not in name_list) and (d not in name_list) and (yr not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{n},{d},{yr},{dtString},{d1},Present")






    #====================face recognition==============
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                ID,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password=".", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Id="+str(ID))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("SELECT Dept FROM student WHERE Id="+str(ID))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("SELECT Year FROM student WHERE Id="+str(ID))
                yr = my_cursor.fetchone()
                yr = "+".join(yr)

                my_cursor.execute("SELECT Id FROM student WHERE Id="+str(ID))
                i = my_cursor.fetchone()
                i = "+".join(i)

                


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-76),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Dept:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Year:{yr}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                    self.mark_attendance(i, n, d, yr)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown detected",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()