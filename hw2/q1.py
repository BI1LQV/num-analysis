A = [
    [10, -7, 0],
    [-3, 2, 6],
    [5, -1, 5]
]

b = [7, 4, 6]


def GaussSolve(A, b):
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
        x[i] = b[i]/A[i][i]
    return x


print(GaussSolve(A, b))
