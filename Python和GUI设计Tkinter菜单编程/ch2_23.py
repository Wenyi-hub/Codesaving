from  tkinter import *

counter = 0
def run_counter(digit):
    def counting():
        global counter
        counter +=1
        digit.config(text=str(counter))
        digit.after(1000,counting)
    counting()

root = Tk()
root.title("ch2_23")
root.iconbitmap(r"C:\Users\wywu\Downloads\favicon (4).ico")     #改变图标

digit = Label(root, bg ="yellow", fg = "blue",
            height=3,width=10,
            font="Fangsong 20 bold")
digit.pack()
run_counter(digit)

root.mainloop()