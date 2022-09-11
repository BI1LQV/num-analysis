from functools import reduce
from numpy import exp

TOLERANCE = 1e-16
toExamine = [-1, 1, -5, 5, -10, 10, -15, 15, -20, 20]


def calcUnit(x, n):
    # x^n/n!
    return reduce(lambda x, y: x/y, range(1, n+1), x**n)


def assess(fn):
    myRes = map(fn, toExamine)
    accRes = map(exp, toExamine)
    delta = map(lambda x: (x[0]-x[1])/x[1], zip(myRes, accRes))
    return list(delta)


def calcPowerE1(x):
    def partSum(x, n):
        unit = calcUnit(x, n)
        if abs(unit) > TOLERANCE:
            return partSum(x, n+1)+unit
        return 0
    return partSum(x, 0)


def calcPowerE2(x):
    def partSum(x, n):
        unit = calcUnit(x, n)
        if abs(unit) > TOLERANCE:
            return partSum(x, n+1)+unit
        return 0
    sign = 1 if x > 0 else -1
    return partSum(abs(x), 0)**sign


def calcPowerE3(x):
    def partSum(x, n):
        unit = calcUnit(x, n)
        if abs(unit) > TOLERANCE:
            return partSum(x, n+2)+unit
        return 0
    return partSum(x, 0)+partSum(x, 1)


print(assess(calcPowerE1))
print(assess(calcPowerE2))
print(assess(calcPowerE3))
