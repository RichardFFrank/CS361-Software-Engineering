from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os
from time import sleep

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# click event for UI button
def generate_pokemon(label):
    # run the number generator and the image service to genrate a random number and populate a path for a pokemon.
    os.system('python3 PRNG.py')
    os.system('python3 image_service.py')
    # read the img_handler file to determine the path of the pokemon photo for use by the UI.
    with open('image-service.txt', 'r') as pipe:
        command =  pipe.readline()
        if command == "RUN\n":
            image_file = pipe.readline()
        else:
            return -1
    pipe.close()
    # build the path based on the current working directory.
    path = os.getcwd()
    path = path+image_file
    # generate the new image and update the label.
    new_img = ImageTk.PhotoImage(Image.open(path))
    label.configure(image=new_img)
    label.image = new_img



# ~~~~~~~~~~~~~~~~~~~~~~~~ UI ELEMENTS ~~~~~~~~~~~~~~~~~~~~~~~~~~

window = Tk()

window.title("Assignment 1 UI")
title = Label(window, text="Click on the button to generate a random Pokemon.")
title.pack()

label1 = Label(window)
img = ImageTk.PhotoImage(Image.open("question_mark.png"))
label1.configure(image=img)
label1.pack()

button = Button(window, text="Random Pokemon", command=lambda:generate_pokemon(label1))
button.pack()

window.mainloop()