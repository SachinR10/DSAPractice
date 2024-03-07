class Tree:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        parent = self.parent
        lev = 0
        while parent:
            parent = parent.parent
            lev +=1
        return lev
    
    def print_tree(self):

        print("  "*self.get_level()+self.data)
        for i in self.children:
            i.print_tree()
        