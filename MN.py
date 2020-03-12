import sympy
from random import randint
import base64
import io

from sympy import *
from numpy import *
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

plt.switch_backend('agg')

x, y = sympy.symbols('x y')

def Graficacion(fx):
    y = fx
    x = linspace(-5,5,100)
    y = eval(y)
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.grid(alpha=.4,linestyle='--')

    plt.plot(x,y,'g')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String

def Newton(valor):
    
    fx = parse_expr(valor)
    
    resultados = []
    ER = 100
    ban = 0
    aleatorio = 2
    dx = sympy.diff(fx,x)

    while ER > 0:
        ban = ban + 1
        arriba = fx.subs(x,aleatorio)
        abajo = dx.subs(x,aleatorio)    
            
        vx = round(aleatorio - float(arriba/abajo),4)
        VA = float((vx-aleatorio)/vx)
        VA = abs(round(VA,4))
        ER = round(VA * 100,4) 

        resultados.append(["Caso "+str(ban),vx,str(ER)+"%"])

        aleatorio = vx
            
        if ban > 10:
            break

    return resultados