from tkinter import *

def btn_hit():
    if x.get() == "":
        x.set("I like tkinter")
    else:
        x.set("")

root = Tk()
root.title("ch6_2")
root.iconbitmap("favicon (4).ico")

x = StringVar()

label = Label(root,textvariable=x,
                fg="blue",
                font="Fangsong 12 bold",
                width=25,height=2)
label.pack()
btn = Button(root,text="Click me",command=btn_hit)
btn.pack()

root.mainloop()