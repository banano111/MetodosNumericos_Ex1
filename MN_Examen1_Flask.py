from flask import Flask
from flask import render_template, request, redirect, url_for

import MN as mn

app = Flask(__name__, template_folder="templates")
    
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/MNR', methods=["GET"])
def MNR():
    return render_template('derivadas.html')

@app.route('/MNR', methods=["POST"])
def MNRes():
    fx = request.form['fx']
    resultados = mn.Newton(fx)
    pngImageB64String = mn.Graficacion(fx)
    
    return render_template('derivadasres.html', resultados = resultados, image = pngImageB64String)

@app.route('/graficas', methods=["GET"])
def graficas():
    return render_template('graficas_form.html')

@app.route('/graficas', methods=["POST"])
def graficas_res():

    fx = request.form['fx']
    pngImageB64String = mn.Graficacion(fx)

    return render_template('graficas.html', image = pngImageB64String)

if __name__ == '__main__':
    app.run(debug = True, port=8000)

