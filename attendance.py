from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
       self.root = root
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")

       self.var_atten_id=StringVar()
       self.var_atten_roll=StringVar()
       self.var_atten_name=StringVar()
       self.var_atten_dep=StringVar()
       self.var_atten_time=StringVar()
       self.var_atten_date=StringVar()
       self.var_atten_attendance=StringVar()
#first image
       img = Image.open("college_images\\download.webp")
       img = img.resize((800, 200))
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl = Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=800,height=200)

#second image
       img1 = Image.open("college_images\\download.webp")
       img1 = img1.resize((800, 200))
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl = Label(self.root,image=self.photoimg1)
       f_lbl.place(x=800,y=0,width=800,height=200)

       title_lbl = Label(root, text="Attendance management  System", font=("times new roman",35,"bold"),bg="red",fg="white")
       title_lbl.place(x=0, y=0, width=1530, height=45)

       main_frame=Frame(self.root, bd=2,bg="white")
       main_frame.place(x=0, y=170, width=1550,height=700)

#left frame
       Left_frame = LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text= "Student Attendance details", font=("times new roman",12,"bold"))
       Left_frame.place(x=10,y=250, width=730,height=580)
       
       left_inside_frame=Frame(Left_frame, bd=2,relief=RIDGE,bg="white")
       left_inside_frame.place(x=5, y=50, width=720,height=500)

#labels and entries

        #attendance ID
       attendanceId_label = Label(left_inside_frame, text="Attendance Id:", font=("times new roman", 12, "bold"), bg="white")
       attendanceId_label.grid(row=0, column=0, sticky=W)
       attendanceId_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id,font=("times new roman", 12, "bold"))
       attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

       #roll
       roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white")
       roll_label.grid(row=0, column=2, sticky=W)
       roll_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll,font=("times new roman", 12, "bold"))
       roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

       #name
       name_label = Label(left_inside_frame,  text="Name:", font=("times new roman", 12, "bold"), bg="white")
       name_label.grid(row=1, column=0, sticky=W)
       name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
       name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #dep
       dep_label = Label(left_inside_frame,  text="Department:", font=("times new roman", 12, "bold"), bg="white")
       dep_label.grid(row=1, column=2, sticky=W)
       dep_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep,font=("times new roman", 12, "bold"))
       dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

       #date
       date_label = Label(left_inside_frame,  text="Date:", font=("times new roman", 12, "bold"), bg="white")
       date_label.grid(row=2, column=0, sticky=W)
       date_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
       date_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

       #time
       time_label = Label(left_inside_frame,  text="Time:", font=("times new roman", 12, "bold"), bg="white")
       time_label.grid(row=2, column=2, sticky=W)
       time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
       time_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

       #attendance
       time_label = Label(left_inside_frame,  text="Attendance status:", font=("times new roman", 12, "bold"), bg="white")
       time_label.grid(row=3, column=0)

       self.atten_combo= ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
       self.atten_combo["values"]=("Status", "Present", "Absent",)
       self.atten_combo.current(0)
       self.atten_combo.grid(row=3, column=1, pady=8)



         # button_frame
       button_frame = Frame(left_inside_frame, bd = 2, relief=RIDGE )
       button_frame.place(x=0, y=220, width=700, height=35)

       save_btn= Button(button_frame, text="Import CSV",command=self.importCsv,width=20,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       save_btn.grid(row=0, column=0)

       update_btn= Button(button_frame, text="Export CSV",command=self.exportCsv,width=20,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       update_btn.grid(row=0, column=1)

       delete_btn= Button(button_frame, text="Update",width=20,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       delete_btn.grid(row=0, column=2)

       reset_btn= Button(button_frame, text="Reset",width=20,command=self.reset_data,font=("times new roman", 12, "bold"), bg="blue", fg="white")
       reset_btn.grid(row=0, column=3)


       

#right frame
       Right_frame = LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text= "Attendance details", font=("times new roman",12,"bold"))
       Right_frame.place(x=780,y=250, width=730,height=580)

       table_frame = Frame(Right_frame, bd = 2, relief=RIDGE )
       table_frame.place(x=5, y=5, width=710, height=580)

       # scroll bar and table
       scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
       self.attendanceTable= ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)
       scroll_x.config(command= self.attendanceTable.xview)
       scroll_y.config(command= self.attendanceTable.yview)

       self.attendanceTable.heading("id",text="Attendance ID")
       self.attendanceTable.heading("roll",text="Roll")
       self.attendanceTable.heading("name",text="Name")
       self.attendanceTable.heading("dep",text="Department")
       self.attendanceTable.heading("time",text="Time")
       self.attendanceTable.heading("date",text="Date")
       self.attendanceTable.heading("attendance",text="Attendance")

       self.attendanceTable["show"] = "headings"
       self.attendanceTable.column("id",width=100)
       self.attendanceTable.column("roll",width=100)
       self.attendanceTable.column("name",width=100)
       self.attendanceTable.column("dep",width=100)
       self.attendanceTable.column("time",width=100)
       self.attendanceTable.column("date",width=100)
       self.attendanceTable.column("attendance",width=100)

       self.attendanceTable.pack(fill=BOTH,expand=1)

       self.attendanceTable.bind("<ButtonRelease>",self.get_cursor)


       #fetch Data

    def fetchDaat(self,rows):
        self.attendanceTable.delete(*self.attendanceTable.get_children())
        for i in rows:
            self.attendanceTable.insert("",END,values=i)
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread= csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchDaat(mydata)

        #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                    messagebox.showinfo("Data Export","your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
              messagebox.showerror("Error",f"due to :{str(es)}", parent=self.root)

    
    def get_cursor(self,event=""):
        cursor_row = self.attendanceTable.focus()
        content = self.attendanceTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


        #reset
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



       
if __name__ == "__main__":
    root = Tk()  # Create a Tkinter root window
    obj = Attendance(root)  # Create an instance of the Student class
    root.mainloop()  