# Importa el sistema (sirve para manejar argumentos y cerrar la app correctamente)
import sys

# Importa las clases necesarias de PyQt5
from PyQt5.QtWidgets import QApplication, QWidget

# Importa tu interfaz creada en Qt Designer (convertida a .py)
from login_ui import Ui_Form


# Creamos una clase para la ventana
class Login(QWidget, Ui_Form):
    def __init__(self):
        # Inicializa la ventana base (QWidget)
        super().__init__()

        # Carga todos los elementos de la interfaz (botones, inputs, etc.)
        self.setupUi(self)


# Punto de inicio del programa
if __name__ == "__main__":
    
    # Crea la aplicación (obligatorio en PyQt)
    app = QApplication(sys.argv)

    # Crea la ventana
    ventana = Login()

    # Muestra la ventana en pantalla
    ventana.show()

    # Mantiene la app corriendo hasta que la cierres
    sys.exit(app.exec_())