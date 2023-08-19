class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data=} {self.next=}'


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def add_node(self, data):
        self.head = Node(data, self.head)
        # self.head = node

    def print_lst(self):
        current = self.head
        while current:
            print(current)
            current = current.next


lst = LinkedList()

lst.add_node('1')
lst.add_node('2')
lst.add_node('3')
lst.add_node('4')

lst.print_lst()
