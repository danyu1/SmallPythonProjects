from tkinter import *
import PIL
from PIL import ImageTk, Image

root = Tk ()
root.title("IMAGES")
root.iconbitmap('Lock.ico')

my_img = ImageTk.PhotoImage(Image.open("x.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button (root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop ()