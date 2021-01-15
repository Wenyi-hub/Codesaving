from tkinter import *

window = Tk()
window.title('ch9_1')
window.iconbitmap('favicon (4).ico')

slider1 = Scale(window,from_=0,to=10).pack()
slider2 = Scale(window,from_=0,to=10,length=300,orient=HORIZONTAL).pack()

window.mainloop()