import re
from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.compras import Compra

@app.route('/compras')
def inicializacionCompras():
    nombreUser = session['nombreUsuario']
    all_insumos = Compra.get_all_insumos()
    total_ventas = Compra.get_ventas_mes()
    total_gastos = Compra.get_gastos_mes() 
    return render_template('/compras.html',insumos=all_insumos,nombreUser=nombreUser,total_ventas=total_ventas,total_gastos=total_gastos)

@app.route('/crear/compra', methods=['POST'])
def crear_compra():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    #validacion
    if not Compra.validacion(request.form): 
        return redirect('/compras')

    Compra.save(request.form)
    flash("Guardado", '/compras')
    return redirect('/compras')