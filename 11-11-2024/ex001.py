import numpy as np

'''
    x + y = 1
    -x + y = 5
'''

a = np.array([[1, 1], [-1, 1]])
b = np.array([[1], [5]])

result = np.dot(np.linalg.inv(a), b)
print(result)