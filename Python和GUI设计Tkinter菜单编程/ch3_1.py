from tkinter import *

window = Tk()
window.title("ch3_1")
window.iconbitmap(r"C:\Users\wywu\Downloads\favicon (4).ico")

lab1 = Label(window,text="明智科技大学",
            bg="lightyellow")
lab2 = Label(window,text="长庚大学",
            bg="lightgreen")
lab3 = Label(window,text="长庚科技大学",
            bg="lightblue")
lab1.pack()
lab2.pack()
lab3.pack()

window.mainloop()