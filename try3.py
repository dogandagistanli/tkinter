from tkinter import *
from tkinter import ttk

def summation():
    n1 = int(s1.get())
    n2 = int(s2.get())
    l3["text"] = "Your Result: " + str(n1+n2)
def extract():
    n1 = int(s1.get())
    n2 = int(s2.get())
    l3["text"] = "Your Result: " + str(n1-n2)
    
def product():
    n1 = int(s1.get())
    n2 = int(s2.get())
    l3["text"] = "Your Result: " + str(n1*n2)

def division():
    n1 = int(s1.get())
    n2 = int(s2.get())
    l3["text"] = "Your Result: " + str(n1/n2)
    

w = Tk()
w.title("Calculator")
w.geometry("500x300")
w.columnconfigure(0, weight=1)


form = ttk.Frame(w, padding=10)
form.grid()

s1 = StringVar()
s2 = StringVar()
l1 = Label(form, text="First Number")
l2 = Label(form, text="Second Number")
bSum = Button(form, text="+", command=summation)
bExt = Button(form, text="-", command=extract)
bPro = Button(form, text="x", command=product)
bDiv = Button(form, text="/", command=division)
e1 = Entry(form, textvariable=s1)
e2 = Entry(form, textvariable=s2)
l3 = Label(form, text="")

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=0, column=2)
e2.grid(row=0, column=3)
bSum.grid(row=1, column=0, columnspan=1, sticky="we")
bExt.grid(row=1, column=1,columnspan=2, sticky="we")
bPro.grid(row=1, column=2,columnspan=1, sticky="we")
bDiv.grid(row=1, column=3,columnspan=2, sticky="we")
l3.grid(row=2, column=0)

w.mainloop()