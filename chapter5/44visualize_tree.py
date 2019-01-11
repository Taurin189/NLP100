# coding: utf-8
import pydot
import pydotplus
from IPython.display import Image

G = pydot.Dot(graph_type='digraph',rankdir='LR',splines='false',dpi='250',pad='0',margin='0',fontsize='9.5')
G.set_node_defaults(label='',shape='circle',penwidth='0.35')
G.set_edge_defaults(arrowsize='0.5',penwidth='0.35')

I = pydot.Subgraph('cluster_i',graph_type='digraph',label='Input',margin='0',fontcolor='red',penwidth='0')
for i in range(1,4):
    I.add_node(pydot.Node("i%d" % i, color='red'))

H = pydot.Subgraph('cluster_h',graph_type='digraph',label='Hidden',margin='0',fontcolor='blue',penwidth='0')
for i in range(1,5):
    H.add_node(pydot.Node("h%d" % i, color='blue'))

O = pydot.Subgraph('cluster_o',graph_type='digraph',label='Output',margin='0',fontcolor='darkgreen',penwidth='0')
for i in range(1,3):
    O.add_node(pydot.Node("o%d" % i, color='darkgreen'))

G.add_subgraph(I)
G.add_subgraph(H)
G.add_subgraph(O)

for i in range(1,4):
    for j in range(1,5):
        G.add_edge(pydot.Edge('i%d' % i, 'h%d' % j))

for i in range(1,5):
    for j in range(1,3):
        G.add_edge(pydot.Edge('h%d' % i, 'o%d' % j))

G.write(path='pydot_ann.dot')
graph = pydotplus.graphviz.graph_from_dot_file('pydot_ann.dot')
graph.write_png('pydot_ann.png')
Image(graph.create_png())