from __future__ import print_function
from bd import obtener_conexion
import sys

def insertar_usuario(nombre, apellido1, apellido2,fechanacimiento):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios(nombre, apellido1, apellido2, fechanacimiento) VALUES (%s, %s, %s,%s)",
                       (nombre, apellido1, apellido2,fechanacimiento))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        print("Excepcion al insertar un usuario", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_usuario_a_json(usuario):
    d = {}
    d['id'] = usuario[0]
    d['nombre'] = usuario[1]
    d['apellido1'] = usuario[2]
    d['apellido2'] = usuario[3]
    d['fechanacimiento'] = usuario[4]
    return d

def obtener_usuarios():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, apellido1, apellido2,fechanacimiento FROM usuarios")
            usuarios = cursor.fetchall()
            usuariosjson=[]
            if usuarios:
                for usu in usuarios:
                    usuariosjson.append(convertir_usuario_a_json(usu))
        conexion.close()
        code=200
    except:
        print("Excepcion al obtener los usuarios", file=sys.stdout)
        usuariosjson=[]
        code=500
    return usuariosjson,code

def obtener_usuario_por_id(id):
    usuariojson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            #cursor.execute("SELECT id, nombre, descripcion, precio,foto FROM juegos WHERE id = %s", (id,))
            cursor.execute("SELECT id, nombre, apellido1, apellido2,fechanacimiento FROM usuarios WHERE id =" + id)
            usuario = cursor.fetchone()
            if usuario is not None:
                usuariojson = convertir_usuario_a_json(usuario)
        conexion.close()
        code=200
    except:
        print("Excepcion al recuperar un usuario", file=sys.stdout)
        code=500
    return usuariojson,code


def eliminar_usuario(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un usuario", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_usuario(id, nombre, apellido1, apellido2, fechanacimiento):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE usuarios SET nombre = %s, apellido1 = %s, apellido2 = %s, fechanacimiento=%s WHERE id = %s",
                       (nombre, apellido1, apellido2, fechanacimiento,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Excepcion al eliminar un usuario", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
