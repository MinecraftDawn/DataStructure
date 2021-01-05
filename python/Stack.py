class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = Node(None)
        self.top:Node
        self.__size = 0

    def __len__(self):
        return self.__size

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
        self.__size += 1

    def peek(self):
        return self.top.val

    def pop(self):
        val = self.top.val
        self.top = self.top.next
        self.__size -= 1
        return val
