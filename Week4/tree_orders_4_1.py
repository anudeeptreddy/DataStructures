# python2

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order_traversal(self, idx):
        if self.left[idx] != -1:
            self.in_order_traversal(self.left[idx])
        self.result.append(self.key[idx])
        if self.right[idx] != -1:
            self.in_order_traversal(self.right[idx])

    def inOrder(self):
        self.result = []
        self.in_order_traversal(0)
        return self.result

    def pre_order_traversal(self, idx):
        self.result.append(self.key[idx])
        if self.left[idx] != -1:
            self.pre_order_traversal(self.left[idx])
        if self.right[idx] != -1:
            self.pre_order_traversal(self.right[idx])

    def preOrder(self):
        self.result = []
        self.pre_order_traversal(0)
        return self.result

    def post_order_traversal(self, idx):
        if self.left[idx] != -1:
            self.post_order_traversal(self.left[idx])
        if self.right[idx] != -1:
            self.post_order_traversal(self.right[idx])
        self.result.append(self.key[idx])

    def postOrder(self):
        self.result = []
        self.post_order_traversal(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print " ".join(str(x) for x in tree.inOrder())
    print " ".join(str(x) for x in tree.preOrder())
    print " ".join(str(x) for x in tree.postOrder())


threading.Thread(target=main).start()
