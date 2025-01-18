#import the required libraries
#tkinter library to create GUI
#random library because we're randomly selecting numbers
from tkinter import *
import random
 
#create tkinter instance
root=Tk()
#define geometry
root.geometry("400x400")
 
#GUI will have two basic components
#1.Button which will trigger the rolling of dice
#2.Dice label
l1=Label(root,font=("Helvetica",260))
 
def roll():
    #create a number variable in which the list of all the ASCII characters of the string will be stored
    #Use backslash because unicode must have a backslash 
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    #configure the label
    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()
     
b1=Button(root,text="Roll the Dice!",foreground='blue',command=roll)
b1.place(x=300,y=0)
b1.pack()
 
root.mainloop()