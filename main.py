import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        # setting geometery
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # FIRST image

        img1 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\recogn.jpg")
        img1 = img1.resize((500, 150), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label = Label(self.root, image=self.photoimg1)
        f_label.place(x=0, y=0, width=500, height=130)

        # Second image

        img2 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\eye-futuristic-robot.jpg")
        img2 = img2.resize((500, 150), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label = Label(self.root, image=self.photoimg2)
        f_label.place(x=500, y=0, width=500, height=130)

        # Third image

        img3 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\face.jpg")
        img3 = img3.resize((500, 150), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_label = Label(self.root, image=self.photoimg3)
        f_label.place(x=1000, y=0, width=500, height=130)

        # BACKGROUND IMAGE

        img = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\blue-brushstrokes-background.jpg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=130, width=1530, height=790)

        #label title

        title_label = Label(bg_image,text = "SMART ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg = "maroon" , fg = "yellow")
        title_label.place(x=0,y=0,width=1530,height=45)



        #time
        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text = string)
            lb1.after(1000,time)

        lb1 = Label(title_label,font=("times new roman",20,"bold"),bg = "gold",foreground="black")
        lb1.place(x=0,y=0,width=170,height=50)
        time()

        #student button
        img4 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\download.jpeg")
        img4 = img4.resize((220,220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_image,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)

        b1 = Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg = "gold" , fg = "black")
        b1.place(x=100, y=300, width=220, height=40)

        # detect face button
        img5 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\2412383.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_image, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=400, y=100, width=220, height=220)

        b1 = Button(bg_image, text="Face Detector", cursor="hand2", command=self.face_data,font=("times new roman", 20, "bold"), bg="gold",fg="black")
        b1.place(x=400, y=300, width=220, height=40)


        # Attendance face button
        img6 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\istockphoto-1059233806-612x612.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_image, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=700, y=100, width=220, height=220)

        b1 = Button(bg_image, text="Attendance", cursor="hand2", command = self.attendance_data,font=("times new roman", 20, "bold"), bg="gold",fg="black")
        b1.place(x=700, y=300, width=220, height=40)


        # Train face button
        img7 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\AI_HERO-58306268c6f4b659459f5b7b2dd3e8a5.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_image, image=self.photoimg7, cursor="hand2")
        b1.place(x=1000, y=100, width=220, height=220)

        b1 = Button(bg_image, text="Train Data", cursor="hand2", font=("times new roman", 20, "bold"), bg="gold",
                    fg="black")
        b1.place(x=1000, y=300, width=220, height=40)

        # Photos face button
        img8 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\download (1).jpeg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_image, image=self.photoimg8, cursor="hand2",command=self.open_img)
        b1.place(x=1000, y=100, width=220, height=220)

        b1 = Button(bg_image, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 20, "bold"), bg="gold",
                    fg="black")
        b1.place(x=1000, y=300, width=220, height=40)

        # Train data button
        img9 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\training data.webp")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_image, image=self.photoimg9, cursor="hand2",command=self.train_data)
        b1.place(x=540, y=360, width=220, height=190)

        b1 = Button(bg_image, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 20, "bold"), bg="gold",
                    fg="black")
        b1.place(x=540, y=520, width=220, height=40)


    def open_img(self):
        os.startfile("data")

    #=============FUNCTIONS BUTTON==================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()