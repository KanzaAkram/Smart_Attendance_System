# Smart-Attendance-System
An efficient way to mark daily attendance in multiple domains of life
“SMART ATTENDANCE SYSTEM” is a database application. The 
program first saves the record of the students and takes 100 photo samples 
of the respective student. It also provides the facility to delete or update any 
record. Each photo sample is trained and is stored in a separate file. The 
program then detects the face and mark the attendance which is stored in 
excel file. The program has a user friendly interface.
#LIBRARY
The GUI library of python used in the program is “tkinter”. Computer vision 
library for face recognition used in python is “OpenCV”.
#METHODOLOGY
 The program first imports the tkinter library and then imports some
of its modules (that are ttk and messagebox).
 By importing ttk the control of the treeview is achieved.
 It then imports the pillow library which adds support for opening, 
manipulating, and saving images in RGB format.
 It also imports mysql.connector to connect the tkinter python 
application with the MySQL database.
 The Tk() class then creates a root window for the program.
 Later the program also imports the os module which provides functions for 
creating and removing a directory(folder), fetching its contents, changing 
and identifying the current directory etc.
 OpenCV and Numpy libraries are also imported in the program.
 OpenCV is designed to solve computer vision problems whereas Numpy is 
used for working with arrays.
 Cv2.imshow() method is used to display an image in a window. The 
window automatically fits the image.
 Buttons, labels and entry boxes are used and designed to carry out 
theprocedure in entire program.
 PhotoImage function is used to get images of .png extension from 
the device.
 The program uses Haarcascade Frontalface algorithm that can detect 
objects in images. This algorithm is not so complex and can run in 
real-time.
 The program also uses LBPH algorithm which is a face-recognition 
algorithm and is used to recognize the face of a person. It is known 
for its performance and how it is able to recognize the face of a 
person from both front and side.
 StringVar() a class from tkinter, is used to easily monitor changes
to tkinter variables if they occur many times.
 Layout functions such as grid and pack are used for placement 
ofbuttons, labels and entry boxes.
 Many formatting features of tkinter are used for styling the 
boxes(such as padx, pady, font, fg, bg, borderwidth, relief 
(function to defined the style of border))
 Frame widget class is used to show a pop up window when button 
isclicked.
 The fetchall() function is used to display the records of the database.
 A messagebox is displayed for confirmation.
 In the connection with the database a cursor command is used 
which executes the SQL statements (like insert into-which adds 
record to MySQL database and delete from-which deletes records 
from the database.
 The con.commit() statement modifies the data for the tables is access
database. It makes sure that the changes to the database are
consistent.
 The mainloop() function is an infinite loop used to run the
applicationwhich ends the process when the window is closed.
#FACE RECOGNITION PROCESS
The user adds his record in the database and then clicks on the “Take Photo 
Sample” button through which the webcam opens and it takes 100 samples. 
These samples are then trained. Later on, whenever the user wants to mark 
his attendance, he just clicks on the “Face Recognition” button and his 
attendance is marked which is shown in the “Attendance” window. 
Here the user can also update, delete or reset the records or even the photo 
samples.
#LBPH ALGORITHM:
Local Binary Pattern (LBP) is a simple yet very efficient texture operator 
which labels the pixels of an image by thresholding the neighborhood of 
each pixel and considers the result as a binary number. When LBP is 
combined with histograms of oriented gradients (HOG) descriptor, it 
improves the detection performance considerably on some datasets. It is 
provided by the OpenCV library (Open Source Computer Vision Library).
