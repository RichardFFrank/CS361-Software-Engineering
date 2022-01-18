from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os, os.path
from time import sleep

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# click event for UI button
def generate_pokemon(label):
    # add "RUN" to the prng_service file to tell PRNG to return a random number
    with open('prng-service.txt', 'w') as start:
        start.write("RUN\n")
    start.close()
    sleep(5)
    # read the random number from the prng_service file
    with open('prng-service.txt', 'r+') as rand_file:
        rand_num = rand_file.readline()
        sleep(3)
        rand_file.truncate(0)
    rand_file.close()

    # write the random number to the image service file
    with open('image-service.txt', 'w') as image:
            image.truncate(0)
            image.write("RUN\n")
            image.write(str(rand_num))
    image.close()
    sleep(5)

    with open('image-service.txt', 'r+') as ret_image:
        image_file =ret_image.readline()
        ret_image.truncate(0)
    ret_image.close()
    sleep(5)
    # build the path based on the current working directory.
    path = os.getcwd()
    path = path+image_file
        # generate the new image and update the label.
    new_img = ImageTk.PhotoImage(Image.open(path))
    # else:
    #     new_img = ImageTk.PhotoImage(Image.open("question_mark.png"))
    #     print("image not found")
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