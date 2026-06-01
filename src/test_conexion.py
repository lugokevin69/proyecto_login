from database.conexion import conectar

try:
    conexion = conectar()

    print("conexion exitosa")

    conexion.close()

except Exception as e:
    print("Error", e)