from flask_app import app
from flask_app.controllers import users_controller, postulantes_controller,compras_controller, insumos_controller, produccion_controller, ventas_controller

if __name__=="__main__":
    app.run(debug=True)