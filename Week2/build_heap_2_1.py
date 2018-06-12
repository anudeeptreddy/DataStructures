# python3


class HeapBuilder:
    def __init__(self):
        self.n = 0
        self._swaps = []
        self._data = []

    def read_data(self):
        self.n = int(input())
        self._data = [int(s) for s in input().split()]
        assert self.n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def generate_swaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # more efficient implementation that takes linear time below - generate_heap
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_down(self, i):
        min_index = i
        size = len(self._data)
        left_child_index = 2*i + 1
        if left_child_index < size and self._data[left_child_index] < self._data[min_index]:  # left child exists?
            min_index = left_child_index
        right_child_index = 2*i + 2
        if right_child_index < size and self._data[right_child_index] < self._data[min_index]:  # right child exists?
            min_index = right_child_index
        if i != min_index:  # a child node with lower value is found, hence sift down
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self._sift_down(min_index)

    def generate_heap(self):
        # Algorithm to heapify an array using heap operations
        for i in range(self.n//2-1, -1, -1):   # 0-based indices
            self._sift_down(i)

    def solve(self):
        self.read_data()
        self.generate_heap()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
