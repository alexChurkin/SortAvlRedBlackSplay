from structures.AVLTree import AVLTree


def avlSort(inputList: list) -> list:
    tree = AVLTree()

    for item in inputList:
        tree.insert(item)

    outputList = list()

    for element in tree:
        outputList.append(element)

    return outputList


def redBlackSort(inputList: list) -> list:
    a = 2


def splaySort(inputList: list) -> list:
    a = 3
