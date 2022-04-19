#! /usr/bin/env python


from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from PIL import Image
import os
import shutil

def startfile():
    filepath = filedialog.askopenfilename()
    target = 'Start.jpeg'
    shutil.copyfile(filepath, target)
    ButtonFive['state'] = NORMAL
    ButtonFour['state'] = NORMAL
    return None
def display_width():
   global entryOne
   string= entryOne.get()
   floatwidth = float(string)
   convertwidth = floatwidth * 96
   global finalwidth
   finalwidth = round(int(convertwidth))
def display_height():
   global entryTwo
   stringtwo= entryTwo.get()
   floatheight = float(stringtwo)
   convertheight = floatheight * 96
   global finalheight
   finalheight = round(int(convertheight))
   ButtonThree['state'] = NORMAL
   ButtonTwo['state'] = NORMAL
def thumbnail():
    pictureone = Image.open('Start.jpeg')
    pictureone.thumbnail((finalwidth, finalheight))
    pictureone.save('thumbnail.jpeg')
    pictureone.close()
    os.remove('Start.jpeg')
def resize():
    pictureone = Image.open('Start.jpeg')
    new_image = pictureone.resize((finalwidth, finalheight))
    new_image.save('resized.jpeg')
    pictureone.close()
    new_image.close()
    os.remove('Start.jpeg')
root = Tk()



labelone = Label(root, text = "Welcome to your PEC maker version 1.0").grid(row = 1, column = 5)



entryOne = Entry(root)
entryOne.grid(row = 10, column = 3)
entryOne.insert(0, 'choose width in inches ie: 2.25')
labelfour = Label(root, text = "choose between manual resizing and preserving aspect ratio").grid(row = 15, column = 5)
entryTwo = Entry(root)
entryTwo.grid(row = 10, column = 8)
entryTwo.insert(0, "choose height in inches ie: 2.25")

buttonOne = Button(root, text = 'choose your file', command = startfile, padx = 8, pady=3)
buttonOne.grid(row= 5, column = 5)
ButtonTwo = Button(root, text = "click me for manual resize", padx = 8, pady = 5, command = resize, state = DISABLED)
ButtonTwo.grid(row = 21, column = 2)
ButtonThree = Button(root, text = "click me to preserve aspect ratio", padx = 8, pady = 5, command = thumbnail, state = DISABLED)
ButtonThree.grid(row = 21, column = 8)
ButtonFour = Button(root, text = 'confirm width', padx = 6, pady = 5, command = display_width, state = DISABLED)
ButtonFour.grid(row = 12, column = 3)
ButtonFive = Button(root, text = 'confirm height', padx = 6, pady = 5, command = display_height, state = DISABLED)
ButtonFive.grid(row = 12, column = 8)





root.mainloop()