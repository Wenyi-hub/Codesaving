from tkinter import *

root = Tk()
root.title("ch5_1")
root.iconbitmap("favicon (4).ico")

nameL = Label(root,text="Name")
nameL.grid(row=0)
addressL = Label(root,text="Address")
addressL.grid(row=1)

nameE = Entry(root)
addressE = Entry(root)
nameE.grid(row=0,column=1)
addressE.grid(row=1,column=1)

root.mainloop()