#!/usr/bin/python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"'Node({self.data})'"

    def __str__(self):
        return f'(id: 0x{id(self):X}, {self.data}, {type(self.data)})'


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            # nodes.append(node.data)
            nodes.append(node)
            node = node.next
        nodes.append('None')
        return '->'.join([repr(i) for i in nodes])

    def append(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        n = 1
        if self.head is None:
            self.head = data
            return n
        node = self.head
        while node.next is not None:
            node = node.next
            n += 1
        node.next = data
        return n

    def extend(self, data):
        for d in data:
            self.append(d)


a = Node(1)
#print(a)
#print(repr(a))
b = LinkedList(a)
print(b)
b.append(Node(3))
print(b)
b.append(Node(5))
print(b)
b.extend('test')
print(b)
