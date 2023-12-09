# Smart Attendance System

**An efficient way to mark daily attendance in multiple domains of life.**

"Smart Attendance System" is a versatile database application designed to streamline attendance tracking. The program allows users to save student records, capture photo samples, and mark attendance, all while maintaining an easy-to-use interface.

## Library

- **tkinter:** The graphical user interface (GUI) library used for creating the program's interface.
- **OpenCV:** A computer vision library for face recognition.
- **Pillow:** A library for handling and manipulating images in RGB format.
- **mysql.connector:** Used to connect the Python application with a MySQL database.
- **Numpy:** A library for working with arrays.

## Methodology

Here's an overview of the program's key components and methods:

- **tkinter:** The program utilizes tkinter's modules, including ttk and messagebox, for GUI elements.
- **Pillow:** Importing Pillow provides support for image operations.
- **mysql.connector:** Enables the connection between the Python application and a MySQL database.
- **OpenCV and Numpy:** OpenCV is used for computer vision tasks, and Numpy is employed for array manipulation.
- **Haarcascade Frontalface Algorithm:** Detects objects in images, particularly faces, and can run in real-time.
- **LBPH Algorithm:** A robust face recognition algorithm known for its performance in recognizing faces from various angles.
- **StringVar():** A tkinter class used to monitor changes in tkinter variables.
- **Layout Functions:** Grid and pack for organizing GUI elements.
- **Formatting Features:** Styling elements using attributes like padx, pady, font, fg, bg, borderwidth, and relief.
- **Frame Widget:** Utilized for pop-up windows.
- **fetchall():** Retrieves database records.
- **Cursor Command:** Executes SQL statements for database operations.
- **con.commit():** Ensures data consistency in the database.
- **mainloop():** An infinite loop that runs the application until the window is closed.

## Face Recognition Process

- Users add their records to the database and capture 100 photo samples using the "Take Photo Sample" button.
- These samples are then used for training.
- To mark attendance, users simply click the "Face Recognition" button, and their attendance is recorded and displayed in the "Attendance" window.
- Users can also update, delete, or reset records and photo samples.


## LBPH Algorithm

Local Binary Pattern (LBP) is a powerful texture operator that labels image pixels by thresholding their neighborhoods, resulting in a binary number. When combined with histograms of oriented gradients (HOG), it enhances detection performance, especially on challenging datasets. The program leverages the LBPH algorithm provided by the OpenCV library for accurate face recognition.



## SCREENSHOTS

![s](https://github.com/KanzaAkram/Smart_Attendance_System/assets/85638781/ec98dceb-4975-4afc-a6f1-5a007e7907ec)



![m](https://github.com/KanzaAkram/Smart_Attendance_System/assets/85638781/cf6c8fec-fbe0-4a11-929f-ed26c268d2b3)



![a](https://github.com/KanzaAkram/Smart_Attendance_System/assets/85638781/64dfcce2-71ed-4d68-ac6c-ad48aa634cb7)



![r](https://github.com/KanzaAkram/Smart_Attendance_System/assets/85638781/3f3f3256-f89a-4755-92d1-700f4f8df989)



![t](https://github.com/KanzaAkram/Smart_Attendance_System/assets/85638781/ff2c710a-3ac4-4e45-93b6-92f9dbe66329)







