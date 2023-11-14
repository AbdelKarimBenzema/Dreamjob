
import os
#Importas la clase Flask de flask (para crear servidor web)
from flask import Flask
#Impoeras un archivo nuestro
from variables import cargarvariables

#Crea un objeto de la clase Flask
#app = Flask(__name__,
#            static_url_path='',
#            static_folder='static',
#            template_folder='template')
app = Flask(__name__)

#Añade configuración al servidor web
app.config.from_pyfile('settings.py')
#metodo del archivo cargarVariables
cargarvariables()

#Carga archivos
import rutas_inicio

import rutas_upload

import rutas_verfichero

import rutas_juegos

if __name__ == '__main__':
    port = int(os.environ.get('PORT'))
    host = os.environ.get('HOST')
    app.run(host=host, port=port)