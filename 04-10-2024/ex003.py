# multiplicacao de matrizes utilizando o numpy
import numpy as np

matrizA = [
            [1, 2, 3],
            [4, 5, 6]
        ]

matrizB = [
            [7, 8],
            [9, 10],
            [11, 12]
        ]

resultado = np.dot(matrizA, matrizB)
print(resultado)