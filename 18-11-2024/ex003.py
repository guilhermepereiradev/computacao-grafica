from sympy import *

from sympy import *
def imprimirResultado(questao):
    print(questao+": "+str(diff(f,x)))

x = symbols('x')
f=x**3
imprimirResultado("a")

f=sqrt(x)
imprimirResultado("b")

f=1/x
imprimirResultado("c")

f=x**3-x
imprimirResultado("d")