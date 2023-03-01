#from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start
        # first header image
       
        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------

        title_label = Label(self.root,text = "FACE RECOGNITION",font=("times new roman",35,"bold"),bg = "maroon" , fg = "yellow")
        title_label.place(x=0,y=0,width=1530,height=56)

        # 1 image

        img_top = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\shutterstock_1046253838_small.jpg")
        img_top = img_top.resize((650,700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=55, width=650, height=700)

        # 2 image

        img_bot = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.webp")
        img_bot = img_bot.resize((950,700), Image.LANCZOS)
        self.photoimg_bot = ImageTk.PhotoImage(img_bot)

        f_label = Label(self.root, image=self.photoimg_bot)
        f_label.place(x=650, y=55, width=950, height=640)
        
        # Training button 1

        b1 = Button(f_label,text="Face Recognition",command =self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg = "gold" , fg = "black")
        b1.place(x=365, y=560, width=200, height=40)

    # =====================Attendance===================

    def mark_attendance(self,a,r,n,i):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((a not in name_list)) and ((r not in name_list)) and ((n not in name_list))and ((i not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{a}, {r}, {n},{i}, {dtString}, {d1}, Present")

    # ================face recognition==================
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            featuers = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in featuers:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(username='root', password='Football.321', host='localhost',
                                               database='face_recognitions')
                cursor = conn.cursor()

                

                cursor.execute("select ID from studentss where ID=" + str(id))
                a = cursor.fetchone()
                a = "+".join(a)

                cursor.execute("select roll_no from studentss where ID=" + str(id))
                r = cursor.fetchone()
                r = "+".join(r)

                cursor.execute("select name from studentss where ID=" + str(id))
                n = cursor.fetchone()
                n = "+".join(n)

                cursor.execute("select dep from studentss where ID=" + str(id))
                i = cursor.fetchone()
                i = "+".join(i)

                

                if confidence > 77:
                    cv2.putText(img, f"ID:{a}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll Number:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Department:{i}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(a,r,n,i)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, y]

            return coord

            # ==========

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()