class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            raise IndexError("Heap is empty")
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        self._heapify_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            raise IndexError("Heap is empty")

        self._swap(0, len(self.arr) - 1)
        self.arr.pop()
        self._heapify_down(0)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.arr[parent] > self.arr[index]:
                self._swap(parent, index)
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.arr)
        while index < size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child < size and self.arr[left_child] < self.arr[smallest]:
                smallest = left_child

            if right_child < size and self.arr[right_child] < self.arr[smallest]:
                smallest = right_child

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

