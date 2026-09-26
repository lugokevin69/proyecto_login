from database.conexion import conectar

def obtener_alumnos():
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT id, nombre, apellido, dni, carrera, anio
        FROM alumnos
        """)
    
    alumnos = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    return alumnos