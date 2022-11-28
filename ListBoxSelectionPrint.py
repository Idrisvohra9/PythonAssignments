from select import select
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("500x500")


def getCourses():
    selectCourses = []
    curSelected = lb.curselection()
    for i in curSelected:
        c = lb.get(i)
        selectCourses.append(c)
    print(selectCourses)


# def Validate

courses = Label(text="Select Courses")
courses.pack()
courseslist = ["Software development", "Animation", "ITIMS", "Digital design"]
lb = Listbox(font=("Arial", 15), selectmode="multiple")
# submit = Button(w,text="Insert",font=('Arial',50))
# submit.pack()

for i in range(len(courseslist)):
    lb.insert(END, courseslist[i])

btn = Button(text="Get Cousrses", command=getCourses)
btn.pack()
lb.pack()
root.mainloop()
