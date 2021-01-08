#Python 与 Tkinter编程

[TOC]

## 第一部分 基本概念

### 第二章 Tkinter

#### 2.1 Tkinter模块

##### 2.1.1 Tkinter是什么

Tkinter是给Python的应用提供了一个易编程的用户界面。\
Tkinter是Python与Tk的接口，Tcl/Tk的GUI工具箱。

> **GUI**（Graphical User Interface）：图形用户界面是指采用图形方式显示的计算机操作用户界面。\
**Tcl**是一种脚本语言，用于快速原型开发RAD、脚本编程、GUI编程和测试等方面。\
**Tk**是一种开放源代码的图形用户界面开发工具。

Tkinter的接口是作为一个Python组件Tkinter.py来实现的。在许多情况下，Tkinter程序不需要关注Tcl/Tk的实现，，因为Tkinter可作为独立的Python的扩展来看待。

[计算器示例1](https://github.com/Wenyi-hub/Codesaving/blob/master/Tkinter%E7%BB%83%E4%B9%A0/3.0%E8%AE%A1%E7%AE%97%E5%99%A81.py)

[计算器示例2](https://github.com/Wenyi-hub/Codesaving/blob/52505e2e4c24262d00d26ca003114a59aad6ec24/Tkinter%E7%BB%83%E4%B9%A0/3.1%E8%AE%A1%E7%AE%97%E5%99%A82.py)

<!-- pagebreak -->

### 第三章 建立一个应用

#### 3.3 检查应用结构

Tkinter 为应用提供了大量的结构，输入 Tkinter 建立了系统的基础对象，并且只需增加一点代码即可演示图形用户界面。

[实际上可以写成的最少的Tkinter码](https://github.com/Wenyi-hub/Codesaving/blob/master/Tkinter%E7%BB%83%E4%B9%A0/3.3%E5%AE%9E%E9%99%85%E4%B8%8A%E5%8F%AF%E4%BB%A5%E5%86%99%E6%88%90%E7%9A%84%E6%9C%80%E5%B0%91%E7%9A%84Tkinter%E7%A0%81.py)

> 标签控件被用pack方法实现\
> 启动Tkinter时间的循环则需要靠mainloop来实现

![ ](D:\Onedrive\OneDrive\文档\代码\Tkinter练习\应用结构.png)

按照[应用结构](D:\Onedrive\OneDrive\文档\代码\Tkinter练习\应用结构.png)填写分块，基本上就行了。\
应用结构中最重要的是最后一块: "Test code"。

---

## 第二部分 显示

### 第四章 Tkinter 控件

#### 4.1 Tkinter 控件漫游

##### 4.1.1 顶层
