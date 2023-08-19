class Node:

    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return f'{self.data = } {self.next = } {self.previous = }'
    
class Linked_list:

    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def print_list(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def add_node(self, data):
        node = Node(data, self.head)
        if self.head:
            self.head.previous = node
        self.head = node
        if not self.tail:
            self.tail = node

    def del_first(self):
        node = self.head
        self.head = self.head.next
        self.head.previous = None
        node.next = None

    def del_last(self):
        node = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        node.previous = None

    def add_last(self, data):
        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

    def find_node(self, data):
        current = self.head
        while current:
            if data == current.data:
                print(current)
                return
            current = current.next
        print('not found')

    def list_sort(self):
        max_node = None
        while max_node != self.head:
            current = self.head
            while current.next != max_node:
                node = current.next
                if current.data > node.data:
                    current.next = node.next
                    node.previous = current.previous
                    current.previous = node
                    node.next = current
                    if current.next:
                        current.next.previous = current
                    if node.previous:
                        node.previous.next = node
                    if node == self.tail:
                        self.tail = current
                    if current == self.head:
                        self.head = node
                    current = node
                current = current.next
            max_node = current
    
    def data_sort(self):
        max_node = None
        while max_node != self.head:
            current = self.head
            while current.next != max_node:                
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
            max_node = current


lst = Linked_list()
lst.add_node('1')
lst.add_node('2')
lst.add_node('3')
lst.add_node('4')
lst.add_node('5')

lst.add_last('0')

lst.print_list()
print()
print(lst.head)
print(lst.tail)
print()

lst.data_sort()

lst.print_list()
print()
print(lst.head)
print(lst.tail)
print()





        