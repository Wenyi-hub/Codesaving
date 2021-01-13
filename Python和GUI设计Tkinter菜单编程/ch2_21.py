from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch2_21 ")
root.iconbitmap(r"C:\Users\wywu\Downloads\favicon (4).ico")     #改变图标

sseText = """SSE 全名是Silicon Stone Education，这家公司在美国，
这是国际专业证照公司，产品多元与丰富。"""

image = Image.open(r'unnamed.jpg')
sse_jpg = ImageTk.PhotoImage(image)
label=Label(root,text=sseText, #underline=0,
            image=sse_jpg,
            justify="left",
            compound="right",
            fg="green", bg="#f0f0f0",
            font="Fangsong 14 bold")
label.pack()

root.mainloop()