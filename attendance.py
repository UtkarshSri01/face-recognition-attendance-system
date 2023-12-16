import time
from datetime import datetime, timedelta
from tkinter import*
from tkinter import ttk
import os
import cvzone
import csv
from PIL import Image, ImageTk
from tkinter import messagebox as msg
import mysql.connector as sql
import cv2
from tkinter import filedialog

mydata = []
class Attendance_Dash:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")
        self.root.state('zoomed')

        ########################### VARIABLES #######################
        self.stdId_Var = StringVar()
        self.name_Var = StringVar()
        self.roll_Var = StringVar()
        self.course_Var = StringVar()
        self.time_Var = StringVar()
        self.date_Var = StringVar()
        self.status_Var = StringVar()


        # ######################### BACKGROUND IMAGE ###########################
        # Setting Background image
        img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\attendance_background.jpg")
        self.bgImage = ImageTk.PhotoImage(img)
        bgImage = Label(self.root, image=self.bgImage)
        bgImage.place(x=0, y=0, width=1536, height=864)

        # ########################### FRAME CREATION #############################
        main_frame = Frame(bgImage, bd=2, bg="white")
        main_frame.place(x=65, y=140, width=1400, height=600)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="  STUDENT ATTENDANCE  ",
                                font=("Trebuchet MS", 12, "bold"))
        left_frame.place(x=10, y=10, width=680, height=570)

        # ############## Current Attendance Info Frame #################
        # Current Attendance info text
        current_attend_lbl = Label(left_frame, text="STUDENT ATTENDANCE DETAILS", font=("Trebuchet MS", 15), bg="black",
                                   fg="white")
        current_attend_lbl.place(x=6, y=8, width=665, height=60)

        # Current attendance info label frame
        attendFrame = LabelFrame(left_frame, bd=2, relief=RIDGE)
        attendFrame.place(x=6, y=73, width=664, height=250)

        # Student ID Section
        studId_lbl = Label(attendFrame, text="Student Id:", font=("times new roman", 14, "bold"), fg="black")
        studId_lbl.grid(row=0, column=0, padx=15, sticky=W)

        studId_textbox = ttk.Entry(attendFrame, textvariable=self.stdId_Var, width=20, font=("Trebuchet MS", 12))
        studId_textbox.grid(row=0, column=1, padx=0, pady=15, sticky=W)

        # Student rollNo Section
        Roll_lbl = Label(attendFrame, text="Roll Number:", font=("times new roman", 14, "bold"), fg="black")
        Roll_lbl.grid(row=0, column=2, padx=30, sticky=W)

        Roll_textbox = ttk.Entry(attendFrame, width=20, font=("Trebuchet MS", 12),textvariable=self.roll_Var)
        Roll_textbox.grid(row=0, column=3, padx=0, pady=15, sticky=W)

        # Student Name Section
        Name_lbl = Label(attendFrame, text="Name:", font=("times new roman", 14, "bold"), fg="black")
        Name_lbl.grid(row=1, column=0, padx=15, sticky=W)

        Name_textbox = ttk.Entry(attendFrame, width=20, font=("Trebuchet MS", 12),textvariable=self.name_Var)
        Name_textbox.grid(row=1, column=1, padx=0, pady=15, sticky=W)

        # Student Course Section
        Course_lbl = Label(attendFrame, text="Course:", font=("times new roman", 14, "bold"), fg="black")
        Course_lbl.grid(row=1, column=2, padx=30, sticky=W)

        Course_textbox = ttk.Entry(attendFrame, width=20, font=("Trebuchet MS", 12),textvariable=self.course_Var)
        Course_textbox.grid(row=1, column=3, padx=0, pady=15, sticky=W)

        # Student Time Section
        Time_lbl = Label(attendFrame, text="Time:", font=("times new roman", 14, "bold"), fg="black")
        Time_lbl.grid(row=2, column=0, padx=15, sticky=W)

        Time_textbox = ttk.Entry(attendFrame, width=20, font=("Trebuchet MS", 12),textvariable=self.time_Var)
        Time_textbox.grid(row=2, column=1, padx=0, pady=15, sticky=W)

        # Student Date Section
        studDate_lbl = Label(attendFrame, text="Date:", font=("times new roman", 14, "bold"), fg="black")
        studDate_lbl.grid(row=2, column=2, padx=30, sticky=W)

        studDate_textbox = ttk.Entry(attendFrame, width=20, font=("Trebuchet MS", 12),textvariable=self.date_Var)
        studDate_textbox.grid(row=2, column=3, padx=0, pady=15, sticky=W)

        # Student Attendance Status Section
        attendance_lbl = Label(attendFrame, text="Status:", font=("times new roman", 14, "bold"), fg="black")
        attendance_lbl.grid(row=3, column=0, padx=15, sticky=W)

        attendance_lbl_dropdown = ttk.Combobox(attendFrame, font=("Trebuchet MS", 11),
                                         state="readonly", width=15,textvariable=self.status_Var)
        attendance_lbl_dropdown["values"] = ("Select Type", "Present", "Absent")
        attendance_lbl_dropdown.current(0)
        attendance_lbl_dropdown.grid(row=3, column=1, padx=0, pady=15, sticky=W)

        # Button Label Frame
        buttonFrame = LabelFrame(left_frame, bd=2, relief=RIDGE,bg="white")
        buttonFrame.place(x=6, y=390, width=664, height=150)

        space1_lbl = Label(buttonFrame, text="",bg="white")
        space1_lbl.grid(row=0,column=0,pady=0)

        space2_lbl = Label(buttonFrame, text="",bg="white")
        space2_lbl.grid(row=0, column=1,pady=0)

        update_btn = Button(buttonFrame, text="Update Details", font=("Trebuchet MS", 11), bg="black",
                          fg="white",width=35, command=self.updateRecord)
        update_btn.grid(row=1,column=0,pady=10,padx=20)

        reset_btn = Button(buttonFrame, text="Reset Details", font=("Trebuchet MS", 11), bg="black",
                          fg="white",width=35,command=self.resetData)
        reset_btn.grid(row=1,column=1,pady=10,padx=20)

        importCSV_btn = Button(buttonFrame, text="Import CSV", font=("Trebuchet MS", 11), bg="#285A5D",
                            fg="white", width=35,command=self.importCsv)
        importCSV_btn.grid(row=2, column=0, padx=20)

        ExportCSV_btn = Button(buttonFrame, text="Export CSV", font=("Trebuchet MS", 11), bg="#285A5D",
                            fg="white", width=35,command=self.exportCSV)
        ExportCSV_btn.grid(row=2, column=1, padx=20)


        # ===========================  Right Label Frame  ============================= #
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="  ALL STUDENT ATTENDANCE INFO  ",
                                font=("Trebuchet MS", 12, "bold"))
        right_frame.place(x=705, y=10, width=680, height=570)

        # Current Attendance info text
        current_attend_lbl = Label(right_frame, text="ALL STUDENTS ATTENDANCE INFO", font=("Trebuchet MS", 15), bg="black",
                                   fg="white")
        current_attend_lbl.place(x=6, y=8, width=665, height=60)

        #################  Table Frame  ####################
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=73, width=666, height=467)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("id","roll","name","course","time","date","status")
                                                  ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("course",text="Course")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("status",text="Status")

        self.AttendanceReportTable['show'] = "headings"
        self.AttendanceReportTable.column("id",width=80)
        self.AttendanceReportTable.column("roll",width=80)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("course",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("status",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.getCursor)

        '''======  load data & changeSchedule functions only called if there is any
            records exist in attendance.csv file  ======'''

        with open("Attendance.csv") as myFile:
            csvRead = csv.reader(myFile, delimiter=',')
            if len(list(csvRead))>0:
                self.loadData()
                self.changeSchedule()



    def fetch_data(self,rows):
        # deleting all the previous records from the table
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        # it is used to push new records(rows) in the table
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        # function-> importing and setting all the records in the table
        global mydata
        fileName = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fileName) as myFile:
            csvRead = csv.reader(myFile,delimiter=',')
            next(csvRead)
            for i in csvRead:
                mydata.append(i)
            self.fetch_data(mydata)


    def exportCSV(self):
        # function-> exporting all the records from the table in the disk
        try:
            if len(mydata)<1:
                msg.showerror("Error","No data found!!",parent=self.root)
                return
            fileName = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),parent=self.root)
            with open(fileName,mode='w',newline='') as myFile:
                exportFile = csv.writer(myFile,delimiter=',')
                for i in mydata:
                    exportFile.writerow(i)
                msg.showinfo("Success",f"File saved as: '{os.path.basename(fileName)}'",parent=self.root)
        except Exception as es:
            msg.showerror("Error",f"Error due to {es}",parent=self.root)


    def loadData(self):
        # pushing all the csv records to a global list from attendance.csv
        global mydata
        mydata = []
        with open("Attendance.csv") as myFile:
            csvRead = csv.reader(myFile, delimiter=',')
            next(csvRead)
            for i in csvRead:
                mydata.append(i)
            self.fetch_data(mydata)

    def fetch_LastDate(self):
        # this function is returning only date from attendance.csv file
        with open("Attendance.csv") as myFile:
            # used to store the csv file records in list format
            myList = []
            csvRead = csv.reader(myFile, delimiter=',')
            # next(csvRead) -> read the file text from next line
            next(csvRead)
            # appending csv file records into List
            for i in csvRead:
                myList.append(i)

        # finally accessing only date element from list
        dateObj = str(myList[0][5])

        return dateObj

    def changeSchedule(self):
        # Get last attendance date and get current date of capturing attendance
        lastDate = self.fetch_LastDate()
        currDate = time.strftime("%d-%m-%Y")
        currDate = str(currDate)

        # Converting last attendance date into '01 Nov 2023' format to save as file name
        timeObject = datetime.strptime(lastDate,"%d-%m-%Y")
        timeObject = datetime.strftime(timeObject,"%d %b %Y")

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
            # Now making last Attendance csv file empty
            lastFile = open("Attendance.csv",'w')


    def getCursor(self,event):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.stdId_Var.set(rows[0])
        self.roll_Var.set(rows[1])
        self.name_Var.set(rows[2])
        self.course_Var.set(rows[3])
        self.time_Var.set(rows[4])
        self.date_Var.set(rows[5])
        self.status_Var.set(rows[6])

    def resetData(self):
        self.stdId_Var.set("")
        self.roll_Var.set("")
        self.name_Var.set("")
        self.course_Var.set("")
        self.time_Var.set("")
        self.date_Var.set("")
        self.status_Var.set("Select Type")

    def updateRecord(self):
        stdId = self.stdId_Var.get()
        roll = self.roll_Var.get()
        name = self.name_Var.get()
        course = self.course_Var.get()
        timeVal = self.time_Var.get()
        dateVal = self.date_Var.get()
        status = self.status_Var.get()

        if (stdId=="" or roll=="" or name=="" or course=="" or timeVal=="" or dateVal==""
            or status=="Select Type"):
            msg.showerror("Error","All fields are required!!",parent=self.root)
        else:
            file = open("Attendance.csv",'r')
            reader = csv.reader(file)
            record = [stdId,roll,name,course,timeVal,dateVal,status]
            found = False
            next(reader)
            for row in reader:
                if row[0]==stdId:
                    found = True
            file.close()

            if not found:
                msg.showerror("Error","Student Id not found. Please do not update Student Id",parent=self.root)
            else:
                choice = msg.askyesno("Update","Do you really want to update?")
                if choice!=0:
                    file = open("Attendance.csv", 'r+', newline="")
                    file.seek(1)
                    Writer = csv.writer(file)
                    Writer.writerow(record)
                    # self.loadData()
                    file.close()
                else:
                    return











if __name__ == "__main__":
    wind = Tk()
    obj = Attendance_Dash(wind)
    wind.mainloop()
