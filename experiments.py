import time

from assist.advanced_drawing import drawPlot, showPlot, usePlotLegend


def runExperiment1():
    """xValues = []
    yValuesNaive = []
    yValuesEffective = []

    print("Эксперимент 1...")
    for n in range(1, 10_002, 100):
        kSegments, _, _, otherSegments \
            = generateRandomSegments(MODE_RANDOM_1, n)
        segments = []
        segments += kSegments
        segments += otherSegments

        t1Start = time.time()
        intersectionExists1, s1, s2 = intersectionNaive(segments)
        t1Finish = time.time()

        t2Start = time.time()
        intersectionExists2, s1, s2 = intersectionEffective(segments)
        t2Finish = time.time()

        if intersectionExists1 != intersectionExists2:
            raise Exception("Something went wrong!")

        xValues.append(n)
        yValuesNaive.append(t1Finish - t1Start)
        yValuesEffective.append(t2Finish - t2Start)

    drawPlot(xValues, yValuesNaive, clr="b", label="Naive")
    drawPlot(xValues, yValuesEffective, clr="green", label="Effective")
    usePlotLegend()
    showPlot(title="Эксперимент 1: n = 1...10^4 + 1 (шаг 100)",
             xLabel="Число n (отрезков)", yLabel="Время t (с)")"""
    print("TODO")


def runExperiment2():
    print("TODO")
