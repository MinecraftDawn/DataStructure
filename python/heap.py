class MaxHeap:
    def __init__(self):
        self.heap = []

    def isEmpty(self):
        return not bool(self.heap)

    def getLeftIndex(self, index: int) -> int:
        return index * 2 + 1

    def getRightIndex(self, index: int) -> int:
        return index * 2 + 2

    def getParentIndex(self, index: int) -> int:
        return (index - 1) // 2

    def swapValue(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def isLeaf(self, index: int) -> bool:
        return self.getLeftIndex(index) >= len(self.heap) > index >= 0

    def hasRight(self, index: int) -> bool:
        return 0 < self.getRightIndex(index) < len(self.heap)

    def heapify(self, index: int) -> None:
        if not self.isLeaf(index):
            if self.hasRight(index):
                if self.heap[index] < self.heap[self.getLeftIndex(index)] or self.heap[index] < self.heap[
                    self.getRightIndex(index)]:
                    left = self.getLeftIndex(index)
                    right = self.getRightIndex(index)

                    if self.heap[left] > self.heap[right]:
                        self.swapValue(index, left)
                        self.heapify(left)
                    else:
                        self.swapValue(index, right)
                        self.heapify(right)
            else:
                if self.heap[index] < self.heap[self.getLeftIndex(index)]:
                    left = self.getLeftIndex(index)
                    self.swapValue(index, left)
                    self.heapify(left)

    def push(self, value: int) -> None:
        self.heap.append(value)
        index = len(self.heap) - 1

        while self.getParentIndex(index) >= 0 and self.heap[index] > self.heap[self.getParentIndex(index)]:
            self.swapValue(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        pop = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return pop
