from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Insumo:

    def __init__(self, data):
        self.id = data['id']
        self.nombre_in = data['nombre_in']
        self.und_medida = data['und_medida']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def valida_insumos(formulario):
        es_valido = True

        if len(formulario['nombre_in']) < 3:
            flash("El nombre debe tener al menos 3 caracteres", "insumo")
            es_valido = False
        if len(formulario['und_medida']) < 2:
            flash("Por favor describir la unidad de medidad", "insumo")
            es_valido = False     
        return es_valido 

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO insumos (nombre_in, und_medida) VALUES ( %(nombre_in)s, %(und_medida)s)"
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM insumos" 
        results = connectToMySQL('proyecto_dojo').query_db(query) 
        insumos = []
        for insumo in results:
            insumos.append(cls(insumo))
        return insumos

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT * FROM insumos WHERE insumos.id = %(id)s" 
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario) 
        insumo = cls(result[0])
        return insumo

    @classmethod
    def update(cls, formulario):
        query = "UPDATE insumos SET nombre_in = %(nombre_in)s, und_medida = %(und_medida)s WHERE id = %(id)s"
        print(query)
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): 
        query = "DELETE FROM insumos WHERE id = %(id)s"
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario)
        return result