from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")


        #=================variable==================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


        #bg image
        self.bg = ImageTk.PhotoImage(file="Images_FRS/defaultt.jpg")

        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #frame
        frame = Frame(self.root, bg="white")
        frame.place(x=300,y=100,width=760,height=550)


        register_lbl = Label(frame,text="REGISTER HERE", font=("roboto", 20, "bold"), fg = "white", bg="black")
        register_lbl.place(x=20,y=20)

        #labels and entries
        #===============row1==========================
        fname = Label(frame,text="First Name", font=("roboto", 15, "bold"), bg="white")
        fname.place(x=20,y=70)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("roboto", 15, "bold"))
        fname_entry.place(x=20, y=100, width=200)

        lname = Label(frame,text="Last Name", font=("roboto", 15, "bold"), bg="white")
        lname.place(x=320,y=70)

        self.lname_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("roboto", 15, "bold"))
        self.lname_entry.place(x=320, y=100, width=200)

        #==================row2===========================
        contact = Label(frame,text="Contact No.", font=("roboto", 15, "bold"), bg="white")
        contact.place(x=20,y=150)

        self.contact_entry = ttk.Entry(frame,textvariable=self.var_contact, font=("roboto", 15, "bold"))
        self.contact_entry.place(x=20, y=180, width=200)

        email = Label(frame,text="Email", font=("roboto", 15, "bold"), bg="white")
        email.place(x=320,y=150)

        self.email_entry = ttk.Entry(frame,textvariable=self.var_email, font=("roboto", 15, "bold"))
        self.email_entry.place(x=320, y=180, width=200)

        #==================row3==========================
        secQue = Label(frame,text="Select Security Question", font=("roboto", 15, "bold"), bg="white")
        secQue.place(x=20,y=230)

        self.secQue_combo = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("roboto", 14, "bold"), state="readonly")
        self.secQue_combo["values"] = ("Select", "Your Favorite Coding Language", "Your Favorite Subject", "Your Favorite Movie", "Your Middle School crush name")
        self.secQue_combo.current(0)
        self.secQue_combo.place(x=20, y=260, width=200)

        secAns = Label(frame,text="Security Question Answer", font=("roboto", 15, "bold"), bg="white")
        secAns.place(x=320,y=230)

        self.secAns_entry = ttk.Entry(frame,textvariable=self.var_securityA, font=("roboto", 15, "bold"))
        self.secAns_entry.place(x=320, y=260, width=200)

        #==================row4===========================
        password = Label(frame,text="Password", font=("roboto", 15, "bold"), bg="white")
        password.place(x=20,y=310)

        self.password_entry = ttk.Entry(frame,textvariable=self.var_pass, font=("roboto", 15, "bold"))
        self.password_entry.place(x=20, y=340, width=200)

        confirmP = Label(frame,text="Confirm Password", font=("roboto", 15, "bold"), bg="white")
        confirmP.place(x=320,y=310)

        self.confirmP_entry = ttk.Entry(frame, textvariable=self.var_confpass,font=("roboto", 15, "bold"))
        self.confirmP_entry.place(x=320, y=340, width=200)


        #check button
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree to the terms and conditions", font=("roboto", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=20, y=390)

        #buttons
        #registor
        img = Image.open("Images_FRS/defaultt.jpg")
        img = img.resize((200,50),Image.LANCZOS)
        self.photoim = ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoim, command=self.register_data,cursor="hand2", borderwidth=0)
        b1.place(x=20,y=450,width=200) #register now button


        #login
        imgg = Image.open("Images_FRS/defaultt.jpg")
        imgg = imgg.resize((200,50),Image.LANCZOS)
        self.photoimm = ImageTk.PhotoImage(imgg)
        b1 = Button(frame,image=self.photoimm, cursor="hand2", borderwidth=0)
        b1.place(x=310,y=450,width=200) #login now button



    #==========function declaration=============
    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_securityA.get() == "" or self.var_pass.get() == "" or self.var_confpass.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "You must agree to the Terms and Conditions to proceed")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password=".", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE Email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists")
            else:
                my_cursor.execute("INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)", (self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registered succesfully")


        



if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()