class Node:
    left = None
    right = None
    value = None
    balance_factor = 0

    def __init__(self, value, balance_factor=0):
        self.value = value
        self.balance_factor = balance_factor

    def visit(self):
        print(self)

    def get_height(self):
        left_height = 0
        right_height = 0

        if self.left is not None:
            left_height = self.left.get_height()+1
        if self.right is not None:
            right_height = self.right.get_height()+1

        return max(left_height, right_height)

    def update_balance_factor(self):
        left_height = right_height = 0
        if self.left is not None:
            left_height = self.left.get_height()+1
        if self.right is not None:
            right_height = self.right.get_height()+1

        self.balance_factor = left_height - right_height
        return self.balance_factor


    def preorder(self):
        self.visit()
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.preorder()
        self.visit()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
        self.visit()

    def __str__(self):
        return str(self.value)