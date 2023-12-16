from tkinter import*
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import mysql.connector as sql

global body_textbox
global sub_textbox

class Support:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x780+0+0")
        self.root.title("Help Desk")

        ############## VARIABLES ##############
        self.subject = StringVar()
        self.message = StringVar()


        def eraseSubText(event):
            if sub_textbox.get() == "Enter Subject":
                sub_textbox.delete(0,END)

        def putSubText(event):
            if sub_textbox.get() == "":
                sub_textbox.insert(0,"Enter Subject")


        # -------------------------- BACKGROUND IMAGES  ---------------------------
        # Setting Background image
        img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\support_background.jpg")
        self.photoimg = ImageTk.PhotoImage(img)
        bgImage = Label(self.root, image=self.photoimg)
        bgImage.place(x=0, y=0, width=1530, height=790)

        ############################ MAIN FRAME ###########################
        frame = Frame(self.root, width=620, height=425)
        frame.place(x=50, y=300)


        mail = self.fetchMail()

        # ===================== MAIN FRAME BOUNDARY ======================== #
        mainFrame_boundary = LabelFrame(frame, bd=2, relief=RIDGE)
        mainFrame_boundary.place(x=10, y=10, width=600, height=405)

        # ---------- GET IN TOUCH TITLE TEXT ------------
        title_lbl = Label(mainFrame_boundary, text=" ~ Get in Touch ~", font=("Trebuchet MS", 28, "bold"), fg="black")
        title_lbl.grid(row=0,column=0,padx=80,pady=15)


        # ---------- SENDER NAME TEXT ------------
        from_text = Label(mainFrame_boundary,text="From: ",font=("Trebuchet MS", 14,"bold"),fg="#575757")
        from_text.grid(row=1, column=0,sticky=W,padx=83,pady=12)

        # ======================== SENDER LABEL FRAME ======================== #
        mailFrame = Frame(mainFrame_boundary, width=300, height=28, bg="#417F82")
        mailFrame.place(x=180,y=95)

        # ---------- SENDER NAME VALUE ------------
        sender_name = Label(mailFrame, text=f'@ {mail}', font=("Arial", 11),fg="white", bg="#417F82")
        sender_name.place(x=10,y=2)

        # ======================== SUBJECT LABEL FRAME ======================== #
        subjectFrame = Frame(mainFrame_boundary, width=300, height=30, bg="#CBCACA")
        subjectFrame.place(x=180, y=147)
        # ---------- SUBJECT NAME TEXT ------------
        sub_text = Label(mainFrame_boundary, text="Subject: ", font=("Trebuchet MS", 14, "bold"), fg="#575757")
        sub_text.grid(row=2, column=0,sticky=W,padx=83,pady=10)
        # ---------- SENDER NAME TEXTBOX ------------
        global sub_textbox
        sub_textbox = Entry(subjectFrame, width=35, font=("Canva Sans", 11), bg="#CBCACA",
                               border=0, fg="black")
        sub_textbox.place(x=10,y=5)
        sub_textbox.insert(0, "Enter Subject")
        sub_textbox.bind('<FocusIn>', eraseSubText)
        sub_textbox.bind('<FocusOut>', putSubText)

        # ======================== MESSAGE LABEL FRAME ======================== #
        messageFrame = Frame(mainFrame_boundary, width=300,height=140, bg="#CBCACA")
        messageFrame.place(x=180, y=200)

        # ---------- MESSAGE NAME TEXT ------------
        message_text = Label(mainFrame_boundary, text="Message: ", font=("Trebuchet MS", 14, "bold"), fg="#575757")
        message_text.grid(row=3, column=0,sticky=W,padx=83,pady=12)
        # ---------- MESSAGE NAME TEXTBOX ------------
        global body_textbox
        body_textbox = Text(messageFrame,height=7 ,width=34, font=("Canva Sans", 11), bg="#CBCACA",
                               border=0, fg="black")
        body_textbox.place(x=10,y=10)
        body_textbox.insert('1.0',"Enter Message")
        self.message = body_textbox.get('1.0','end')

        send_button = Button(mainFrame_boundary,text="Submit",font=("Canva Sans", 11),bg="#417F82",cursor='hand2',fg="white",
                             height=1,width=10,border=0,activebackground="#CBCACA",command=self.onSubmitClick)
        send_button.grid(row=4, column=0,sticky=W,padx=180,pady=120)




    ############################## - FUNCTIONS - ################################


    def getId(self):
        file = open("facultyId.txt", 'r')
        val = file.read()
        file.close()
        return val

    def fetchMail(self):
        facultyId = self.getId()
        conn = sql.connect(host="localhost", user="root", password="Harsh_23",
                           database="facerecoglib")
        my_cursor = conn.cursor()
        my_cursor.execute(f"select email from faculty_db where facultyId = {facultyId}")
        gotData = my_cursor.fetchone()

        return gotData[0]

    def onSubmitClick(self):
        messageVal = body_textbox.get('1.0','end')
        subjectVal = sub_textbox.get()

        if((messageVal=="Enter Message") or (subjectVal=="Enter Subject") or
                (messageVal=="") or (subjectVal=="")):
            msg.showwarning("Warning","All entry fields are required!!",parent=self.root)
        else:
            msg.showinfo("Sucess","Your info has submitted to the team for review.")

        print(subjectVal)
        print(messageVal)












if __name__ == "__main__":
    root = Tk()
    obj = Support(root)
    root.mainloop()
