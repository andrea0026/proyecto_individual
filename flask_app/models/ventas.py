from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Venta:

    def __init__(self, data):
        self.id = data['id']
        self.fecha_v = data['fecha_v']
        self.cantidad_v = data['cantidad_v']
        self.valor_kilo = data['valor_kilo']
        self.total_venta = data['total_venta']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.suma = data['suma']

    @staticmethod
    def validacion(formulario):
        es_valido = True

        if formulario['fecha_v'] == "":
            flash("Ingrese una fecha", "ventas")
            es_valido = False   
        #validar entero pisitivo
        if len(formulario['cantidad_v']) <= 0:
            flash('La cantidad debe ser mayor a 0', 'ventas')
            es_valido = False
        if len(formulario['valor_kilo']) < 0:
            flash('El valor debe ser mayor a 0', 'ventas')
            es_valido = False
        if len(formulario['total_venta']) < 0:
            flash('El valor debe ser mayor a 0', 'ventas')
            es_valido = False
        return es_valido 

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO ventas (fecha_v, cantidad_v, valor_kilo, total_venta) VALUES ( %(fecha_v)s, %(cantidad_v)s, %(valor_kilo)s, %(total_venta)s)"
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ventas;"
        results = connectToMySQL('proyecto_dojo').query_db(query)
        total_ventas = []
        for row in results:
            total_ventas.append(cls(row))
        return total_ventas

    @classmethod
    def sumatoria(cls,formulario):
        query  = "SELECT SUM(total_venta) FROM ventas WHERE fecha_v = %(fecha_v)s;"
        suma = connectToMySQL("proyecto_dojo").query_db(query,formulario)
        return suma

    @classmethod
    def get_by_id(cls,formulario):
        query  = "SELECT * FROM ventas WHERE id = %(id)s;"
        result = connectToMySQL("proyecto_dojo").query_db(query,formulario)
        venta = cls(result[0])
        return venta
