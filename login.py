from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
from main import Face_Recognition_System


# Function to change color on focus
def on_entry_click(event):
    event.widget.config(bg="#ECDFCC", fg="#1E201E")

# Function to revert color on focus out
def on_focusout(event):
    event.widget.config(bg="#1E201E", fg="#ECDFCC")

    
#=================main function==================
def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


#=============login class===========================
class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        # self.bg = ImageTk.PhotoImage(file="Images_FRS/login_bg.jpg")

        # Define the target screen size
        target_width = 1490
        target_height = 790

        image = Image.open("Images_FRS/login_bg.jpg")

        self.bg = ImageTk.PhotoImage(image.resize((target_width, target_height), Image.LANCZOS))

        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #frame
        frame = Frame(self.root, bg="#1E201E")
        frame.place(x=500,y=50,width=380,height=600)

        img1 = Image.open("Images_FRS/icons8-user-90.png")
        img1 = img1.resize((90,90),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(image=self.photoimage1, bg="#1E201E", borderwidth=0)
        lblimg1.place(x=640, y=90, width=100, height=100)

        #heading
        get_str = Label(frame, text="Login", font=("roboto", 20, "bold"), fg = "#ECDFCC", bg="#1E201E")
        get_str.place(x=148, y=140)

        

        #label
        username = Label(frame, text="Username", font=("roboto", 13), fg = "#f2ebe0", bg="#1E201E")
        username.place(x=80, y=210)

        self.textuser = Entry(frame, font=("roboto", 14, "bold"), fg="#f2ebe0", bg="#1E201E")
        self.textuser.place(x=55, y=240, width=260, height=30)

        password = Label(frame, text="Password", font=("roboto", 13), fg = "#f2ebe0", bg="#1E201E")
        password.place(x=80, y=290)

        self.textpass = Entry(frame, font=("roboto", 14, "bold"), fg="#f2ebe0", bg="#1E201E")
        self.textpass.place(x=55, y=320, width=260, height=30)

        # Bind events to the entry boxes
        self.textuser.bind("<FocusIn>", on_entry_click)
        self.textuser.bind("<FocusOut>", on_focusout)

        self.textpass.bind("<FocusIn>", on_entry_click)
        self.textpass.bind("<FocusOut>", on_focusout)

        #Icon images
        img2 = Image.open("Images_FRS/username.png")
        img2 = img2.resize((24,24),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="#1E201E", borderwidth=0)
        lblimg2.place(x=555, y=260, width=25, height=25)

        img3 = Image.open("Images_FRS/password.png")
        img3 = img3.resize((24,24),Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="#1E201E", borderwidth=0)
        lblimg3.place(x=555, y=340, width=25, height=25)


        #login button
        login_btn = Button(frame, command=self.login, text="Login",cursor="hand2", font=("roboto", 13, "bold"), fg="#f2ebe0", bg="#CD3826", activeforeground="#c2c9c7", activebackground="#a62a1b")
        login_btn.place(x=55, y=410, width=120,height=29)

        #register button
        Register_btn = Button(frame, text="New here? Register now", command=self.register_window,cursor="hand2", font=("roboto", 10, "bold"),borderwidth=0, fg="#f2ebe0", bg="#1E201E", activeforeground="red", activebackground="#1E201E")
        Register_btn.place(x=83, y=530, width=200)

        #forget password button
        forgetPass_btn = Button(frame, text="Forgot Password?", command=self.forgot_password_window,cursor="hand2", font=("roboto", 9, "bold"),borderwidth=0, fg="#f2ebe0", bg="#1E201E", activeforeground="red", activebackground="#1E201E")
        forgetPass_btn.place(x=34, y=365, width=150)



    #===================register window linking==================
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


    #==================login function============
    def login(self):
        if self.textuser.get() == "" or self.textpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.textuser.get() == "sam" and self.textpass.get() == "ass":
            messagebox.showinfo("Success", "welcome")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password=".", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE Email=%s AND Password=%s", (self.textuser.get(), self.textpass.get()))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                open_main = messagebox.askyesno("Access", "Admin Access only")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                    
            conn.commit()
            conn.close()


    #===================reset password==================================
    def reset_password(self):
        if self.secQue_combo1.get() == "Select":
            messagebox.showerror("Error", "Select the security question ",parent=self.root2)
        elif self.secAns_entry1.get() == "":
            messagebox.showerror("Error", "Please enter answer",parent=self.root2)
        elif self.password_entry1.get() == "":
            messagebox.showerror("Error", "Please enter new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password=".", database="face_recognizer")
            my_cursor = conn.cursor()
            qury = ("SELECT * FROM register WHERE Email=%s AND SecurityQ=%s AND SecurityA=%s")
            vall = (self.textuser.get(), self.secQue_combo1.get(), self.secAns_entry1.get(),)
            my_cursor.execute(qury, vall)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer",parent=self.root2)
            else:
                query = ("UPDATE register SET Password=%s WHERE Email=%s")
                val = (self.password_entry1.get(), self.textuser.get())
                my_cursor.execute(query, val)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()


    #==================forget password===============================
    def forgot_password_window(self):
        if self.textuser.get() == "":
            messagebox.showerror("Error", "Please Enter Username to reset Password")      
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password=".", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE Email=%s")
            value = (self.textuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Please enter valid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x570+490+80") #widthxheight+x+y

                #frame
                frame = Frame(self.root2, bg="#f2ebe0")
                frame.place(x=0,y=0,width=400,height=570)

                l = Label(self.root2, text="Reset Password", font=("roboto", 20, "bold"), fg="#1E201E", bg="#f2ebe0")
                l.place(x=0, y=40, relwidth=1)

                #question
                secQue1 = Label(self.root2,text="Select Security Question", font=("roboto", 13), bg="#f2ebe0", fg="#1E201E")
                secQue1.place(x=55, y=110)

                self.secQue_combo1 = ttk.Combobox(self.root2, font=("roboto", 14), state="readonly")
                self.secQue_combo1["values"] = ("Select", "Your Favorite Coding Language", "Your Favorite Subject", "Your Favorite Movie", "Your Middle School crush name")
                self.secQue_combo1.current(0)
                self.secQue_combo1.place(x=55, y=140, width=280)

                #answer
                secAns1 = Label(self.root2,text="Security Question Answer", font=("roboto", 13), bg="#f2ebe0", fg="#1E201E")
                secAns1.place(x=55,y=190)

                self.secAns_entry1 = ttk.Entry(self.root2, font=("roboto", 14))
                self.secAns_entry1.place(x=55, y=220, width=280)

                #new password
                password1 = Label(self.root2,text="New Password", font=("roboto", 13), bg="#f2ebe0", fg="#1E201E")
                password1.place(x=55,y=270)

                self.password_entry1 = ttk.Entry(self.root2, font=("roboto", 14))
                self.password_entry1.place(x=55, y=300, width=280)


                #reset password button
                b1 = Button(frame, text="Reset Password", command=self.reset_password,cursor="hand2", font=("roboto", 15, "bold"),borderwidth=0, fg="#fbf7f1", bg="#579d69", activeforeground="#c3bdb4", activebackground="#497f57")
                b1.place(x=55, y=415, width=280, height=50)
                


#=====================register class====================
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
        # self.bg = ImageTk.PhotoImage(file="Images_FRS/login_bg.jpg")

        # lbl_bg = Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        target_width = 1490
        target_height = 790

        image = Image.open("Images_FRS/login_bg.jpg")

        self.bg = ImageTk.PhotoImage(image.resize((target_width, target_height), Image.LANCZOS))

        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #frame
        frame = Frame(self.root, bg="#1E201E")
        frame.place(x=330,y=80,width=680,height=550)


        register_lbl = Label(frame,text="GET STARTED", font=("roboto", 21, "bold"), fg = "#B4F0BA", bg="#1E201E")
        register_lbl.place(x=80,y=30, width=500)

        #labels and entries
        #===============row1==========================
        fname = Label(frame,text="First Name", font=("roboto", 13), bg="#1E201E", fg="#f2ebe0")
        fname.place(x=60,y=83)

        fname_entry = Entry(frame,textvariable=self.var_fname, font=("roboto", 14),bd=3, fg="white", bg="#1E201E")
        fname_entry.place(x=60, y=113, width=270)

        lname = Label(frame,text="Last Name", font=("roboto", 13), fg="#f2ebe0", bg="#1E201E")
        lname.place(x=362,y=83)

        self.lname_entry = Entry(frame,textvariable=self.var_lname, font=("roboto", 14),bd=3, fg="white", bg="#1E201E")
        self.lname_entry.place(x=362, y=113, width=270)

        #==================row2===========================
        contact = Label(frame,text="Contact No.", font=("roboto", 13), fg="#f2ebe0", bg="#1E201E")
        contact.place(x=60,y=163)

        self.contact_entry = Entry(frame,textvariable=self.var_contact, font=("roboto", 14),bd=3, fg="white", bg="#1E201E")
        self.contact_entry.place(x=60, y=193, width=270)

        email = Label(frame,text="Email", font=("roboto", 13), fg="#f2ebe0", bg="#1E201E")
        email.place(x=362,y=163)

        self.email_entry = Entry(frame,textvariable=self.var_email, font=("roboto", 14),bd=3, fg="white", bg="#1E201E")
        self.email_entry.place(x=362, y=193, width=270)

        #==================row3==========================
              
        secQue = Label(frame,text="Select Security Question", font=("roboto", 13), fg="#f2ebe0", bg="#1E201E")
        secQue.place(x=60,y=239)

        self.secQue_combo = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("roboto", 14), state="readonly", foreground="black", background="#1E201E")
        self.secQue_combo["values"] = ("Select", "Your Favorite Coding Language", "Your Favorite Subject", "Your Favorite Movie", "Your Middle School crush name")
        self.secQue_combo.current(0)
        self.secQue_combo.place(x=60, y=269, width=270)

        secAns = Label(frame,text="Security Question Answer", font=("roboto", 13), fg="#f2ebe0", bg="#1E201E")
        secAns.place(x=362,y=239)

        self.secAns_entry = Entry(frame,textvariable=self.var_securityA, font=("roboto", 14),bd=3, fg="white", bg="#1E201E")
        self.secAns_entry.place(x=362, y=269, width=270)

        #==================row4===========================
        password = Label(frame,text="Password", font=("roboto", 13), fg="#f2ebe0", bg="#1E201E")
        password.place(x=60,y=310)

        self.password_entry = Entry(frame,textvariable=self.var_pass, font=("roboto", 14),bd=3, fg="white", bg="#1E201E")
        self.password_entry.place(x=60, y=340, width=270)

        confirmP = Label(frame,text="Confirm Password", font=("roboto", 13), fg="#f2ebe0", bg="#1E201E")
        confirmP.place(x=362,y=310)

        self.confirmP_entry = Entry(frame, textvariable=self.var_confpass,font=("roboto", 14),bd=3, fg="white", bg="#1E201E")
        self.confirmP_entry.place(x=362, y=340, width=270)


        #check button
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree to the terms and conditions", font=("roboto", 12, "bold"), onvalue=1, offvalue=0, bg="#1E201E",fg="#f2ebe0")
        checkbtn.place(x=60, y=390)

        #buttons
        
        #register button
        b1 = Button(frame, command=self.register_data, text="Register",cursor="hand2", font=("roboto", 14, "bold"), fg="#f2ebe0", bg="#8abf8f", activeforeground="#c2c9c7", activebackground="#a62a1b")
        b1.place(x=60, y=450, width=286,height=35)

        #login button
        b11 = Button(frame, command=self.return_login, text="Login",cursor="hand2", font=("roboto", 14, "bold"), fg="#f2ebe0", bg="#373A37", activeforeground="#c2c9c7", activebackground="#a62a1b")
        b11.place(x=345, y=450, width=286,height=35)



    #==========function declaration=============
    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_securityA.get() == "" or self.var_pass.get() == "" or self.var_confpass.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "You must agree to the Terms and Conditions to proceed", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password=".", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE Email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists", parent=self.root)
            else:
                my_cursor.execute("INSERT INTO register VALUES(%s,%s,%s,%s,%s,%s,%s)", (self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registered succesfully", parent=self.root)


    def return_login(self):
        self.root.destroy()




#============main function call==============
if __name__ == "__main__":
    main()


