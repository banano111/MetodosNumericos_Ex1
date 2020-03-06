from flask import Flask
from flask import render_template, request, redirect, url_for

import sympy
import msvcrt
import os
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="templates")
x, y = sympy.symbols('x y')

@app.route('/')
def index():
    fx = x**2 + 3*x + x**4
    dx = sympy.diff(fx,x)
   
    return render_template('index.html', derivada=dx)

@app.route('/derivadas', methods=["GET"])
def formulario():
    return render_template('derivadas.html')

@app.route('/derivadas', methods=["POST"])
def derivadas():
    fx = request.form['fx']
    dx = sympy.diff(fx,x)

    return render_template('derivadasres.html', funcion_usr= fx, derivada=dx)

if __name__ == '__main__':
    app.run(debug = True, port=8000)
