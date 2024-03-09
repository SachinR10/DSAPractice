from binarySearchTreeDS import BinarySearchTree

BST1 = BinarySearchTree(18)

BST1.add_child(17)
BST1.add_child(7)
BST1.add_child(45)
BST1.add_child(64)
BST1.add_child(100)
BST1.add_child(7)

print(BST1.is_pressent(100))
print(BST1.get_max())
print(BST1.get_min())