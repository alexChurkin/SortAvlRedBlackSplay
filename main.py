import math

from assist.advanced_input import readInt, readFloatList, readFloatRange
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


    # >>> Выбран ручной способ задания массива
    else:
        inputList = readFloatList("Введите элементы массива:\n",
                                  minimum=1,
                                  maximum=10, includeR=False)


    t1Start = time.time()
    t1Finish = time.time()


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
