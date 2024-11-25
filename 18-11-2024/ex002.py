from sympy import *    

x = symbols('x')
f = x+1
print("a: "+str(integrate(f, x)))

f = x**2 + sqrt(x)
print("b: "+str(integrate(f, (x, 0, 1))))

f = (1 + cos(2 * x)) /2
print("c: "+str(integrate(f, (x, 0, pi/2))))