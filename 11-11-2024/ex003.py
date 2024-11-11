import sympy as sp

'''
1) Determine f’(x) para as funções a seguir:
a) f(x) = x^3
b) f(x) = √x
c) f(x) = 1/x
d) f(x) = x^3− x
'''

# a)
x = sp.symbols('x')
f=x**3
print('a) '+str(sp.diff(f,x)))

# b)
f=sp.sqrt(x)
print('b) '+str(sp.diff(f,x)))

# c)
f=1/x
print('c) '+str(sp.diff(f,x)))

# d)
f=x**3-x
print('d) '+str(sp.diff(f,x)))