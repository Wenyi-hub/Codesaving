---
marp: false
theme: giga
class: invert
paginate: true
---

<!--paginate: true-->

# 如何使用 Markdown Mermaid 功能

---

## Markdown

**Markdown** 是如今十分流行的一种轻量级标记语言，它允许人们使用易读易写的纯文本格式编写文档。

在 **Markdown** 的使用过程中，可以使用 **Mermaid** 命令语句，通过一些[简单的文本](https://www.jianshu.com/p/e3901c57b596)输入，实现类似于 Visio 的图表功能。

---

### 流程图

```mermaid
graph LR
A{Start}-->B["这是个什么东西？"]
A-->|操作方法|C(Round)
B-->D(("这里是可以添加内容的呗"))
C-->D
```
