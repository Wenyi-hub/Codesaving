from tkinter import *

root = Tk()
root.title('ch9_2')
root.iconbitmap('favicon (4).ico')

slider = Scale(root,
                from_=0,
                to=10,
                troughcolor='lightgrey',
                width='30',
                tickinterval=2,
                label='My Scale',
                length=300,
                orient=HORIZONTAL)
slider.pack()

root.mainloop()