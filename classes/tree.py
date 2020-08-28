from classes.node import Node
from utils.print_tree import printBTree
from utils.print_tree_preorder import get_matrix_tree_preorder, show_tree
import time

class Tree:
    root = None
    final_matrix = None
    current_row = 0
    max_height = 0

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return self.root
        self.root = self.balanced_insert(value, self.root)
        return self.root

    def balanced_insert(self, value, node):
        if node == None:
            return Node(value)
        elif node.value > value: # Node is bigger, left insertion
            node.left = self.balanced_insert(value, node.left)
        else: # Node is smaller, right insertion
            node.right = self.balanced_insert(value, node.right)

        balance_factor = node.update_balance_factor()

        # Left Left 
        if balance_factor > 1 and value < node.left.value: 
            print("Right")
            time.sleep(2)
            return self.right(node) 
        # Right Right 
        if balance_factor < -1 and value > node.right.value:
            print("Left")
            time.sleep(2)
            return self.left(node) 
        # Left Right 
        if balance_factor > 1 and value > node.left.value:
            print("Left Right") 
            node.left = self.left(node.left)
            self.print()
            time.sleep(5)
            return self.right(node) 
        # Right Left 
        if balance_factor < -1 and value < node.right.value: 
            print("Right Left") 
            node.right = self.right(node.right)
            self.print()
            time.sleep(5)
            return self.left(node) 
        
        return node
  
    def left(self, node): 
        new_root = node.right 
        temp = new_root.left 
        new_root.left = node 
        node.right = temp 
        return new_root 
  
    def right(self, node):
        new_root = node.left 
        temp = new_root.right 
        new_root.right = node 
        node.left = temp 
        return new_root 

    def get_height(self):
        if self.root is not None:
            return self.root.get_height()
        return None

    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder()

    def postorder(self):
        self.root.postorder()

    def tree_preorder(self):
        self.max_height = self.get_height()
        matrix_tree = get_matrix_tree_preorder(self)
        show_tree(matrix_tree)
        
    def print(self):
        if self.root is not None:
            return printBTree(self.root,lambda n: (str(n.value), n.left, n.right) )
        return None