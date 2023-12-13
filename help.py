from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Help:
    def __init__(self,root):
       self.root = root
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")


       title_lbl = Label(root, text="Help Desk", font=("times new roman",35,"bold"),bg="white",fg="blue")
       title_lbl.place(x=0, y=0, width=1530, height=45)

       img_top = Image.open("college_images\help.jpg")
       img_top = img_top.resize((1530, 720))
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl = Label(self.root,image=self.photoimg_top)
       f_lbl.place(x=0,y=55,width=1520,height=720) 


       dev_label = Label(f_lbl,  text="Email:yogeshfunde5@gmail.com", font=("times new roman", 12, "bold"), bg="white")
       dev_label.place(x=550, y=400)

if __name__ == "__main__":
    root = Tk()  # Create a Tkinter root window
    obj = Help(root)  # Create an instance of the Student class
    root.mainloop() 
