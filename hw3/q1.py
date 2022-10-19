from copy import deepcopy
from functools import reduce
from math import inf
from numpy import array, ndarray, zeros


def calc(x, A, b, withCopy):
    toX = deepcopy(x)  # 故意深拷贝的 让函数无副作用
    fromX = toX
    if withCopy:
        fromX = deepcopy(toX)
    for i in range(0, len(x)):
        sum1 = reduce(
            lambda sum, j: sum + A[i][j]*fromX[j],
            list(range(0, i))+list(range(i+1, len(x))), 0)
        toX[i] = (b[i]-sum1)/A[i][i]
    return toX


def solver(A, b, e, isJacobi, x=None, delta=inf, iterTimes=0):
    if not (type(x) is ndarray):
        x = zeros(len(A))
    if delta < e:
        return x, iterTimes
    nextX = calc(x, A, b, isJacobi)
    delta = reduce(
        lambda sum, i: sum + (nextX[i]-x[i])**2,
        range(0, len(A)), 0)
    return solver(A, b, e, isJacobi, nextX, delta, iterTimes+1)


def JacobSolve(A, b, e):
    return solver(A, b, e, True)


def GSSolve(A, b, e):
    return solver(A, b, e, False)


jb = JacobSolve(array([
    [10, 3, 1],
    [2, -10, 3],
    [1, 3, 10]
], dtype=float), array([14, -5, 14], dtype=float), 0.001)
print(jb)


gs = GSSolve(array([
    [10, 3, 1],
    [2, -10, 3],
    [1, 3, 10]
], dtype=float), array([14, -5, 14], dtype=float), 0.001)
print(gs)
