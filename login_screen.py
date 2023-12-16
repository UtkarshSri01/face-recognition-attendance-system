import os
from tkinter import*
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import mysql.connector as sql
from faculty_dash import Faculty_Dash

class Login_Screen:
    def __init__(self,root):
        self.root = root
        width = 1100
        height = 680
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cord = (screen_width/2)-(width/2)
        y_cord = (screen_height/2)-(height/2)
        self.root.geometry("%dx%d+%d+%d"%(width,height,x_cord,y_cord))
        self.root.title("")
        self.root.overrideredirect(1)
        # self.root.resizable(False,False)

        def erasePassText(event):
            if userPass_textbox.get() == "Enter Phone no":
                userPass_textbox.delete(0,END)

        def eraseIdText(event):
            if userId_textbox.get() == "Enter Id":
                userId_textbox.delete(0,END)

        def putIdText(event):
            if userId_textbox.get() == "":
                userId_textbox.insert(0,"Enter Id")

        def putPassText(event):
            if userPass_textbox.get() == "":
                userPass_textbox.insert(0,"Enter Phone no")


        ########################### VARIABLES #######################
        self.stdId_Var = StringVar()
        self.stdPass_Var = StringVar()
        self.isFaculty_Var = IntVar()

        # -------------------------- BACKGROUND IMAGES  ---------------------------
        # Setting Background image
        self.bgImage = ImageTk.PhotoImage(file="C:/Users/Harsh Sri/PycharmProjects/FaceRecog/Face Recog Library/home_background.jpg")
        canvas = Canvas(self.root)
        canvas.create_image(0, 0, image=self.bgImage, anchor=NW)
        canvas.pack(fill="both", expand=True)

        # -------------------- LOGIN SCREEN FRAME ------------------------- #

        # Frame Creation ----
        frame = Frame(self.root,width=750,height=450)
        frame.place(x=170,y=140)
        self.frame_bg = ImageTk.PhotoImage(file="C:/Users/Harsh Sri/PycharmProjects/FaceRecog/Face Recog Library/login_frame.png")
        Label(frame,image=self.frame_bg).pack()

        # Title Text -----
        signIN_title = Label(frame,text="Sign In",font=("Canva Sans", 20, "bold"), fg="black",bg="white")
        signIN_title.place(x=110,y=50)

        #Sub-Title Text ----
        sub_title = Label(frame,text="Students can directly enter their details \n"
                                     "but faculty needs to tick checkbox above submit",font=("Arial", 9), fg="#575757",bg="white")
        sub_title.place(x=30,y=93)

        # User Id TextBox ----
        userId_textbox = Entry(frame,textvariable=self.stdId_Var,width=22, font=("Canva Sans", 9),bg="#E9E6E6",border=0,fg="#575757")
        userId_textbox.place(x=95,y=178)
        userId_textbox.insert(0,"Enter Id")
        userId_textbox.bind('<FocusIn>', eraseIdText)
        userId_textbox.bind('<FocusOut>', putIdText)

        # User Password TextBox ----
        userPass_textbox = Entry(frame,textvariable=self.stdPass_Var,width=22, font=("Canva Sans", 9),bg="#E9E6E6",border=0,fg="#575757")
        userPass_textbox.place(x=95,y=241)
        userPass_textbox.insert(0, "Enter Phone no")
        userPass_textbox.bind('<FocusIn>',erasePassText)
        userPass_textbox.bind('<FocusOut>',putPassText)

        # Faculty CheckBox ----
        faculty_checkbox = Checkbutton(frame,variable=self.isFaculty_Var, text="Faculty Login",font=("Trebuchet MS",9),bg="white",fg="#272626")
        faculty_checkbox.place(x=47,y=280)

        # Submit Button ---
        submit_btn = Button(frame, text="Submit",command=self.LoginBtn, font=("Trebuchet MS", 10, "bold"),bg="black",fg="white")
        submit_btn.place(x=50,y=330,height=33,width=230)

        # Exit Button ----
        exitBtn_img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\exit_btn.png")
        # exitBtn_img.resize((180, 170))
        self.photoImg = ImageTk.PhotoImage(exitBtn_img)
        exitBtn = Button(self.root,image=self.photoImg, cursor="hand2",bg="#193335",activebackground="#193335",bd=0,command=self.exit)
        exitBtn.place(x=1050, y=19, width=30, height=30)

    ############################## - FUNCTIONS - ################################

    def exit(self):
        choice = msg.askyesno("Quit","Are you sure you want to exit ?",parent=self.root)
        if(choice!=0):
            self.root.destroy()
        else:
            return

    def facultyDash_Window(self):
        self.new_window = Toplevel(self.root)
        self.app = Faculty_Dash(self.new_window)

    def LoginBtn(self):
        # Fetching value from id and Pass varaibles
        Id = self.stdId_Var.get()
        Phone = self.stdPass_Var.get()
        isFaculty = self.isFaculty_Var.get()


        # Establishing database connection
        conn = sql.connect(host="localhost", user="root", password="Harsh_23",
                           database="facerecoglib")
        my_cursor = conn.cursor()

        # Checking for empty fields
        if (Id == "" or Id == "Enter Id"
            or Phone == "" or Phone == "Enter Phone no"):
            msg.showwarning("Warning","All fields are required!!", parent=self.root)
        elif(len(Phone) != 10):
            msg.showwarning("Warning","Please enter a valid phone number", parent=self.root)
        else:
            # Fetch data from Faculty Table
            if(isFaculty!=0):
                try:
                    my_cursor.execute(f"select * from faculty_db where facultyId = {Id} and phone = {Phone}")
                    gotData = my_cursor.fetchone()
                    if gotData == None:
                        msg.showerror("Failed", "Invalid Id or Password",parent=self.root)

                    else:
                        choice = msg.askyesno("Restricted","Faculty Access Only",parent=self.root)
                        if(choice != 0):
                            facultyId = self.stdId_Var.get()
                            file = open("facultyId.txt", 'w')
                            file.write(facultyId)
                            file.close()
                            # Closing Login Screen Window
                            self.root.destroy()
                            # Opening Faculty Window
                            os.system("faculty_dash.py")


                        else:
                            return

                except Exception as es:
                    msg.showerror("Error",f"Unable to validate due to:{es}",parent=self.root)

                finally:
                    conn.commit()
                    conn.close()
            else:
                # Fetch data from Student Table
                try:
                    my_cursor.execute(f"select * from studdata where studId = {Id} and phone = {Phone}")
                    gotData = my_cursor.fetchone()
                    if gotData == None:
                        msg.showerror("Failed", "Invalid Id or Password",parent=self.root)

                    else:
                        msg.showinfo("Success", "Successfully Signed In",parent=self.root)
                        studId = self.stdId_Var.get()
                        file = open("StudId.txt", 'w')
                        file.write(studId)
                        file.close()

                        # Closing Login Screen Window
                        self.root.destroy()
                        # Opening Faculty Window
                        os.system("student_dash.py")

                except Exception as es:
                    msg.showerror("Error", f"Unable to validate due to:{es}",parent=self.root)

                finally:
                    conn.commit()
                    conn.close()
        return



if __name__ == "__main__":
    wind = Tk()
    obj = Login_Screen(wind)
    wind.mainloop()
