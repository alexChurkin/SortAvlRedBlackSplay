from structures.AVLTree import AVLTree


def avlSort(inputList: list) -> list:
    tree = AVLTree()

    for item in inputList:
        tree.insert(item)

    return [element for element in tree]


def redBlackSort(inputList: list) -> list:
    a = 2


def splaySort(inputList: list) -> list:
    a = 3
