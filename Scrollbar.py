from tkinter import *

w = Tk()
w.config(background="maroon")
scroll = Scrollbar(w)
scroll.pack(fill=Y,side="right")

lb = Listbox(w,yscrollcommand=scroll.set)
for i in range(31):
    lb.insert(END,"Number: " + str(i))
lb.pack()

scroll.config(command=lb.yview)
w.mainloop()