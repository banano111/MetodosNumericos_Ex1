import sympy
import msvcrt
import os
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


x, y = sympy.symbols('x y')
sympy.init_printing(use_unicode=false)

def menu():
    print("Metodos Numericos \n")
    print("Primer Examen Parcial - Metodo Newton Raphson \n")

    print("¿Que desea hacer? \n")
    print("1. Graficar Funcion")
    print("2. Realizar Metodo de Newton Raphson")
    print("3. Realizar Metodo de Newton Raphson con Grafica de la funcion")
    print("4. Salir del Programa \n")

    opc = eval(input("Introduce tu opcion: "))

    dict.get(opc,default)()
    
    return opc

def Graficas():
    os.system ("cls")
    print("1. Graficar Funcion \n")

    x = np.linspace(-5,5,100)
    y = eval(input("Ingrese la funcion a Graficar: "))

    CrearGrafica(x,y)    

def NR():
    os.system ("cls")
    print("2. Realizar Metodo de Newton Raphson \n")

    fx = input("Introduce la funcion a derivar: ")

    dx = sympy.diff(fx,x)

    print("\n\n")
    pprint (dx)

    print("\n\nPresione una tecla para continuar...")
    msvcrt.getch()

def NRG():
    os.system ("cls")
    print("3. Realizar Metodo de Newton Raphson con Grafica de la funcion\n")

    x = np.linspace(-5,5,100)
    y = eval(input("Ingrese la funcion a Graficar: "))

    CrearGrafica(x,y) 

def default():
    print("Opcion Incorrecta, Intente de Nuevo!")

def Salida():
    os.system ("cls")
    print("Gracias por ocupar la aplicacion...")

def CrearGrafica(x,y):

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x,y,'g')

    plt.grid(alpha=.4,linestyle='--')

    plt.show()

    
dict = {
    1: Graficas,
    2: NR,
    3: NRG,
    4: Salida
}

bandera = 1

while bandera<4 :
    os.system ("cls")
    bandera = menu()