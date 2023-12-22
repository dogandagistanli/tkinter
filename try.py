from tkinter import *
from tkinter import ttk

def updateLabel():
    l2["text"] = "Hello " + s.get()
    
w = Tk()
w.title("Dogan")
w.geometry("300x200")
w.columnconfigure(0,weight=1)

form = ttk.Frame(w, padding=10)
form.grid()

s = StringVar()
l1 = Label(form, text="İsİM GİR")
l2= Label(form, text=" ", font="Monospace")
e1 = Entry(form, textvariable=s)
b1 = Button(form, text="Close", command= w.destroy, bg="red")
b2 = Button(form, text="Say Hello", command=updateLabel, bg="green")

l1.grid(column=0, row=0)
e1.grid(column=1, row=0)
b2.grid(column=0, columnspan=2, row=2, sticky="we")
l2.grid(column=0, columnspan=2, row=3, sticky="we")
b1.grid(column=0, columnspan=2, row=4, sticky="we")

w.mainloop()