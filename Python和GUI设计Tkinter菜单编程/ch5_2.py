from tkinter import *

root = Tk()
root.title("ch5_2")
root.iconbitmap("favicon (4).ico")

accountL = Label(root,text="Account")
accountL.grid(row=0)
pwdL = Label(root,text="Password")
pwdL.grid(row=1)

accountE = Entry(root)
accountE.grid(row=0,column=1)
pwdE = Entry(root,show="*")
pwdE.grid(row=1,column=1)

root.mainloop()