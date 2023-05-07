#2. Write a program to display a menu on the menu bar.

from tkinter import *  
  
top = Tk()  
  
def first():  
    print("this is the first key ") 

def second():
    print("this is the second key")
    
def third():
    print("this is the third key")

menubar = Menu(top)  
menubar.add_command(label="one", command=first)
menubar.add_command(label="two", command=second)
menubar.add_command(label="three", command=third)
menubar.add_command(label="quit", command=top.quit)  
  
# display the menu  
top.config(menu=menubar)  
  
top.mainloop()