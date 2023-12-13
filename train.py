from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self,root):
       self.root = root
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")

       title_lbl = Label(root, text="Train data", font=("times new roman",35,"bold"),bg="white",fg="red")
       title_lbl.place(x=0, y=0, width=1530, height=45)

       img_top = Image.open("C:\\Users\\LENOVO\\OneDrive\\Desktop\\smart attendence system\\college_images\\download.webp")
       img_top = img_top.resize((1530, 325))
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl = Label(self.root,image=self.photoimg_top)
       f_lbl.place(x=0,y=55,width=1520,height=325)  

#button
       b1_1=Button(self.root,text="Train data",cursor="hand2",font=("times new roman",25,"bold"),bg="red",fg="white")
       b1_1.place(x=0,y=380,width=1520,height=60)


       img_bottom = Image.open("C:\\Users\\LENOVO\\OneDrive\\Desktop\\smart attendence system\\college_images\\download.webp")
       img_bottom = img_bottom.resize((1530, 325))
       self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

       f_lbl = Label(self.root,image=self.photoimg_bottom)
       f_lbl.place(x=0,y=440,width=1520,height=325) 

    def train_data(self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        id=[]

        for image in path:
            img = Image.open(image).convert("L")  #gray scale image 
            imageNp = np.array(img,"unit8")
            id = int(os.path.split(image)[1].split('.')[1])
 
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)


        # train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")




if __name__ == "__main__":
    root = Tk()  # Create a Tkinter root window
    obj = Train(root)  # Create an instance of the Student class
    root.mainloop()  