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
  
def taylor(x, numero, centro):
  c = Symbol('c')
  f = sin(c)
  suma = f.evalf(subs={c: centro})
  for i in range (1,numero + 1):
    f_i = diff(f, c)
    v = f_i.evalf(subs={c: centro})
    s= (v / factorial(i)) * ((x - centro) ** i)    
    suma = suma + s
    f = f_i
  return taylor

def taylor1(x, numero, centro):
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
  return taylor1

def lista():
  f=open("Taylor.tex", 'w')
  f.write('Grado del polinomio (n), Punto Central (c), Punto de evaluación (x), Aproximación, Error, Tiempo CPU \n ')
  f.write('==================================================================================================== \n')
  f.close()
  for i in range (0,numero+1):
    p=[]
    inicio = time.time()
    p=p+[modulo.taylor(x, i, centro)]
    fin = time.time
    tiempo_total = fin - inicio
    p=p+[tiempo_total]
    f.write(str(p)) 
    f.write("\n")
  modulo.taylor1(x, i, centro)
  f.close()
