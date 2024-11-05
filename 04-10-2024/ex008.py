import numpy as np
import math

def calcular_determinante(matriz):
    determinante = np.linalg.det(matriz)
    print(round(determinante))

matriz = [[5, -5], [2, -3]]
calcular_determinante(matriz)

matriz = [[math.sqrt(5), math.sqrt(2)], [-math.sqrt(2), math.sqrt(5)]]
calcular_determinante(matriz)

matriz = [[3, 2, 5], [4, 1, 3], [2, 3, 4]]
calcular_determinante(matriz)