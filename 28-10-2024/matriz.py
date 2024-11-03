import numpy as np

def popular_matriz(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(input("Linha: "+str(i)+" Coluna: "+str(j)+" = "))

def multiplicar_matrizes(matA, matB):
    linhasA, colunasA = len(matA), len(matA[0])
    linhasB, colunasB = len(matB), len(matB[0])
    
    if colunasA != linhasB:
        print("As matrizes não podem ser multiplicadas.")
        return
    
    resultado = np.zeros((linhasA, colunasB))
    
    for i in range(linhasA):
        for j in range(colunasB):
            for k in range(colunasA):
                resultado[i][j] += matA[i][k] * matB[k][j]
    
    print(resultado)

linhasA = int(input("Quantas linhas tem a matriz A? "))
colunasA = int(input("Quantas colunas tem a matriz A? "))
matrizA = np.zeros((linhasA, colunasA))
popular_matriz(matrizA)

linhasB = int(input("Quantas linhas tem a matriz B? "))
colunasB = int(input("Quantas colunas tem a matriz B? "))
matrizB = np.zeros((linhasB, colunasB))
popular_matriz(matrizB)

print("A x B =")
multiplicar_matrizes(matrizA, matrizB)

print("B x A =")
multiplicar_matrizes(matrizB, matrizA)