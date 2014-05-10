#!/src/bin/python
#!encoding: UTF-8
import math 
from sympy import *
import modulo
import time
import numpy as np 
import matplotlib.pyplot as mp

numero = int(raw_input("Introduzca el grado que desea que tenga el Polinomio de Taylor: "))
centro = float(raw_input("Introduzca el punto central donde desea que se evalue el Polinomio de Taylor: "))
x = float(raw_input("Introduzca el punto x donde desea evaluar el Polinomio de Taylor: "))

modulo.taylor1(x, numero, centro)

y1 = np.arange(0,10,0.1)
y2 = np.sin(y1)
  
mp.plot(y1,y2)
mp.savefig('grafico.png',dpi = 30)
mp.show()
