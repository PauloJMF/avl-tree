from classes.tree import Tree
import sys

tree = Tree()
tree.visit_preorder()

for i in range(10):
    print(i)
    tree.insert(i)
tree.visit_inorder()
tree
#tree.visit_preorder()
#tree.visit_preorder()
#tree.visit_inorder()
#tree.visit_postorder()
#tree.print_inorder()
#tree.print_postorder()


