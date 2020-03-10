from flask import Flask
from flask import render_template, request, redirect, url_for

import sympy
from random import randint
import msvcrt
import os
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="templates")
x, y = sympy.symbols('x y')
    
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/MNR', methods=["GET"])
def MNR():
    return render_template('derivadas.html')

@app.route('/MNR', methods=["POST"])
def MNRes():
    fx = eval(request.form['fx'])
    ER = 100
    ban = 0

    while ER > 0:
        ban = ban + 1
        aleatorio = randint(-5,5)
        dx = sympy.diff(fx,x)
        
        vx = aleatorio - ( ( fx.subs(x,aleatorio) ) / (dx) )

        ER = ((vx - aleatorio) / vx) * 100

        print ("El Valor aleatorio usado es: ", aleatorio)
        print ("El Error Relativo del Caso ", ban, " es:", ER)

        if ER == 0:
            print ("El Valor de Xn es: ", vx)
    
    return render_template('derivadasres.html', funcion_usr= fx, derivada=dx)

if __name__ == '__main__':
    app.run(debug = True, port=8000)

