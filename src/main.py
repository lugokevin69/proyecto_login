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

        # ejemplo: conectar botón
        self.boton_ingresar.clicked.connect(self.abrir_registro)

    def abrir_registro(self):
        self.registro = Registro()
        self.registro.show()
        self.close()


# 🟣 Ventana REGISTRO
class Registro(QWidget, Ui_Registro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# 🚀 INICIO DEL PROGRAMA
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Registro()   # 👉 ventana inicial
    ventana.show()

    sys.exit(app.exec_())