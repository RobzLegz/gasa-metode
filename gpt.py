import numpy as np

A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

def gauss(A, b):
    n = len(A)
    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        for j in range(i+1, n):
            factor = A[j][i]/A[i][i]
            for k in range(i+1, n):
                A[j][k] -= factor*A[i][k]
            b[j] -= factor*b[i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        s = sum(A[i][j]*x[j] for j in range(i+1, n))
        x[i] = (b[i] - s)/A[i][i]
    return x

x = gauss(A, b)
print(x)