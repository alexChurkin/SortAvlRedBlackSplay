from time import time

from structures.AVLTree import AVLTree


def avlSort(inputList: list) -> list:
    tree = AVLTree()

    _t1 = time()

    for item in inputList:
        tree.insert(item)

    _t2 = time()

    print(f"diff = {_t2 - _t1}")

    outputList = list()

    for element in tree:
        outputList.append(element)

    return outputList


def redBlackSort(inputList: list) -> list:
    a = 2


def splaySort(inputList: list) -> list:
    a = 3
