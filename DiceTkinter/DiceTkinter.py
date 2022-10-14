from tkinter import *
import random

SelectFace = ""
img =1
diceFaces = ["DiceTkinter\d1.png","DiceTkinter\d2.png","DiceTkinter\d3.png","DiceTkinter\d4.png","DiceTkinter\d5.png","DiceTkinter\d6.png"]

def Randomize():
    random.shuffle(diceFaces)
    global SelectFace

    SelectFace = random.choice(diceFaces)
    print(SelectFace)
    global img
    img = PhotoImage(file=SelectFace)
    

def Start():

    w = Tk()
    w.geometry("640x560")

    Randomize()


    display = Label(image=img,width=600,height=600)

    display.place(x=20,y=0)
    
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
    w.mainloop()

Start()