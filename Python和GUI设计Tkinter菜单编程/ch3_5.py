from tkinter import *

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

root = Tk()
root.title("ch3_5")
root.iconbitmap(r"C:\Users\wywu\Downloads\favicon (4).ico")

for Relief in Reliefs:
    Label(root,text=Relief,relief=Relief,
        fg="blue",
        font="Times 20 bold").pack(side=LEFT,padx=5)

root.mainloop()