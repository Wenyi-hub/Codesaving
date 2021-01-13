from tkinter import *

def yellow():
    root.config(bg="yellow")
def blue():
    root.config(bg="blue")

root = Tk()
root.title("ch4_5")
root.iconbitmap(r"favicon (4).ico")
root.geometry("300x200")
exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",fg="blue",command=blue)
yellowbtn = Button(root,text="Yellow",fg="yellow",command=yellow)
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()