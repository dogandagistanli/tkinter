from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")

def add_task():
    task = s1.get()
    if task:
        listbox.insert(END, task)
        s1.set("")  # Clear the entry after adding a task

def remove_task():
    selection = listbox.curselection()
    for index in reversed(selection):
        listbox.delete(index)

def clear_task():
    listbox.delete(0,END)





s1 = StringVar()
e1 = tk.Entry(root, font=("Arial", 15), textvariable=s1)
b1 = tk.Button(root, text="Add task", font=("Arial", 15), command=add_task)
b2 = tk.Button(root, text="Remove selected task", font=("Arial", 15),command=remove_task)
b3 = tk.Button(root, text="Clear all tasks", font=("Arial", 15),command=clear_task)

l1 = tk.Label(root, text="Tasks:", font=("Arial", 15))
listbox = Listbox(root, font=("Arial", 15))

e1.pack(fill=BOTH)
b1.pack(fill=BOTH)
b2.pack(fill=BOTH)
b3.pack(fill=BOTH)

l1.pack(fill=BOTH)
listbox.pack(fill=BOTH)

root.mainloop()
