from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.compras import Compra

@app.route('/compras')
def inicializacionCompras():
    nombreUser = session['nombreUsuario']
    all_insumos = Compra.get_all_insumos()
    return render_template('/compras.html',insumos=all_insumos,nombreUser=nombreUser)

@app.route('/crear/compra', methods=['POST'])
def crear_compra():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    #validacion
    if not Compra.validacion(request.form): 
        return redirect('/crear/registro')

    Compra.save(request.form)
    return redirect('/compras')