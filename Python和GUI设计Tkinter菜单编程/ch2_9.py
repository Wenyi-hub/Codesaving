from tkinter import *

root = Tk()
root.title("ch2_9")
root.iconbitmap(r"C:\Users\wywu\Downloads\favicon (4).ico")     #改变图标

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 600
h = 400
x = (screenWidth-w)/2
y = (screenHeight-h)/3
root.geometry("%dx%d+%d+%d"% (w, h, x, y))

label=Label(root, bitmap="hourglass")
label.pack()
label1=Label(root, bitmap="error")
label1.pack()
label2=Label(root, bitmap="info")
label2.pack()
label3=Label(root, bitmap="question")
label3.pack()
label4=Label(root, bitmap="questhead")
label4.pack()
label5=Label(root, bitmap="warning")
label5.pack()
label6=Label(root, bitmap="gray50")
label6.pack()

root.mainloop()