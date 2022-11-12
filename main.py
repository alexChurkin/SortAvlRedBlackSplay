import math

import algorithms
from assist.advanced_io import readInt, readFloatList, readFloatRange, listToStr
from assist.randint_lists import *
from experiments import *

RANDOM = 1
RANDOM_ASC = 2
RANDOM_DESC = 3
MANUAL_INPUT = 4

RUN_EXPERIMENTS = 5


# Меню
def showMenu() -> int:
    print()
    print("Меню:")
    print("------------------------------------------------------")
    print("1. Автогенерация случайного неотсортированного массива")
    print("2. Автогенерация случайного массива, отсортированного по возрастанию (неубыванию)")
    print("3. Автогенерация случайного массива, отсортированного по убыванию (невозрастанию)")
    print("4. Ручной ввод массива для сортировки в формате x1 x2 x3 ... xn")
    print("------------------------------------------------------")
    print("5. Построить графики")
    print("------------------------------------------------------")
    print()
    mode: int = readInt("Ваш выбор: ", minimum=1, maximum=5)
    return mode


# Запуск одиночного эксперимента
def runSingleExperiment(mode: int):
    # >>> Выбран автоматический способ генерации массива
    if mode in [RANDOM, RANDOM_ASC, RANDOM_DESC]:
        n: int = readInt("Введите размер [2, inf) массива n: ",
                         minimum=2, maximum=math.inf, includeR=False)

        q, w = readFloatRange("Введите нижнюю и верхнюю (q и w) границы для элементов массива: ",
                              minimum=-float('inf'),
                              maximum=float('inf'), includeR=False, includeL=False)

        inputList = None

        if mode == RANDOM:
            inputList = generateRandomList(size=n, minimum=q, maximum=w)
        elif mode == RANDOM_ASC:
            inputList = generateRandomListAsc(size=n, minimum=q, maximum=w)
        else:
            inputList = generateRandomListDesc(size=n, minimum=q, maximum=w)

        if len(inputList) <= 50:
            print(f"\nСгенерирован следующий массив:\n{inputList}\n")

    # >>> Выбран ручной способ задания массива
    else:
        inputList = readFloatList("Введите элементы массива:\n",
                                  minimum=1,
                                  maximum=10, includeR=False)

    t1Start = time()
    avlSortedList = algorithms.avlSort(inputList)
    t1Finish = time()

    t2Start = time()
    redBlackSortedList = algorithms.redBlackSort(inputList)
    t2Finish = time()

    t3Start = time()
    splaySortedList = algorithms.splaySort(inputList)
    t3Finish = time()

    print(f">> Результат сортировки при помощи AVL-дерева:\n   {listToStr(avlSortedList)}\n")
    print(f">> Результат сортировки при помощи Красно-чёрного дерева:\n   {listToStr(redBlackSortedList)}\n")
    print(f">> Результат сортировки при помощи Splay-дерева:\n   {listToStr(splaySortedList)}\n")

    print(f">>> Время:")
    print(f"    При помощи AVL-дерева: {t1Finish - t1Start}")
    print(f"    При помощи Красно-чёрного дерева: {t2Finish - t2Start}")
    print(f"    При помощи Splay-дерева: {t3Finish - t3Start}")


# Массовый запуск экспериментов и построение сравнительных графиков скорости работы
def runStatExperiments():
    runExperiment1()
    runExperiment2()


def main():
    menuResult = showMenu()

    if menuResult in [RANDOM, RANDOM_ASC, RANDOM_DESC, MANUAL_INPUT]:
        runSingleExperiment(menuResult)
    else:
        runStatExperiments()


if __name__ == "__main__":
    main()
