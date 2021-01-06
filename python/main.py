from python.Deque import Deque

deque = Deque()

for i in range(5):
    deque.push(i)

for i in range(5):
    print(deque.pophead())