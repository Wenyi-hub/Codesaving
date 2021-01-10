from tkinter import *
root = Tk()
#root.option_readfile('optionDB')  ###optionDB需要额外的配置。
#root.option_add('*background', '#CCC9C1')
#root.option_add('*Entry*background', '#FFFFFF')
root.title('含有不同边界的浮雕式样的框架')

class GUI:
    def __init__(self):
        of = [None]*5
        for bdw in range(5):
            of[bdw] = Frame(self.root, borderwidth=0)
            Label(of[bdw], text='borderwidth = %d'% bdw).pack(side=LEFT)
            ifx = 0
            iff = []
            for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
                iff.append(Frame(of[bdw], borderwidth=bdw, relief=relief))
                Label(iff[ifx], text=relief, width=10).pack(side=LEFT)
                iff[ifx].pack(side=LEFT, padx=7-bdw, pady=5+bdw)
                ifx = ifx+1
            of[bdw].pack()

mainloop()