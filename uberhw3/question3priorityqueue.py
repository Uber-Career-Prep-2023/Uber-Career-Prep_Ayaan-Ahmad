class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        if not self.arr:
            raise IndexError("PriorityQueue is empty")
        return self.arr[0]

    def insert(self, x, weight):
        self.arr.append((x, weight))
        self._heapify_up(len(self.arr) - 1)

    def remove(self):
        if not self.arr:
            raise IndexError("PriorityQueue is empty")

        self._swap(0, len(self.arr) - 1)
        self.arr.pop()
        self._heapify_down(0)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.arr[parent][1] < self.arr[index][1]:
                self._swap(parent, index)
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.arr)
        while index < size:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            highest_priority = index

            if left_child < size and self.arr[left_child][1] > self.arr[highest_priority][1]:
                highest_priority = left_child

            if right_child < size and self.arr[right_child][1] > self.arr[highest_priority][1]:
                highest_priority = right_child

            if highest_priority != index:
                self._swap(index, highest_priority)
                index = highest_priority
            else:
                break

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
