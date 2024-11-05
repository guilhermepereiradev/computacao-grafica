import matplotlib.pyplot as plt
import numpy as np

matriz = [
    [200, 300, 400],
    [250, 350, 400],
    [220, 320, 390],
    [280, 360, 410],
    [260, 340, 380],
    [400, 400, 600],
    [230, 300, 470] 
]
diasDaSemana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
totalDiario = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(matriz)):
    totalDiario[i] = sum(matriz[i])

plt.title('Calorias consumidas')
plt.bar(np.array(diasDaSemana), np.array(totalDiario))
plt.ylabel('kcal')
plt.xlabel('Dias da semana')
plt.show()      
