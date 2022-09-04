from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.compras import Compra
from flask_app.models.insumos import Insumo

@app.route('/compras')
def inicializacionCompras():
    userId = session['user_id']
    nombreUser = session['nombreUsuario']
    nombre_in = ""

    return render_template('/compras.html',userId=userId,nombreUser=nombreUser,nombre_in=nombre_in,insumos=Insumo.get_all)

@app.route('/crear/compra', methods=['POST'])
def crear_compra():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    #validacion
    if not Compra.validacion(request.form): 
        return redirect('/crear/registro')

    Compra.save(request.form)
    return redirect('/compras')