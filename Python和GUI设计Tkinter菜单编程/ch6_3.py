from tkinter import *

def callback(*args):
    print("data change:",xE.get())

root = Tk()
root.title("ch6_3")
root.iconbitmap("favicon (4).ico")

xE = StringVar()
entry = Entry(root,textvariable=xE)
entry.pack(pady=5,padx=10)
xE.trace("w",callback)

root.mainloop()