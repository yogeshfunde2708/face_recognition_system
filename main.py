from tkinter import*
from tkinter import Toplevel,Button
from PIL import Image, ImageTk
import tkinter
from student import Student
from train import Train
from face_recognition import Face_Recognition
from devloper import Devloper
from attendance import Attendance
from help import Help
import os

class Face_Recognition_System:
    def __init__(self,root):
       self.root = root
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")

#bg image
       img3 = Image.open("college_images\\wallpaperflare.com_wallpaper.jpg")
       img3 = img3.resize((1530, 710))
       self.photoimg3=ImageTk.PhotoImage(img3)

       bg_image = Label(self.root,image=self.photoimg3)
       bg_image.place(x=0,y=45,width=1530,height=870)

       
       title_lbl = Label(root, text="Face Recognition Attendance System", font=("times new roman",35,"bold"),bg="white",fg="red")
       title_lbl.place(x=0, y=0, width=1530, height=45)

#student button
       img4 = Image.open("college_images\\download.webp")
       img4 = img4.resize((220, 220))
       self.photoimg4=ImageTk.PhotoImage(img4)

       b1=Button(root, image=self.photoimg4,cursor="hand2",command= self.student_details)
       b1.place(x=200,y=140,width=220,height=220)
       
       b1_1=Button(root,text="Student Details",command= self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
       b1_1.place(x=200,y=340,width=220,height=40)

#student button
       img5 = Image.open("college_images\\download.webp")
       img5 = img5.resize((220, 220))
       self.photoimg5=ImageTk.PhotoImage(img5)

       b1=Button(root, image=self.photoimg4,cursor="hand2",command=self.face_data)
       b1.place(x=500,y=140,width=220,height=220)
       
       b1_1=Button(root,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
       b1_1.place(x=500,y=340,width=220,height=40)

       #Attendance
       img6 = Image.open("college_images\\download.webp")
       img6 = img6.resize((220, 220))
       self.photoimg6=ImageTk.PhotoImage(img6)

       b1=Button(root, image=self.photoimg4,cursor="hand2",command=self.attendance_data)
       b1.place(x=800,y=140,width=220,height=220)
       
       b1_1=Button(root,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
       b1_1.place(x=800,y=340,width=220,height=40)

#help
       img7 = Image.open("college_images\\download.webp")
       img7 = img7.resize((220, 220))
       self.photoimg7=ImageTk.PhotoImage(img7)

       b1=Button(root, image=self.photoimg4,cursor="hand2",command=self.help)
       b1.place(x=1100,y=140,width=220,height=220)
       
       b1_1=Button(root,text="Help Desk",cursor="hand2",command=self.help,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
       b1_1.place(x=1100,y=340,width=220,height=40)

       #train
       img8 = Image.open("college_images\\download.webp")
       img8 = img8.resize((220, 220))
       self.photoimg8=ImageTk.PhotoImage(img8)

       b1=Button(root, image=self.photoimg4,cursor="hand2", command=self.train_data)
       b1.place(x=200,y=420,width=220,height=220)
       
       b1_1=Button(root,text="Train",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
       b1_1.place(x=200,y=620,width=220,height=40)

              #photos
       img9 = Image.open("college_images\\download.webp")
       img9 = img9.resize((220, 220))
       self.photoimg9=ImageTk.PhotoImage(img9)

       b1=Button(root, image=self.photoimg4,cursor="hand2", command=self.open_img)
       b1.place(x=500,y=420,width=220,height=220)
       
       b1_1=Button(root,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
       b1_1.place(x=500,y=620,width=220,height=40)

              #Devloper
       img10 = Image.open("college_images\\download.webp")
       img10 = img10.resize((220, 220))
       self.photoimg10=ImageTk.PhotoImage(img10)

       b1=Button(root, image=self.photoimg4,cursor="hand2",command=self.devloper_data )
       b1.place(x=800,y=420,width=220,height=220)
       
       b1_1=Button(root,text="Devloper",cursor="hand2",command=self.devloper_data, font=("times new roman",15,"bold"),bg="darkblue",fg="red")
       b1_1.place(x=800,y=620,width=220,height=40)
       
       #Exit face button
       img11 = Image.open("college_images\\download.webp")
       img11 = img11.resize((220, 220))
       self.photoimg10=ImageTk.PhotoImage(img11)

       b1=Button(root, image=self.photoimg4,cursor="hand2",command=self.iExit )
       b1.place(x=1100,y=420,width=220,height=220)
       
       b1_1=Button(root,text="Exit",cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"),bg="darkblue",fg="red")
       b1_1.place(x=1100,y=620,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("face recognition","Are you sure exit this project",parent=self.root)
       if self.iExit>0:
          self.root.destroy()

# function button
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

    def devloper_data(self):
       self.new_window = Toplevel(self.root)
       self.app = Devloper(self.new_window)
    
    def help(self):
       self.new_window = Toplevel(self.root)
       self.app = Help(self.new_window)
    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
