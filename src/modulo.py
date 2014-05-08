#!/src/bin/python

import math
from sympy import *
import time

def factorial(numero):
  factorial = 1
  while(numero > 1):
    factorial = factorial * numero
    numero = numero - 1
  return factorial

def taylor1(x, numero, centro):
  inicio = time.time()
  c = Symbol('c')
  f = sin(c)
  func = f.evalf(subs={c: centro})
  suma = func
  for i in range (1,numero + 1):
    f_i = diff(f, c)
    v = f_i.evalf(subs={c: centro})
    s= (v / factorial(i)) * ((x - centro) ** i)    
    suma = suma + s
    f = f_i
  error = func - suma
  print 'El valor de la funcion original sin(%f) es igual a %f ' % (centro, func)
  print 'El Polinomio de Taylor de grado n=%d en el punto centro c=%f evaluada en el punto x=%f es igual a %f' % (numero, centro, x, suma)
  print 'El Error de la funcion original con el Polinomio de Taylor es: error=%f' % error
  l=[numero                       , centro                     , x                         , suma                          , error]
  f = open("Taylor.tex", 'a')
  f.write('Grado del Polinomio (n)|| Punto Central (c) || Punto de Evaluacion (x) || Aproximacion || Error || Tiempo CPU \n ')
  fin = time.time()
  tiempo_total = fin - inicio
  l=l+[tiempo_total]
  f.write(str(l))
  f.write("\n")
  f.close()
  f=open("Taylor.tex","r")
  print(f.read())
  f.close()
  return taylor1
  
