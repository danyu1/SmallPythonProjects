from tkinter import *
#create the things and then put them on the screen

#root widget window
root = Tk()

def myClick ():
    myLabel = Label (root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button (root, text="Click Me!", command=myClick, fg="blue")
myButton.pack()

root.mainloop ()