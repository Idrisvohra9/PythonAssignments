import tkinter as tk
from tkinter import *

w = Tk()
w.geometry("500x500")

label1 = Label(text="Listbox single selection:", font=("Arial",20))
label1.pack()
listSample = Listbox(w, width=70, height=30, fg="maroon", font=("Arial",20),justify=CENTER, bg="lightgrey")

listSample.insert(1,"Pizza")
listSample.insert(2,"Burger")
listSample.insert(3,"Noodles")
listSample.insert(4,"French Fries")

listSample.pack()

label2 = Label(text="Listbox Multiple selection:",font=("Arial",20))
label2.pack()

listSample2 = Listbox(w,width=70,height=30,fg="maroon",font=("Arial",20),justify=CENTER,bg="lightgrey", selectmode="multiple",selectbackground="grey")

listSample2.insert(1,"Pizza")
listSample2.insert(2,"Burger")
listSample2.insert(3,"Noodles")
listSample2.insert(4,"French Fries")

listSample2.pack()

w.mainloop()