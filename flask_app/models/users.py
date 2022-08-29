from flask_app.config.mysqlconnection import connectToMySQL
import re #Importamos expresiones regulares
#crear una expresión regular para verificar que tengamos el email con formato correcto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash #mandar mensajes a la plantilla

class User:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.perfil = data['perfil']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO usuarios(nombre, apellido, email, password, perfil) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(perfil)s)"
        print(query)
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario) #1 - Insert recibe id
        return result #result = Identificador del nuevo registro

    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
        
        if len(formulario['nombre']) < 3:
            flash('Nombre debe de tener al menos 3 caracteres', 'registro')
            es_valido = False
        
        if len(formulario['apellido']) < 3:
            flash('Apellido debe de tener al menos 3 caracteres', 'registro')
            es_valido = False
        
        #Valido email con expresiones regulares
        if not EMAIL_REGEX.match(formulario['email']): 
            flash('Email invalido', 'registro')
            es_valido = False

        if len(formulario['password']) < 6:
            flash('Contraseña debe tener al menos 6 caracteres', 'registro')
            es_valido = False
        
        if formulario['password'] != formulario['confirm_password']:
            flash('Contraseñas no coiniciden', 'registro')
            es_valido = False
        
        #Consultar si ya existe el correo
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        results = connectToMySQL('proyecto_dojo').query_db(query, formulario)
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False

        # check si la contraseña tiene al menos: un numero y una letra mayuscula
        if not any(char.isdigit() for char in formulario["password"]):
            flash('La contraseña debe contener al menos un número','registro')
            es_valido = False
        if not any(char.isupper() for char in formulario["password"]):
            flash('La contraseña debe contener al menos una mayuscula','registro')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_email(cls, formulario):
        #formulario = {
        #   "email": "elena@cd.com", "password": "12345}
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            #result = [ {nombre: Elena, apellido: De Troya.....} ]
            user = cls(result[0]) #Haciendo una instancia de User -> CON los datos que recibimos de la base de datos
            return user

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario) #Select recibe lista
        user = cls(result[0])
        return user