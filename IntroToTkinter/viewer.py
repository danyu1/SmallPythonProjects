from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title("IMAGES")
root.iconbitmap('Lock.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/download.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/y.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/z.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/a.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/download copy.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label (root, text = "Image 1 of" + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid (row=0, column=0, columnspan=3)

button_back = Button (root, text="<<", command=lambda: back(4))
button_quit = Button (root, text="Exit Program", command=root.quit)
button_forward = Button (root, text=">>", command=lambda: forward (1))

button_back.grid (row=1, column=0)
button_quit.grid (row=1, column=1)
button_forward.grid(row=1, column=2)

def forward (image_index):
    global my_label
    global button_forward
    global button_back
    
    if (image_index == len(image_list)):
        my_label.grid_forget()
        my_label = Label (image=image_list[0])
        button_forward = Button (root, text=">>", command=lambda: forward(1))
        button_back = Button (root, text="<<", command=lambda: back(4))
        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid (row=1, column=0)
        button_forward.grid(row=1, column=2)
    else:
        my_label.grid_forget()
        my_label = Label (image=image_list[image_index])
        button_forward = Button (root, text=">>", command=lambda: forward(image_index+1))
        button_back = Button (root, text="<<", command=lambda: back(image_index-1))
        my_label.grid (row=0, column=0, columnspan=3)
        button_back.grid (row=1, column=0)
        button_forward.grid(row=1, column=2)

        #updates status bar
        status = Label (root, text = "Image " + str(image_index) + " of" + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid (row=2, column=0, columnspan=3, sticky=W+E)


def back (image_index):
    global my_label
    global button_forward
    global button_back

    if (image_index == -1):
        my_label.grid_forget()
        my_label = Label (image=image_list[len(image_list)-1])
        button_forward = Button (root, text=">>", command=lambda: forward(0))
        button_back = Button (root, text="<<", command=lambda: back (3))
        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid (row=1, column=0)
        button_forward.grid(row=1, column=2)

    else:
        my_label.grid_forget()
        my_label = Label (image=image_list[image_index])
        button_forward = Button (root, text=">>", command=lambda: forward(image_index+1))
        button_back = Button (root, text="<<", command=lambda: back(image_index-1))
        my_label.grid (row=0, column=0, columnspan=3)
        button_back.grid (row=1, column=0)
        button_forward.grid(row=1, column=2)
    
    #updates status bar
    status = Label (root, text = "Image " + str(image_index) + " of" + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid (row=2, column=0, columnspan=3, sticky=W+E)

status.grid (row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop ()