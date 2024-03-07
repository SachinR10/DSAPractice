from TreesDS import Tree

root = Tree("CEO")
cto = Tree("CTO")
cfo = Tree("CFO")
cho = Tree("CHO")

#root.print_tree()

root.add_child(cto)
root.add_child(cfo)
root.add_child(cho)

cto.add_child(Tree("t1"))
cto.add_child(Tree("t2"))
cto.add_child(Tree("t3"))

cfo.add_child(Tree("f1"))
cfo.add_child(Tree("f2"))
cfo.add_child(Tree("f3"))

root.print_tree()

