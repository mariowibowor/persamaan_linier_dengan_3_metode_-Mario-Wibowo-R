import numpy as np

# Mendefinisikan matriks A sebagai nilai koefisien variabel dengan Numpy arrays
A = np.array([[3, 9], [1, 6]])

# Mendefinisikan matriks B sebagai nilai konstanta hasil
B = np.array([33, 36])

# Mencari matriks balikan dari A
A_inv = np.linalg.inv(A)

# Menggunakan matriks balikan untuk menemukan solusi
solusi = np.dot(A_inv, B)

print('Solusi sistem persamaan adalah ', solusi)