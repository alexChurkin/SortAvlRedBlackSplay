from structures.AVLTree import AVLTree
from structures.RedBlackTree import RBTree


def avlSort(inputList: list) -> list:
    tree = AVLTree()

    for item in inputList:
        tree.insert(item)

    return [element for element in tree]


def redBlackSort(inputList: list) -> list:
    tree = RBTree()

    for item in inputList:
        tree.insert(item)

    return [element for element in tree]


def splaySort(inputList: list) -> list:
    a = 3
