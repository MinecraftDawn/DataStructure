class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None
        self.pre: Node
        self.next: Node


class Deque:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, val):
        node = Node(val)
        node.pre = self.tail.pre
        node.next = self.tail
        node.pre.next = node
        self.tail.pre = node
        self.size += 1

    def pop(self):
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        self.size -= 1
        return node.val

    def pushhead(self, val):
        node = Node(val)
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.pre = node
        self.size += 1

    def pophead(self):
        node = self.head.next
        node.next.pre = self.head
        self.head.next = node.next
        self.size -= 1
        return node.val
