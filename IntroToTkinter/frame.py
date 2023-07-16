from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title ("Frame Test")

frame = LabelFrame (root, text="This is my frame...", padx = 5, pady = 5)
frame.pack (padx = 100, pady = 100);

b = Button (frame, text="Don't Click Here!")
#with a frame you can grid the button, you don't also have to pack the button
b.grid(row=0, column=0)

root.mainloop ()