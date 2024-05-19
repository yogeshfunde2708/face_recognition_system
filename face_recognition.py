
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2
import mysql.connector
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(root, text="Face Recognition", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("college_images/facialrecognition.png")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=70, width=750, height=800)

        img_bottom = Image.open("college_images/recognition.jpg")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=800, y=70, width=700, height=800)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recognition, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=0, y=50, width=200, height=40)

    def mark_attendance(self, i, r, n, d):
        with open("yogesh.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]
            if i not in name_list and r not in name_list and n not in name_list and d not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def face_recognition(self):
        try:
            def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))

                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Yogesh270801",  # Replace with your MySQL password
                        database="face_recognizer",
                    )
                    my_cursor = connection.cursor()
                    my_cursor.execute("SELECT name FROM student WHERE student_id=" + str(id))
                    n = my_cursor.fetchone()
                    if n:
                        n = n[0]
                    else:
                        n = "Unknown"

                    my_cursor.execute("SELECT roll FROM student WHERE student_id=" + str(id))
                    r = my_cursor.fetchone()
                    if r:
                        r = r[0]
                    else:
                        r = "Unknown"

                    my_cursor.execute("SELECT dep FROM student WHERE student_id=" + str(id))
                    d = my_cursor.fetchone()
                    if d:
                       d = d[0]
                    else:
                       d = "Unknown"

                    my_cursor.execute("SELECT student_id FROM student WHERE student_id=" + str(id))
                    i = my_cursor.fetchone()
                    if i:
                        i = i[0]
                    else:
                        i = "Unknown"

                        connection.close()

                    if confidence > 77:
                        cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, h]

                return coord

            def recognize(img, clf, faceCascade):
                coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
                return img

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                if not ret:
                    break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to Face Recognition", img)

                if cv2.waitKey(1) == 13:  # Press Enter to exit
                    break

            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
