from tkinter import *
#create the things and then put them on the screen

#root widget window
root = Tk()

#myLabel1 = Label(root, text="Hello World").grid (row=0, column=0)

#creating a label widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Daniel Hernandez")
#tell the program where you want the labels
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop ()