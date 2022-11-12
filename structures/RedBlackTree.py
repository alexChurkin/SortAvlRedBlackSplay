import random

from structures.Stack import Stack


class RBNode:
    def __init__(self, key):
        self.red = False
        self.parent = None
        self.key = key
        self.left = None
        self.right = None


class RBIterator:
    def __init__(self, tree):
        self.pos = 0
        self.count = tree.count
        self.stack = Stack()

        self.currNode = tree.root

        while self.currNode.left is not None and self.currNode.key != 0:
            self.stack.push(self.currNode)
            self.currNode = self.currNode.left

        if not self.stack.isEmpty():
            self.currNode = self.stack.peek()

    def __iter__(self):
        return self

    def getNextNode(self):
        node = self.stack.pop()

        if self.currNode.right is not None:
            self.currNode = self.currNode.right
            while self.currNode is not None:
                self.stack.push(self.currNode)
                self.currNode = self.currNode.left
            self.currNode = self.stack.peek()
        else:
            if self.stack.size() == 0:
                self.currNode = node.right
            else:
                self.currNode = self.stack.peek()

        if self.currNode.key == 0:
            return None
        else:
            return self.currNode

    def __next__(self):
        if self.pos == self.count:
            raise StopIteration
        if self.pos == 0:
            self.pos += 1
            return self.currNode.key

        node = None
        while node is None:
            node = self.getNextNode()

        self.currNode = node
        self.pos += 1

        return self.currNode.key


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
        self.count = 0

    def insert(self, key):
        # Ordinary Binary Search Insertion
        new_node = RBNode(key)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.key < current.key:
                current = current.left
            elif new_node.key > current.key:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

        self.count += 1

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def exists(self, key):
        curr = self.root
        while curr != self.nil and key != curr.key:
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __iter__(self):
        return RBIterator(self)

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.key != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.key) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)


def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(1, num - 1))
    return nums


def main():
    tree = RBTree()
    for x in range(1, 51):
        tree.insert(x)
    print(tree)


main()
