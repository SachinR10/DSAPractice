class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,newdata):
        if newdata==self.data:
            return
        #if value is less,insert at left
        if newdata<self.data:
            if self.left==None:
                self.left = BinarySearchTree(newdata)
            else:
                self.left.add_child(newdata)
        #if value is more,insert at right
        else:
            if self.right == None:
                self.right = BinarySearchTree(newdata)
            else:
                self.right.add_child(newdata)
    def get_min(self):
        if self.left ==None:
            return self.data
        else:
            return self.left.get_min()

    def get_max(self):
        if self.right == None:
            return self.data
        else:
            return self.right.get_max()

    def inorder_traversal(self):
        pass

    def preorder_traversal(self):
        pass
    def postorder_traversal(self):
        pass

    def is_pressent(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left==None:
                return False
            else:
                return self.left.is_pressent(val)
        else:
            if self.right == None:
                return False
            else:
                return self.right.is_pressent(val)



