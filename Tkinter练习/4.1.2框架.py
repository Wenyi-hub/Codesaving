from tkinter import *
root = Tk()
#root.option_readfile('optionDB')  ###optionDB需要额外的配置。
#root.option_add('*background', '#CCC9C1')
#root.option_add('*Entry*background', '#FFFFFF')
root.title('Containers')

for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
    f = Frame(root, borderwidth=2, relief=relief)
    Label(f, text=relief, width=10).pack(side=LEFT)
    f.pack(side=LEFT, padx=5, pady=5)

root.mainloop()