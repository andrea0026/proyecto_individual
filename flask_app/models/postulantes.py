from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash,jsonify

class Postulante:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.identificacion = data['identificacion']
        self.telefono1 = data['telefono1']
        self.telefono2 = data['telefono2']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO postulantes(nombre, apellido, identificacion, telefono1, telefono2) VALUES (%(nombre)s, %(apellido)s, %(identificacion)s, %(telefono1)s, %(telefono2)s)"
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario) #1 - Insert recibe id
        return result #result = Identificador del nuevo registro

    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
        
        if len(formulario['nombre']) < 3:
            #flash('Nombre debe de tener al menos 3 caracteres', 'registro')
            return jsonify(message='Nombre debe de tener al menos 3 caracteres')
            es_valido = False
        
        if len(formulario['apellido']) < 3:
            #flash('Apellido debe de tener al menos 3 caracteres', 'registro')
            return jsonify(message='Apellido debe de tener al menos 3 caracteres')
            es_valido = False
        
        if len(formulario['identificacion']) < 6:
            #flash('La identificación debe de tener al menos 6 caracteres', 'registro')
            return jsonify(message='La identificación debe tener al menos 6 caracteres')
            es_valido = False

        if len(formulario['telefono1']) < 10:
            #flash('El teléfono celular debe de tener al menos 10 caracteres', 'registro')
            return jsonify(message='El teléfono celular debe de tener al menos 10 caracteres')
            es_valido = False
        return es_valido

    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM postulantes WHERE id = %(id)s"
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario) #Select recibe lista
        postulante = cls(result[0])
        return postulante
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM postulantes"
        results = connectToMySQL('proyecto_dojo').query_db(query) 
        postulantes = []
        for postulante in results:
            postulantes.append(cls(postulante))
        return postulantes