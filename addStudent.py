import os
from tkinter import*
from tkinter import ttk

import cvzone
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as sql
import cv2


class add_Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")
        self.root.state('zoomed')

        ########################### VARIABLES #######################
        self.stdId_Var = StringVar()
        self.name_Var = StringVar()
        self.type_Var = StringVar()
        self.course_Var = StringVar()
        self.year_Var = StringVar()
        self.sem_Var = StringVar()
        self.sec_Var = StringVar()
        self.rollNo_Var = StringVar()
        self.gender_Var = StringVar()
        self.dob_Var = StringVar()
        self.email_Var = StringVar()
        self.phone_Var = StringVar()
        self.address_Var = StringVar()
        self.teacher_Var = StringVar()

        # ######################### BACKGROUND IMAGE ###########################
        # Setting Background image
        img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\addStudent_background.jpg")
        self.photoimg = ImageTk.PhotoImage(img)
        bgImage = Label(self.root, image=self.photoimg)
        bgImage.place(x=0, y=0, width=1536, height=864)

        # ########################### FRAME CREATION #############################
        main_frame = Frame(bgImage,bd=2,bg="white")
        main_frame.place(x=25,y=100,width=1480,height=665)

        # Left Label Frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="  STUDENT INFORMATION  ",font=("Trebuchet MS",12,"bold"))
        left_frame.place(x=10,y=10,width=720,height=635)

        # ############## Current Course Info Frame #################
        # Current course info text
        current_course_lbl = Label(left_frame, text="Current Course Information", font=("Trebuchet MS",15),bg="black", fg="white")
        current_course_lbl.place(x=5,y=3,width=705,height=40)

        # Current course info label frame
        current_course = LabelFrame(left_frame, bd=2, relief=RIDGE)
        current_course.place(x=5, y=47, width=705, height=130)

        # Course Type Section
        type_lbl = Label(current_course,text="Course type",font=("times new roman",13,"bold"),fg="black")
        type_lbl.grid(row=0,column=0,padx=15,sticky=W)

        type_lbl_dropdown = ttk.Combobox(current_course,textvariable=self.type_Var, font=("Trebuchet MS",11),state="readonly",width=20)
        type_lbl_dropdown["values"]=("Select Type","Professional","Non-Professional")
        type_lbl_dropdown.current(0)
        type_lbl_dropdown.grid(row=0,column=1,padx=0,pady=20,sticky=W)

        # Course Section
        course_lbl = Label(current_course, text="Course", font=("times new roman", 13, "bold"),fg="black")
        course_lbl.grid(row=0, column=2,padx=40,sticky=W)

        course_lbl_dropdown = ttk.Combobox(current_course,textvariable=self.course_Var, font=("Trebuchet MS", 11), state="readonly",width=20)
        course_lbl_dropdown["values"] = ("Select Course", "BCA", "BBA", "BSC", "B.COM", "BA", "MBA", "MCA")
        course_lbl_dropdown.current(0)
        course_lbl_dropdown.grid(row=0, column=3, padx=0, pady=10, sticky=W)

        # Year Section
        year_lbl = Label(current_course, text="Year", font=("times new roman", 13, "bold"), fg="black")
        year_lbl.grid(row=1, column=0, padx=15,sticky=W)

        year_lbl_dropdown = ttk.Combobox(current_course,textvariable=self.year_Var, font=("Trebuchet MS", 11), state="readonly",width=20)
        year_lbl_dropdown["values"] = ("Select Year", "2023-2024", "2022-2023", "2021-2022", "2020-2021", "2019-2020")
        year_lbl_dropdown.current(0)
        year_lbl_dropdown.grid(row=1, column=1, padx=0, pady=10, sticky=W)

        # Semester Section
        sem_lbl = Label(current_course, text="Semester", font=("times new roman", 13, "bold"), fg="black")
        sem_lbl.grid(row=1, column=2, padx=40,sticky=W)

        sem_lbl_dropdown = ttk.Combobox(current_course,textvariable=self.sem_Var, font=("Trebuchet MS", 11), state="readonly",width=20)
        sem_lbl_dropdown["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6")
        sem_lbl_dropdown.current(0)
        sem_lbl_dropdown.grid(row=1, column=3, padx=0, pady=10,sticky=W)

        #######################  Student Class Info Frame ######################

        # Student Class info text
        studClass_lbl = Label(left_frame, text="Student Class Information", font=("Trebuchet MS", 15), bg="black", fg="white")
        studClass_lbl.place(x=5, y=183, width=705, height=40)

        # Student class info label frame
        studClass_frame = LabelFrame(left_frame, bd=2, relief=RIDGE)
        studClass_frame.place(x=5, y=228, width=705, height=290)

        # Student ID Section
        studentId_lbl = Label(studClass_frame, text="Student Id", font=("times new roman", 13, "bold"), fg="black")
        studentId_lbl.grid(row=0, column=0, padx=15, sticky=W)

        studentId_textbox = ttk.Entry(studClass_frame,textvariable=self.stdId_Var,width=20,font=("Trebuchet MS", 11))
        studentId_textbox.grid(row=0, column=1, padx=7, pady=15, sticky=W)


        # Student Name Section
        studentName_lbl = Label(studClass_frame, text="Student Name", font=("times new roman", 13, "bold"), fg="black")
        studentName_lbl.grid(row=0, column=2, padx=40, sticky=W)

        studentName_textbox = ttk.Entry(studClass_frame,textvariable=self.name_Var ,width=20, font=("Trebuchet MS", 11))
        studentName_textbox.grid(row=0, column=3, padx=0, pady=10, sticky=W)

        # Class division Section
        section_lbl = Label(studClass_frame, text="Section", font=("times new roman", 13, "bold"), fg="black")
        section_lbl.grid(row=1, column=0, padx=15, sticky=W)

        section_dropdown = ttk.Combobox(studClass_frame, textvariable=self.sec_Var, font=("Trebuchet MS", 11), state="readonly", width=18)
        section_dropdown["values"] = ("Select Section", "Section-A", "Section-B", "Section-C", "Section-D")
        section_dropdown.current(0)
        section_dropdown.grid(row=1, column=1, padx=7, pady=10, sticky=W)

        # Roll No Section
        rollNum_lbl = Label(studClass_frame, text="Roll No", font=("times new roman", 13, "bold"), fg="black")
        rollNum_lbl.grid(row=1, column=2, padx=40, sticky=W)

        rollNum_textbox = ttk.Entry(studClass_frame, textvariable=self.rollNo_Var, width=20, font=("Trebuchet MS", 11))
        rollNum_textbox.grid(row=1, column=3, padx=0, pady=10, sticky=W)

        # Email Section
        email_lbl = Label(studClass_frame, text="Email", font=("times new roman", 13, "bold"), fg="black")
        email_lbl.grid(row=2, column=0, padx=15, sticky=W)

        email_textbox = ttk.Entry(studClass_frame, textvariable=self.email_Var, width=20, font=("Trebuchet MS", 11))
        email_textbox.grid(row=2, column=1, padx=7, pady=10, sticky=W)

        # Gender Section
        gender_lbl = Label(studClass_frame, text="Gender", font=("times new roman", 13, "bold"), fg="black")
        gender_lbl.grid(row=2, column=2, padx=40, sticky=W)

        gender_dropdown = ttk.Combobox(studClass_frame, textvariable=self.gender_Var, font=("Trebuchet MS", 11), state="readonly", width=18)
        gender_dropdown["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_dropdown.current(0)
        gender_dropdown.grid(row=2, column=3, padx=0, pady=10, sticky=W)

        # Date Of Birth Section
        dob_lbl = Label(studClass_frame, text="D.O.B", font=("times new roman", 13, "bold"), fg="black")
        dob_lbl.grid(row=3, column=0, padx=15, sticky=W)

        dob_textbox = ttk.Entry(studClass_frame,textvariable=self.dob_Var, width=20, font=("Trebuchet MS", 11))
        dob_textbox.grid(row=3, column=1, padx=7, pady=10, sticky=W)

        # Phone number Section
        phoneNum_lbl = Label(studClass_frame, text="Phone No", font=("times new roman", 13, "bold"), fg="black")
        phoneNum_lbl.grid(row=3, column=2, padx=40, sticky=W)

        phoneNum_textbox = ttk.Entry(studClass_frame,textvariable=self.phone_Var, width=20, font=("Trebuchet MS", 11))
        phoneNum_textbox.grid(row=3, column=3, padx=0, pady=10, sticky=W)

        # Address
        address_lbl = Label(studClass_frame, text="Address", font=("times new roman", 13, "bold"), fg="black")
        address_lbl.grid(row=4, column=0, padx=15, sticky=W)

        address_textbox = ttk.Entry(studClass_frame, textvariable=self.address_Var, width=20, font=("Trebuchet MS", 11))
        address_textbox.grid(row=4, column=1, padx=7, pady=10, sticky=W)

        # Teacher's Name Section
        teacher_lbl = Label(studClass_frame, text="Assigned Teacher", font=("times new roman", 13, "bold"), fg="black")
        teacher_lbl.grid(row=4, column=2, padx=40, sticky=W)

        teacher_textbox = ttk.Entry(studClass_frame, textvariable=self.teacher_Var, width=20, font=("Trebuchet MS", 11))
        teacher_textbox.grid(row=4, column=3, padx=0, pady=10, sticky=W)

        # Radio Buttons Section
        self.radioBtn_Var = StringVar()
        radioBtn1 = ttk.Radiobutton(studClass_frame, variable=self.radioBtn_Var, text="Take Photo Sample",value="Yes")
        radioBtn1.grid(row=6,column=1, pady=10)

        radioBtn2 = ttk.Radiobutton(studClass_frame, variable=self.radioBtn_Var, text="No Photo Sample",value="No")
        radioBtn2.grid(row=6,column=3,sticky=W)


        ##########################   BUTTONS  ###########################

        # Save Button
        save_btn = Button(left_frame, text="Save",command=self.add_data, font=("Trebuchet MS", 11),bg="black",fg="white")
        save_btn.place(x=10,y=525,width=160,height=35)

        # Update Button
        update_btn = Button(left_frame,text="Update", command=self.update_data,font=("Trebuchet MS", 11),bg="black",fg="white")
        update_btn.place(x=187,y=525,width=160,height=35)

        # Delete Button
        delete_btn = Button(left_frame,text="Delete", command=self.delete_data, font=("Trebuchet MS", 11),bg="black",fg="white")
        delete_btn.place(x=365,y=525,width=160,height=35)

        # Reset Button
        reset_btn = Button(left_frame,text="Reset", command=self.reset_data, font=("Trebuchet MS", 11),bg="black",fg="white",)
        reset_btn.place(x=545,y=525,width=160,height=35)

        # Take Photo Sample Button
        take_photo_btn = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\take_photo_sample.png")
        take_photo_btn.resize((340, 35))
        self.photo_img1 = ImageTk.PhotoImage(take_photo_btn)

        take_photo_btn = Button(left_frame, command=self.generate_dataset, image=self.photo_img1, cursor="hand2")
        take_photo_btn.place(x=10,y=566,width=337,height=35)

        # Update Photo Sample Button
        update_photo_btn = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\delete_photo_sample.png")
        update_photo_btn.resize((340, 35))
        self.photo_img2 = ImageTk.PhotoImage(update_photo_btn)

        update_photo_btn = Button(left_frame, command=self.delete_Datasets, image=self.photo_img2, cursor="hand2")
        update_photo_btn.place(x=365,y=566,width=340,height=35)


        #######################  Right Label Frame  #########################

        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="  STUDENT DETAILS  ",font=("Trebuchet MS",12,"bold"))
        right_frame.place(x=740,y=10,width=720,height=635)

        # Student Details text
        student_detail_lbl = Label(right_frame, text="Student Records", font=("Trebuchet MS", 15), bg="black",
                                   fg="white")
        student_detail_lbl.place(x=5, y=3, width=705, height=40)

        ##############  Search Data Label Frame  ################

        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE)
        search_frame.place(x=5, y=47, width=705, height=70)

        # Search label text
        search_lbl = Label(search_frame,text="Search By:",font=("times new roman", 13, "bold"),fg="black")
        search_lbl.grid(row=0,column=0,padx=10,pady=16,sticky=W)

        search_lbl_dropdown = ttk.Combobox(search_frame, font=("Trebuchet MS", 11), state="readonly", width=15)
        search_lbl_dropdown["values"] = ("Select", "Roll Number", "Phone Number")
        search_lbl_dropdown.current(0)
        search_lbl_dropdown.grid(row=0, column=1, padx=2, pady=16, sticky=W)

        # Search TextBox
        search_textbox = ttk.Entry(search_frame, width=20, font=("Trebuchet MS", 11))
        search_textbox.grid(row=0, column=3, padx=20, pady=16)

        # Search Button
        search_btn = Button(search_frame, text="Search", font=("Trebuchet MS", 10), bg="black", fg="white")
        search_btn.place(x=470,y=13,width=100,height=30)

        # Show All Button
        showAll_btn = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\showAll_btn.png")
        showAll_btn.resize((340, 35))
        self.photo_img3 = ImageTk.PhotoImage(showAll_btn)

        showAll_btn = Button(search_frame, image=self.photo_img3, cursor="hand2")
        showAll_btn.place(x=580,y=13,width=100,height=30)

        #################  Table Frame  ####################
        table_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=125, width=705, height=477)

        # ----------- Setting Up Scroll Bar ------------ #
        scrollX = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(table_frame,orient=VERTICAL)

        # Setting Table Id's to be added in the table
        self.studentTable = ttk.Treeview(table_frame,columns=("id","name","type","course","year","sem","section","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.studentTable.xview)
        scrollY.config(command=self.studentTable.yview)

        #  Setting up headings to show in the table
        self.studentTable.heading("id", text="Student ID")
        self.studentTable.heading("name", text="Name")
        self.studentTable.heading("type",text="Type")
        self.studentTable.heading("course",text="Course")
        self.studentTable.heading("year",text="Year")
        self.studentTable.heading("sem",text="Semester")
        self.studentTable.heading("section",text="Section")
        self.studentTable.heading("roll",text="Roll No")
        self.studentTable.heading("gender",text="Gender")
        self.studentTable.heading("dob",text="DOB")
        self.studentTable.heading("email",text="Email")
        self.studentTable.heading("phone",text="Phone")
        self.studentTable.heading("address",text="Address")
        self.studentTable.heading("teacher",text="Teacher")
        self.studentTable.heading("photo",text="Photo Sample")

        self.studentTable["show"] = "headings"


        # Setting Up Column Width
        self.studentTable.column("id", width=80)
        self.studentTable.column("name", width=150)
        self.studentTable.column("type", width=120)
        self.studentTable.column("course", width=100)
        self.studentTable.column("year", width=100)
        self.studentTable.column("sem", width=100)
        self.studentTable.column("section", width=100)
        self.studentTable.column("roll", width=100)
        self.studentTable.column("gender", width=100)
        self.studentTable.column("dob", width=100)
        self.studentTable.column("email", width=100)
        self.studentTable.column("phone", width=100)
        self.studentTable.column("address", width=100)
        self.studentTable.column("teacher", width=100)
        self.studentTable.column("photo", width=100)

        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease>",self.fill_data)
        self.fetch_data()


    ####################  FUNCTION DECLARATION  ######################

    #---------------- FUNCTION FOR STUDENT ID VALIDATION ---------------#
    def checkExists(self,StudentId):
        conn = sql.connect(host="localhost", username="root", password="Harsh_23", database="facerecoglib")
        my_cursor = conn.cursor()
        my_cursor.execute("select studId from studdata")
        idList = my_cursor.fetchall()

        flag = 0
        for i in idList:
            # it converts elements from (101,),(102,) to '101'
            val1 = str(i).removeprefix('(')
            val2 = val1.removesuffix(',)')
            if val2 == StudentId:
                flag = 1

        if flag == 1:
            return True
        else:
            return False

    #----------------- ADDING STUDENT DETAILS FUNCTION -------------------#
    def add_data(self):
        if (self.stdId_Var.get() == "Select Type" or self.course_Var.get() == "Select Course" or
            self.year_Var.get() == "Select Year" or self.sem_Var.get() == "Select Semester" or
            self.stdId_Var.get() == "" or self.name_Var.get() == "" or self.sec_Var.get() == "Select Section" or
            self.rollNo_Var.get() == "" or self.email_Var.get() == "" or self.gender_Var.get() == "Select Gender" or
            self.dob_Var.get() == "" or self.phone_Var.get() == "" or self.address_Var.get() == "" or
            self.teacher_Var.get() == ""):
                messagebox.showerror("Error", "All fields are required!!", parent=self.root)

        elif not self.stdId_Var.get().isdigit():
            messagebox.showerror("Error","Student Id is Invalid",parent=self.root)

        elif self.checkExists(self.stdId_Var.get())==True:
            messagebox.showerror("Error","Student Id Already Exist",parent=self.root)

        elif not self.rollNo_Var.get().isdigit():
            messagebox.showerror("Error","Roll Number is Invalid",parent=self.root)

        elif len(self.phone_Var.get())!=10 or (not self.phone_Var.get().isdigit()):
            messagebox.showerror("Error","Phone Number is Invalid",parent=self.root)

        else:
            try:
                conn = sql.connect(host="localhost", username="root", password="Harsh_23", database="facerecoglib")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into studdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.stdId_Var.get(),
                                  self.name_Var.get(), self.type_Var.get(), self.course_Var.get(), self.year_Var.get(), self.sem_Var.get(),
                                  self.sec_Var.get(), self.rollNo_Var.get(), self.gender_Var.get(), self.dob_Var.get(), self.email_Var.get(),
                                  self.phone_Var.get(), self.address_Var.get(), self.teacher_Var.get(), self.radioBtn_Var.set("No"),0))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Details Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Fail To Add Details\nDue To: {es}",parent=self.root)

    # -------------- FETCHING STUDENT DETAILS FUNCTION ------------------ #
    def fetch_data(self):
        conn = sql.connect(host="localhost", username="root", password="Harsh_23", database="facerecoglib")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from studdata")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.studentTable.delete(*self.studentTable.get_children())
            for i in data:
                self.studentTable.insert("",END,values=i)
                conn.commit()
        conn.close()

    # ----------------- UPDATING STUDENT DETAILS FUNCTION ------------------- #
    def update_data(self):
        if (self.stdId_Var.get() == "Select Type" or self.course_Var.get() == "Select Course" or
            self.year_Var.get() == "Select Year" or self.sem_Var.get() == "Select Semester" or
            self.stdId_Var.get() == "" or self.name_Var.get() == "" or self.sec_Var.get() == "Select Section" or
            self.rollNo_Var.get() == "" or self.email_Var.get() == "" or self.gender_Var.get() == "Select Gender" or
            self.dob_Var.get() == "" or self.phone_Var.get() == "" or self.address_Var.get() == "" or
            self.teacher_Var.get() == ""):
                messagebox.showerror("Error", "All fields are required!!", parent=self.root)

        elif (not self.stdId_Var.get().isdigit()):
            messagebox.showerror("Error","Student Id is Invalid", parent=self.root)

        elif (self.checkExists(self.stdId_Var.get()) == False):
            messagebox.showerror("Error","Student Id does not Exist", parent=self.root)

        elif (not self.rollNo_Var.get().isdigit()):
            messagebox.showerror("Error","Roll Number is Invalid", parent=self.root)

        elif (len(self.phone_Var.get())!=10 or (not self.phone_Var.get().isdigit())):
            messagebox.showerror("Error","Phone Number is Invalid", parent=self.root)

        else:
            choice = messagebox.askyesno("Confirm","Do you really want to update details",parent=self.root)
            if(choice!=0):
                try:
                    conn = sql.connect(host="localhost", username="root", password="Harsh_23", database="facerecoglib")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update studdata set name=%s,type=%s,course=%s,year=%s,sem=%s,sec=%s,roll=%s,gender=%s,"
                                      "dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photoSample=%s where studId=%s",(
                                      self.name_Var.get(), self.type_Var.get(), self.course_Var.get(), self.year_Var.get(), self.sem_Var.get(),
                                      self.sec_Var.get(), self.rollNo_Var.get(), self.gender_Var.get(), self.dob_Var.get(), self.email_Var.get(),
                                      self.phone_Var.get(), self.address_Var.get(), self.teacher_Var.get(), self.radioBtn_Var.get(),self.stdId_Var.get()))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Details Updated Successfully", parent=self.root)
                except Exception:
                    messagebox.showerror("Error",f"Fail To Update Details\nDue To: {self}",parent=self.root)
            else:
                return

    # ----------------- DELETING STUDENT DETAILS FUNCTION -------------------#
    def delete_data(self):
        if (self.stdId_Var.get() == ""):
            messagebox.showerror("Error","Student Id Must Be Required", parent=self.root)
        elif (self.checkExists(self.stdId_Var.get()) == False):
            messagebox.showerror("Error","Student Id Does Not Exist", parent=self.root)
        else:
            choice = messagebox.askyesno("Confirm","Do you really want to delete details",parent=self.root)
            if(choice != 0):
                try:
                    conn = sql.connect(host="localhost", username="root", password="Harsh_23", database="facerecoglib")
                    my_cursor = conn.cursor()
                    my_cursor.execute(f"delete from studdata where studId={self.stdId_Var.get()}")
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    self.reset_data()
                    messagebox.showinfo("Success", "Details Deleted Successfully", parent=self.root)
                except Exception:
                    messagebox.showerror("Error", f"Fail To Delete Details\nDue To: {self}", parent=self.root)
            else:
                return

    # ----------------- AUTO FILL STUDENT DETAILS FUNCTION -------------------#
    def fill_data(self,event):
        cursor_focus = self.studentTable.focus()
        content = self.studentTable.item(cursor_focus)
        data = content["values"]

        self.stdId_Var.set(data[0])
        self.name_Var.set(data[1])
        self.type_Var.set(data[2])
        self.course_Var.set(data[3])
        self.year_Var.set(data[4])
        self.sem_Var.set(data[5])
        self.sec_Var.set(data[6])
        self.rollNo_Var.set(data[7])
        self.gender_Var.set(data[8])
        self.dob_Var.set(data[9])
        self.email_Var.set(data[10])
        self.phone_Var.set(data[11])
        self.address_Var.set(data[12])
        self.teacher_Var.set(data[13])
        self.radioBtn_Var.set(data[14])

    # ----------------- RESET STUDENT DETAILS FUNCTION -------------------#
    def reset_data(self):
        self.stdId_Var.set("")
        self.name_Var.set("")
        self.type_Var.set("Select Type")
        self.course_Var.set("Select Course")
        self.year_Var.set("Select Year")
        self.sem_Var.set("Select Semester")
        self.sec_Var.set("Select Section")
        self.rollNo_Var.set("")
        self.gender_Var.set("Select Gender")
        self.dob_Var.set("")
        self.email_Var.set("")
        self.phone_Var.set("")
        self.address_Var.set("")
        self.teacher_Var.set("")
        self.radioBtn_Var.set("")



    #########################  GENERATING DATA SETS OR TAKE PHOTO SAMPLES  ###########################
    def generate_dataset(self):
        if (self.stdId_Var.get() == "Select Type" or self.course_Var.get() == "Select Course" or
            self.year_Var.get() == "Select Year" or self.sem_Var.get() == "Select Semester" or
            self.stdId_Var.get() == "" or self.name_Var.get() == "" or self.sec_Var.get() == "Select Section" or
            self.rollNo_Var.get() == "" or self.email_Var.get() == "" or self.gender_Var.get() == "Select Gender" or
            self.dob_Var.get() == "" or self.phone_Var.get() == "" or self.address_Var.get() == "" or
            self.teacher_Var.get() == ""):
                messagebox.showerror("Error", "All fields are required!!", parent=self.root)

        elif not self.stdId_Var.get().isdigit():
            messagebox.showerror("Error","Student Id is Invalid", parent=self.root)

        elif self.checkExists(self.stdId_Var.get()) == False:
            messagebox.showerror("Error","Student Id does not Exist", parent=self.root)

        elif not self.rollNo_Var.get().isdigit():
            messagebox.showerror("Error","Roll Number is Invalid", parent=self.root)

        elif len(self.phone_Var.get())!=10 or not self.phone_Var.get().isdigit():
            messagebox.showerror("Error","Phone Number is Invalid", parent=self.root)

        elif self.isPhotoExist(self.stdId_Var.get()):
            messagebox.showerror("Error","Student Image already exists!",parent=self.root)

        else:
            try:
                id = int(self.stdId_Var.get())

                conn = sql.connect(host="localhost", username="root", password="Harsh_23", database="facerecoglib")
                my_cursor = conn.cursor()
                '''
                for x in myResult:
                    id +=1
                my_cursor.execute("update studdata set name=%s,type=%s,course=%s,year=%s,sem=%s,sec=%s,roll=%s,gender=%s,"
                                  "dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photoSample=%s where studId=%s", (
                                      self.name_Var.get(), self.type_Var.get(), self.course_Var.get(), self.year_Var.get(),
                                      self.sem_Var.get(),
                                      self.sec_Var.get(), self.rollNo_Var.get(), self.gender_Var.get(), self.dob_Var.get(),
                                      self.email_Var.get(),
                                      self.phone_Var.get(), self.address_Var.get(), self.teacher_Var.get(),
                                      self.radioBtn_Var.get(), self.stdId_Var.get()==id+1))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                '''

                # --------------------  LOAD PREDEFINED DATA ON FACE FRONTAL FROM OPENCV  ------------------ #

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor -> 1.3
                    # minimum neighbour -> 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                # Opening camera window, 0 -> pc default camera
                cap = cv2.VideoCapture(0)
                img_id = 0
                imgBackground = cv2.imread("C:/Users/Harsh Sri/PycharmProjects/FaceRecog/Face Recog Library/Photo Sample Canvas.png")
                while True:
                    ret, newFrame = cap.read()
                    if face_cropped(newFrame) is not None:
                        img_id += 1
                        # cropping captured images 450 width, 450 height
                        face = cv2.resize(face_cropped(newFrame),(640,480))
                        # converting captured images in GrayScale(black & white)
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        imgBackground[168:168+480,92:92+640] = newFrame
                        # creating captured image name like (stud.1.12jpg)
                        file_path = "Face Asset/stud."+str(id)+"."+str(img_id)+".jpg"
                        # storing image to the Asset folder [imwirte() -> saves an image to a specified file]
                        cv2.imwrite(file_path,face)
                        # adding counter text on the camera window
                        # cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",imgBackground)


                    # Camera window closes when press 13(Enter key) or 50 samples done
                    if cv2.waitKey(1) == 13 or int(img_id) == 50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                self.radioBtn_Var.set("Yes")

                # Updating Photo sample status to YES
                my_cursor.execute("update studdata set photoSample=%s where studId=%s", ("Yes",id))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Result","New Dataset Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Adding DataSets Failed\nDue to: {es}",parent=self.root)


    def delete_Datasets(self):
        studId = self.stdId_Var.get()
        if (self.stdId_Var.get() == "Select Type" or self.course_Var.get() == "Select Course" or
            self.year_Var.get() == "Select Year" or self.sem_Var.get() == "Select Semester" or
            self.stdId_Var.get() == "" or self.name_Var.get() == "" or self.sec_Var.get() == "Select Section" or
            self.rollNo_Var.get() == "" or self.email_Var.get() == "" or self.gender_Var.get() == "Select Gender" or
            self.dob_Var.get() == "" or self.phone_Var.get() == "" or self.address_Var.get() == "" or
            self.teacher_Var.get() == ""):
                messagebox.showerror("Error", "All fields are required!!", parent=self.root)

        elif not self.stdId_Var.get().isdigit():
            messagebox.showerror("Error","Student Id is Invalid", parent=self.root)

        elif self.checkExists(self.stdId_Var.get()) == False:
            messagebox.showerror("Error","Student Id does not Exist", parent=self.root)

        elif not self.rollNo_Var.get().isdigit():
            messagebox.showerror("Error","Roll Number is Invalid", parent=self.root)

        elif len(self.phone_Var.get())!=10 or (not self.phone_Var.get().isdigit()):
            messagebox.showerror("Error","Phone Number is Invalid", parent=self.root)

        elif self.isPhotoExist(studId) == False:
            messagebox.showerror("Error", "Student Image not found", parent=self.root)

        else:
            choice = messagebox.askyesno("Confirm", "Do you really want to delete photo samples?",parent=self.root)
            if choice != 0:
                os.chdir(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Asset")
                photoId = 1
                for file in os.listdir():
                    if file.split('.')[1] == studId:
                        path = "C:/Users/Harsh Sri/PycharmProjects/FaceRecog/Face Asset/stud.1."+str(photoId)+".jpg"
                        os.remove(path)
                        photoId += 1
                conn = sql.connect(host="localhost", username="root", password="Harsh_23", database="facerecoglib")
                my_cursor = conn.cursor()
                my_cursor.execute("update studdata set photoSample=%s where studId=%s",("No",studId))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Photo samples removed successfully", parent=self.root)
            else:
                return




    # def delPhotos(self,id):
    #     os.chdir(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Asset")
    #     photoId = 1
    #     for file in os.listdir():
    #         if file.split('.')[1] == id:
    #             path = "C:/Users/Harsh Sri/PycharmProjects/FaceRecog/Face Asset/stud.1." + str(photoId) + ".jpg"
    #             os.remove(path)
    #             photoId += 1


    def isPhotoExist(self,id):
        conn = sql.connect(host="localhost", username="root", password="Harsh_23", database="facerecoglib")
        my_cursor = conn.cursor()
        my_cursor.execute("select photoSample from studdata where studId=%s",(id,))
        myResult = my_cursor.fetchall()
        if myResult[0][0] == "Yes":
            return True
        else:
            return False





if __name__ == "__main__":
    root = Tk()
    obj = add_Student(root)
    root.mainloop()