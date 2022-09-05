from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app
from flask_app.models.postulantes import Postulante

@app.route('/convocatoria')
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
    session['postulantes_id'] = id #Guardando en sesion el identificador

    return redirect('/dashboard')

#-----------------------------------------------

@app.route('/dashboard')
def dashboard():
    formulario = {
        "id": session['postulantes_id']
    }
    postulante = Postulante.get_by_id(formulario)

    return render_template('dashboard.html', postulante=postulante)

#-----------------------------------------------

@app.route('/info_postulantes') #A través de la URL recibimos el ID del postulante
def ver_postulantes():
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')


    #llamar a una función y debo de recibir al postulante
    postulantes = Postulante.get_all()

    return render_template('info_postulantes.html',postulantes=postulantes)


#-----------------------------------------------

@app.route('/ver/postulantes/<int:id>') #A través de la URL recibimos el ID del postulante
def ver_postulante(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario_p = { "id": id }
    #llamar a una función y debo de recibir al postulante
    postulante = Postulante.get_by_id(formulario_p)

    return render_template('info_postulantes.html', postulante=postulante)

