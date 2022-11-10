import random


def generateRandomList(size: int, minimum: float, maximum: float):
    return [random.uniform(minimum, maximum) for _ in range(size)]


def generateRandomListAsc(size: int, minimum: float, maximum: float):
    return generateRandomList(size, minimum, maximum).sort()


def generateRandomListDesc(size: int, minimum: float, maximum: float):
    return generateRandomList(size, minimum, maximum).sort(reverse=True)
