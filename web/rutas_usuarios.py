from flask import request, session
import json
import decimal
from __main__ import app
import web.controlador_usuarios as controlador_usuarios

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/usuarios",methods=["GET"])
def usuarios():
    code= controlador_usuarios.obtener_usuarios()
    return json.dumps(usuarios, cls = Encoder),code

@app.route("/usuario/<id>",methods=["GET"])
def usuario_por_id(id):
    usuario,code = controlador_usuarios.obtener_usuario_por_id(id)
    return json.dumps(usuario, cls = Encoder),code

@app.route("/usuarios",methods=["POST"])
def guardar_usuario():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        usuario_json = request.json
        ret,code=controlador_usuarios.insertar_usuario(usuario_json["nombre"], usuario_json["apellido1"], float(usuario_json["apellido2"]), usuario_json["fechanacimiento"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/usuarios/<id>", methods=["DELETE"])
def eliminar_usuario(id):
    ret,code=controlador_usuarios.eliminar_usuario(id)
    return json.dumps(ret), code

@app.route("/usuarios", methods=["PUT"])
def actualizar_usuario():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        usuario_json = request.json
        ret,code=controlador_usuarios.actualizar_usuario(usuario_json["id"],usuario_json["nombre"], usuario_json["apellido1"], usuario_json["apellido2"], usuario_json["fechanacimiento"])
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code