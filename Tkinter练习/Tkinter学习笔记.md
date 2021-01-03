#

[TOC]

## 第二章 Tkinter

### 2.1 Tkinter模块

#### 2.1.1 Tkinter是什么

Tkinter是给Python的应用提供了一个易编程的用户界面。\
Tkinter是Python与Tk的接口，Tcl/Tk的GUI工具箱。

> **GUI**（Graphical User Interface）：图形用户界面是指采用图形方式显示的计算机操作用户界面。\
**Tcl**是一种脚本语言，用于快速原型开发RAD、脚本编程、GUI编程和测试等方面。\
**Tk**是一种开放源代码的图形用户界面开发工具。

Tkinter的接口是作为一个Python组件Tkinter.py来实现的。在许多情况下，Tkinter程序不需要关注Tcl/Tk的实现，，因为Tkinter可作为独立的Python的扩展来看待。

计算器示例1:

```python
#Calcl.py 
from tkinter import *

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculator')
        self.master.iconname("calcl")

        display = StringVar()
        Entry(self,relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)

        for key in ("123", "456", "789", "0"):
            keyF = frame(self, TOP)
            for char in key:
                button (keyF, LEFT, char, lambda w=display, s='%s'%char: w.set(w.get()+s))


        opsF = frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, LEFT, char, lambda w=display, c=char: w.set(w.get()+''+c+''))

        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))

    def calc(self, display):
        try:
            display.set('eval(display.get())')
        except ValueError:
            display.set("ERROR")

if __name__ == '__main__':
    Calculator().mainloop()
```
