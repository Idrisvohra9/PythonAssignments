from tkinter import *

w = Tk()
w.geometry('500x500')
w.title('')

w.config()
# Spinbox is a counter of number input kindof box in which count can be increased or decreased by one
spin = Spinbox(w,from_=0,to=25)
spin.pack()
w.mainloop()