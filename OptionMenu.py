from tkinter import *

w = Tk()
w.geometry("500x200")

var = StringVar()

opt = [1,2,3,4,5]
opt = map(str,opt)


dropdown = OptionMenu(w,var,*opt).pack()

w.mainloop()