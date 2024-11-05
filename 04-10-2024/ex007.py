# determinante de uma matriz é um valor escalar que pode
# ser calculado a partir de uma matriz quadrada
import numpy as np

matriz = [
    [1, 5],
    [2, 3]
]

determinante = np.linalg.det(matriz)
print(round(determinante))