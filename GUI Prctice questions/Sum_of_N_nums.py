from tkinter import *

w = Tk()
w.geometry("500x200")

w.title("Second question")
sum = 0
var = IntVar()
def Sum_naturalNum():
    n = var.get()
    return Label(w,text=f"{(n*(n+1))/2}").pack()

l1 = Label(w,text="Enter value:",font=("Satisfy",20),justify=CENTER).pack()

input = Entry(w,font=("satisfy",20),textvariable=var).pack()
btn = Button(w,text="Validate",font=("satisfy",20),command=Sum_naturalNum).pack()

w.mainloop()