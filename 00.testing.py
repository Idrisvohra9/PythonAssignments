from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from tkinter import ttk

client = MongoClient("localhost", 27017)
DB = client.get_database("Student_DB")
Coll = DB.get_collection("student_Data")
root = Tk()
root.state("zoomed")  # to maximize window

g = IntVar()
gender = ""


def HandleInsert():
    # Get values:
    name = name_e.get()
    email = email_e.get()
    age = age_e.get()
    if g.get() == 1:
        gender = "Male"
    else:
        gender = "Female"
    # Insert into DB:
    Coll.insert_one({"Name": name, "Email": email, "Gender": gender, "Age": age})

    # Delete all previous records in the tree (Does't cause repeatation)
    for existingdata in tree.get_children():
        tree.delete(existingdata)
     
    tree.insert("", END, values=[name, email, gender, age])
    messagebox.showinfo("Success", "Data Inserted sucessfully.....")
    reset()


def HandleUpdate():
    pass


def HandleDelete():
    pass


def HandleGet():
    pass


def reset():
    name_e.delete(0, END)
    email_e.delete(0, END)
    age_e.delete(0, END)


# frame for form
f1 = Frame(root)
f1.place(x=200, y=200)
# frame for radio button
f2 = Frame(f1)
f2.grid(row=2, column=1)
name_l = Label(f1, text="Name")
name_l.grid(row=0, column=0)
name_e = Entry(f1, width=30)
name_e.grid(row=0, column=1)
email_l = Label(f1, text="Email Address")
email_l.grid(row=1, column=0)
email_e = Entry(f1, width=30)
email_e.grid(row=1, column=1)
gender_l = Label(f1, text="Gender")
gender_l.grid(row=2, column=0)

cols = (1, 2, 3, 4)
tree = ttk.Treeview(root, selectmode="browse", columns=cols, show="headings")
tree.pack(side="right")

tree.heading(1, text="Name")
tree.heading(2, text="Email")
tree.heading(3, text="Gender")
tree.heading(4, text="Age")


Radiobutton(f2, text="Male", variable=g, value=1).grid(row=0, column=0)
Radiobutton(f2, text="Female", variable=g, value=0).grid(row=0, column=1)


age_l = Label(f1, text="Age")
age_l.grid(row=3, column=0)
age_e = Entry(f1, width=30)
age_e.grid(row=3, column=1)
b1 = Button(root, bg="brown", fg="white", text="Submit", width=30, command=HandleInsert)
b1.place(x=200, y=400)
b2 = Button(root, bg="brown", fg="white", text="Edit", width=30, command=HandleUpdate)
b2.place(x=200, y=430)
b3 = Button(root, bg="brown", fg="white", text="Delete", width=30, command=HandleDelete)
b3.place(x=200, y=460)

b4 = Button(root, bg="brown", fg="white", text="Get", width=30, command=HandleGet)
b4.place(x=200, y=490)

b5 = Button(root, bg="brown", fg="white", text="Reset", width=30, command=reset)
b5.place(x=200, y=520)
root.mainloop()
