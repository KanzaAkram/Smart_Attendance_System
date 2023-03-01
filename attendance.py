
import re
from sys import path
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
import csv
from tkinter import filedialog

# Global variable for importCsv Function
mydata = []


class Attendance:

        def __init__(self, root):
            self.root = root
            self.root.geometry("1530x790+0+0")
            self.root.title("Attendance Pannel")


            # -----------Variables-------------------
            self.var_id = StringVar()
            self.var_roll = StringVar()
            self.var_name = StringVar()
            self.var_dep = StringVar()
            self.var_time = StringVar()
            self.var_date = StringVar()
            self.var_attend = StringVar()

            # This part is image labels setting start
            # first header image
            #FIRST image

            img1 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\What-is-the-importance-of-facial-recognition-in-todays-world.jpg")
            img1 = img1.resize((800, 200), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_label = Label(self.root, image=self.photoimg1)
            f_label.place(x=0, y=0, width=750, height=200)

            # Second image

            img2 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\face-recognition-attendance-system.jpg")
            img2 = img2.resize((800, 200), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_label = Label(self.root, image=self.photoimg2)
            f_label.place(x=750, y=0, width=800, height=200)

            
            # BACKGROUND IMAGE

            img = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\vector-abstract-background-design-wavy.jpg")
            img = img.resize((1530, 790), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)

            bg_image = Label(self.root, image=self.photoimg)
            bg_image.place(x=0, y=200, width=1530, height=790)

            # title section

            title_label = Label(bg_image, text="ATTENDANCE  MANAGEMENT  SYSTEM", font=("times new roman", 35, "bold"), bg="black",fg="yellow")
            title_label.place(x=0, y=0, width=1530, height=50)

            # ========================Section Creating==================================

            # Creating Frame
            main_frame = Frame(bg_image,bd=3,background="coral1")
            main_frame.place(x=5,y=55,width=1350,height=430)

        
            #left side label frame

            left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details" ,background="bisque", font=("times new roman" ,12,"bold" ))
            left_frame.place(x=10,y=10,width=655,height=400)

            img_left = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\pattern-vector-dark-background-wallpaper-preview.jpg")
            img_left = img_left.resize((645, 80), Image.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)

            f_label = Label(left_frame, image=self.photoimg_left)
            f_label.place(x=5, y=0, width=645, height=40)

            left_inside_frame = Frame(left_frame,bd=3,relief=RIDGE,background="LightGoldenrod1")
            left_inside_frame.place(x=6,y=60,width=640,height=300)

            # right side label frame

            right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", background="bisque",font=("times new roman", 12, "bold"))
            right_frame.place(x=680, y=10, width=655, height=400)

            img_right = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\pattern-vector-dark-background-wallpaper-preview.jpg")
            img_right = img_right.resize((645, 80), Image.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)

            f_label = Label(right_frame, image=self.photoimg_right)
            f_label.place(x=2, y=0, width=645, height=40)

            # ==================================Text boxes and Combo Boxes====================

            #ATTENDANCE ID
            attendanceid_label = Label(left_inside_frame, text="Attendance ID", font=("times new roman", 12, "bold"), bg="salmon")
            attendanceid_label.grid(row=0, column=0,pady=12,padx=8, sticky=W)

            attendanceid_entry = ttk.Entry(left_inside_frame,textvariable = self.var_id,width=20,font=("times new roman", 12, "bold"))
            attendanceid_entry.grid(row=0,column=1,padx=10,pady = 12,sticky=W)


            # Name
            rollLabel = Label(left_inside_frame, text="Roll Number:", font=("times new roman", 12, "bold"), bg="salmon")
            rollLabel.grid(row=0, column=2,pady=12, sticky=W)

            attendanceroll_entry = ttk.Entry(left_inside_frame,textvariable = self.var_roll,width=20,font=("times new roman", 12, "bold"))
            attendanceroll_entry.grid(row=0,column=3,padx=8,pady = 12,sticky=W)

            #Date

            nameLabel = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="salmon")
            nameLabel.grid(row=1, column=0)

            attendancename = ttk.Entry(left_inside_frame,textvariable = self.var_name,width=20,font=("times new roman", 12, "bold"))
            attendancename.grid(row=1,column=1,padx=8,sticky=W)


            #Department

            depLabel = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="salmon")
            depLabel.grid(row=1, column=2)

            attendancedep = ttk.Entry(left_inside_frame,textvariable = self.var_dep,width=20,font=("times new roman", 12, "bold"))
            attendancedep.grid(row=1,column=3,padx=8,sticky=W)

            #Time

            timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="salmon")
            timeLabel.grid(row=2, column=0,pady=12)

            attendancetime = ttk.Entry(left_inside_frame,textvariable = self.var_time,width=20,font=("times new roman", 12, "bold"))
            attendancetime.grid(row=2,column=1,padx=8,sticky=W,pady=12)

            #Date

            dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="salmon")
            dateLabel.grid(row=2, column=2)

            attendancedate = ttk.Entry(left_inside_frame,textvariable = self.var_date,width=20,font=("times new roman", 12, "bold"))
            attendancedate.grid(row=2,column=3,padx=8,sticky=W)



            #Attendance

            attendancelabel1 = Label(left_inside_frame,text="Attendance Status",font=("times new roman", 12, "bold"), bg="salmon")
            attendancelabel1.grid(row=3,column=0,padx=8)

            self.attendance_status = ttk.Combobox(left_inside_frame,textvariable = self.var_attend,width=20,font=("times new roman", 12, "bold"),state="readonly")
            self.attendance_status["values"] = ("Status","Present","Absent")
            self.attendance_status.grid(row=3,column=1,pady=8,padx=8)
            self.attendance_status.current(0)

            #buttons frame
            btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="salmon")
            btn_frame.place(x=0,y=259,width=700,height=35)

            save_btn = Button(btn_frame,text="Import csv" , command = self.importCsv,font=("times new roman", 12, "bold"),bg="black" , fg="yellow",width=22 )
            save_btn.grid(row=0,column=0)

            update_btn = Button(btn_frame, text="Export csv", command = self.exportCsv,font=("times new roman", 12, "bold"), bg="black", fg="yellow",width=24)
            update_btn.grid(row=0, column=1 )

            reset_btn = Button(btn_frame, command = self.reset_data,text="Reset", font=("times new roman", 12, "bold"), bg="black", fg="yellow",width=22)
            reset_btn.grid(row=0, column=3 )


            # ===============================Table Sql Data View==========================
            table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
            table_frame.place(x=10, y=50, width=635, height=315)

            # scroll bar
            scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

            # create table
            self.attendanceReport_left = ttk.Treeview(table_frame,
                                                    column=("ID", "Roll_No", "Name", "Department","Time", "Date", "Attendance"),
                                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.attendanceReport_left.xview)
            scroll_y.config(command=self.attendanceReport_left.yview)

            self.attendanceReport_left.heading("ID", text="Std-ID")
            self.attendanceReport_left.heading("Roll_No", text="Roll.No")
            self.attendanceReport_left.heading("Name", text="Std-Name")
            self.attendanceReport_left.heading("Department", text="Department")
            self.attendanceReport_left.heading("Time", text="Time")
            self.attendanceReport_left.heading("Date", text="Date")
            self.attendanceReport_left.heading("Attendance", text="Attendance")
            self.attendanceReport_left["show"] = "headings"

            # Set Width of Colums
            self.attendanceReport_left.column("ID", width=100)
            self.attendanceReport_left.column("Roll_No", width=100)
            self.attendanceReport_left.column("Name", width=100)
            self.attendanceReport_left.column("Department", width=100)
            self.attendanceReport_left.column("Time", width=100)
            self.attendanceReport_left.column("Date", width=100)
            self.attendanceReport_left.column("Attendance", width=100)

            self.attendanceReport_left.pack(fill=BOTH,expand=1)
        
            self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
            
