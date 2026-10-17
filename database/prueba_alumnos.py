from database.alumnos import obtener_alumnos

alumnos = obtener_alumnos()

for alumno in alumnos:
    print(alumno)