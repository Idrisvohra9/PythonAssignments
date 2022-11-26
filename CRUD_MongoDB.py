from tkinter import *
from pymongo import MongoClient

w = Tk()
w.geometry("500x500")
w.title("CRUD operations MongoDB")
client = MongoClient()

# db
database = client["student"]

# collection
col = database["student_info"]
output = Label(w, text="Output", fg="dark green", bg="darkslategray4")
output.grid(row=6, column=0)
# insert
def HandleInsert():
    name = e1.get()
    col.insert_one({"name": name})
    output.config(text="Data sucessfully inserted...")


# to get values from collection
def HandleGet():
    data = col.find({"name": e1.get()})

    for i in data:
        output.config(text=i)


# to delete value from collection
def HandleDelete():
    col.delete_one({"name": e1.get()})
    output.config(text="Deleted Sucessfully...")


l2 = Label(w, text="to Name: ", bg="darkslategray4")
e2 = Entry(w)


def insertUpdate():
    l2.grid(row=5, column=0)
    e2.grid(row=5, column=1)

    b5 = Button(w, text="Update", command=update)
    b5.grid(row=5, column=2)


def update():
    col.update_one({"name": e1.get()}, {"$set": {"name": e2.get()}})
    output.config(text="Data updated sucessfully!")


l = Label(w, text="Enter Name: ", bg="darkslategray4")
l.grid(row=0, column=0)

e1 = Entry(w)
e1.grid(row=0, column=1)

b1 = Button(w, text="Submit", command=HandleInsert, width=10, height=2)
b1.grid(row=1, column=1, pady=5)
b2 = Button(w, text="Get", command=HandleGet, width=10, height=2)
b2.grid(row=2, column=1, pady=5)
b3 = Button(w, text="Delete", command=HandleDelete, width=10, height=2)
b3.grid(row=3, column=1, pady=5)
b4 = Button(w, text="Update", command=insertUpdate, width=10, height=2)
b4.grid(row=4, column=1, pady=5)

w.config(bg="darkslategray4")
w.mainloop()