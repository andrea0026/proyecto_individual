from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Produccion:

    def __init__(self, data):
        self.id = data['id']
        self.fecha_p = data['fecha_p']
        self.cantidad_p = data['cantidad_p']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.suma = data['suma']

    @staticmethod
    def validacion(formulario):
        es_valido = True

        if formulario['fecha_p'] == "":
            flash("Ingrese una fecha", "produccion")
            es_valido = False     
        #validar que ingrese un numero positivo
        if len(formulario['cantidad_p']) <= 0:
            flash('La cantidad debe ser mayor a 0', 'produccion')
            es_valido = False
        return es_valido 

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO produccion (fecha_p, cantidad_p) VALUES ( %(fecha_p)s, %(cantidad_p)s)"
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM produccion;"
        results = connectToMySQL('proyecto_dojo').query_db(query)
        total_produccion = []
        for row in results:
            total_produccion.append(cls(row))
        return total_produccion

    @classmethod
    def sumatoria(cls,formulario):
        query  = "SELECT SUM(cantidad_p) FROM produccion WHERE fecha_p = %(fecha_p)s;"
        suma = connectToMySQL("proyecto_dojo").query_db(query,formulario)
        return suma

    @classmethod
    def get_by_id(cls,formulario):
        query  = "SELECT * FROM produccion WHERE id = %(id)s;"
        result = connectToMySQL("proyecto_dojo").query_db(query,formulario)
        un_producto = cls(result[0])
        return un_producto
