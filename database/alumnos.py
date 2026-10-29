from database.conexion import conectar


def obtener_alumnos():
    """Devuelve los datos que se ven en la tabla de Inicio:
    id, nombre, apellido, dni, telefono, correo"""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, nombre, apellido, dni, telefono, correo
            FROM alumnos
            ORDER BY id
        """)
        alumnos = cursor.fetchall()
        cursor.close()
        return alumnos
    finally:
        conexion.close()


def insertar_alumno(nombre, apellido, dni, carrera, anio,
                    localidad, fecha_nacimiento, correo, telefono):
    """Guarda un alumno nuevo con todos sus datos."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            INSERT INTO alumnos
            (nombre, apellido, dni, carrera, anio,
             localidad, fecha_nacimiento, correo, telefono)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (nombre, apellido, dni, carrera, anio,
             localidad, fecha_nacimiento, correo, telefono),
        )
        conexion.commit()
        cursor.close()
    finally:
        conexion.close()


def buscar_alumno_por_dni(dni):
    """Devuelve todos los datos de un alumno o None si no existe."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            SELECT id, nombre, apellido, dni, carrera, anio,
                   localidad, fecha_nacimiento, correo, telefono
            FROM alumnos
            WHERE dni = %s
            """,
            (dni,),
        )
        alumno = cursor.fetchone()
        cursor.close()
        return alumno
    finally:
        conexion.close()