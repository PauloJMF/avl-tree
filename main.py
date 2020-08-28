from classes.tree import Tree
import os
import sys
import time
tree = Tree()
# tree.insert(10)
# tree.insert(20)
# tree.insert(30)
# tree.insert(6)
# tree.insert(5)
# tree.insert(7)
# tree.insert(25)
os.system('cls')

while True:
    os.system('cls')
    print("AVL TREE")
    tree.print()
    print("Insert value")
    value = input()
    tree.insert(int(value))
