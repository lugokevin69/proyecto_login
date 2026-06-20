from database.conexion import conectar
# Este archivo es para probar la conexion a la base de datos, si no funciona revisar el archivo conexion.py y revisar los datos de conexion.
try:
    conexion = conectar()

    print("Conexión exitosa")

    conexion.close()

except Exception as e:
    print("Error:", e)