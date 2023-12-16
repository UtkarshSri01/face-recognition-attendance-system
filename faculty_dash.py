import os
from tkinter import*
from tkinter import messagebox as msg
import cv2
from PIL import Image, ImageTk
from addStudent import add_Student
from support import Support
from attendance import Attendance_Dash
import numpy as np

class Faculty_Dash:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Faculty Dashboard")
        self.root.state('zoomed')


        # -------------------------- BACKGROUND IMAGES  ---------------------------
        # Setting Background image
        img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\faculty_background.jpg")
        self.photoimg = ImageTk.PhotoImage(img)
        bgImage = Label(self.root, image=self.photoimg)
        bgImage.place(x=0, y=0, width=1536, height=864)


        # --------------------------  BUTTONS CREATION ------------------------------ #

        # Button1 - Add Student
        button_img = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\add_student.png")
        button_img.resize((180,170))
        self.photoimg1=ImageTk.PhotoImage(button_img)

        button1 = Button(self.root,image=self.photoimg1,cursor="hand2",command=self.stud_details)
        button1.place(x=380,y=320,width=180,height=170)

        # Button2 - Attendance
        button_img2 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\attendence.png")
        button_img2.resize((180,170))
        self.photoimg2 = ImageTk.PhotoImage(button_img2)

        button2 = Button(self.root,image=self.photoimg2,cursor="hand2",command=self.attendance_screen)
        button2.place(x=680,y=320,width=180,height=170)

        # Button3 - Help Desk
        button_img3 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\help_support.png")
        button_img3.resize((180,170))
        self.photoimg3=ImageTk.PhotoImage(button_img3)

        button3 = Button(self.root,image=self.photoimg3,cursor="hand2",command=self.support_screen)
        button3.place(x=970,y=320,width=180,height=170)

        # Button4 - Train Data
        button_img4 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\analyze_data.png")
        button_img4.resize((180,170))
        self.photoimg4 = ImageTk.PhotoImage(button_img4)

        button4 = Button(self.root,image=self.photoimg4,command=self.train_classifier, cursor="hand2")
        button4.place(x=240,y=530,width=180,height=170)

        # Button5 - Asset Data
        button_img5 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\asset_data.png")
        button_img5.resize((180,170))
        self.photoimg5=ImageTk.PhotoImage(button_img5)

        button5 = Button(self.root,image=self.photoimg5,cursor="hand2",command=self.asset_folder)
        button5.place(x=540,y=530,width=180,height=170)

        # Button6 - About Us
        button_img6 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\about_us.png")
        button_img6.resize((180,170))
        self.photoimg6=ImageTk.PhotoImage(button_img6)

        button6 = Button(self.root,image=self.photoimg6,cursor="hand2")
        button6.place(x=830,y=530,width=180,height=170)

        # Button7 - Exit
        button_img7 = Image.open(r"C:\Users\Harsh Sri\PycharmProjects\FaceRecog\Face Recog Library\exit.png")
        button_img7.resize((180,170))
        self.photoimg7=ImageTk.PhotoImage(button_img7)

        button7 = Button(self.root,image=self.photoimg7,cursor="hand2",command=self.exitBtn)
        button7.place(x=1120,y=530,width=180,height=170)

    ########################################  FUNCTION BUTTONS  ############################################

    def stud_details(self):
        self.new_window = Toplevel(self.root)
        self.app = add_Student(self.new_window)

    def support_screen(self):
        self.new_window = Toplevel(self.root)
        self.app = Support(self.new_window)

    def attendance_screen(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance_Dash(self.new_window)

    def asset_folder(self):
        os.startfile("Face Asset")

    def train_classifier(self):
        data_dir = "Face Asset"
        path = [os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces = []
        ids = []
        msg.showinfo("Processing", "Training Data Sets In Progress, Please wait for 30 seconds",parent=self.root)
        
        # converting every image portion into grayscale
        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            # cv2.imshow('Training',imageNp)
            # cv2.waitKey(1)

        ids = np.array(ids)

        ###################  TRAINING IMAGES AND SAVING IT  ################
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,np.array(ids))
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        
        msg.showinfo("Result","Training Dataset Complete")

    def exitBtn(self):
        choice = msg.askyesno("Exit","Do you really want to exit!",parent=self.root)
        if choice != 0:
            self.root.destroy()
            # Opening Faculty Window
            os.system("login_screen.py")
        else:
            return




if __name__ == "__main__":
    root = Tk()
    obj = Faculty_Dash(root)
    root.mainloop()
