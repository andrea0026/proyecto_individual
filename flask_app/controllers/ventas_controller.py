from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.ventas import Venta

@app.route('/produccion')
def inicializacionVentas(cantidadTotal):
    cantidadTotal = 0
    return render_template('/produccion', cantidadTotal=cantidadTotal)

@app.route('/crear/venta', methods=['POST'])
def crear_venta():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    #validacion
    if not Venta.validacion(request.form): 
        return redirect('/crear/venta')

    Venta.save(request.form)
    return redirect('/produccion')

@app.route('/produccion/sumaVentas', methods=['POST'])
def produccion_sumaVentas():

    formulario={
        "sumaVentas": request.form['sumaVentas']
    }
    Venta.sumatoria(request.form)
    return redirect('/produccion')