#1. Write a program to display two labels with different colored background.

import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Red", width="90", height="10",borderwidth=1, relief="solid")
label1 = tk.Label(root, text="White", width = "90", height = "10",borderwidth=1, relief="solid")
label2 = tk.Label(root, text="Blue", width = "90", height = "10",borderwidth=1, relief="solid")

label.config(bg="red")
label1.config(bg="white")
label2.config(bg="blue")

label.grid(column=0, row=1, padx=100, pady=10)
label1.grid(column=0, row=2, padx=100, pady=10)
label2.grid(column=0, row=3, padx=100, pady=10)

root.mainloop()