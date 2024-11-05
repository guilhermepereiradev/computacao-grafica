import numpy as np
alfabeto = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H',
                      9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
                      15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
                      21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z', 27: ' '}

matrizA=[[3, 4], [2, 3]]
matrizAM=[[117, 23, 156, 7, 89, 63, 92, 87, 28, 35] , [87, 17, 113, 5, 66, 45, 68, 65, 20, 25]] 

matrizAi = np.linalg.inv(matrizA);
resultado = np.dot(matrizAi, matrizAM)

frase = ''
for i in range(len(resultado)):
    for j in range(len(resultado[i])):
        frase += alfabeto.get(round(resultado[i][j]))

print(frase)