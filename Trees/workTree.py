class WorkTree:
    def __init__(self,position,name):
        self.position = position
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        temp_parent = self.parent
        lev = 0
        while temp_parent:
            temp_parent = temp_parent.parent
            lev +=1
        return lev
    
    def print_tree(self):
        print("    "*self.get_level(),"|--",self.position,self.name)
        for i in self.children:
            i.print_tree()
    
    def print_tree(self,only_name):
        print("    "*self.get_level(),"|--",self.name)
        for i in self.children:
            i.print_tree(only_name=True)

        

