import math as math

#Pip sympy lib
from sympy import *
from sympy.parsing.sympy_parser import (parse_expr,
standard_transformations, implicit_multiplication_application)
from sympy.parsing.latex import parse_latex
from os import system, name

def biseccion(a, b, fun, error):
  limI = a
  limD = b
  e = limD - limI/(2)
  i = 1
  while(e - error > 0 or e == 0):
    FA = fun(a)
    FB = fun(b)
    c = (a+b)/2
    FC = fun(c)
    e = abs(limD - limI)/(2**i)
    print("%2d| [a= %15.11f] [b= %15.11f] [f(a)=%15.11f] [f(b)=%15.11f] [R=%15.11f] [f(R)=%15.11f] [error=%15.11f] " %(i, a, b, FA, FB, c, FC, e))
    if(FA*FC < 0):
      b = c
    else:
      a = c
    i += 1  

def newton(x, fun, dFun, error):
  a = 0
  i = 1
  while(abs(a-x) > error and i < 30):
    FA = fun(x)
    FDA = dFun(x)
    provisional = x - FA/FDA #provisional = r, x= semilla
    a = x
    x = provisional
    print("%2d| [Xn= %15.11f] [F(Xn)= %15.11f] [F´(Xn)= %15.11f] [Error Absoluto= %15.11f]" %(i, x, fun(x), dFun(x), abs(a-x)))
    i += 1

def secante(xm1, x, fun, error): 
  #xm1 = b
  #x = a
  #Epsilon = Error
  #Ep < F(x)
  i = 1                           
  while(abs(x-xm1) > error): #criterio dle aprada
    FX = fun(x)
    FXM1 = fun(xm1)
    provisional = x - FX*(x-xm1)/(FX-FXM1) #R = provisional
    FR = fun(provisional)
    print("%2d| [a=%15.11f] [b= %15.11f] [F(a)= %15.11f] [F(b)=%15.11f] [R=%15.11f] [F(R)=%15.11f] [(Ep) Error Absoluto= %15.11f]" %(i, xm1, x, FXM1, FX,provisional, FR, abs(x-xm1)))
    xm1 = x
    x = provisional
    i += 1

def falsa(a, b, fun, error):
  ant = b
  c = a
  i = 1
  while(abs(ant-c) > error):
    FB = fun(b)
    FA = fun(a)
    if(i != 1):
       ant = c
    c = b - FB*(b-a)/(FB-FA)
    FC = fun(c)
    print("%2d|[a= %15.11f] [b= %15.11f] [f(a)=%15.11f] [f(b)=%15.11f] [R=%15.11f] [f(R)=%15.11f] [error=%15.11f]" %(i, a, b, FA, FB, c, FC, abs(ant-c)))
    if(FA*FC < 0):
      b = c
    else:
      a = c
    i += 1

# def punto_fijo(xi,error,fun):
#   r = fun(xi)
#   while (xi - )

def fun(derivada,f):
  x = symbols('x')
  f_prima = f.diff(x)
  if (derivada == "no"):
    return lambdify(x,f)
  else:
    #print(lambdify(x,f_prima))
    return lambdify(x,f_prima)

  return

def clear():
  if name == 'nt': 
    system('cls')
  else:
    system('clear')
  
  
def main():
    div = '='*125
    limI = 0.5
    limD = 1.0
    op = 1 
    while((op == 1) or (op == 2)):
      print(" "+div,"\n arctan = atan / exp = ** / seno = sin / logaritmo = (ln ó log)\n",div)
      funcion = input('Escribe la funcion: ')
      funcion = parse_expr(funcion,
      transformations=(standard_transformations + #transformación del input a sympy
      (implicit_multiplication_application,)), local_dict={"log10": lambda x: log(x,10), "log2": lambda x: log(x,2)})
      error= float(input("Error: "))
      print('funcion-> ',funcion)
    
    
    
      metodo = input("\n metodo: ").lower()
      
      
      if (metodo == "falsa"):
          print(div,"\nFalsa:") #regula falsi????
          falsa(float(input("a: ")), float(input("b: ")), fun("no",funcion), error)
          print(div)
      
      if (metodo == "secante"):
          print(div,"\nSecante: \n")
          secante(float(input("a: ")), float(input("b: ")),fun("no",funcion),error)
          print(div)

      if (metodo == "newton"):
          print(div,"\nNewton: \n")
          newton(float(input('x: ')),fun("no",funcion),fun("si",funcion),error)
          print(div)
      
      if (metodo == "biseccion"):
          print(div,"\Biseccion: \n")
          biseccion(float(input('a: ')),float(input('b: ')),fun('no',funcion),error)
      op = float(input("1. continuar\n2. continuar y limpiar\n   Otra tecla salir\n"))

      if(op == 2):
          clear()
      if (op != 2) and (op != 1):
          clear()


if __name__ == '__main__':	
    main()












