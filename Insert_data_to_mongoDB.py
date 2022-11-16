from pymongo import MongoClient
from tkinter import *

w = Tk()
w.geometry('500x500')
w.title('Form Submission To MongoDB')

# Steps to getting connected to MongoDB:
# 1. Instantiate mongo client
# 2. create or connect to a database using the client
# 3. instantiate a collection to the database
# 4. Now you can perfrom any operations you want!!

client = MongoClient() # if we do not specify the hostname or port, it will take the default value for hostname and port that is localhost and 27017 and point to the localhost connection in the machine's mongoDB's default connection.

# insert
def HandleInsert():
    # Create a database
    database = client["student"]# Creating a database like this does not make duplicate database with a same name it only works for once.

    # Collection
    col = database["student_info"]

    name = e1.get() # One thing to note that without making a string variable for Entry widget we can directly get the value from the object itself by using var.get()
    col.insert_one({"name":name})
    print("Data inserted successfully.")
    

l = Label(w,text="Enter name: ",bg="grey")
l.grid(column=0,row=0)
e1 = Entry(w)
e1.grid(column=1,row=0)
b1 = Button(w,text="Submit", command=HandleInsert)
b1.grid(column=1,row=1,pady=10,padx=10)

w.config(bg="grey")
w.mainloop()