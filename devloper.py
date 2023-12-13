from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Devloper:
    def __init__(self,root):
       self.root = root
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")

       title_lbl = Label(root, text="Developer", font=("times new roman",35,"bold"),bg="white",fg="blue")
       title_lbl.place(x=0, y=0, width=1530, height=45)

       img_top = Image.open("college_images\developer.webp")
       img_top = img_top.resize((1530, 720))
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl = Label(self.root,image=self.photoimg_top)
       f_lbl.place(x=0,y=55,width=1520,height=720) 

       main_frame=Frame(f_lbl, bd=2,bg="white")
       main_frame.place(x=1000, y=0, width=500,height=600)

       dev_label = Label(main_frame,  text="Developers:", font=("times new roman", 12, "bold"), bg="white")
       dev_label.place(x=0, y=5)
       dev_label = Label(main_frame,  text="Rutwik sawarkar", font=("times new roman", 12, "bold"), bg="white")
       dev_label.place(x=60, y=25)
       dev_label = Label(main_frame,  text="Kumkum Rathi", font=("times new roman", 12, "bold"), bg="white")
       dev_label.place(x=60, y=50)
       dev_label = Label(main_frame,  text="Parth Thakre", font=("times new roman", 12, "bold"), bg="white")
       dev_label.place(x=60, y=75)
       dev_label = Label(main_frame,  text="Yogesh Funde", font=("times new roman", 12, "bold"), bg="white")
       dev_label.place(x=60, y=100)



if __name__ == "__main__":
    root = Tk()  # Create a Tkinter root window
    obj = Devloper(root)  # Create an instance of the Student class
    root.mainloop() 