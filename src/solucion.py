#!/src/bin/python

import math 
from sympy import *
import modulo

numero = int(raw_input("Introduzca el grado que desea que tenga el Polinomio de Taylor: "))
centro = float(raw_input("Introduzca el punto central donde desea que se evalue el Polinomio de Taylor: "))
x = float(raw_input("Introduzca el punto x donde desea evaluar el Polinomio de Taylor: "))

for i in range (0,numero+1):
  modulo.taylor(x, i, centro)
  
print suma
