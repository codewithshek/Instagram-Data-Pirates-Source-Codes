from tkinter import *
root = Tk()

# the function for user desire shoping list
def user_desire():
    x = int(take_value.get())
    Label(root,text="Make your list", font="comicsansms 10 bold").grid(row=4,column=4)
    for i in range(0,x):
        Entry(root,bg="green").grid(row=i+5,column=4)
        Checkbutton(root,bg="green").grid(row=i+5,column=1)

    


root.geometry("570x400")
Heading = Label(root, text="Wellcome to shoping app", font="comicsansms 33 bold", bg="purple")
Heading.grid(row=0,column=4)
root.configure(bg="orange")

# ask customer how many items they want to purchase
f1 = Frame(root,borderwidth=3, relief=SUNKEN, bg="red")
f1.grid(row=1,column=4)
l1 = Label(f1, text="How many items you want to purchase",bg="yellow")
l1.grid(row=1, column=4)

# take user input for the number of items
take_value = StringVar() #a variable to store the value of the user input
f2 = Frame(root,borderwidth=2, width=5,relief=SUNKEN)
f2.grid(row=2,column=4)
user_input = Entry(f2,bg="red",textvariable=take_value)
user_input.grid()

# the number of box they want for their shoping list
Button(root, text="Submit", command=user_desire).grid(row=3, column=4)

root.mainloop()
