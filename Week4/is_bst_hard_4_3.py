#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size
result = []

INT_MIN = float('-inf')
INT_MAX = float('inf')


def is_bst(tree, idx, mini, maxi):
    # Algorithm to verify if the given tree is a bst, returns True if BST
    # tree[idx] is a node represented by a list with following indices
    # 0 = key of the node (tree[idx][0])
    # 1 = Left child of the node (tree[idx][1])
    # 2 = right child of the node (tree[idx][2])
    # value of -1 in either of left / right indicates absence of corresponding sub tree

    # An empty tree is a BST
    if not tree:
        return True

    # False if the node violate min or max condition
    if tree[idx][0] < mini or tree[idx][0] > maxi:
        return False

    # Otherwise check the subtrees recursively tightening the min or max constraint
    # Left subtree cannot hve a node with value greater than current root value, hence assign this as max to left tree
    # Right subtree cannot have a node with value lesser than current root value, hence assign this as min to right tree
    # Note that right subtree can have a value equal to the root as its immediate child
    if (tree[idx][1] != -1 and not is_bst(tree, tree[idx][1], mini, tree[idx][0]-1)) or \
            (tree[idx][2] != -1 and not is_bst(tree, tree[idx][2], tree[idx][0], maxi)):
        return False

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    # first element it the list is the root of the tree
    if is_bst(tree, 0, INT_MIN, INT_MAX):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

# i/p
#
# 4
# 4 1 -1
# 2 2 3
# 1 -1 -1
# 5 -1 -1
#
# o/p
# INCORRECT