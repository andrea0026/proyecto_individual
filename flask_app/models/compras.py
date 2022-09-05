from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.insumos import Insumo
from datetime import date

class Compra:

    def __init__(self, data):
        self.id = data['id']
        self.fecha_g = data['fecha_g']
        self.concepto = data['concepto']
        self.valor = data['valor']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.id_insumo = data['id_insumo']
        self.suma = data['suma']

    @staticmethod
    def validacion(formulario):
        es_valido = True
        if formulario['fecha_g'] == "":
            flash("Ingrese una fecha", "compras")
            es_valido = False 
        if len(formulario['valor']) < 0:
            flash('El valor debe ser mayor a 0', 'compras')
            es_valido = False    
        return es_valido 

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO gastos (fecha_g, concepto, valor,id_insumo) VALUES ( %(fecha_g)s, %(concepto)s, %(valor)s,%(id_insumo)s)"
        print(query)
        result = connectToMySQL('proyecto_dojo').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT gastos.*, nombre_in FROM gastos LEFT JOIN insumos ON insumos.id = gastos.id"
        query = "SELECT * FROM gastos;"
        results = connectToMySQL('proyecto_dojo').query_db(query)
        total_compras = []
        for row in results:
            total_compras.append(cls(row))
        return total_compras

    @classmethod
    def sumatoria(cls,formulario):
        query  = "SELECT SUM(valor) FROM gastos WHERE fecha_v = %(fecha_v)s;"
        suma = connectToMySQL("proyecto_dojo").query_db(query,formulario)
        return suma

    @classmethod
    def get_by_id(cls,formulario):
        query  = "SELECT * FROM gastos WHERE id = %(id)s;"
        result = connectToMySQL("proyecto_dojo").query_db(query,formulario)
        compra = cls(result[0])
        return compra

    @classmethod
    def get_all_insumos(cls):
        all_insumos = Insumo.get_all()
        return all_insumos

    @classmethod
    def get_ventas_mes(cls):
        today = date.today()

        mount = today.strftime("%m")
        year = today.strftime("%Y")
        query  = "SELECT * FROM ventas WHERE MONTH(fecha_v) = " + mount + " AND YEAR(fecha_v) = " + year + ";"
        result = connectToMySQL("proyecto_dojo").query_db(query)
        suma = 0

        for row in result:
            suma += row['total_venta']
    
        return suma

    @classmethod
    def get_gastos_mes(cls):
        today = date.today()

        mount = today.strftime("%m")
        year = today.strftime("%Y")
        query  = "SELECT * FROM gastos WHERE MONTH(fecha_g) = " + mount + " AND YEAR(fecha_g) = " + year + ";"
        print(query)
        result = connectToMySQL("proyecto_dojo").query_db(query)
        suma = 0

        for row in result:
            suma += row['valor']
    
        return suma
    