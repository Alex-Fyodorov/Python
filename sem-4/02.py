class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value        
        self.left = left
        self.right = right

    def __str__(self):        
        res = f'Значение узла: {self.value}'        
        if self.left:
            res +=  f', значение левого: {self.left.value}'
        if self.right:
            res +=  f', значение правого: {self.right.value}'            
        return res

class Tree:
    def __init__(self, root = None):
        self.root = root        

    def search(self, node, data, parent = None):                     
        if node == None or data == node.value:              
            return [node, parent]
        if data > node.value:             
            return self.search(node.right, data, node)
        if data < node.value:            
            return self.search(node.left, data, node)        

    def add_node(self, value):        
        if self.root == None:
            self.root = Node(value)            
        else:
            res = self.search(self.root, value)
            if res[0] == None:
                new_node = Node(value)                
                if value > res[1].value:
                    res[1].right = new_node
                else:
                    res[1].left = new_node
            else:
                print('Ой все, такое значение уже есть')

    def print_tree(self, node):
        if node != None:
            self.print_tree(node.left)
            print(node)
            self.print_tree(node.right)

    def delete_node(self, value):
        node_parent = self.search(self.root, value)
        if node_parent[0] == None:
            print('Такого узла нет')
        else:
            if node_parent[0].left == node_parent[0].right == None:
                self.delete_leaf(node_parent)                                
            elif node_parent[0].left == None or node_parent[0].right == None:
                self.delete_node_with_one_child(node_parent)
            else:
                self.delete_node_with_two_child(node_parent)
            node_parent[0].left = node_parent[0].right = None

    def find_successor(self, node):
        parent = node
        current = node.right
        while current.left != None:
            parent = current
            current = current.left
        return current, parent
    
    def delete_leaf(self, node_and_parent):
        if node_and_parent[0] == self.root:
            self.root = None
        elif node_and_parent[1].right == node_and_parent[0]:
            node_and_parent[1].right = None
        else:
            node_and_parent[1].left = None

    def delete_node_with_one_child(self, node_parent):
        if node_parent[0].left == None:
            node = node_parent[0].right
        else: node = node_parent[0].left
        if node_parent[0] == self.root:
            self.root = node
        elif node_parent[1].right == node_parent[0]:
            node_parent[1].right = node
        else: node_parent[1].left = node
    
    def delete_node_with_two_child(self, node_parent):
        successor = self.find_successor(node_parent[0])
        if node_parent[0] == successor[1]:
            successor[0].left = node_parent[0].left
        else:
            successor[1].left = successor[0].right
            successor[0].right = node_parent[0].right
            successor[0].left = node_parent[0].left
        if node_parent[0] == self.root:
            self.root = successor[0]
        elif node_parent[0] == node_parent[1].right:
            node_parent[1].right = successor[0]
        else:
            node_parent[1].left = successor[0]
