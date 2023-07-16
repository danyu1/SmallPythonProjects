from tkinter import *
#create the things and then put them on the screen

#root widget window
root = Tk()

e = Entry(root, width=50, bg="blue", borderwidth="5")
e.pack()
e.insert(0, "Enter your name: ")

def myClick ():
    hello = "Hello " + e.get()
    myLabel = Label (root, text=hello)
    myLabel.pack()

myButton = Button (root, text="Enter Your Name", command=myClick, fg="blue")
myButton.pack()

root.mainloop ()