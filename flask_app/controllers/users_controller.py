from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app
from flask_app.models.users import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

#-----------------------------------------------
#Creando una ruta para /register
@app.route('/register', methods=['POST'])
def register():
    print("entro")
    if not User.valida_usuario(request.form):
        return redirect('/')


    pwd = bcrypt.generate_password_hash(request.form['password']) #Me encripta el password
    print("encripto")

    formulario = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": pwd,
        "perfil": request.form['perfil']
    }
    print("creo formulario")
    id = User.save(formulario) #Guardando a mi usuario y recibo el ID del nuevo registro
    print("guardo")
    session['user_id'] = id #Guardando en sesion el identificador

    return redirect('/produccion')

#-----------------------------------------------
@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user: #si user=False
        flash("E-mail no encontrado", 'login')
        return redirect('/')
    #Comparando la contraseña encriptada con la contraseña del LOGIN
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Password incorrecto", 'login')
        return redirect('/')
    session['user_id'] = user.id
    session['perfil_id'] = user.perfil

    return redirect('/produccion')

#-----------------------------------------------
@app.route('/produccion')
def produccion():
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    user = User.get_by_id(formulario)

    return render_template('produccion.html', user=user)

#-----------------------------------------------
@app.route('/logout')
def logout():
    session.clear() #Elimina la sesión
    return redirect('/')