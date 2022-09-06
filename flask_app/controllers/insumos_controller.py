from flask import render_template, redirect, session, request, flash 
from flask_app import app
from flask_app.models.insumos import Insumo

@app.route('/crear/insumo', methods=['POST'])
def crear_insumo():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    #validacion
    if not Insumo.valida_insumos(request.form): 
        return redirect('/compras')

    Insumo.save(request.form)
    flash("Guardado", '/crear/insumo')
    return redirect('/compras')

@app.route('/borrar/insumo/<int:id>')
def borrar_insumo(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    Insumo.delete(formulario)

    return redirect('/compras')

@app.route('/editar/insumo/<int:id>')
def editar_insumo(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    nombreUser = session['nombreUsuario']
    formulario_insumo = { "id": id }
    insumo = Insumo.get_by_id(formulario_insumo)

    return render_template('/editar_insumos.html',insumo=insumo,nombreUser=nombreUser)


@app.route('/editar/insumo', methods=['POST'])
def editarInsumo():
    print("entro a editar")
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    if not Insumo.valida_insumos(request.form): 
        return redirect('/editar/insumo/'+request.form['id'])
    
    Insumo.update(request.form)

    return redirect('/compras')






