from flask import render_template, redirect, session, request, flash 
from flask_app import app
from flask_app.models.users import User

#Importar el modelo de insumos
from flask_app.models.insumos import Insumo

@app.route('/nuevo/insumo')
def nuevo_insumo():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario)
    
    return render_template('compras.html', user=user)

@app.route('/crear/insumo', methods=['POST'])
def crear_insumo():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    #validar formulario de insumos
    if not Insumo.valida_insumos(request.form):
        return redirect('/nuevo/insumo')

    Insumo.save(request.form)
    return redirect('/compras.html')

@app.route('/editar/insumo/<int:id>') #Recibo el identificador del insumo que quiero editar
def editar_insumo(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    formulario_insumos = { "id": id }
    insumo = Insumo.get_by_id(formulario_insumos)

    return render_template('edit_recipe.html', user=user, recipe=recipe)

@app.route('/update/recipe', methods=['POST'])
def update_recipe():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    if not Recipe.valida_receta(request.form):
        return redirect('/editar/insumo/'+request.form['id']) #/editar/insumo/1

    Insumo.update(request.form)

    return redirect('/compras.html')

@app.route('/mostrar/insumos/<int:id>') #A través de la URL recibimos el ID del insumo
def mostrar_insumos(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    formulario_insumos = { "id": id }
    insumo = Insumo.get_by_id(formulario_insumos)

    return render_template('compras.html', user=user, insumo=insumo)

@app.route('/borrar/insumo/<int:id>')
def borrar_insumo(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/index')
    
    formulario = {"id": id}
    Insumo.delete(formulario)

    return redirect('/compras.html')