from tkinter import *
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.get_database("FormCredentials")
col = db.get_collection("Credentials")


def validateLogin(username, password):
	uname = username.get()
    psw = password.get()
    return
    

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  



#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()