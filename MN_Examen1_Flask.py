from flask import Flask
from flask import render_template, request, redirect, url_for

import sympy
from random import randint
import base64
import io

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


app = Flask(__name__, template_folder="templates")
x, y = sympy.symbols('x y')

def Graficacion():
    
    x = np.linspace(-5,5,100)
    y = eval(request.form['fx'])
    
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

    plt.grid(alpha=.4,linestyle='--')

    plt.plot(x,y,'g')

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String

def Newton():
    prev = eval(request.form['fx'])
    
    fx = prev.replace("np.",)
    
    resultados = []
    ER = 100
    ban = 0
    aleatorio = 2
    dx = sympy.diff(fx,x)

    while ER > 0:
        ban = ban + 1
        arriba = fx.subs(x,aleatorio)
        abajo = dx.subs(x,aleatorio)    
        
        vx = aleatorio - float(arriba/abajo)
        vx = round(vx,4)
        VA = float((vx-aleatorio)/vx)
        VA = round(VA,4)
        VA = abs(VA)
        ER = VA * 100
        ER = round(ER,4)        

        resultados.append(["Caso "+str(ban),vx,str(ER)+"%"])

        aleatorio = vx

        if ER == 0:
            res_final = VA

    return resultados
    
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/MNR', methods=["GET"])
def MNR():
    return render_template('derivadas.html')

@app.route('/MNR', methods=["POST"])
def MNRes():
    resultados = Newton()
    
    
    return render_template('derivadasres.html', resultados = resultados )

@app.route('/graficas', methods=["GET"])
def graficas():
    return render_template('graficas_form.html')

@app.route('/graficas', methods=["POST"])
def graficas_res():

    pngImageB64String = Graficacion()

    return render_template('graficas.html', image = pngImageB64String)

if __name__ == '__main__':
    app.run(debug = True, port=8000)

