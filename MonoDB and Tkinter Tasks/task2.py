from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pymongo import MongoClient

root =Tk()

root.geometry("800x600")
root.title("Employee Management System")
root.resizable(0,0)

# database connection and collection formation.

client = MongoClient("localhost",27017)

db = client["Employee_management_system"]
col = db["Employee_data"]
i =0

# commands
def GetId():
    i+=1

def add():
    # Get Values
    name_value = name_entry.get()
    age_value = age_entry.get()
    doj_value = doj_entry.get()
    email_value = email_entry.get()
    gen_value = Variable.get()
    contact_value = contact_entry.get()
    address_value = address_entry.get("1.0",END)

    if len(name_value and age_value and doj_value and email_value and contact_value and address_value and gen_value)==0:    
        messagebox.showinfo('Error !!','Fields are empty')
    else:
        # Insert to database
        col.insert_one({"name":name_value,"age":age_value,"D.O.J":doj_value,"email":email_value,"Gender":gen_value,"Contact":contact_value,"Address":address_value})
        
        # id = col.find_one({},{"_id":1})["_id"]
        # Delete all previous records in the tree to avoid repetition
        # for existingdata in tree.get_children():
        #     tree.delete(existingdata)
        GetId()
        tree.insert("",END,values=[i,name_value,age_value,doj_value,email_value,gen_value,contact_value,address_value])

def delete():
    try:
        selected_item = tree.selection()[0]
        print(selected_item)
        # col.delete_one({selected_item})
        tree.delete(selected_item)
    except:
        messagebox.showinfo('Error !!',"No record Selected.Can't delete")

def delete_all():
    col.delete_many({})
    for item in tree.get_children():
        tree.delete(item)

def update():
    col.update_one({"name": name_entry.get(),"age":age_entry.get()}, {"$set": {"name": name_entry.get(),"age":age_entry.get()}})
    
    
def reset():
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    doj_entry.delete(0,END)
    email_entry.delete(0,END)
    contact_entry.delete(0,END)
    address_entry.delete(1.0,END)
    Variable.set("")
    
# Labels and fields

heading = Label(root,text="Employee Management System",font="Arial 15 bold",bg="navy",fg="white")
heading.place(x=30,y=30)

name = Label(root,text="Name",font="Arial 15",bg="navy",fg="white")
name.place(x=30,y=80)

name_entry = Entry(root,width=20,font="Arial 15")
name_entry.place(x=130,y=80)

age = Label(root,text="Age",font="Arial 15",bg="navy",fg="white")
age.place(x=430,y=80)

age_entry = Entry(root,width=20,font="Arial 15")
age_entry.place(x=530,y=80)

doj = Label(root,text="D.O.J",font="Arial 15",bg="navy",fg="white")
doj.place(x=30,y=120)

doj_entry = Entry(root,width=20,font="Arial 15")
doj_entry.place(x=130,y=120)

email = Label(root,text="Email",font="Arial 15",bg="navy",fg="white")
email.place(x=430,y=120)

email_entry = Entry(root,width=20,font="Arial 15")
email_entry.place(x=530,y=120)

gender = Label(root,text="Gender",font="Arial 15",bg="navy",fg="white")
gender.place(x=30,y=160)

Options = ['male','female','other                                                  ']
Variable = StringVar(root)
Variable.set("")
font_size=12
font_style="Arial"

gender_opt = OptionMenu(root,Variable,*Options)
gender_opt.configure(width=20,font=(font_style,font_size),bg="white",borderwidth=0)
gender_opt.place(x=131,y=160)

contact = Label(root,text="Contact",font="Arial 15",bg="navy",fg="white")
contact.place(x=430,y=160)

contact_entry = Entry(root,width=20,font="Arial 15")
contact_entry.place(x=530,y=160)

address = Label(root,text="Address",font="Arial 15",bg="navy",fg="white")
address.place(x=30,y=200)

address_entry = Text(root,height=5,width=65,font="monospace 15")
address_entry.place(x=33,y=240)

# Buttons

add_btn = Button(root,text="Add Details",font="comicsansms 13",bg="medium sea green",fg="ghostwhite",width=17,command=add)
add_btn.place(x=30,y=380)

update_btn = Button(root,text="Update Details",font="comicsansms 13",bg="steel blue",fg="ghostwhite",width=17,command=update)
update_btn.place(x=215,y=380)

delete_btn = Button(root,text="Delete Details",font="comicsansms 13",bg="brown",fg="ghostwhite",width=17,command=delete_all)
delete_btn.place(x=405,y=380)

clear_btn = Button(root,text="Clear Details",font="comicsansms 13",bg="dark orange",fg="ghostwhite",width=17,command=reset)
clear_btn.place(x=590,y=380)

cols=(1,2,3,4,5,6,7,8)

tree = ttk.Treeview(root,selectmode="browse",columns = cols,show="headings")
tree.place(x=30,y=430)

tree.column(1,anchor=CENTER,stretch=NO,width=30)
tree.heading(1,text="ID")
tree.column(2,anchor=CENTER,stretch=NO,width=100)
tree.heading(2,text="Name")
tree.column(3,anchor=CENTER,stretch=NO,width=40)
tree.heading(3,text="Age")
tree.column(4,anchor=CENTER,stretch=NO,width=80)
tree.heading(4,text="D.O.J")
tree.column(5,anchor=CENTER,stretch=NO,width=150)
tree.heading(5,text="Email")
tree.column(6,anchor=CENTER,stretch=NO,width=60)
tree.heading(6,text="Gender")
tree.column(7,anchor=CENTER,stretch=NO,width=90)
tree.heading(7,text="Contact")
tree.column(8,anchor=CENTER,stretch=NO,width=170)
tree.heading(8,text="Address")

root.config(bg="navy")

root.mainloop()