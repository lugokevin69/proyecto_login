import mysql.connector

def conectar():

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="contra2005",
        database="instituto"
    )

    return conexion