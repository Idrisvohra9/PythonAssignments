from tkinter import *
import random

w = Tk()
w.geometry("640x560")

diceFaces = [PhotoImage(file="DiceTkinter\d1.png"),PhotoImage(file="DiceTkinter\d2.png"),PhotoImage(file="DiceTkinter\d3.png"),PhotoImage(file="DiceTkinter\d4.png"),PhotoImage(file="DiceTkinter\d5.png"),PhotoImage(file="DiceTkinter\d6.png")]

def Randomize():
    random.shuffle(diceFaces)

    SelectFace = random.choice(diceFaces)
    display = Label(image=SelectFace,width=600,height=600)
    display.place(x=20,y=0)
    print(SelectFace)
    btn = Button(
    width=14,
    height=2,
    background="orange",
    text="Roll",
    justify=CENTER,
    relief=SUNKEN,
    activebackground="gold",
    activeforeground="white",
    command=Randomize
    )

    btn.place(x= 260, y = 0)

Randomize()

w.mainloop()