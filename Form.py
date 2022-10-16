from tkinter import *

w = Tk()
U = StringVar()
P = StringVar()

def Submit():
    Username = U.get()
    Password = P.get()
    ValueLabel = Label(w,text=f"Submitted Values: \n\
Username: {Username}\n\
Password: {Password}",
        justify=CENTER,
        font=("Arial",20))
    ValueLabel.grid(row=4, column=1, sticky=S, pady=10,padx=10)

def Start():
    w.geometry("500x400")
    w.configure(background="white")

    Heading = Label(w,text="Form:",font=("Arial",20))
    Heading.grid(row=0,column=1, sticky=S, pady=10,padx=10)

    uLabel = Label(w,text="Username:",font=("Arial",10))
    pLabel = Label(w,text="Password:",font=("Arial",10))

    uLabel.grid(row=1, column=0, sticky=W, pady=10,padx=10)
    pLabel.grid(row=2, column=0, sticky=W, pady=10,padx=10)

    Username = Entry(w,font=("Arial",10),background="lightgrey",width=40,textvariable=U)
    Pass = Entry(w,font=("Arial",10),show="*",background="lightgrey",width=40,textvariable=P)

    Username.grid(row=1, column=1, sticky=W, pady=10,padx=10)
    Pass.grid(row=2, column=1, sticky=W,pady=10,padx=10)

    submit = Button(w,text="Submit",font=("Arial",15),background="lightgrey",command=Submit)
    submit.grid(row=3, column=1, sticky=S,pady=10,padx=10)

    
    w.mainloop()

Start()