from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Radiobutton
from tkinter import messagebox
import mysql.connector
import cv2


class Student:

    def __init__(self, root):
        self.root = root
        # setting geometery
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #===========variables=========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_roll = StringVar()
        self.var_semester = StringVar()
        self.var_ID = StringVar()
        self.var_name = StringVar()
        self.var_DOB = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
       # self.var_radio1 = StringVar()

#This part is image labels setting start
        #FIRST image

        img1 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\0x0.jpg")
        img1 = img1.resize((500, 150), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label = Label(self.root, image=self.photoimg1)
        f_label.place(x=0, y=0, width=500, height=130)

        # Second image

        img2 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\4-reasons-college-students-struggle.png")
        img2 = img2.resize((500, 150), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label = Label(self.root, image=self.photoimg2)
        f_label.place(x=500, y=0, width=500, height=130)

        # Third image

        img3 = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\2018_03_12_UCR_day1_post-79.jpg")
        img3 = img3.resize((500, 150), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_label = Label(self.root, image=self.photoimg3)
        f_label.place(x=1000, y=0, width=500, height=130)

        # BACKGROUND IMAGE

        img = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\vector-abstract-background-design-wavy.jpg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=130, width=1530, height=790)

        # label title

        title_label = Label(bg_image, text="STUDENT  MANAGEMENT  SYSTEM", font=("times new roman", 35, "bold"), bg="black",fg="yellow")
        title_label.place(x=0, y=0, width=1530, height=45)


        main_frame = Frame(bg_image,bd=3,background="yellow")
        main_frame.place(x=5,y=55,width=1350,height=499)


        #left side label frame

        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details" ,background="bisque", font=("times new roman" ,12,"bold" ))
        left_frame.place(x=10,y=10,width=655,height=478)

        img_left = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\pattern-vector-dark-background-wallpaper-preview.jpg")
        img_left = img_left.resize((645, 80), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_label = Label(left_frame, image=self.photoimg_left)
        f_label.place(x=5, y=0, width=645, height=30)

        #current course information
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course Information",background="bisque",font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=35, width=640, height=115)


        #department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman" ,12,"bold"),bg="salmon")
        dep_label.grid(row=0,column=0,padx=12)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman" ,12,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","CSIT" , "Software Engineering" , "Civil Engineering","Mechanical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="salmon")
        course_label.grid(row=0, column=2, padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="read only",width=20)
        course_combo["values"] = ("Select Course","SE","FE","TE","BE","MS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        #year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="salmon")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="read only",width=20)
        year_combo["values"] = ("Select Year","2017-21","2018-22","2019-23","2020-24","2021-25","2022-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="salmon")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="read only",width=20)
        semester_combo["values"] = ("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information",background="bisque", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=160, width=640, height=180)


        #student id

        student_id_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="salmon")
        student_id_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        student_id_entry = ttk.Entry(class_student_frame,textvariable=self.var_ID,width=20,font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0,column=1,padx=10,sticky=W)


        #student name

        student_name_label = Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"),bg="salmon")
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_name,width=20, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)

    

        # roll number
        roll_no_label = Label(class_student_frame, text="Roll number", font=("times new roman", 12, "bold"),bg="salmon")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"),bg="salmon")
        gender_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, width=18, font=("times new roman", 12, "bold"),state="readonly")
        gender_combo["values"] = ("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # dob
        dob_label = Label(class_student_frame, text="Date of Birth", font=("times new roman", 12, "bold"),bg="salmon")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_DOB, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # email
        email_label = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"), bg="salmon")
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # phone number
        phone_label = Label(class_student_frame, text="Phone Number", font=("times new roman", 12, "bold"), bg="salmon")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"), bg="salmon")
        address_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        #radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(left_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=1,pady=354,padx=20,sticky=W)

        radiobtn2 = ttk.Radiobutton(left_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=2,padx=60,sticky=W)


        #buttons frame
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="salmon")
        btn_frame.place(x=0,y=390,width=715,height=90)

        save_btn = Button(btn_frame,text="Save" ,command=self.add_data,font=("times new roman", 12, "bold"),bg="black" , fg="yellow",width=17 )
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update",command = self.update_data, font=("times new roman", 12, "bold"), bg="black", fg="yellow",width=17)
        update_btn.grid(row=0, column=1 )

        delete_btn = Button(btn_frame, text="Delete",command = self.delete_data, font=("times new roman", 12, "bold"), bg="black", fg="yellow",width=17)
        delete_btn.grid(row=0, column=2 )

        reset_btn = Button(btn_frame, text="Reset",command = self.reset_data, font=("times new roman", 12, "bold"), bg="black", fg="yellow",width=17)
        reset_btn.grid(row=0, column=3 )

        photo_sample_btn = Button(btn_frame,command=self.generate_dataset, text="Take Photo Sample", font=("times new roman", 12, "bold"), bg="black", fg="yellow",width=17)
        photo_sample_btn.grid(row=1, column=1)



        # right side label frame

        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", background="bisque",font=("times new roman", 12, "bold"))
        right_frame.place(x=680, y=10, width=655, height=478)

        img_right = Image.open(r"C:\Users\kanza\OneDrive\Desktop\smart attendance system\Images\pattern-vector-dark-background-wallpaper-preview.jpg")
        img_right = img_right.resize((645, 80), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_label = Label(right_frame, image=self.photoimg_right)
        f_label.place(x=5, y=0, width=645, height=30)


        #==========SEARCH SYSTEM================
        
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System",background="bisque", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=32, width=635, height=70)

        search_label = Label(search_frame, text="Search By", font=("times new roman", 12, "bold"), bg="salmon")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.var_searchTX=StringVar()

        search_combo = ttk.Combobox(search_frame,textvariable=self.var_searchTX, font=("times new roman", 12, "bold"), state="read only",width=15)
        search_combo["values"] = ("Select", "Roll number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        self.var_search = StringVar()

        search_entry = ttk.Entry(search_frame,textvariable=self.var_search, width=19, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=12, pady=5, sticky=W)

        search_btn = Button(search_frame, command=self.search_data,text="Search", font=("times new roman", 12, "bold"), bg="black", fg="yellow",width=9)
        search_btn.grid(row=0, column=3,padx=6)

        showall_btn = Button(search_frame,command=self.fetch_data, text="Show All", font=("times new roman", 12, "bold"), bg="black", fg="yellow",width=9)
        showall_btn.grid(row=0, column=4)



        #===========Table frame================
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, background="bisque")
        table_frame.place(x=5, y=107, width=640, height=340)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =  ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","roll","semester","ID","name","DOB","gender","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course Name")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("roll" , text="Roll Number")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("DOB", text="Date of Birth")
        self.student_table.heading("gender" , text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone Number")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo Sample status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("gender" , width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #===========function declaration===================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error" , "All Fields are required!", parent = self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="Football.321",database = "face_recognitions")
                mycursor = con.cursor()
                mycursor.execute("insert into studentss values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_roll.get(),
                self.var_semester.get(),
                self.var_ID.get(),
                self.var_name.get(),
                self.var_DOB.get(),
                self.var_gender.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_radio1.get()))
                con.commit()           #for updating database
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success","Student details has been added successfully" , parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


                #=================fetch data=============
    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", username="root", password="Football.321",database="face_recognitions")
        mycursor = con.cursor()
        mycursor.execute("select * from studentss")
        data = mycursor.fetchall()              #stored all data in variable data

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("" , END,values=i)
            con.commit()
        con.close()

        #==================get cursor=====================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_ID.set(data[5]),
        self.var_name.set(data[6]),
        self.var_DOB.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

        # update function

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "All Fields are required!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to Update this Student Details!", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='Football.321', host='localhost',database='face_recognitions')
                    mycursor = conn.cursor()
                    sql1=("UPDATE studentss SET `dep`=%s,`course`=%s,`year`=%s,`roll_no`=%s,`semester`=%s,`name`=%s,`DOB`=%s,`gender`=%s,`email`=%s,`phone`=%s,`address`=%s,`photosamplestatus`=%s WHERE `ID`=%s")
                    val1=            (self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_roll.get(),
                                      self.var_semester.get(),
                                      self.var_name.get(),
                                      self.var_DOB.get(),
                                      self.var_gender.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_radio1.get(),
                                      self.var_ID.get())
                    mycursor.execute(sql1,val1)
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Successfully Updated!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ==============================Delete Function=========================================
    def delete_data(self):
        if self.var_ID.get() == "":
            messagebox.showerror("Error", "Student Id Must be Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(username='root', password='Football.321', host='localhost',database='face_recognitions')
                    mycursor = conn.cursor()
                    sql = "delete from studentss where ID=%s"
                    val = (self.var_ID.get(),)
                    mycursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully Deleted!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

                # Reset Function

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_roll.set(""),
        self.var_semester.set("Select Semester"),
        self.var_ID.set(""),
        self.var_name.set(""),
        self.var_DOB.set(""),
        self.var_gender.set("Male"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_radio1.set("")


    # ===========================Search Data===================
    def search_data(self):
        if self.var_searchTX.get() =="" or self.var_search.get() =="Select":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='Football.321', host='localhost',
                                               database='face_recognitions')
                my_cursor = conn.cursor()
                sql = "SELECT dep,course,year,roll_no,semester,ID,name,DOB,gender,email,phone,address,photosamplestatus FROM studentss where roll_no='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # =====================This part is related to Opencv Camera part=======================
    # ==================================Generate Data set take photo sample=========================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host='localhost',username='root', password='Football.321',
                                               database='face_recognitions')
                mycursor = conn.cursor()
                mycursor.execute("select * from studentss")
                myresult = mycursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1

                conn = mysql.connector.connect(username='root', password='Football.321', host='localhost',database='face_recognitions')
                mycursor = conn.cursor()
                sql2=("UPDATE studentss SET `dep`=%s,`course`=%s,`year`=%s,`roll_no`=%s,`semester`=%s,`name`=%s,`DOB`=%s,`gender`=%s,`email`=%s,`phone`=%s,`address`=%s,`photosamplestatus`=%s WHERE `ID`=%s")
                val2=            (self.var_dep.get(),
                                      self.var_course.get(),
                                      self.var_year.get(),
                                      self.var_roll.get(),
                                      self.var_semester.get(),
                                      self.var_name.get(),
                                      self.var_DOB.get(),
                                      self.var_gender.get(),
                                      self.var_email.get(),
                                      self.var_phone.get(),
                                      self.var_address.get(),
                                      self.var_radio1.get(),
                                      self.var_ID.get())
                mycursor.execute(sql2,val2)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                #===========Load predefined data on face frontals from opencv=========================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # convert to gray scale
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor 1.3
                    # Minimum neighbour= 5

                    for (x, y, w, h) in faces:
                        face_croped = img[y:y + h, x:x + w]
                        return face_croped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_croped(my_frame), (300, 300))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()