from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox


class Train:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # This part is image labels setting start
        # first header image
        
        # title section
        title_label = Label(self.root,text = "TRAIN DATA SET",font=("times new roman",35,"bold"),bg = "maroon" , fg = "yellow")
        title_label.place(x=0,y=0,width=1530,height=56)

        img_top = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\AI_HERO-58306268c6f4b659459f5b7b2dd3e8a5.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=55, width=1530, height=325)

         # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # Training button 1
        b1 = Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg = "gold" , fg = "black")
        b1.place(x=0, y=380, width=1530, height=60)

        img_bot = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\recogn.jpg")
        img_bot = img_bot.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bot = ImageTk.PhotoImage(img_bot)

        f_label = Label(self.root, image=self.photoimg_bot)
        f_label.place(x=0, y=440, width=1530, height=325)


       

    # ==================Create Function of Training===================

    #Using LBPH ALGORITHM
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []            #images of same person should have same id
        ids = []

        for image in path:                  #images will all come from path to image
            img = Image.open(image).convert('L')  # convert in gray scale image
            imageNp = np.array(img, 'uint8')         #in array uint is a datatype
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training", imageNp)            #title of window which will appear
            cv2.waitKey(1) == 13

        ids = np.array(ids)     #ids will convert to numpy

        # =================Train Classifier=============
        clf = cv2.face.LBPHFaceRecognizer_create()            #stored the algo inside clf
        clf.train(faces, ids)
        clf.write("classifier.xml")         #after training data it is written inside classifier.xml

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Complated!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()