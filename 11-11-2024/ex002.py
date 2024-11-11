import numpy as np

'''
    2x + 3y = 16
    4x + 5y = 29
'''

a = np.array([[2, 3], [4, 5]])
b = np.array([[16], [29]])

result = np.dot(np.linalg.inv(a), b)
print(result)