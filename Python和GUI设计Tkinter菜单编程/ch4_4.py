from tkinter import *

counter = 0
def run_counter(digit):
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000,counting)
    counting()

root = Tk()
root.title("ch4_4")
root.iconbitmap(r"favicon (4).ico")
digit=Label(root,#bg="yellow",
            fg="blue",
            height=3,width=10,
            font="Times 20 bold")
digit.pack()
run_counter(digit)
Button(root,text="结束",width=15,command=root.destroy).pack(pady=10)

root.mainloop()