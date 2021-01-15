from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch8_7")
root.iconbitmap("favicon (4).ico")

msg = "欢迎进入Silicon Stone Education系统"

image = Image.open("unnamed.jpg")
sse_jpg = ImageTk.PhotoImage(image)

logo = Label(root,image=sse_jpg,text=msg,compound=BOTTOM)
logo.pack()

labFrame = LabelFrame(root,text="数据验证")
accountL = Label(labFrame,text="Account:")
accountL.grid(row=0,column=0)
pwdL = Label(labFrame,text="Password:")
pwdL.grid(row=1,column=0)
accountE = Entry(labFrame)
accountE.grid(row=0,column=1)
pwdE = Entry(labFrame,show="*")
pwdE.grid(row=1,column=1,pady=10)
labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)

def printInfo():
    print("Account: %s\nPassword: %s"% (accountE.get(),pwdE.get()))

loginbtn = Button(labFrame,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0)
quitbtn = Button(labFrame,text="Quit",command=root.quit)
quitbtn.grid(row=3,column=1)

root.mainloop()
