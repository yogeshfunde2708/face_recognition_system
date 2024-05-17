from tkinter import*
from tkinter import ttk, Tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yogesh270801",
        database="face_recognizer",
    )
    print("Connected to MySQL Server")
    connection.close()
except Exception as e:
    print(f"Error: {e}")

class Student:
    def __init__(self,root):
       self.root = root
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")

       #variables
       self.var_dep=StringVar()
       self.var_course=StringVar()
       self.var_year=StringVar()
       self.var_semester=StringVar()
       self.var_std_id=StringVar()
       self.var_std_name=StringVar()
       self.var_div=StringVar()
       self.var_roll=StringVar()
       self.var_gender=StringVar()
       self.var_dob=StringVar()
       self.var_email=StringVar()
       self.var_phone=StringVar()
       self.var_address=StringVar()
       self.var_teacher=StringVar()


#first image
       img = Image.open("college_images\\manage.jpeg")

       img = img.resize((500, 130))
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl = Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=400,height=270)

#second image
       img1 = Image.open("college_images\\studentdata.jpeg")

       img1 = img1.resize((500, 130))
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl = Label(self.root,image=self.photoimg1)
       f_lbl.place(x=500,y=0,width=400,height=270)

#third image
       img2 = Image.open("college_images\\management.jpeg")

       img2 = img2.resize((500, 130))
       self.photoimg2=ImageTk.PhotoImage(img2)

       f_lbl = Label(self.root,image=self.photoimg2)
       f_lbl.place(x=1000,y=0,width=400,height=270)

#bg image
       
       title_lbl = Label(root, text="student management System", font=("times new roman",35,"bold"),bg="red",fg="white")
       title_lbl.place(x=0, y=0, width=1530, height=45)

       main_frame=Frame(self.root, bd=2,bg="white")
       main_frame.place(x=0, y=170, width=1550,height=700)

# left label frame
       Left_frame = LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text= "Student Details", font=("times new roman",12,"bold"))
       Left_frame.place(x=10,y=200, width=730,height=620)

       img_left = Image.open("college_images\\student.jpeg")
       img_left = img_left.resize((500, 130))
       self.photoimg_left=ImageTk.PhotoImage(img_left)

       f_lbl = Label(self.root,image=self.photoimg_left)
       f_lbl.place(x=15,y=220,width=720,height=130)    

