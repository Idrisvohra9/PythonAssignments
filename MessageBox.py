from tkinter import *
from tkinter import messagebox

root=Tk()

messagebox.showinfo("Info","Saved Succesfully")
messagebox.showerror("Error","Oops Something Went Wrong")
messagebox.askokcancel("I Helped your mom","Can't do anything.")
messagebox.showwarning("Warning","Warning")
messagebox.askquestion("Are you dumb?","Probably")
messagebox.askretrycancel("Well fuck it.","Yeah")
messagebox.askyesno("Want something?")
messagebox.askyesnocancel("Are you sure you want to continue?","You cannot reverse this action!")
root.mainloop()