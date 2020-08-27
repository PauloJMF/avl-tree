from classes.tree import Tree
import sys

tree = Tree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(6)
tree.insert(5)
tree.insert(7)
tree.insert(25)
# print(tree.get_height())
# tree.preorder()
tree.print()
#tree.visit_preorder()
#tree.visit_inorder()
#tree.visit_postorder()
#tree.print_inorder()
#tree.print_postorder()
tree.tree_preorder()


