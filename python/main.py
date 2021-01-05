from python.Stack import Stack
s = Stack()
for i in range(5):
    s.push(i)
while len(s):
    print(s.pop())