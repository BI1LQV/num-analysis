from copy import deepcopy
from functools import reduce
from math import inf
from numpy import array, ndarray, zeros


def calc(x, A, b, withCopy):
    toX = deepcopy(x)  # 故意深拷贝的 让函数无副作用
    fromX = x
    if withCopy:
        fromX = deepcopy(x)
    for i in range(0, len(x)):
        sum1 = reduce(
            lambda sum, j: sum + A[i][j]*fromX[j],
            list(range(0, i))+list(range(i+1, len(x))), 0)
        toX[i] = (b[i]-sum1)/A[i][i]
    return toX


def JacobSolve(A, b, e, x=None, delta=inf, iterTimes=0):
    if not (type(x) is ndarray):
        x = zeros(len(A))
    if delta < e:
        return x, iterTimes
    nextX = calc(x, A, b, True)
    delta = reduce(
        lambda sum, i: sum + (nextX[i]-x[i])**2,
        range(0, len(A)), 0)
    return JacobSolve(A, b, e, nextX, delta, iterTimes+1)


res = JacobSolve(array([
    [10, 3, 1],
    [2, -10, 3],
    [1, 3, 10]
], dtype=float), array([14, -5, 14], dtype=float), 0.01)
print(res)
