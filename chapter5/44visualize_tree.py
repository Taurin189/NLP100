# coding: utf-8
import pydot
import pydotplus
from IPython.display import Image
from chapter5.morph_utils import get_dot_node_from_chunk, get_chunk_list, get_chunk_dict

G = pydot.Dot(graph_type='digraph', rankdir='LR', splines='false', dpi='250', pad='0', margin='0', fontsize='9.5')
G.set_node_defaults(shape='box')
G.set_edge_defaults(arrowsize='0.5', penwidth='0.35')

chunk_list = get_chunk_list("neko.txt.cabocha", 8)
chunk_dict = get_chunk_dict("neko.txt.cabocha", 8)
for chunk in chunk_list:
    G.add_node(get_dot_node_from_chunk(chunk))
    src = chunk.get_num()
    dst = chunk.get_dst()
    if dst in chunk_dict.keys():
        G.add_edge(pydot.Edge(src, dst))

G.write(path='pydot_ann.dot')
graph = pydotplus.graphviz.graph_from_dot_file('pydot_ann.dot')
graph.write_png('pydot_ann.png')
Image(graph.create_png())