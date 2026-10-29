# Importa los paquetes y modulos necesarios
import sys
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QMainWindow,
    QTableWidgetItem
)

# Importa las ventanas
from src.login_ui import Ui_Form
from src.interfaz_registro_ui import Ui_Form as Ui_Registro
from src.interfaz_inicio_ui import Ui_MainWindow

# Importa las funciones de la base de datos
from database.alumnos import obtener_alumnos, insertar_alumno


# Ventana INICIO (interfaz principal despues del login)
class Inicio(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Boton para volver al login
        self.bt_volver2.clicked.connect(self.volver_login)

        # Boton "Agregar Alumno" (ajusta el nombre al de tu boton en Designer)
        self.bt_agregar.clicked.connect(self.abrir_registro)

        # Columnas definidas desde el codigo para que coincidan con el SELECT
        self.tabla_alumnos.setColumnCount(6)
        self.tabla_alumnos.setHorizontalHeaderLabels(
            ["ID", "NOMBRE", "APELLIDO", "D.N.I", "TELÉFONO", "CORREO"]
        )
        self.tabla_alumnos.verticalHeader().setVisible(False)
        self.tabla_alumnos.verticalHeader().setDefaultSectionSize(40)

        self.cargar_alumnos()

    def abrir_registro(self):
        # Registro avisa a Inicio para que recargue la tabla al guardar
        self.registro = Registro(callback=self.cargar_alumnos)
        self.registro.show()

    def cargar_alumnos(self):
        alumnos = obtener_alumnos()   # id, nombre, apellido, dni, telefono, correo
        self.tabla_alumnos.setRowCount(0)

        for fila, alumno in enumerate(alumnos):
            self.tabla_alumnos.insertRow(fila)
            for columna, dato in enumerate(alumno):
                texto = "" if dato is None else str(dato)
                self.tabla_alumnos.setItem(fila, columna, QTableWidgetItem(texto))

    def volver_login(self):
        self.login = Login()
        self.login.show()
        self.close()


# Ventana LOGIN
class Login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Boton Crear Cuenta / Registrar Alumno abre la ventana de registro
        self.BotonCrearCuenta.clicked.connect(self.abrir_registro)

        # Boton administrador abre la ventana de inicio
        self.bt_admin.clicked.connect(self.abrir_inicio)

    def abrir_registro(self):
        self.registro = Registro()
        self.registro.show()
        self.close()

    def abrir_inicio(self):
        self.inicio = Inicio()
        self.inicio.show()
        self.close()


# Ventana REGISTRO
class Registro(QWidget, Ui_Registro):
    def __init__(self, callback=None):
        super().__init__()
        self.setupUi(self)
        self.callback = callback

        self.bt_volver.clicked.connect(self.volver)
        self.bt_guardar.clicked.connect(self.guardar_alumnos)

    def volver(self):
        if self.callback:        # vino desde Inicio: solo se cierra
            self.close()
        else:                    # vino desde Login: vuelve al Login
            self.login = Login()
            self.login.show()
            self.close()

    def guardar_alumnos(self):
        # Datos de los campos
        nombre = self.input_nombre.text().strip()
        apellido = self.input_apellido.text().strip()
        dni = self.input_dni.text().strip()
        carrera = self.combo_carrera.currentText()
        anio = self.combo_anio.currentText()

        # Campos nuevos (revisa los nombres en Qt Designer)
        localidad = self.combo_localidad.currentText()
        fecha_nacimiento = self.date_nacimiento.date().toString("yyyy-MM-dd")
        correo = self.input_correo.text().strip()
        telefono = self.input_telefono.text().strip()

        # Validaciones
        if not nombre or not apellido:
            QMessageBox.warning(self, "Error", "Debe ingresar nombre y apellido")
            return
        if not dni.isdigit() or not (7 <= len(dni) <= 8):
            QMessageBox.warning(self, "Error", "El DNI debe tener 7 u 8 dígitos numéricos")
            return
        if correo and ("@" not in correo or "." not in correo):
            QMessageBox.warning(self, "Error", "El correo electrónico no es válido")
            return
        if telefono and not telefono.isdigit():
            QMessageBox.warning(self, "Error", "El teléfono debe contener solo números")
            return

        # Guardar en MySQL
        try:
            insertar_alumno(
                nombre, apellido, dni, carrera, anio,
                localidad, fecha_nacimiento,
                correo or None, telefono or None
            )
        except mysql.connector.IntegrityError:
            QMessageBox.warning(self, "Error", "Ya existe un alumno con ese DNI")
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        QMessageBox.information(self, "Éxito", "Alumno registrado correctamente")

        # Limpiar campos
        self.input_nombre.clear()
        self.input_apellido.clear()
        self.input_dni.clear()
        self.input_correo.clear()
        self.input_telefono.clear()

        # Refrescar la tabla de Inicio si Registro se abrio desde ahi
        if self.callback:
            self.callback()


# INICIO DEL PROGRAMA
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Login()
    ventana.show()

    sys.exit(app.exec_())