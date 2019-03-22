# -*- coding: utf-8 -*-
from graphviz import Digraph
from graphviz import Source

dot = Digraph(comment = 'Automotive software', format = 'pdf')
dot.node('A','Automotive software')
dot.node('B','Communication')
dot.node('C','Digital control')
dot.node('D','Sensing')
dot.node('E','Gate Driver')
dot.node('F','Interface')
dot.node('1','CAN')
dot.node('3','EVSE')
dot.node('4','OBC|DCDC')
dot.node('5','Vehicle')
dot.node('2','PLC|Qualcomm')
dot.node('G','Standard')
dot.node('H','AutoSAR')
dot.node('I','OSEK')
dot.node('J','volt',shape = 'none')
dot.node('K','current',shape = 'none')
dot.node('L','temp',shape = 'none')

dot.edges(['AB','AC','BF','AG','F1','F2','13','14','15','GH','GI','CD','CE','DJ','DK','DL'])
dot.edge('D','E','CTRL LOOP',color = "red",style='dashed')

dot.save('test-table.gv')
dot.render('test-table.gv')

dot.view()
s = Source.from_file('test-table.gv')
print(s.source)