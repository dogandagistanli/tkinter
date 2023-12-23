from tkinter import *
from tkinter import ttk
from tkinter import font



def drawPattern():
    ch = ch1.get()
    line = int(line1.get())
    square_pattern = ""
    for i in range(line):
        if(i==0 or i==line-1):
            for j in range(line): 
                square_pattern += ch   
            square_pattern +="\n"
        else:
            square_pattern += ch 
            for c in range(0,line-2):
                square_pattern +=" "
            square_pattern += ch       
            square_pattern += "\n"
    l3["text"]=square_pattern
        
        
        

w = Tk()
w.title("PATTERN")
w.geometry("200x300")
w.columnconfigure(0,weight=1)

form = ttk.Frame(w, padding=10)
form.grid()

ch1 = StringVar()
line1 = StringVar()
l1 = Label(form, text="Lines: ")
l2 = Label(form, text="Character: ")
e1 = Entry(form, textvariable=line1)
e2 = Entry(form, textvariable=ch1)
b1 = Button(form, text="Draw", command=drawPattern)
l3 = Label(form,text="",font=font.nametofont("TkFixedFont"),justify="left")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b1.grid(row=2, column=0, columnspan=2, sticky="we")
l3.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

w.mainloop()





