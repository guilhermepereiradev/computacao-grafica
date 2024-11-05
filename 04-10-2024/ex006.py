#matriz inversa é o inverso de uma matriz baseado no conceito do inverso de um numero
# ex. o inverso de n é n^-1
import numpy as np

matriz = [
    [3, 1],
    [5, 2]
]

print(np.linalg.inv(matriz))