import random


def generateRandomList(size: int, q: float, w: float):
    return [random.uniform(q, w) for _ in range(size)]


def generateRandomListAsc(size: int, q: float, w: float):
    return generateRandomList(size, q, w).sort()


def generateRandomListAsc(size: int, q: float, w: float):
    return generateRandomList(size, q, w).sort(reverse=True)
