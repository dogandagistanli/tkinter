from tkinter import *
from tkinter import ttk

def calculate():
    year = int(s1.get())
    age = int(s2.get())
    l3["text"] = "Your age " + str(age-year)
    
w = Tk()
w.title("Age Calculator")
w.geometry("300x300")
w.rowconfigure(0,weight=1)

form = ttk.Frame(w, padding=10)
form.grid()


s1 = StringVar()
s2 = StringVar()
l1 = Label(form, text="Enter birth year")
l2 = Label(form, text="Enter current year")
l3 = Label(form, text="")
e1 = Entry(form, textvariable=s1)
e2 = Entry(form, textvariable=s2)
b1 = Button(form, text="Calculate", command=calculate)

l1.grid(column=0, row=0)
e1.grid(column=1, row=0)
l2.grid(column=0, row=1)
e2.grid(column=1, row=1)
b1.grid(column=0, row=2, columnspan=2, sticky="we")
l3.grid(column=0, row=3, columnspan=2)

w.mainloop()
