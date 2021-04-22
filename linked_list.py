#!/usr/bin/python3


class Node:
    @staticmethod
    def is_node(data):
        return isinstance(data, Node)

    def __init__(self, data):
        # !!
        if Node.is_node(data):
            self.data = data.data
        else:
            self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'

    def __str__(self):
        return f'(id: 0x{id(self):X}, {self.data}, {type(self.data)})'

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

    def append(self, data):
        data = Node(data)
        if self.head is None:
            self.head = data
            return
        for node in self:
            if node.next is None:
                node.next = data
                break
        return

    def append_left(self, data):
        data = Node(data)
        data.next = self.head
        self.head = data
        return

    def extend(self, data):
        for d in data:
            self.append(d)
        return

    def insert_after(self, old, new):
        old = Node(old)
        new = Node(new)
        if len(self) == 0:
            raise ValueError('Empty linked list.')
        for node in self:
            if node.data == old.data:
                new.next = node.next
                node.next = new
                return
        node.next = new

    def insert_before(self, old, new):
        old = Node(old)
        new = Node(new)
        if len(self) == 0:
            raise ValueError('Empty linked list.')
        previous = self.head
        if previous.data == old.data:
            self.append_left(new)
            return
        for node in self:
            if node.data == old.data:
                previous.next = new
                new.next = node
                return
            previous = node
        raise ValueError(f'{old} not found in linked list.')

    def remove(self, data):
        if len(self) == 0:
            raise ValueError('Empty linked list.')
        if self.head.data == data:
            self.head = self.head.next
            return
        previous = self.head
        for node in self:
            if node.data == data:
                previous.next = node.next
                return
            previous = node
        raise ValueError(f'{data} not found in linked list.')

    def reverse(self):
        stack = []
        new = LinkedList()
        for node in self:
            stack.append(node)
        while stack:
            node = stack.pop()
            new.append(node)
        return new


def test():
    a = Node(1)
    x = Node(a)
    print('a', a, 'x', x)
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
    b.remove(999)
    print(b)
    b.remove('e')
    print(b)
    print(b.reverse())


test()
