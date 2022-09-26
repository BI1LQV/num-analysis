from copy import deepcopy


def LUFactorization(iA):
    A = deepcopy(iA)
    n = len(A)
    L = [[0 for i in range(n)] for j in range(n)]
    U = [[0 for i in range(n)] for j in range(n)]

    for k in range(0, n-1):
        if A[k][k] == 0:
            return None
        for i in range(k+1, n):
            A[i][k] = A[i][k]/A[k][k]
            for j in range(k+1, n):
                A[i][j] = A[i][j]-A[i][k]*A[k][j]

    for i in range(0, n):
        L[i][i] = 1
        for j in range(0, i):
            L[i][j] = A[i][j]
        for j in range(i, n):
            U[i][j] = A[i][j]
    return L, U


A = [
    [1, 2, 2],
    [4, 4, 2],
    [4, 6, 4]
]

L, U = LUFactorization(A)
print("L:", L)
print("U:", U)
