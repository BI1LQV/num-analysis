from copy import deepcopy
from functools import reduce

A1 = [
    [10, -7, 0],
    [-3, 2, 6],
    [5, -1, 5]
]

A2 = [
    [10, -7, 0],
    [10, -7, 0],
    [5, -1, 5]
]


b = [7, 4, 6]


def GaussSolve(iA, ib):
    A = deepcopy(iA)
    b = deepcopy(ib)
    n = len(A)
    x = [0]*n
    for k in range(0, n):
        if A[k][k] == 0:
            break
        for i in range(0, n):
            if i == k:
                continue
            c = A[i][k]/A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j]-c*A[k][j]
            b[i] = b[i]-c*b[k]

    for i in range(0, n):
        if A[i][i] == 0:
            return None
        x[i] = b[i]/A[i][i]
    return x


def assess(A, b):
    res = GaussSolve(A, b)
    if res:
        return reduce(
            lambda before, cur: f"{before}x{cur[0]}={cur[1]}; ",
            zip(range(1, len(res)+1), res), ""
        )
    return "无唯一解"


print("对于A1:", assess(A1, b))
print("对于A2:", assess(A2, b))
