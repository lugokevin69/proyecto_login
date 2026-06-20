import mysql.connector

print("Inicio")

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3305,
        user="root",
        password="contra2005",
        database="instituto"
    )

    print("Conexión exitosa")

    conexion.close()

except Exception as e:
    print("Error:")
    print(type(e))
    print(e)

print("Fin")