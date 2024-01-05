import tkinter as tk
from tkinter import *

class Books:
    def __init__(self, root):
        self.root = root
        self.book_list = []
        
    def bookList(self, index):
        # It's not clear what you want to do with the index parameter
        pass
        
    def add_book(self, book_name):
        self.book_list.append(book_name)
        listbox.insert(tk.END, book_name)
        
    def on_select(self, event):
        selected_index = listbox.curselection()
        if selected_index:
            if event == 'delete':
                listbox.delete(selected_index)

root = tk.Tk()
root.title("BOOK OPERATOR")
root.geometry("500x500")

books_app = Books(root)

s1 = StringVar()
e1 = tk.Entry(root, textvariable=s1)
b1 = tk.Button(root, text="DELETE", command=lambda: books_app.on_select('delete'))
b2 = tk.Button(root, text="ADD", command=lambda: books_app.add_book(e1.get()))
listbox = Listbox(root, font=("Arial", 15))
listbox.pack(fill=BOTH)

e1.pack()
b1.pack()
b2.pack()
root.mainloop()
