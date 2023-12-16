from tkinter import*
from PIL import Image, ImageTk
import mysql.connector as sql
import time

class My_Account:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Dashboard")
        self.root.state('zoomed')

        studDetail = self.fetchData()

        def get_time():
            timeVar = time.strftime("%d-%m-%Y")
            clock.config(text=timeVar)
            clock.after(200, get_time)


        # -------------------------- BACKGROUND IMAGES  ---------------------------
        # Setting Background image
        img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\student_details.jpg")
        self.photoimg = ImageTk.PhotoImage(img)
        bgImage = Label(self.root, image=self.photoimg)
        bgImage.place(x=0, y=0, width=1536, height=864)

        # ########################### FRAME CREATION #############################
        main_frame = Frame(bgImage, bd=2, bg="white")
        main_frame.place(x=20, y=100, width=380, height=500)

        # ----------- Profile Photo Addition ------------ #
        profile = Frame(main_frame, width=105, height=105)
        profile.place(x=120, y=20)

        if studDetail[8] == "Male":
            self.frame_bg = ImageTk.PhotoImage(
                file="C:/Users/Harsh Sri/PycharmProjects/FaceRecog/Face Recog Library/male_profile.png")
            Label(profile, image=self.frame_bg).pack()
        else:
            self.frame_bg = ImageTk.PhotoImage(
                file="C:/Users/Harsh Sri/PycharmProjects/FaceRecog/Face Recog Library/female_profile.png")
            Label(profile, image=self.frame_bg).pack()

        # ----------- Verification Image ------------ #
        badgeImage = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\verified.png")
        self.bgimage = ImageTk.PhotoImage(badgeImage)
        check = Label(self.root, image=self.bgimage)
        check.place(x=35, y=238, width=40, height=40)

        verified_lbl = Label(main_frame, text="Verified", font=("Trebuchet MS", 12,"bold"), fg="#193335", bg="white")
        verified_lbl.place(x=50, y=140)

        # ----------- Calendar Image ------------ #
        dateImage = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\date.png")
        self.datebgImage = ImageTk.PhotoImage(dateImage)
        date_lbl = Label(self.root, image=self.datebgImage)
        date_lbl.place(x=250, y=238, width=40, height=40)

        clock = Label(main_frame, font=("Trebuchet MS", 11, "bold"), fg="#193335", bg="white")
        clock.place(x=265, y=141)

        # Calling date display function
        get_time()

        # ====================================== PROFILE BOUNDARY FRAME ======================================= #
        mainFrame_boundary = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, font=("Trebuchet MS", 12, "bold"))
        mainFrame_boundary.place(x=10, y=212, width=355, height=270)

        info_heading = Label(main_frame, text="STUDENT INFO", font=("Trebuchet MS", 13), bg="#E1DFDF", fg="black",width=39)
        info_heading.place(x=11,y=182,width=355, height=30)

        #----------- Student Id ----------#
        studId = Label(mainFrame_boundary, text="Student Id:", font=("Trebuchet MS", 13, "bold"), fg="black", bg="white")
        studId.grid(row=0,column=0,padx=30,pady=20,sticky=W)

        studId_Val = StringVar()
        studId_lbl = Label(mainFrame_boundary, textvariable=studId_Val, font=("Trebuchet MS", 12), fg="#193335",
                           bg="white")
        studId_lbl.grid(row=0,column=1,padx=10,sticky=W)
        studId_Val.set(studDetail[0])

        # ----------- Student Name ----------#
        studName = Label(mainFrame_boundary, text="Name:", font=("Trebuchet MS", 13, "bold"), fg="black", bg="white")
        studName.grid(row=1,column=0,padx=30,pady=0,sticky=W)

        studName_Val = StringVar()
        studName_lbl = Label(mainFrame_boundary, textvariable=studName_Val, font=("Trebuchet MS", 12), fg="#193335",
                           bg="white")
        studName_lbl.grid(row=1,column=1,padx=10,sticky=W)
        studName_Val.set(studDetail[1])

        # ----------- Student Roll Number ----------#
        studRoll = Label(mainFrame_boundary, text="Roll no:", font=("Trebuchet MS", 13, "bold"), fg="black", bg="white")
        studRoll.grid(row=2,column=0,padx=30,pady=20,sticky=W)

        studRoll_Val = StringVar()
        studCount_lbl = Label(mainFrame_boundary, textvariable=studRoll_Val, font=("Trebuchet MS", 12), fg="#193335",
                           bg="white")
        studCount_lbl.grid(row=2,column=1,padx=10,sticky=W)
        studRoll_Val.set(studDetail[7])

        # ----------- Student Course ----------#
        studCourse = Label(mainFrame_boundary, text="Enrolled in:", font=("Trebuchet MS", 13, "bold"), fg="black", bg="white")
        studCourse.grid(row=3,column=0,padx=30,pady=0,sticky=W)

        studCourse_Val = StringVar()
        studCourse_lbl = Label(mainFrame_boundary, textvariable=studCourse_Val, font=("Trebuchet MS", 12),fg="#193335",
                               bg="white")
        studCourse_lbl.grid(row=3,column=1,padx=10,sticky=W)
        studCourse_Val.set(studDetail[3])

        # ----------- Student Gender ----------#
        studGen = Label(mainFrame_boundary, text="Gender:", font=("Trebuchet MS", 13, "bold"), fg="black",
                            bg="white")
        studGen.grid(row=4,column=0,padx=30,pady=20,sticky=W)

        studGen_Val = StringVar()
        studGen_lbl = Label(mainFrame_boundary, textvariable=studGen_Val, font=("Trebuchet MS", 12),fg="#193335",
                               bg="white")
        studGen_lbl.grid(row=4,column=1,padx=10,sticky=W)
        studGen_Val.set(studDetail[8])

        ################################   RIGHT FRAME  ####################################
        right_frame = Frame(bgImage, bd=2, bg="white")
        right_frame.place(x=420, y=100, width=1080, height=660)

        ###############################  ACADEMIC INFO FRAME BOUNDARY  ##############################

        academic_heading = Label(right_frame, text="STUDENT ACADEMIC INFO", font=("Trebuchet MS", 13), bg="#E1DFDF",
                                 fg="black", justify="right")
        academic_heading.place(x=20, y=20, width=1035, height=40)

        academicHeading_boundary = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, font=("Trebuchet MS", 12, "bold"))
        academicHeading_boundary.place(x=20, y=60, width=1035, height=210)

        course = Label(academicHeading_boundary, text="Course:", font=("Trebuchet MS", 13), fg="black",
                       bg="white")
        course.grid(row=0, column=0, padx=50, pady=20, sticky=W)

        course_lbl = Label(academicHeading_boundary, textvariable=studCourse_Val, font=("Trebuchet MS", 13),
                           fg="#343434", bg="white")
        course_lbl.grid(row=0, column=1, padx=20, sticky=W)

        studYear = Label(academicHeading_boundary, text="Session:", font=("Trebuchet MS", 13), fg="black",
                         bg="white")
        studYear.grid(row=0, column=2, padx=100, pady=20, sticky=W)

        studYear_val = StringVar()
        studYear_lbl = Label(academicHeading_boundary, textvariable=studYear_val, font=("Trebuchet MS", 13),
                             fg="#343434", bg="white")
        studYear_lbl.grid(row=0, column=3, padx=20, sticky=W)
        studYear_val.set(studDetail[4])

        studSem = Label(academicHeading_boundary, text="Current Semester:", font=("Trebuchet MS", 13), fg="black",
                        bg="white")
        studSem.grid(row=2, column=0, padx=50, pady=10, sticky=W)

        studSem_val = StringVar()
        studSem_lbl = Label(academicHeading_boundary, textvariable=studSem_val, font=("Trebuchet MS", 13),
                            fg="#343434", bg="white")
        studSem_lbl.grid(row=2, column=1, padx=20, sticky=W)
        studSem_val.set(studDetail[5])

        studSec = Label(academicHeading_boundary, text="Section:", font=("Trebuchet MS", 13), fg="black",
                        bg="white")
        studSec.grid(row=2, column=2, padx=100, pady=0, sticky=W)

        studSec_val = StringVar()
        studSec_lbl = Label(academicHeading_boundary, textvariable=studSec_val, font=("Trebuchet MS", 13),
                            fg="#343434", bg="white")
        studSec_lbl.grid(row=2, column=3, padx=20, sticky=W)
        studSec_val.set(studDetail[6])

        studAttend = Label(academicHeading_boundary, text="Class Attended:", font=("Trebuchet MS", 13), fg="black",
                        bg="white")
        studAttend.grid(row=3, column=0, padx=50, pady=15, sticky=W)

        attend = self.getCount(studDetail[0])
        studAttend_lbl = Label(academicHeading_boundary, text=f'{attend}/240', font=("Trebuchet MS", 13),
                            fg="#343434", bg="white")
        studAttend_lbl.grid(row=3, column=1, padx=20, sticky=W)

        teacher = Label(academicHeading_boundary, text="Assigned Tecaher:", font=("Trebuchet MS", 13), fg="black",
                        bg="white")

        teacher.grid(row=3, column=2, padx=100, pady=15, sticky=W)

        teacher_val = StringVar()
        teacher_lbl = Label(academicHeading_boundary,textvariable=teacher_val, font=("Trebuchet MS", 13),
                            fg="#343434", bg="white")
        teacher_lbl.grid(row=3, column=3, padx=20, sticky=W)
        teacher_val.set(studDetail[13])




        # --------------------------------  PERSONAL INFO FRAME BOUNDARY ----------------------------- #

        personal_heading = Label(right_frame, text="STUDENT PERSONAL INFO", font=("Trebuchet MS", 13), bg="#E1DFDF",
                                 fg="black", justify="right")
        personal_heading.place(x=20, y=300, width=1035, height=40)

        personalHeading_boundary = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                              font=("Trebuchet MS", 12, "bold"))
        personalHeading_boundary.place(x=20, y=340, width=1035, height=290)

        # ============================  LABELS  ============================ #

        studName2 = Label(personalHeading_boundary, text="Student Name:", font=("Trebuchet MS", 13), fg="black",
                          bg="white")
        studName2.grid(row=0, column=0, padx=50, pady=20, sticky=W)

        studName_lbl2 = Label(personalHeading_boundary, textvariable=studName_Val, font=("Trebuchet MS", 13),
                              fg="#343434", bg="white")
        studName_lbl2.grid(row=0, column=1, padx=20, sticky=W)

        studPhone = Label(personalHeading_boundary, text="Phone Number:", font=("Trebuchet MS", 13), fg="black",
                          bg="white")
        studPhone.grid(row=1, column=0, padx=50, pady=0, sticky=W)

        studPhone_Val = StringVar()
        studPhone_lbl = Label(personalHeading_boundary, textvariable=studPhone_Val, font=("Trebuchet MS", 13),
                              fg="#343434", bg="white")
        studPhone_lbl.grid(row=1, column=1, padx=20, sticky=W)
        studPhone_Val.set(studDetail[11])

        # Saving Address in form of list for extracting building no, city, country separately
        fullAdd = self.extractAddress()

        studStreet = Label(personalHeading_boundary, text="Address:", font=("Trebuchet MS", 13), fg="black",
                           bg="white")
        studStreet.grid(row=2, column=0, padx=50, pady=15, sticky=W)

        studStreet_Val = StringVar()
        studStreet_lbl = Label(personalHeading_boundary, textvariable=studStreet_Val, font=("Trebuchet MS", 13),
                               fg="#343434", bg="white")
        studStreet_lbl.grid(row=2, column=1, padx=20, sticky=W)
        studStreet_Val.set(fullAdd[0])

        studCity = Label(personalHeading_boundary, text="City:", font=("Trebuchet MS", 13), fg="black",
                         bg="white")
        studCity.grid(row=3, column=0, padx=50, pady=15, sticky=W)

        studCity_Val = StringVar()
        studCity_lbl = Label(personalHeading_boundary, textvariable=studCity_Val, font=("Trebuchet MS", 13),
                             fg="#343434", bg="white")
        studCity_lbl.grid(row=3, column=1, padx=20, sticky=W)
        studCity_Val.set(fullAdd[1].strip(" "))

        # ---------- Email Label ----------- #

        studEmail = Label(personalHeading_boundary, text="Email id:", font=("Trebuchet MS", 13), fg="black",
                          bg="white")
        studEmail.grid(row=0, column=2, padx=100, pady=20, sticky=W)

        studEmail_Val = StringVar()
        studEmail_lbl = Label(personalHeading_boundary, textvariable=studEmail_Val, font=("Trebuchet MS", 13),
                              fg="#343434", bg="white")
        studEmail_lbl.grid(row=0, column=3, sticky=W)
        studEmail_Val.set(studDetail[10])

        studDob = Label(personalHeading_boundary, text="Date Of Birth:", font=("Trebuchet MS", 13), fg="black",
                        bg="white")
        studDob.grid(row=1, column=2, padx=100, pady=15, sticky=E)

        studDob_Val = StringVar()
        studDob_lbl = Label(personalHeading_boundary, textvariable=studDob_Val, font=("Trebuchet MS", 13),
                            fg="#343434", bg="white")
        studDob_lbl.grid(row=1, column=3, sticky=W)
        studDob_Val.set(studDetail[9])

        # Saving age by converting it from user age with current age
        age = self.getAge()
        age = str(age)

        studAge = Label(personalHeading_boundary, text="Age:", font=("Trebuchet MS", 13), fg="black",
                        bg="white")
        studAge.grid(row=2, column=2, padx=100, pady=15, sticky=W)

        studAge_lbl = Label(personalHeading_boundary, text=f"{age} yrs", font=("Trebuchet MS", 13),
                            fg="#343434", bg="white")
        studAge_lbl.grid(row=2, column=3, sticky=W)

        studState = Label(personalHeading_boundary, text="State:", font=("Trebuchet MS", 13), fg="black",
                          bg="white")
        studState.grid(row=3, column=2, padx=100, pady=15, sticky=W)

        studState_Val = StringVar()
        studState_lbl = Label(personalHeading_boundary, textvariable=studState_Val, font=("Trebuchet MS", 13),
                              fg="#343434", bg="white")
        studState_lbl.grid(row=3, column=3, sticky=W)
        studState_Val.set(fullAdd[2].strip(" "))



    ##############################   FUNCTIONS IMPLEMENTATION   ################################


    def getId(self):
        file = open("StudId.txt", 'r')
        val = file.read()
        file.close()
        return val

    def fetchData(self):
        studId = self.getId()
        conn = sql.connect(host="localhost", user="root", password="Harsh_23",
                           database="facerecoglib")
        my_cursor = conn.cursor()
        my_cursor.execute(f"select * from studdata where studId = {studId}")
        studDetails = my_cursor.fetchone()
        return studDetails

    def getAge(self):
        studDetails = self.fetchData()
        year = studDetails[9].split('-')
        year = year[2]
        currYear = time.strftime('%Y')
        finalAge = int(currYear)-int(year)
        return finalAge

    def extractAddress(self):
        studDetails = self.fetchData()
        full_add = studDetails[12].split(',')

        address = []

        street = full_add[0].removeprefix("'")
        street = street.removesuffix("'")

        city = full_add[1].removeprefix("' ")
        city = city.removesuffix("'")

        country = full_add[2].removeprefix("' ")
        country = country.removesuffix("'")

        address.append(street)
        address.append(city)
        address.append(country)

        return address


    def getCount(self,id):
        conn = sql.connect(host="localhost", user="root", password="Harsh_23",
                           database="facerecoglib")
        my_cursor = conn.cursor()
        my_cursor.execute(f"select attendCount from studdata where studId={id}")
        attendCount = my_cursor.fetchone()
        attendCount = attendCount[0]
        return attendCount

















if __name__ == "__main__":
    root = Tk()
    obj = My_Account(root)
    root.mainloop()