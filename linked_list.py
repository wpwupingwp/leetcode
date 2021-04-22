#!/usr/bin/python3


class Node:
    def __init__(self, data):
        # !!
        if isinstance(data, Node):
            self.data = data.data
        else:
            self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'

    def __str__(self):
        return f'(id: 0x{id(self):X}, {self.data}, {type(self.data)})'

    @staticmethod
    def is_node(data):
        return isinstance(data, Node)

    def __eq__(a, b):
        if not Node.is_node(b):
            raise TypeError(f'{b} is not a Node')
        return (a.data == b.data)

    def __gt__(a, b):
        if not Node.is_node(b):
            raise TypeError(f'{b} is not a Node')
        return (a.data > b.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        nodes = []
        for node in self:
            # debug
            # print(node, end='->')
            nodes.append(node)
        return '->'.join([repr(i) for i in nodes])

    def __len__(self):
        n = 0
        for node in self:
            n += 1
        return n

    @staticmethod
    def to_node(data):
        if not isinstance(data, Node):
            return Node(data)
        else:
            return data

    def append(self, data):
        data = self.to_node(data)
        if self.head is None:
            self.head = data
            return
        for node in self:
            if node.next is None:
                node.next = data
                break
        return

    def append_left(self, data):
        data = self.to_node(data)
        data.next = self.head
        self.head = data
        return

    def extend(self, data):
        for d in data:
            self.append(d)
        return

    def insert_after(self, old, new):
        old = self.to_node(old)
        new = self.to_node(new)
        if len(self) == 0:
            raise ValueError('Empty linked list.')
        for node in self:
            if node == old:
                new.next = node.next
                node.next = new
                return
        node.next = new

    def insert_before(self, old, new):
        old = self.to_node(old)
        new = self.to_node(new)
        if len(self) == 0:
            raise ValueError('Empty linked list.')
        previous = self.head
        if previous == old:
            self.append_left(new)
            return
        for node in self:
            if node == old:
                previous.next = new
                new.next = node
                return
            previous = node
        raise ValueError(f'{old} not found in linked list.')


a = Node(1)
x = Node(a)
print('x', x, x.data,)
print(a==Node(1), a>Node(3), a<Node(10))
aa = LinkedList()
print(aa, len(aa))
b = LinkedList(a)
print(b)
b.append(Node(3))
print(b)
b.append(Node(5))
print(b)
b.extend('test')
print(b)
print('length', len(b))
b.append_left(999)
print(b)
b.insert_after('e', 'insert')
print(b)
b.insert_after('notfound', 'insert_to_end')
print(b)
b.insert_before(999, 'before')
print(b)
b.insert_before('e', 'e-before')
print(b)
b.insert_before(1000, 'insertbefore')
print(b)
