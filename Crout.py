import numpy as np

def crout(A):
    n = len(A)
    L = np.zeros((n,n))
    U = np.eye(n)
    for j in range(n):
        for i in range(j,n):
            temp = sum(L[i][k]*U[k][j] for k in range(j))
            L[i][j] = A[i][j] - temp
        for i in range(j+1,n):
            temp = sum(L[j][k]*U[k][i] for k in range(j))
            U[j][i] = (A[j][i] - temp) / L[j][j]
    return L, U

def solve_crout(L, U, B):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)
    for i in range(n):
        y[i] = (B[i] - sum(L[i][j]*y[j] for j in range(i))) / L[i][i]
    for i in range(n-1, -1, -1):
        x[i] = y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))
    return x

# Mendefinisikan matriks A sebagai nilai koefisien variabel dengan Numpy arrays
A = np.array([[4, 7], [2, 6]])

# Mendefinisikan matriks B sebagai nilai konstanta hasil
B = np.array([33, 36])

# Dekomposisi Crout pada matriks A
L, U = crout(A)

# Menggunakan hasil dekomposisi Crout untuk menemukan hasil
solusi = solve_crout(L, U, B)

print('Solusi sistem persamaan adalah ', solusi)