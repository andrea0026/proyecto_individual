from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app
from flask_app.models.postulantes import Postulante

@app.route('/')
def convocatoria():
    return render_template('convocatoria.html')

#-----------------------------------------------
#Creando una ruta para /register
@app.route('/register_p', methods=['POST'])
def register_p():
    #request.form = {
    #   "nombre": "Elena", ....}
    if not Postulante.valida_usuario(request.form):
        return redirect('/convocatoria')


    formulario = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "identificacion": request.form['identificacion'],
        "telefono1": request.form['telefono1'],
        "telefono2": request.form['telefono2']
    }
    id = Postulante.save(formulario) #Guardando a mi usuario y recibo el ID del nuevo registro
    session['usuarios_id'] = id #Guardando en sesion el identificador

    return redirect('/dashboard')

#-----------------------------------------------

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/convocatoria')
    formulario = {
        "id": session['usuario_id']
    }
    postulante = Postulante.get_by_id(formulario)

    return render_template('dashboard.html', postulante=postulante)

