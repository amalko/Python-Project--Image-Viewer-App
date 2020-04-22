
import tkinter as tk
from PIL import ImageTk, Image                                                                                      # package for image manipulation

inum= 0                                                                                                             # global variable

root= tk.Tk()
root.title("Image Viewer")
root.iconbitmap("G:\Python\Projects\Hopstarter-Sleek-Xp-Software-Windows-Messenger.ico")                            # adding icon to the root

# Images in the folder and setting the path
my_img1= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img1.jpg"))
my_img2= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img2.jpg"))
my_img3= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img3.jpg"))
my_img4= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img4.jpg"))
my_img5= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img5.jpg"))
my_img6= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img6.jpg"))
my_img7= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img7.jpg"))
my_img8= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img8.png"))
my_img9= ImageTk.PhotoImage(Image.open("G:\Python\Projects\Images\img9.jpg"))

# Label
label= tk.Label(image= my_img1)
label.grid(row= 0, column= 0, columnspan= 3)

# Declaring an image list
img_list= [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9 ]

# Functions
def next(num):                                                                                                      # function to jump to the next image
    global inum
    global label
    global button_back
    global button_next

    inum= num
    label.grid_forget()                                                                                             # to remove the current image from the label
    label = tk.Label(image=img_list[inum-1])                                                                          # updating new image to the label

    button_next = tk.Button(root, text=">>", command=lambda: next(inum + 1))                                        # moving to next image on the click
    button_back = tk.Button(root, text="<<", command= back)                                                         # moving to the previous image on the click

    if inum == 9:                                                                                                   # disabling the button when the end of the list is reachec
        button_next = tk.Button(root, text=">>", state= tk.DISABLED)


    label.grid(row=0, column=0, columnspan=3)                                                                       # displaying the new image on the label
    button_back.grid(row=1, column=0)                                                                               # displaying the back button on the screen again
    button_next.grid(row=1, column=2)                                                                               # displaying the next button on the screen again

    status= tk.Label(root, text= "Image " + str(inum) + " of " + str(len(img_list)), bd= 1, relief= tk.SUNKEN, anchor= tk.E)
    status.grid(row= 2, column=0, columnspan= 3, sticky= tk.W + tk.E)
    return

def back():                                                                                                         # function to jump to the previous image
    global inum
    global label
    global button_back
    global button_next

    inum-= 1
    label.grid_forget()
    label = tk.Label(image=img_list[inum-1])

    button_next = tk.Button(root, text=">>", command=lambda: next(inum + 1))
    button_back = tk.Button(root, text="<<", command= back)

    if inum == 1:
        button_back = tk.Button(root, text="<<", state= tk.DISABLED)


    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    status = tk.Label(root, text="Image " + str(inum) + " of " + str(len(img_list)), bd= 1, relief= tk.SUNKEN, anchor= tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)
    return

# Creating Buttons
button_back= tk.Button(root, text= "<<", command= back)
button_next= tk.Button(root, text= ">>", command= lambda: next(2))
button_exit= tk.Button(root, text= "Quit", command= root.quit)

button_back.grid(row= 1, column= 0)
button_next.grid(row= 1, column= 2)
button_exit.grid(row= 1, column= 1, pady=10)

# Status Bar
status= tk.Label(root, text= "Image " + str(inum+1) + " of " + str(len(img_list)), bd= 1, relief= tk.SUNKEN, anchor= tk.E)
status.grid(row= 2, column=0, columnspan= 3, sticky= tk.W + tk.E)

# start the program
root.mainloop()