from flask import Flask
from flask import render_template, request, redirect, url_for

import MN as mn

app = Flask(__name__, template_folder="templates")
    
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/MNR', methods=["GET", "POST"])
def MNR():
    if request.method == "GET":
        return render_template('metodoNR.html')
    else:
        fx = request.form['fx']
        resultados = mn.Newton(fx)
        pngImageB64String = mn.Graficacion(fx)
        return render_template('metodoNR_res.html', resultados = resultados, image = pngImageB64String)

@app.route('/graficas', methods=["GET", "POST"])
def graficas():
    if request.method == "GET":
        return render_template('graficas_form.html')
    else:
        fx = request.form['fx']
        pngImageB64String = mn.Graficacion(fx)
        return render_template('graficas.html', image = pngImageB64String)    

if __name__ == '__main__':
    app.run(debug = True, port=8000)

