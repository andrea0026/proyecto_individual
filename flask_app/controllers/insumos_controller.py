from flask import render_template, redirect, session, request, flash 
from flask_app import app
from flask_app.models.insumos import Insumo

@app.route('/crear/insumo', methods=['POST'])
def crear_insumo():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    #validacion
    if not Insumo.valida_insumos(request.form): 
        return redirect('/crear/insumo')

    Insumo.save(request.form)
    return redirect('/compras')

@app.route('/borrar/insumo/<int:id>')
def borrar_insumo(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/compras')
    
    formulario = {"id": id}
    Insumo.delete(formulario)

    return redirect('/compras')