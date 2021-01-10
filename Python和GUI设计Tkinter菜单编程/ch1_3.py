from tkinter import *

root = Tk()
#root.configure(bg='#00ff00')    # 窗口背景颜色
root.iconbitmap(r"C:\Users\wywu\Downloads\favicon (4).ico")     #改变图标

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 600
h = 400
x = (screenWidth-w)/2
y = (screenHeight-h)/3
root.geometry("%dx%d+%d+%d"% (w, h, x, y))

root.mainloop()