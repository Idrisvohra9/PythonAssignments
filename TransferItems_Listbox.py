import tkinter as tk
from tkinter import *

# Setting up a window:
w = Tk()

w.geometry("500x400")
w.configure(background="lightgreen")
w.wm_maxsize(500,400)

# Lists:
favList = ["Pushups","Running","Memes","Coding"]

allList = ["Mobile","Instagram","Twitter","Google"]

# Functions:

def addAll_List2():
    # Delete items from lb1 and insert it to lb2
    for i in range(len(favList)):
        lb2.insert(END,favList[i])
        lb1.delete(0,END)
        
    # It will make the favList empty:
    for i in range(len(favList)-1,-1,-1):
        favList.pop(i)
    

def addSel_List2():
    curSelected=lb1.curselection()
    print("INDEXes of current selection: ",curSelected)
    for i in curSelected:
        c=lb1.get(i)
        lb2.insert(END,c)
        lb1.delete(i)
        if(i<=len(favList)):
            favList.pop(i)
    print(favList)

def addAll_List1():
    for i in range(len(allList)):
        lb1.insert(END,allList[i])
        lb2.delete(0,END)
        
def addSel_List1():
    curSelected=lb2.curselection()
    for i in curSelected:
        c = lb2.get(i)
        lb1.insert(END,c)


# Labels:
l1 = Label(w,text="Favourite List:",font=("Satisfy",20),fg="white",justify=CENTER,background="lightgreen")
l1.grid(row=0,column=0)

l2 = Label(w,text="All things:",font=("Satisfy",20),fg="white",justify=CENTER,background="lightgreen")
l2.grid(row=0,column=2)


# Fav listbox:
lb1 = Listbox(w, width=16, height=8, fg="maroon", font=("Times new roman",16),background="silver",selectmode="multiple",selectbackground="lightgrey",selectforeground="black",justify=CENTER)
lb1.grid(row=1, column=0,padx=4,pady=55,rowspan=4)

# All ListBox:
lb2 = Listbox(w, width = 16, height = 8, fg = "maroon", font = ("Times new roman",16),background= "silver",selectmode="multiple",selectbackground="lightgrey",selectforeground="black",justify=CENTER)

lb2.grid(row=1, column=2,padx=4,pady=55,rowspan=4)

def UpdateList():
    for i in range(len(favList)):
        lb1.insert(END,favList[i])
    for j in range(len(allList)):
        lb2.insert(END,allList[j])

UpdateList()
# Buttons:
LtoR_addAll = Button(text="Add all →",width=12,height=1, justify=CENTER,font=("Satisfy",9,"bold"),command=addAll_List2)
LtoR_addSel = Button(text="Add selected →",width=12,height=1, justify=CENTER,font=("Satisfy",9,"bold"),command=addSel_List2)

RtoL_addAll = Button(text="Add all ←",width=12,height=1, justify=CENTER,font=("Satisfy",9,"bold"),command=addAll_List1)
RtoL_addSel = Button(text="Add selected ←",width=12,height=1, justify=CENTER,font=("Satisfy",9,"bold"),command=addSel_List1)


LtoR_addAll.grid(row=1,column=1,padx=15, pady=2, ipadx=2)

LtoR_addSel.grid(row=2,column=1,padx=15, pady=2, ipadx=2)


RtoL_addAll.grid(row=3,column=1,padx=15, pady=2, ipadx=2)

RtoL_addSel.grid(row=4,column=1,padx=15, pady=2, ipadx=2)

w.mainloop()