from tkinter import *

def printSelection():
    print(cities[var.get()])

root = Tk()
root.title("ch7_2")
root.iconbitmap("favicon (4).ico")
cities = {0:"东京",1:"纽约",2:"巴黎",3:"伦敦",4:"香港"}

var = IntVar()
var.set(0)
label = Label(root,text="选择喜欢的城市",
                fg="blue",bg="lightyellow",width=30,font="Fongsong 20 bold").pack()

for val, city in cities.items():
    Radiobutton(root,
                text=city,
                indicatoron = 0,
                width=20,
                variable=var,value=val,
                command=printSelection).pack()

root.mainloop()