# ===========================fatch data form mysql attendance===========

        def fetch_data(self,rows):
            self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
            for i in rows:
                self.attendanceReport_left.insert("",END,values=i)  
            

    # IMPORT CSV
        def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")    #delimeter will apply comma to separate values
                for i in csvread:
                    mydata.append(i)
                self.fetch_data(mydata)

    #EXPORT CSV

        def exportCsv(self):
            try:
                if len(mydata)<1:
                    messagebox.showerror("Error","No Data Found to export!",parent=self.root)
                    return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Successfuly","Exported Data Successfully!"+os.path.basename(fln)+"Successfully")
            except Exception as es:
                    messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  

      # cursor function for csv                

        def get_cursor_left(self,event=""):
            cursor_row = self.attendanceReport_left.focus()
            content = self.attendanceReport_left.item(cursor_row)
            data = content["values"]

            self.var_id.set(data[0]),
            self.var_roll.set(data[1]),
            self.var_name.set(data[2]),
            self.var_dep.set(data[3])
            self.var_time.set(data[4]),
            self.var_date.set(data[5]),
            self.var_attend.set(data[6])

        #RESET FUNCTION

        def reset_data(self):

            self.var_id.set(""),
            self.var_roll.set(""),
            self.var_name.set(""),
            self.var_dep.set("")
            self.var_time.set(""),
            self.var_date.set(""),
            self.var_attend.set("")


           

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()