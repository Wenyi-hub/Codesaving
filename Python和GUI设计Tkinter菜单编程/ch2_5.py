from tkinter import *

root = Tk()
root.title("ch2_5")

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 600
h = 400
x = (screenWidth-w)/2
y = (screenHeight-h)/3
root.geometry("%dx%d+%d+%d"% (w, h, x, y))

label=Label(root,text="I like thinter", fg="green", bg="#f0f0f0", height=400, width=15, anchor="center")
label.pack()

root.mainloop()