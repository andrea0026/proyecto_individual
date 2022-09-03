from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.produccion import Produccion

@app.route('/produccion')
def inicializacionProduccion(cantidadTotal):
    cantidadTotal = 0
    return render_template('/produccion', cantidadTotal=cantidadTotal)

@app.route('/crear/registro', methods=['POST'])
def crear_registro():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    #validacion
    if not Produccion.validacion(request.form): 
        return redirect('/crear/registro')

    Produccion.save(request.form)
    return redirect('/produccion')

@app.route('/produccion/suma', methods=['POST'])
def produccion_suma():

    formulario={
        "suma": request.form['suma']
    }
    Produccion.sumatoria(request.form)
    return redirect('/produccion')