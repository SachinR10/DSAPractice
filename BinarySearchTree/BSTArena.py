from binarySearchTreeDS import BinarySearchTree

elements = [100,20,200,10,30,150,300]

BST1 = BinarySearchTree(elements[0])

for i in elements[1:]:
    BST1.add_child(i)


print(BST1.inorder_traversal())
print(BST1.postorder_traversal())
print(BST1.preorder_traversal())

