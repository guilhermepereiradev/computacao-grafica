from sympy import *
def imprimirResultado(questao):
    print(questao+": "+str(diff(f,x)))

x = symbols('x')
f=(2*x**2-3*x+5)*(2*x-1)
imprimirResultado("a")

f=(sin(x))/x**2
imprimirResultado("b")

f=ln(x)/sqrt(x)
imprimirResultado("c")

f=sin(x**2)-3*x+6
imprimirResultado("d")

f=-(1/2)*x**4+(2/3)*x**2+(1/4)
imprimirResultado("e")