# python3


import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def __init__(self):
        self.n = 0
        self.parent = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_optimal_height(self):
        max_height = 0
        node_height = [0] * self.n
        for node in range(self.n):
            if node_height[node] != 0:   # Node height already computed so skip this
                continue
            height = 0
            # Go from given node to the root computing tree height from given node
            i = node
            while i != -1:
                if node_height[i] != 0:
                    height += node_height[i]
                    break
                height += 1
                i = self.parent[i]

            max_height = max(max_height, height)

            # Record all the node height from given node to root
            i = node
            while i != -1:
                if node_height[i] != 0:
                    break
                node_height[i] = height
                height -= 1
                i = self.parent[i]
        return max_height

    def compute_height(self):
        # Replace this code with a faster implementation
        max_height = 0
        for node in range(self.n):
                height = 0
                i = node
                while i != -1:
                        height += 1
                        i = self.parent[i]
                max_height = max(max_height, height);
        return max_height;


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_optimal_height())


threading.Thread(target=main).start()
