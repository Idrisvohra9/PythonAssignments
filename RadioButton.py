from tkinter import *

w = Tk()
w.title("Radio Button")

w.geometry("500x400")

var = StringVar(w," ")

l = Label(w,bg="White", width =20)
l.pack()
def printSelected():
    l.config(text="You have selected "+ var.get())

r1 = Radiobutton(w, text="Option A",variable=var, value="A", command=printSelected)
r1.pack()

r2 = Radiobutton(w, text="Option B",variable=var, value="B", command=printSelected)
r2.pack()

r3 = Radiobutton(w, text="Option C",variable=var, value="C", command=printSelected)
r3.pack()

w.mainloop()