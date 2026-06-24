#Importa los paquetes y modulos necesarios
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

#Importa las ventanas
from src.login_ui import Ui_Form
from src.interfaz_registro_ui import Ui_Form as Ui_Registro

#Impota la conexion a la base de datos
from database.conexion import conectar

# 🟢 Ventana LOGIN
class Login(QWidget, Ui_Form): #esto es para crear la clase Login que hereda de QWidget y Ui_Form (que es la interfaz del login)
    def __init__(self): #esto es para inicializar la clase Login
        super().__init__() #esto es para llamar al constructor de la clase QWidget y Ui_Form
        self.setupUi(self) 

        #este codigo conecta el boton botonCrearCuenta y inicia la ventana interfaz_registro
        self.BotonCrearCuenta.clicked.connect(self.abrir_registro)

    def abrir_registro(self):   #esto es para abrir la ventana de registro y cerrar la ventana de login
        self.registro = Registro()
        self.registro.show()
        self.close() 


# 🟣 Ventana REGISTRO
class Registro(QWidget, Ui_Registro):
    def __init__(self):
        super().__init__()
    
        self.setupUi(self)
        #esto define la funcion al boton de volver
        self.bt_volver.clicked.connect(self.volver_login)
        
        #boton guardar
        self.bt_guardar.clicked.connect(self.guardar_alumnos)
    
    #esto es para volver a la ventana de login
    def volver_login(self):
        self.login = Login()
        self.login.show()
        self.close()
    
    
    def guardar_alumnos(self):    #esta funcion es para guardar los datos de alumnos a sql
        
        print("Entró a guardar_alumnos")
        
        #obtener datos de los campos Qline y Combo Box
        nombre = self.input_nombre.text()
        apellido = self.input_apellido.text()
        dni = self.input_dni.text()
            
        carrera = self.combo_carrera.currentText()
        anio = self.combo_anio.currentText()
        
        #Aqui muestra en la termi lo que se guardo en los campos.
        print(nombre)
        print(apellido)
        print(dni)
        print(carrera)
        print(anio)
            
            # Verificar que no esten vacios
            
        if nombre == "":
                QMessageBox.warning(
                    self,
                    "error",
                    "debe ingresar un nombre"
                )
                return
            
        if dni == "":
            QMessageBox.warning(
                self,
                "error",
                "debe ingresar un DNI"
            )
            return
            
            
        try:
                #Conectarse a MySQL
                
            print("Conectando...")
            import mysql.connector    #esto es para importar el conector de mysql y usarlo.

            print("Versión mysql.connector:", mysql.connector.__version__)
            conexion = conectar() #llama la funcion conectar() Q está en el archivo conexion.py
            print("Conexión Exitosa")
            print("Creando cursor...")
            cursor = conexion.cursor() #crea un cursor para ejecutar consultas SQL
            
                
              #Aqui consultamos a sql para insertar los datos de los campos a la tabla de alumnos.
            sql = """ #
            INSERT INTO alumnos
            (nombre,  apellido, dni, carrera, anio)
            VALUES (%s, %s, %s, %s, %s)   
            """  #Python cambia los %s por los datos introducidos en los campos.
                
            datos = (
                nombre,
                apellido,
                dni,
                carrera,
                anio
            )
                # Ejecutar consulta
                
            print("Ejecutando INSERT...")
            cursor.execute(sql, datos)      #esto es para ejecutar la consulta SQL con los datos proporcionados.
                
            # Guardar cambios
            print("commit...")
            conexion.commit() #esto es para que se guarden los cambios y no se borre cuando cerramos conexion.
                
            # Cerrar conexion
            print("Cerrando cursor y conexión...")
            cursor.close()
            conexion.close()
                
            print("Terminado")
                      
            # Mensaje de exito
                
            QMessageBox.information(
                self,
                 "Exito",
                 "Alumno registrado correctamente"
            )
                
            #Estos limpian los campos despues de "Guardar"
            self.input_nombre.clear()
            self.input_apellido.clear()
            self.input_dni.clear()
                        
        except Exception as e:    #esto es para avisar si hay algun error en la conexion cn sql.
            print("ERROR DETECTADO:")
            print(type(e))
            print(e)

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )
    
            

# 🚀 INICIO DEL PROGRAMA
if __name__ == "__main__":
    app = QApplication(sys.argv)     #esto es para iniciar la aplicacion de PyQt5

    ventana = Login()   #ventana inicial
    ventana.show()      #esto es para mostrar la ventana

    sys.exit(app.exec_())    #esto es para cerrar la app