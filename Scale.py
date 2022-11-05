from tkinter import *

w = Tk()
v = 0;
w.title("Scale")
w.config(background="maroon")
w.geometry("500x400")

def ChangeOrient() -> None:
    v+=1
    if(v%2==0):
        s1.config(orient=HORIZONTAL)
    else:
        s1.config(orient=VERTICAL)

v1 = DoubleVar()

s1 = Scale(w,variable=v1, from_=0, to= 100, orient=HORIZONTAL)
l3 = Label(w,text="Horizontal Scale")
b1 = Button(w,text="Change oreintation", command=ChangeOrient, bg="Yellow")

l1 = Label(w)
s1.pack(padx=10)
l3.pack()
b1.pack(anchor=CENTER)
l1.pack()
w.mainloop()