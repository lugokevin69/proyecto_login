import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Importar interfaces
from login_ui import Ui_Form
from interfaz_registro_ui import Ui_Form as Ui_Registro


# 🟢 Ventana LOGIN
class Login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #este codigo conecta el boton botonCrearCuenta y inicia la ventana interfaz_registro
        self.BotonCrearCuenta.clicked.connect(self.abrir_registro)

    def abrir_registro(self):
        self.registro = Registro()
        self.registro.show()
        self.close()


# 🟣 Ventana REGISTRO
class Registro(QWidget, Ui_Registro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #esto define la funcion al boton de volver
        self.BOTONVOLVERREGISTRO.clicked.connect(self.volver_login)

    def volver_login(self):
        self.login = Login()
        self.login.show()
        self.close()
        #viste que era una pavada milencoi

        self.BOTONVOLVERREGISTRO.clicked.connect(self.volver_login)

    def volver_login(self):
        self.login = Login()
        self.login.show()
        self.close()
        #viste que era una pavada milencoi
        


# 🚀 INICIO DEL PROGRAMA
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Login()   # 👉 ventana inicial
    ventana.show()

    sys.exit(app.exec_())