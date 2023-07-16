from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("MessageBox")

#showinfo, showwarning, showerror, askquestion, askcancel, askyseno

def popup():
    response = messagebox.askyesno ("This is my popup", "Hello World")
    Label (root, text=response).pack()
    if response == 1:
        Label (root, text="you clicked yes").pack()
    else:
        Label (root, text="you clicked no").pack()

Button (root, text="Popup", command=popup).pack()
root.mainloop ()
