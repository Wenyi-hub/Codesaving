import graphviz
from graphviz import Digraph

gz=Digraph("test",'comment',None,None,'png',None,"UTF-8",
           {'rankdir':'TB'},
           {'color':'black','fontcolor':'black','fontname':'FangSong','fontsize':'12','style':'rounded','shape':'box'},
           {'color':'#999999','fontcolor':'#888888','fontsize':'10','fontname':'SIMFANG'},None,False)

gz.node('0','0')
gz.node('1','1')
gz.node('2','2')
gz.node('a','a')
gz.node('b','b')
gz.node('i','i')
gz.node('c','c')
gz.node('d','d')
gz.node('j','f')
gz.node('e','e',{'color':'red','fontcolor':'red'})
gz.node('f','f')
gz.node('g','g',{'color':'red','fontcolor':'red'})

t=set(['01','0a','12'])
a=set(['ab','bd','de'])
b=set(['ab','be'])
c=set(['ac','ci','ij','jf','fg'])
d=set(['ac','ci','if','fg'])
gz.edges(a|b|c|d|t)
gz.edge('c','f','finished')
print(gz.source)
gz.view()
