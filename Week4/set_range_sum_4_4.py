# python3

from sys import stdin


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left:
        v.left.parent = v
    if v.right:
        v.right.parent = v


def small_rotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    else:
        # Zig-zag
        small_rotation(v)
        small_rotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v is None:
        return None
    while v.parent:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return next, root


def split(root, key):
    (result, root) = find(root, key)
    if result is None:
        return root, None
    right = splay(result)
    left = right.left
    right.left = None
    if left:
        left.parent = None
    update(left)
    update(right)
    return left, right


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def left_descendant(n):
    if n.left is null:
        return n
    else:
        return left_descendant(n.left)


def right_ancestor(n):
    if n.key < n.parent.key:
        return n.parent
    else:
        return right_ancestor(n.parent)


def next_node(n):
    if n.right:
        return left_descendant(n.right)
    else:
        return right_ancestor(n)


def delete_node(n):
    global root
    if n.right is None:
        root = n.left
    else:
        x = next_node(n)
        n = x
        root = n.right
        root.left = n.left
    if root:
        root.parent = None
    update(root)


def erase(x):
    global root
    vp = find(root, x + 1)
    next = vp[0]
    if next:
        splay(next)
    n = vp[1]
    if n:
        if n.key == x:
            delete_node(n)


def search(x):
    global root
    if root is None:
        return False
    if root.key == x:
        return True
    elif root.key > x:
        if root.left is None:
            return False
        else:
            root = root.left
            return search(x)
    elif root.key < x:
        if root.right is None:
            return False
        else:
            root = root.right
            return search(x)
    return False


def range_sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    if left and fr <= left.key <= to:
        ans += left.sum
    if middle and fr <= middle.key <= to:
        ans += middle.sum
    if right and fr <= right.key <= to:
        ans += right.sum
    root = merge(merge(left, middle), right)
    return ans


MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = range_sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO


# i/p
#
# 15
# ? 1
# + 1
# ? 1
# + 2
# s 1 2
# + 1000000000
# ? 1000000000
# - 1000000000
# ? 1000000000
# s 999999999 1000000000
# - 2
# ? 2
# - 0
# + 9
# s 0 9
#
# o/p
#
# Not found
# Found
# 3
# Found
# Not found
# 1
# Not found
# 10
