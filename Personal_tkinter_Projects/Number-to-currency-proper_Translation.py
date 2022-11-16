from tkinter import *
from tkinter import messagebox
from googletrans import Translator

w = Tk()
w.geometry("650x600")
w.title("Numeric to word currency translator/converter")

font = ("High Tower Text", 20)
bg = "Maroon"
w.config(background=bg)
nInp = StringVar(w)
lang = StringVar(w, " ")

def Unit(n):
    unit = [
        "",
        "One ",
        "Two ",
        "Three ",
        "Four ",
        "Five ",
        "Six ",
        "Seven ",
        "Eight ",
        "Nine ",
    ]
    return unit[int(n)]

def Pref(n):
    pref = ["", "Hundred ", "Thousand ", "Lakh ", "Crore "]
    p = ""
    if(len(n)<3):
        p = pref[0]
    if(len(n)==3):
        p = pref[1]
    if(len(n)==4):
        p = pref[2]
    if(len(n)==6):
        p = pref[3]
    if(len(n)==8):
        p = pref[4]
    return p
    
def Tens(n):
    tens = [
        "",
        "Ten ",
        "Twenty ",
        "Thirty ",
        "Fourty ",
        "Fifty ",
        "Sixty ",
        "Seventy ",
        "Eighty ",
        "Ninety ",
    ]
    return tens[int(n[0])]

def El_l(n):
    el_l = [
        "",
        "Eleven ",
        "Twelve ",
        "Thirteen ",
        "Fourteen ",
        "Fifteen ",
        "Sixteen ",
        "Seventeen ",
        "Eighteen ",
        "Nineteen ",
    ]
    return el_l[int(n[1])]

def ConvertToWord():
    n = nInp.get()
    l = lang.get()
    if l == " ":
        l = "en"
    startI = 0
    l3 = Label(w,fg="white",bg=bg,font=font)
    l3.pack()
    endI = len(n) - 1
    print("Langauge selected: " + l)
    if len(n) != 0:
        # Check if the field has numbers only
        if n.isnumeric():
            # output = El_l()
            if(len(n) == 1):
                output = Unit(n)
            # if(len(n) == 2):
            #     output = 
            txt = Translator.translate("Output: "+output+"\-",l).text
            l3.config(text=txt)
        else:
            messagebox.showwarning(
                "Illegal input",
                "The input field shouldn't contain any charcters other than numbers.",
            )
    else:
        messagebox.showwarning("Illegal input", "The input field shouldn't be empty.")


l1 = LabelFrame(w, text="Enter numeric currency:", font=font, bg=bg)
l1.pack()

entry = Entry(l1, font=font, bg=bg, textvariable=nInp, border=0)
entry.pack()

l2 = LabelFrame(w, text="Translate to:", bg=bg, font=font, fg="Grey")
l2.pack()

# Languages option:

r1 = Radiobutton(l2, text="English", value="en", variable=lang, bg=bg)
r1.grid(row=0, column=0)

r2 = Radiobutton(l2, text="Hindi", value="hi", variable=lang, bg=bg)
r2.grid(row=0, column=1)

r3 = Radiobutton(l2, text="Gujarati", value="gu", variable=lang, bg=bg)
r3.grid(row=0, column=2)

r4 = Radiobutton(l2, text="Urdu", value="ur", variable=lang, bg=bg)
r4.grid(row=0, column=3)

button = Button(w, text="Convert", bg=bg, font=font, command=ConvertToWord)
button.pack(pady=20)
w.mainloop()
