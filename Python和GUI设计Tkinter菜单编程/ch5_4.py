from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch5_4")
root.iconbitmap("favicon (4).ico")

msg = "欢迎进入Silicon Stone Education系统"

image = Image.open("unnamed.jpg")
sse_jpg = ImageTk.PhotoImage(image)

logo = Label(root,
            image=sse_jpg,
            text=msg,
            font="Fangsong",
            compound=BOTTOM)
logo.grid(row=0,column=0,columnspan=2,padx=0,pady=10)

accountL = Label(root,text="Account:")
accountL.grid(row=1)
pwdL = Label(root,text="Password:")
pwdL.grid(row=2)
accountE = Entry(root)
accountE.grid(row=1,column=1)
pwdE = Entry(root,show="*")
pwdE.grid(row=2,column=1)

def printInfo():
    print("Account: %s\nPassword: %s"% (accountE.get(),pwdE.get()))

loginbtn = Button(root,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0,pady=10)
quitbtn = Button(root,text="Quit",command=root.quit)
quitbtn.grid(row=3,column=1,pady=10)

root.mainloop()
