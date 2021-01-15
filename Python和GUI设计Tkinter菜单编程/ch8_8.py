from tkinter import *
import random

root = Tk()
root.title("ch8_8")
root.iconbitmap("favicon (4).ico")

msgYes, msgNo, msgExit = 1,2,3
def MessageBox():
    msgType = random.randint(1,3)
    if msgType ==msgYes:
        labTxt = 'Yes'
    elif msgType == msgNo:
        labTxt = 'No'
    elif msgType == msgExit:
        labTxt = 'Exit'
    tl = Toplevel()
    tl.title('Message Box')
    tl.iconbitmap('favicon (4).ico')
    tl.geometry('300x180')
    Label(tl,text=labTxt).pack(fill=BOTH,expand=True)

btn = Button(root,text='Click Me', command=MessageBox)
btn.pack()

root.mainloop()
