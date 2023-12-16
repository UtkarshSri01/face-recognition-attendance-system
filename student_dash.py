import os
from tkinter import*
from tkinter import messagebox as msg
from time import strftime
from datetime import datetime
import cv2
from PIL import Image, ImageTk
from myAccount import My_Account
import mysql.connector as sql
import time
import csv

class Student_Dash:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Dashboard")
        self.root.state('zoomed')


        # -------------------------- BACKGROUND IMAGES  ---------------------------
        # Setting Background image
        img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\student_dashboard.jpg")
        self.bgimg = ImageTk.PhotoImage(img)
        bgImage = Label(self.root, image=self.bgimg)
        bgImage.place(x=0, y=0, width=1536, height=864)

        # Button1 - Face Recognition ----
        button_img1 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\mark_attendance.png")
        button_img1.resize((220, 210))
        self.photoimg1 = ImageTk.PhotoImage(button_img1)

        button1 = Button(self.root, image=self.photoimg1, command=self.faceRecog, cursor="hand2")
        button1.place(x=300, y=380, width=220, height=210)

        # Button2 - Student Details ----
        button_img2 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\stud_details.png")
        button_img2.resize((180, 170))
        self.photoimg2 = ImageTk.PhotoImage(button_img2)

        button2 = Button(self.root, image=self.photoimg2,command=self.stud_details, cursor="hand2")
        button2.place(x=660,y=380,width=220,height=210)

        # Button3 - Support ----
        button_img3 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\help.png")
        button_img3.resize((180, 170))
        self.photoimg3 = ImageTk.PhotoImage(button_img3)

        button4 = Button(self.root, image=self.photoimg3, cursor="hand2")
        button4.place(x=1000,y=380,width=220,height=210)

        # Exit Button ----
        exitBtn_img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\exit_btn.png")
        # exitBtn_img.resize((180, 170))
        self.photoImg = ImageTk.PhotoImage(exitBtn_img)
        exitBtn = Button(self.root,text="Exit",font=("Trebuchet MS",15), cursor="hand2", bg="#1d3e41", activebackground="#1d3e41",
                         fg="white",bd=0,activeforeground="grey",command=self.exit)
        exitBtn.place(x=1420, y=23, width=80, height=40)

        # ------------ TIME VARIABLE ------------ #
        clock = Label(self.root,font=("Calibri,30"),bg="#0C1718",fg="white")
        clock.place(x=65,y=101)


        with open("Attendance.csv") as myFile:
            csvRead = csv.reader(myFile, delimiter=',')
            if len(list(csvRead))>0:
                self.changeSchedule()


    def stud_details(self):
        self.new_window = Toplevel(self.root)
        self.app = My_Account(self.new_window)

    def exit(self):
        choice = msg.askyesno("Quit","Are you sure you want to exit ?",parent=self.root)
        if(choice!=0):
            # Closing Login Screen Window
            self.root.destroy()
            # Opening Faculty Window
            os.system("login_screen.py")
        else:
            return

    def markAttend(self,Sid,roll,name,course):
        with open("Attendance.csv",'r+',newline='\n') as file:
            myDataList = file.readlines()
            nameList = []
            count = self.getCount(Sid)
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if ((Sid not in nameList) and (roll not in nameList) and
                (name not in nameList) and (course not in nameList)):
                current = datetime.now()
                saveDate = current.strftime("%d-%m-%Y")
                saveTime = current.strftime("%H:%M:%S")
                file.writelines(f"\n{Sid},{roll},{name},{course},{saveTime},{saveDate},Present")
                try:
                    conn = sql.connect(host="localhost", user="root", password="Harsh_23",
                                       database="facerecoglib")
                    my_cursor = conn.cursor()
                    my_cursor.execute(f"update studdata set attendCount={count+1} where studId={Sid}")
                    conn.commit()
                    conn.close()
                except Exception as es:
                    msg.showerror("SQL Error",f"attendance count updation failed because {es}")

    def faceRecog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord = []

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100*(1-predict/300)))

                conn = sql.connect(host="localhost", user="root", password="Harsh_23",
                                   database="facerecoglib")
                my_cursor = conn.cursor()
                my_cursor.execute("select name from studdata where studId=" + str(id))
                name = my_cursor.fetchone()
                name = "+".join(name)

                my_cursor.execute("select roll from studdata where studId=" + str(id))
                roll = my_cursor.fetchone()
                roll = "+".join(roll)

                my_cursor.execute("select course from studdata where studId=" + str(id))
                course = my_cursor.fetchone()
                course = "+".join(course)

                my_cursor.execute("select studId from studdata where studId=" + str(id))
                studId = my_cursor.fetchone()
                studId = "+".join(str(id))


                if confidence>75:
                    cv2.putText(img,f'Roll:{roll}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'Name:{name}',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'Course:{course}',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.markAttend(studId,roll,name,course)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Recognizing Face",img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    def getCount(self,id):
        conn = sql.connect(host="localhost", user="root", password="Harsh_23",
                           database="facerecoglib")
        my_cursor = conn.cursor()
        my_cursor.execute(f"select attendCount from studdata where studId={id}")
        attendCount = my_cursor.fetchone()
        attendCount = attendCount[0]
        return attendCount


    def fetch_LastDate(self):
        with open("Attendance.csv") as myFile:
            myList = []
            csvRead = csv.reader(myFile, delimiter=',')
            next(csvRead)
            for i in csvRead:
                myList.append(i)
        dateObj = str(myList[0][5])

        return dateObj
    def changeSchedule(self):
        # Get last attendance date and get current date of capturing attendance
        lastDate = self.fetch_LastDate()
        currDate = time.strftime("%d-%m-%Y")
        currDate = str(currDate)

        # Converting last attendance date into '01 Nov 2023' format to save as file name
        timeObject = datetime.strptime(lastDate, "%d-%m-%Y")
        timeObject = datetime.strftime(timeObject, "%d %b %Y")

        # Match both the dates if they differ,
        # -create a new file and copy current attendance details
        # -delete last attendance record from attendance.csv
        if currDate != lastDate:
            with open("Attendance.csv") as myFile:
                # Opening a file in write mode and having file name with last date
                newFile = open(rf"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Attendance Records\Attendance Report {timeObject}.csv",'w',newline="")
                csvRead = csv.reader(myFile, delimiter=',')
                # next(csvRead) -> read the file text from next line
                next(csvRead)
                # Copying the last attendance data into new file
                for i in csvRead:
                    data = csv.writer(newFile)
                    data.writerow(i)
            newFile.close()
            # Now making old Attendance csv file empty
            lastFile = open("Attendance.csv",'w')



if __name__ == "__main__":
    root = Tk()
    obj = Student_Dash(root)
    root.mainloop()
