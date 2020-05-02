# -*- coding: utf-8 -*-

# @File    : graphviz_demo.py
# @Date    : 2018-07-03
# @Author  : Peng Shiyu

from graphviz import Digraph

dot = Digraph(comment='The Test Table', format="svg")

# 添加圆点A,A的标签是Dot A
dot.node('A', 'Dot A')

# 添加圆点 B, B的标签是Dot B
dot.node('B', 'Dot B')
# dot.view()

# 添加圆点 C, C的标签是Dot C
dot.node('C', 'Dot C')
# dot.view()

# 创建一堆边，即连接AB的两条边，连接AC的一条边。
dot.edges(['AB', 'AC', 'AB'])
# dot.view()

# 在创建两圆点之间创建一条边
dot.edge('B', 'C', 'test')
# dot.view()


# 获取DOT source源码的字符串形式
# print(dot.source)
# // The Test Table
# digraph {
#   A [label="Dot A"]
#   B [label="Dot B"]
#   C [label="Dot C"]
#   A -> B
#   A -> C
#   A -> B
#   B -> C [label=test]
# }


# 保存source到文件，并提供Graphviz引擎
dot.save('test-table.gv')  # 保存
dot.render('test-table.gv')
# dot.view()  # 显示



# 从保存的文件读取并显示

from graphviz import Source

s = Source.from_file('test-table.gv')
print(s.source)  # 打印代码
# s.view()  # 显示