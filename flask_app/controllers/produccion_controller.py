from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.produccion import Produccion


@app.route('/produccion')
def produccion():
    if 'user_id' not in session:
        return redirect('/')

    user = Produccion.get_user_by_id(session['user_id'])
    cantidadTotal = Produccion.get_produccion_mes()
    totalVentas = Produccion.get_ventas_mes()

    return render_template('produccion.html', user=user,cantidadTotal=cantidadTotal,totalVentas=totalVentas)

@app.route('/crear/registro', methods=['POST'])
def crear_registro():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
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