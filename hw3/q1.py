from copy import deepcopy
from functools import reduce
from math import inf
from numpy import array, ndarray, zeros, max, abs
from numpy.linalg import eigvals


def isIterable(x):
    base = zeros((len(x), len(x)))
    LU = zeros((len(x), len(x)))
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                base[i][j] = 1/x[i][j]
            else:
                LU[i][j] = -x[i][j]
    return max(abs(eigvals(base@LU))) < 1


def calc(x, A, b, withCopy):
    toX = deepcopy(x)  # 故意深拷贝的 让函数无副作用
    fromX = toX
    if withCopy:
        fromX = deepcopy(toX)  # 分别是Jacobi迭代法和Gauss-Seidel迭代法
    for i in range(0, len(x)):
        sum1 = reduce(
            lambda sum, j: sum + A[i][j]*fromX[j],
            list(range(0, i))+list(range(i+1, len(x))), 0)
        toX[i] = (b[i]-sum1)/A[i][i]
    return toX


def solver(A, b, e, isJacobi, x=None, delta=inf, iterTimes=0):
    if not (type(x) is ndarray):
        x = zeros(len(A))  # 初始化x
    if not isIterable(A):  # 不收敛
        return False
    if delta < e:
        return x, iterTimes  # 判停

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

jb = JacobSolve(array([
    [1, 0, 0],
    [0, 1, 1],
    [0, -1, 1]
], dtype=float), array([14, -5, 14], dtype=float), 0.001)
print("Jacob", jb)


gs = GSSolve(array([
    [1, 0, 0],
    [0, 1, 1],
    [0, -1, 1]
], dtype=float), array([14, -5, 14], dtype=float), 0.001)
print("GS", gs)


t2 = array([[3, 3], [2, -12]], dtype=float)

print("JB", JacobSolve(t2, array([14, -5], dtype=float), 0.00001))


print("GS", GSSolve(t2, array([14, -5], dtype=float), 0.00001))
