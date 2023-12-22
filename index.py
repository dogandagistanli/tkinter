from tkinter import *
from tkinter import ttk

w = Tk()
w.title('Merhaba')
w.geometry("200x300")
w.columnconfigure(0,weight=10)
form = ttk.Frame(w,padding=10)
form.grid()
ttk.Label(form,text="Merhaba").grid(column=0,row=0)
ttk.Button(form,text="CLOSE",command=w.destroy).grid(column=0,row=2)
w.mainloop()