#current course
       CurrentCourse_frame = LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text= "Current course information", font=("times new roman",12,"bold"))
       CurrentCourse_frame.place(x=10,y=130, width=710,height=200) 
       #department
       dep_label = Label(CurrentCourse_frame, text="Department",font=("times new roman",12,"bold"), bg="white")
       dep_label.grid(row=0, column=0, padx=10,sticky=W)

       dep_combo= ttk.Combobox(CurrentCourse_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
       dep_combo["values"]=("Select Department", "computer science", "Information Technology","Artificial intelligence", "Civil", "Mechanichal")
       dep_combo.current(0)
       dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

       #Course
       course_label = Label(CurrentCourse_frame, text="Course",font=("times new roman",12,"bold"), bg="white")
       course_label.grid(row=0, column=2, padx=10,sticky=W)

       course_combo= ttk.Combobox(CurrentCourse_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
       course_combo["values"]=("Select Course", "BE", "B TEch", "SE","FE")
       course_combo.current(0)
       course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

       #year
       year_label = Label(CurrentCourse_frame, text="Year",font=("times new roman",12,"bold"), bg="white")
       year_label.grid(row=1, column=0, padx=10,sticky=W)

       year_combo= ttk.Combobox(CurrentCourse_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
       year_combo["values"]=("Select Year", "2020-21", "2021-22", "2022-23","2023-24")
       year_combo.current(0)
       year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

       #semester
       semester_label = Label(CurrentCourse_frame, text="Semetser",font=("times new roman",12,"bold"), bg="white")
       semester_label.grid(row=1, column=2, padx=10,sticky=W)

       semester_combo= ttk.Combobox(CurrentCourse_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
       semester_combo["values"]=("Select Semester", "Semester-1", "Semester-2", "Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
       semester_combo.current(0)
       semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


 #current student information
       ClassStudent_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student information", font=("times new roman", 12, "bold")) 
       ClassStudent_frame.place(x=10, y=240, width=710, height=310)


       #student ID
       studentId_label = Label(ClassStudent_frame,  text="Student Id:", font=("times new roman", 12, "bold"), bg="white")
       studentId_label.grid(row=0, column=0, sticky=W)
       studentId_entry = ttk.Entry(ClassStudent_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
       studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

       #student name
       studentName_label = Label(ClassStudent_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
       studentName_label.grid(row=0, column=2, sticky=W)
       studentName_entry = ttk.Entry(ClassStudent_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
       studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

       #division
       studentDiv_label = Label(ClassStudent_frame, text="Class Division:", font=("times new roman", 12, "bold"), bg="white")
       studentDiv_label.grid(row=1, column=0, sticky=W)

       divi_combo= ttk.Combobox(ClassStudent_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
       divi_combo["values"]=("A", "B","C")
       divi_combo.current(0)
       divi_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

       #roll no
       studentRollNo_label = Label(ClassStudent_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
       studentRollNo_label.grid(row=1, column=2, sticky=W)
       studentRollNo_entry = ttk.Entry(ClassStudent_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
       studentRollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
       #gender
       gender_label = Label(ClassStudent_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
       gender_label.grid(row=2, column=0, sticky=W)
       gender_combo= ttk.Combobox(ClassStudent_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
       gender_combo["values"]=("Male", "Female", "Other",)
       gender_combo.current(0)
       gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
       #DOb
       dob_label = Label(ClassStudent_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
       dob_label.grid(row=2, column=2, sticky=W)
       dob_entry = ttk.Entry(ClassStudent_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
       dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
       #email
       email_label = Label(ClassStudent_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
       email_label.grid(row=3, column=0, sticky=W)
       email_entry = ttk.Entry(ClassStudent_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
       email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
       #phone No
       phone_label = Label(ClassStudent_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
       phone_label.grid(row=3, column=2, sticky=W)
       phone_entry = ttk.Entry(ClassStudent_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
       phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
       #Address
       adress_label = Label(ClassStudent_frame, text="Adress:", font=("times new roman", 12, "bold"), bg="white")
       adress_label.grid(row=4, column=0, sticky=W)
       adress_entry = ttk.Entry(ClassStudent_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
       adress_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
       #Teacher name
       teacher_label = Label(ClassStudent_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
       teacher_label.grid(row=4, column=2, sticky=W)
       teacher_entry = ttk.Entry(ClassStudent_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
       teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

       #radio buttons
       self.var_radio1=StringVar()
       radio1 = ttk.Radiobutton(ClassStudent_frame,variable=self.var_radio1, text="Take a photo sample",value="Yes")
       radio1.grid(row=6, column=0)

    #    self.var_radio2=StringVar()
       radio2 = ttk.Radiobutton(ClassStudent_frame,variable=self.var_radio1, text="No Photo Sample",value="NO")
       radio2.grid(row=6, column=1)

       # button_frame
       button_frame = Frame(ClassStudent_frame, bd = 2, relief=RIDGE )
       button_frame.place(x=0, y=220, width=700, height=35)

       save_btn= Button(button_frame, text="Save",command=self.add_data, width=20,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       save_btn.grid(row=0, column=0)

       update_btn= Button(button_frame, text="Update",command=self.update_data,width=20,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       update_btn.grid(row=0, column=1)

       delete_btn= Button(button_frame, text="Delete",command=self.delete_data,width=20,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       delete_btn.grid(row=0, column=2)

       reset_btn= Button(button_frame, text="Reset",command=self.reset_dat,width=20,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       reset_btn.grid(row=0, column=3)


       button_frame1 = Frame(ClassStudent_frame, bd = 2, relief=RIDGE )
       button_frame1.place(x=0, y=255, width=700, height=35)
       take_photo_btn= Button(button_frame1,command=self.take_photo, text="Take Photo Sample",width=40,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       take_photo_btn.grid(row=0, column=0)

       update_btn= Button(button_frame1,text="Update Photo Sample",width=40,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       update_btn.grid(row=0, column=1)


# right label frame
       Right_frame = LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text= "Student details", font=("times new roman",12,"bold"))
       Right_frame.place(x=780,y=200, width=730,height=620)

       img_right = Image.open("college_images\\data.jpeg")
       img_right = img_right.resize((500, 130))
       self.photoimg_right=ImageTk.PhotoImage(img_right)

       f_lbl = Label(self.root,image=self.photoimg_right)
       f_lbl.place(x=785,y=220,width=720,height=130)


       # Search System
       search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold")) 
       search_frame.place(x=5, y=140, width=710, height=70)

       search_label = Label(search_frame, text="Search:", font=("times new roman", 12, "bold"), bg="white")
       search_label.grid(row=0, column=0, sticky=W)

       search_combo= ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly", width=15)
       search_combo["values"]=("Select", "Roll_no", "Pone_No", "Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
       search_combo.current(0)
       search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

       search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
       search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

       search_btn= Button(search_frame, text="Search",width=17,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       search_btn.grid(row=0, column=3, padx=3)

       showAll_btn= Button(search_frame, text="Show All",width=17,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       showAll_btn.grid(row=0, column=4, padx=3)

#table frame
       table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE) 
       table_frame.place(x=5, y=215, width=710, height=370)

       scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
       self.student_table= ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)
       scroll_x.config(command= self.student_table.xview)
       scroll_y.config(command= self.student_table.yview)

       self.student_table.heading("dep", text="Department")
       self.student_table.heading("course", text="Course")
       self.student_table.heading("year", text="Year")
       self.student_table.heading("sem", text="semester")
       self.student_table.heading("id", text="Student Id")
       self.student_table.heading("name", text="Student Name")
       self.student_table.heading("div", text="Division")
       self.student_table.heading("roll", text="Roll No")
       self.student_table.heading("gender", text="Gender")
       self.student_table.heading("dob", text="DOB")
       self.student_table.heading("email", text="Email")
       self.student_table.heading("phone", text="Phone")
       self.student_table.heading("address", text="Address")
       self.student_table.heading("teacher", text="Teacher Name")
       self.student_table.heading("photo", text="PhotoSampleStatus")
       self.student_table["show"]="headings"

       self.student_table.column("dep", width=100)
       self.student_table.column("course", width=100)
       self.student_table.column("year", width=100)
       self.student_table.column("sem", width=100)
       self.student_table.column("id", width=100)
       self.student_table.column("name", width=100)
       self.student_table.column("div", width=100)
       self.student_table.column("roll", width=100)
       self.student_table.column("gender", width=100)
       self.student_table.column("dob", width=100)
       self.student_table.column("email", width=100)
       self.student_table.column("phone", width=100)
       self.student_table.column("address", width=100)
       self.student_table.column("teacher", width=100)
       self.student_table.column("photo", width=100)

       self.student_table.pack(fill=BOTH, expand=1)
       self.student_table.bind("<ButtonRelease>", self.get_cursor)
       self.fetch_data()

# function declaration

    def add_data(self):
       if self.var_dep.get()=="select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
       else:
           
           try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Yogesh270801",
                    database="face_recognizer",
                )
                my_cursor = connection.cursor()
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                    ))
                connection.commit()
                self.fetch_data()
                messagebox.showinfo("success", "added successfully", parent=self.root)
           except Exception as es:
                messagebox.showerror("Error", f"due to :{str(es)}", parent=self.root)


#fetch data

    def fetch_data(self):
        connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Yogesh270801",
                    database="face_recognizer",
                )
        my_cursor = connection.cursor()
        my_cursor.execute("select * from student")
        data= my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            connection.commit()
        connection.close()
    

#get cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

#update function
    def update_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
               if update:
                     connection = mysql.connector.connect(
                     host="localhost",
                     user="root",
                     password="Yogesh270801",
                     database="face_recognizer",
                     )
                     my_cursor = connection.cursor()
                     my_cursor.execute("UPDATE student SET dep=%s,course=%s,year=%s,semester=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s WHERE student_id=%s",(
                                                                                           self.var_dep.get(),
                                                                                           self.var_course.get(),
                                                                                           self.var_year.get(),
                                                                                           self.var_semester.get(),
                                                                                           self.var_div.get(),
                                                                                           self.var_roll.get(),
                                                                                           self.var_gender.get(),
                                                                                           self.var_dob.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_phone.get(),
                                                                                           self.var_address.get(),
                                                                                           self.var_teacher.get(),
                                                                                           self.var_radio1.get(),
                                                                                           self.var_std_id.get()
                                                                                       ))
               connection.commit()
               self.fetch_data()
               connection.close()
               messagebox.showinfo("Success","Student detail successfully updated",parent=self.root)
            except Exception as es:
              messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)
        

#delete function

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page", "Do you want to delete this student",parent = self.root)
                if delete:
                    connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Yogesh270801",
                    database="face_recognizer",
                )
                    my_cursor = connection.cursor()
                    sql="DELETE FROM student WHERE student_id=%s "
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Delete","Successfully deleted", parent= self.root)
            except Exception as es:
              messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)
                    
         #reset data

    def reset_dat(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(''),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
                 
# take photo sample
    def take_photo(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
             messagebox.showerror("Error","all fields are required",parent=self.root)
        else:
            try:
              connection = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Yogesh270801",
              database="face_recognizer",
              )
              my_cursor = connection.cursor()
              my_cursor.execute("select * from student")
              myresult = my_cursor.fetchall()
              id=0
              for x in myresult:
                  id+=1
              my_cursor.execute("update student SET dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,address=%s,phone=%s,teacher=%s,photosample=%s where student_id=%s", (
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get(),
                                                                                                self.var_std_id.get()==id+1  
                                                                                            ))

              connection.commit() 
              self.fetch_data()
              self.reset_dat()
              connection.close()

              #load predefined data on face frontals from open cv
              face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
              def face_cropped(img):
                  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                  faces = face_classifier.detectMultiScale(gray, 1.3,5)
                  for(x,y,w,h) in faces:
                      face_cropped = img[y:y+h,x:x+w]
                      return face_cropped

              cap =cv2.VideoCapture(0)
              img_id = 0
              while True:
                  ret,my_frame =cap.read()
                  if face_cropped(my_frame) is not None:
                      img_id += 1
                      face = cv2.resize(face_cropped(my_frame),(450,450))
                      face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                      file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                      cv2.imwrite(file_name_path, face)
                      cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                      cv2.imshow("Cropped face",face)

                  if cv2.waitKey(1) == 13 or int(img_id)==100:
                      break
              cap.release()
              cv2.destroyAllWindows()
              messagebox.showinfo("Result", "Generating data set completed!!!")
            except Exception as es:
              messagebox.showerror("Error",f"due to:{str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()  
    obj = Student(root) 
    root.mainloop()  