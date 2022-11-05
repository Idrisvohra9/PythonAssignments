from tkinter import *

w = Tk()
w.geometry("500x400")
w.title("Bill")
w.config(background="maroon")

m1 = IntVar(w)
m2 = IntVar(w)
m3 = IntVar(w)
m4 = IntVar(w)

def Calculate():
    price.pack()
    bill = m1.get() + m2.get() + m3.get() + m4.get()
    price.config(text=f"Price :{bill}/-")

h1 = Label(w,text="Menu:",font=("Times new Roman",30,"bold"))
h1.pack()

item1 = Checkbutton(w,text="Pizza   200/-",font=("sans serif",10),onvalue=200,offvalue=0,variable=m1)
item1.pack(pady=5)

item2 = Checkbutton(w,text="Burger   100/-",font=("sans serif",10),onvalue=100,offvalue=0,variable=m2)
item2.pack(pady=5)

item3 = Checkbutton(w,text="Cold Drinks   20/-",font=("sans serif",10),onvalue=20,offvalue=0,variable=m3)
item3.pack(pady=5)

item4 = Checkbutton(w,text="French Fries   20/-",font=("sans serif",10),onvalue=20,offvalue=0,variable=m4)
item4.pack(pady=5)

Bill = Button(w,text="Bill",font=("sans serif",10),background="black",width=5,height=1, fg="white",command=Calculate)

Bill.pack(pady=5)
price = Label(w,text="",font=("sans serif",20),fg="crimson")

w.mainloop()