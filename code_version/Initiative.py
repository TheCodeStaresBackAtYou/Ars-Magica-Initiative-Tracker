#This is an initive tracker for Ars Magica 5th Edition
#Future features: GitHub, Network functionality, Integration with an upcoming helper suite
#Made by TheCodeStaresBackAtYou with love <3


#uses tkinter for gui elements
import tkinter
from tkinter import *
import Creature as CR

import cx_Freeze
from cx_Freeze import setup, Executable


creature_list = []
main = Tk()
main.title("Ars Initiative")


#Functions
def generateCreature():
   CR.new_creature(main, nameEntry.get(), int(sizeEntry.get()), int(soakEntry.get()), int(initEntry.get()) ) 


#single window instances


#add widgets
sizeVar = StringVar()
sizeLabel = Label (main, textvariable=sizeVar ).grid(row=0)
sizeVar.set("Size: ")


sizeEntry = Entry (main)
sizeEntry.grid(row=0, column=1)

nameVar = StringVar()
nameLabel = Label (main, textvariable=nameVar ).grid(row=1)
nameVar.set("Name: ")


nameEntry = Entry (main)
nameEntry.grid(row=1, column=1)

soakVar = StringVar()
soakLabel = Label (main, textvariable=soakVar ).grid(row=2)
soakVar.set("Soak: ")


soakEntry = Entry (main)
soakEntry.grid(row=2, column=1)

initVar = StringVar()
initLabel = Label (main, textvariable=initVar ).grid(row=3)
initVar.set("Initiative: ")


initEntry = Entry (main)
initEntry.grid(row=3, column=1)



generateButton = tkinter.Button(main, text = "Create Creature.", command = generateCreature)
generateButton.grid(row = 4,column=0, columnspan=1)



#run this shit
main.mainloop()
