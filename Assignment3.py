import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)

canvas.pack()


def canvas_click(event):
    x = event.x
    y = event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")

# Bind the <Button-1> event to the canvas_click function
canvas.bind("<Button-1>", canvas_click)

# Start the main event loop
root.mainloop()
