from tkinter import *
from pymongo import MongoClient
from tkinter import font

client = MongoClient("localhost", 27017)
db = client.get_database("TO-DO")

coll = db.get_collection("Tasks")

w = Tk()
w.geometry('600x600')
w.title('To-do list app')
f= ("Arial",15)
# Colors:
bg = "dark slate grey"
fg = "white"
sc = "sea green"

w.config(bg=bg)

l = Label(w,text="Enter the task:",font=f,bg=bg,fg=fg)
l.place(x=10, y=10)

i = Entry(w,width=35,font=f)
i.place(x=150, y=10)
def HandleAdd():
    task = i.get()
    if task!= "":
        coll.insert_one({"task":task})
        Tasks.insert(END,task)

def HandleDel():
    # selectedTasks = []
    curSelected = Tasks.curselection()
    for e in curSelected[::-1]:
        # selectedTasks.append(Tasks.get(e))
        Tasks.delete(e)
        coll.delete_one({"task":Tasks.get(e)})
    

def HandleDelAll():
    coll.delete_many({})
    # for i in Tasks.get(0,END):
    Tasks.delete(0,END)

def HandleExit():
    w.destroy()

addTask = Button(w,text="Add Task",width=20,height=2,bg=sc,fg=fg, command=HandleAdd)
addTask.place(x=40,y=70)

delTask = Button(w,text="Delete Task",width=20,height=2,bg=sc,fg=fg, command=HandleDel)
delTask.place(x=220,y=70)

delTask = Button(w,text="Delete All Task",width=20,height=2,bg=sc,fg=fg, command=HandleDelAll)
delTask.place(x=390,y=70)

Tasks = Listbox(w,width=48,height=15,font=f,selectmode="multiple",selectbackground="teal")
Tasks.place(x=25, y=130)

Exit = Button(w,text="Exit",width=75,height=2,bg=sc,fg=fg, command=HandleExit)
Exit.place(x=25, y=476)

def DataInsertion():
    data = coll.find()
    for x in data:
        Tasks.insert(END,x["task"])
DataInsertion()
w.mainloop()