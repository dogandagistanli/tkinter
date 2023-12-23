from tkinter import *
from tkinter import ttk

w = Tk()
w.title("Tic-Tac-Toe Game")

form = ttk.Frame(w)
form.grid()



canvas = Canvas()
canvas.create_line(15, 25, 200, 25)  #yatay
canvas.create_line(15, 85, 200, 85)  #yatay
canvas.create_line(15, 145, 200, 145) #yatay
canvas.create_line(75, 25, 75, 205)  #dikey
canvas.create_line(135, 25, 135, 205) #dikey 
canvas.create_line(15, 205, 200, 205) #yatay


def callback(event):
    
    if((event.y<205 and event.y>25) and (event.x>15 and event.x<200)):
        print("clicked at", event.x, event.y)
        l2.place(x=event.x,y=event.y)
        l2["text"] = "O"
        

canvas.bind("<Button-1>",callback)  
canvas.grid()


l1 = Label(text="First player is X")
l1.place(x=250,y=100)
l2 = Label(text="")
l2["text"] = ""

w.mainloop()


