from python.heap import *
import random

heap = MinHeap()

for _ in range(10):
    heap.push(random.randrange(-100,100))

while not heap.isEmpty():
    print(heap.pop())