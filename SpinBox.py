from tkinter import *

w = Tk()
w.geometry('500x500')
w.title('')

w.config()

spin = Spinbox(w,from_=0,to=25)
spin.pack()
w.mainloop()