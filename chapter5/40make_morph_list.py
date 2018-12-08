# coding: utf-8
import CaboCha
# from . import Morph

parser = CaboCha.Parser()
tree = parser.parse("日本語の形態素解析はすごい")
print(tree.toString(CaboCha.FORMAT_LATTICE).split("\n"))
