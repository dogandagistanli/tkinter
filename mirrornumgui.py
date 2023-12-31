import tkinter as tk
from tkinter import StringVar

def control(num1, num2):
    return mirror(num1) == num2

def mirror(n1):
    n2 = (n1 % 10) * 10 + (n1 // 10)
    return n2

def check_numbers():
    c1 = int(s1.get())
    c2 = int(s2.get())
    if control(c1, c2):
        result.config(text="Yes, the numbers are mirrors.")
    else:
        result.config(text="No, the numbers are not mirrors.")

root = tk.Tk()
root.title("Mirror Numbers Checker")
root.geometry("300x300")

s1 = StringVar()
s2 = StringVar()

l1 = tk.Label(root, text="Enter first number:")
b1 = tk.Entry(root, textvariable=s1)
l2 = tk.Label(root, text="Enter second number:")
b2 = tk.Entry(root, textvariable=s2)
button = tk.Button(root, text="Check", command=check_numbers)
result = tk.Label(root)

l1.pack()
b1.pack()
l2.pack()
b2.pack()
button.pack()
result.pack()

root.mainloop()
