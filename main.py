from classes.tree import Tree
import sys

tree = Tree()
tree.insert(40)
tree.insert(30)
tree.insert(20)
tree.insert(10)
tree.insert(0)
tree.insert(-10)
print(tree.get_height())
tree.preorder()
tree
#tree.visit_preorder()
#tree.visit_inorder()
#tree.visit_postorder()
#tree.print_inorder()
#tree.print_postorder()


