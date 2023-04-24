from math import cos, sin, exp
from prettytable import PrettyTable

n = 20  # Кількість вулзів
eps = 0.1  # Коефіціент для зміщенних вузлів


def f(x):
    square = x**2
    return exp(-square) * sin(x) + square


def funcA(a, b, n):
    """
    Задаємо вузли відрізку [a,b]
    x_i=a+ih,i=(0,..,n), h=(b-a)/n
    """
    x = []
    h = float(b - a) / n
    for i in range(n+1):
        x.append(a + i * h)
    return x


def funcB(a, b, n):
    """
    Задаємо вузли відрізку [a,b]
    x_i=1/2 (b+a-(b-a)*cos⁡((2k+1)/2(n+1) * π) ),k=(0,..,n)
    """
    x = []
    pi = 3.1415
    for i in range(n + 1):
        x.append(0.5*(a + b - cos(pi*(2*i+1)/(2*(n + 1))) * (b - a)))
    return x


def Polinom_Lagrange(x, t):
    """
    Будуємо інтерполяційний поліном Лагранжа згідно з формулою
    Ln(t)= ∑fi ∏(t − xk)/(xi − xk)"
    """
    a = -1
    b = 1
    LA = 0
    LB = 0
    xA = funcA(a, b, n)
    xB = funcB(a, b, n)
    for i in range(n):
        tmpA = 1
        tmpB = 1
        for k in range(n):
            if i == k: continue
            tmpA *= float(t - xA[k]) / (xA[i] - xA[k])
            tmpB *= float(t - xB[k]) / (xB[i] - xB[k])
        LA += f(x) * tmpA
        LB += f(x) * tmpB
    return LA, LB



def show(s, INTERPOL, FUNC, e=0.0):
    """
    Функція, яка відображає отримані розрахунки
    """
    t = PrettyTable(['x', 'f(x)', 'P(x)', '|P(x)-f(x)|'])
    x = -1
    while x <= 1:
        fValue = f(x)
        LValue = Polinom_Lagrange(x, x)
        t.add_row([x, fValue, LValue[0], abs(fValue - LValue[0])])
        x += 0.1
    print(t)


show("L(x):A", Polinom_Lagrange, funcA)
show("L(x):B", Polinom_Lagrange, funcB)
show("L(x):A+e", Polinom_Lagrange, funcA, eps)
show("L(x):B+e", Polinom_Lagrange, funcB, eps)
