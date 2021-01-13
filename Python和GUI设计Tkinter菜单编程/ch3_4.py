from tkinter import *

window = Tk()
window.title("ch3_4")
window.iconbitmap(r"C:\Users\wywu\Downloads\favicon (4).ico")

lab1 = Label(window,text="明智科技大学",
            bg="lightyellow",
            width=30)
lab2 = Label(window,text="长庚大学",
            bg="lightgreen",
            width=15)
lab3 = Label(window,text="长庚科技大学",
            bg="lightblue",
            width=15)
lab1.pack()
lab2.pack(side=LEFT)
lab3.pack(side=RIGHT)

window.mainloop()