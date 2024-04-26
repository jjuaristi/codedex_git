'''
=====================================================================
Funciones matemáticas para la calculadora
=====================================================================
'''
import math
from decimal import Decimal
#####################################################################
# Suma
#####################################################################
def suma(a, b):
    return a + b

#####################################################################
# Resta
#####################################################################
def resta(a, b):
    return a - b

#####################################################################
# Multiplicación
#####################################################################
def multiplica(a, b):
    return a * b

#####################################################################
# División
#####################################################################
def divide(a, b):
    div = 0.0
    if b == 0:
        div = 'Indefinido'
    else:
        div = float(a) / float(b)
    return div

#####################################################################
# Módulo
#####################################################################
def modulo(a, b):
    mod = 0.0
    if b == 0:
        mod = 'Indefinido'
        return mod
    else:
        mod = Decimal(a) % Decimal(b)
        print(Decimal(a), ' mod ', Decimal(b))
        print (mod)
        if float(mod) - int(mod) == 0:
            return int(mod)
        else:
            return float(mod)

#####################################################################
# Porcentaje
#####################################################################
def porcentaje(a, b):
    per = (Decimal(a) / 100) * Decimal(b)
    if float(per) - int(per) == 0:
        return int(per)
    else:
        return float(per)

#####################################################################
# Raiz cuadrada
#####################################################################
def raiz(a):
    sqr = math.sqrt(a)
    if float(sqr) - int(sqr) == 0:
        return int(sqr)
    else:
        return float(sqr)

#####################################################################
# Exponencial
#####################################################################
def exponente(a, b):
    exp = a ** b
    return exp

#####################################################################
# Pi
#####################################################################
def pi():
    return '3,141592'