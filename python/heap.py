class MinHeap:
    def __init__(self):
        self.heap = [float("-inf")]

    def isEmpty(self) -> bool:
        return len(self.heap) <= 2

    def isLeaf(self, index: int) -> bool:
        return index >= len(self.heap) // 2 and index < len(self.heap)

    def getLeftIndex(self, index: int) -> int:
        return index << 1

    def getRightIndex(self, index: int) -> int:
        return (index << 1) + 1

    def getParentIndex(self, index: int) -> int:
        return index >> 1

    def swapValue(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify(self, index: int) -> None:
        if not self.isLeaf(index):
            if self.heap[index] > self.heap[self.getLeftIndex(index)] or \
                    self.heap[index] > self.heap[self.getRightIndex(index)]:

                left = self.getLeftIndex(index)
                right = self.getRightIndex(index)

                if self.heap[left] < self.heap[right]:
                    self.swapValue(index, left)
                    self.heapify(left)
                else:
                    self.swapValue(index, right)
                    self.heapify(right)

    def push(self, item: object) -> None:
        self.heap.append(item)
        index = len(self.heap) - 1

        while self.heap[index] < self.heap[self.getParentIndex(index)]:
            parent = self.getParentIndex(index)
            self.swapValue(index, parent)
            index = parent

    def pop(self) -> object:
        if self.isEmpty():
            raise Exception("Heap is empty!")

        pop = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.heapify(1)
        return pop

    def showAll(self) -> None:
        print(self.heap[1:])
