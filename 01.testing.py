from tkinter import *

w=Tk()
w.geometry("400x400")

def gotosecondWindow():
    # to create second window
    second=Toplevel(w)
    second.geometry("300x300")
    btn2=Button(second,text="First")
    btn2.pack()
    # to delete first window
    w.withdraw()
    second.mainloop()


btn=Button(w,text="Open",command=gotosecondWindow)
btn.pack()
w.mainloop()