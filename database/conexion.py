import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        port=3305,
        user="root",
        password="contra2005",
        database="instituto"
    )

    return conexion