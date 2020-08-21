import json
from classes.node import Node
import config

class Tree:
    root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return
        
        new_node = Node(value)
        grandparent = None
        parent = self.root
        child = None
        unbalanced = None
        parent_unbalanced = None
        balance = 0

        while parent is not None:
            if child.value > value:
                child = parent.left
            else:
                child = parent.right
            if child is not None and child.balance_factor != 0:
                parent_unbalanced = parent
                unbalanced = child
            grandparent = parent
            parent = child

        if value < grandparent.value:
            grandparent.left = new_node
        else:
            grandparent.right = new_node
        
        if value < unbalanced.value:
            node = unbalanced.left
        else:
            node = unbalanced.right
        
        parent = node

        while parent != child:
            if value < parent.value:
                parent.balance = 1
                parent = parent.left
            else:
                parent.balance = -1
                parent = parent.right

        if value < unbalanced.value:
            balance = 1
        else:
            balance = -1

        # is balanced
        if unbalanced.balance_factor == 0:
            unbalanced.balance_factor = balance
            return
        if unbalanced.balance_factor != balance:
            unbalanced.balance_factor = 0
            return

        if node.balance_factor == balance:
            parent = node.left
            if balance == 1:
                self.right(unbalanced)
            else:
                self.left(unbalanced)
            unbalanced.balance_factor = 0
            node.balance_factor = 0
        else:
            if balance == 1:
                parent = node.right
                self.left(node)
                unbalanced.left = parent
                self.right(unbalanced)
            else:
                parent = node.left
                self.right(node)
                unbalanced.right = parent
                self.left(unbalanced)
            if parent.balance_factor == 0:
                unbalanced.balance_factor = 0
                node.balance_factor = 0
            else:
                if parent.balance_factor == balance:
                    unbalanced.balance_factor = balance * -1
                    node.balance_factor = 0
                else:
                    unbalanced.balance_factor = 0
                    node.balance_factor = balance
        parent.balance_factor = 0


    def find(self, value):
        return self.root.find(value)

    def visit_preorder(self):
        self.root.visit('PREORDER')

    def visit_inorder(self):
        self.root.visit('INORDER')

    def visit_postorder(self):
        self.root.visit('POSTORDER')

    def print_preorder(self):
        self.root.visit_save('PREORDER', None)
        matrix, N, M = config.preorder_print_matrix, config.N, config.M

        for i in range(N):
            if matrix[i][0] == None:
                    continue
            matrix[i][0] = matrix[i][0].replace("│      ", "  │    ")

        for j in range(1, M):
            for i in range(N):
                if matrix[i][j] == None:
                    continue
                matrix[i][j] = matrix[i][j].replace("│      ", "  │    ")
                if matrix[i][j][0] == '└':
                    matrix[i][j] = matrix[i][j].replace('└', '—')
                    matrix[i][j-1] = "{:7}".format("  └————")

        for j in range(M):
            for i in range(N-1, j, -1):
                if matrix[i][j] == None:
                    continue
                if matrix[i][j][:3] == '  │':
                    matrix[i][j] = "{:8}".format("")
                else:
                    break

        for j in range(M-4):
            son, dad = [], []
            for i in range(N):
                if matrix[i][j] == None:
                    continue
                if matrix[i][j][2] == '└':
                    son.append(i) 
                if matrix[i][j][2] == '[':
                    dad.append(i)

            for i, val in enumerate(dad):
                if i == 0:
                    continue
                aux = -1
                for val2 in son:
                    if val2 > aux and val2 < val:
                        aux = val2
                for z in range(aux+1, val):
                    matrix[z][j] = "{:8}".format("")

        for i in range(N):
            str_ = ""
            for j in range(M):
                if matrix[i][j] == None:
                    continue
                str_ += str(matrix[i][j])
            print(str_)

    def print_inorder(self):
        self.root.visit_save('INORDER', None)

    def print_postorder(self):
        self.root.visit_save('POSTORDER', None)

    def parse(self, letters):
        pass

    def right(self, node):
        new_root = node.left
        hold = new_root.right

        new_root.right = node
        new_root.left = hold
        
        return new_root

    def left(self, node):
        new_root = node.right
        hold = new_root.left

        new_root.left = node
        new_root.right = hold

        return new_root