from tkinter import *

root = Tk()
root.title("ch2_1")
root.iconbitmap(r"C:\Users\wywu\Downloads\favicon (4).ico")     #改变图标

label=Label(root, text="I like tkinter")
label.pack()
print(type(label))

root.mainloop()