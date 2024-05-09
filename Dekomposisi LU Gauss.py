import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Mendefinisikan matriks A sebagai nilai koefisien variabel menggunakan Numpy arrays
A = np.array([[4, 7], [2, 6]])

# Mendefinisikan matriks B sebagai nilai konstanta hasil persamaan linier
B = np.array([33, 36])

# Melakukan dekomposisi LU pada matriks A
lu, piv = lu_factor(A)

# Menggunakan hasil dekomposisi LU untuk menemukan solusi
solusi = lu_solve((lu, piv), B)

print('Solusi sistem persamaan adalah ', solusi)
