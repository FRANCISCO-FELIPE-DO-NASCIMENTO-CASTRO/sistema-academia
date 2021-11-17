import os
import sys
from qt_core import *
from database.connection import create_connection

from PySide6.QtWidgets import QApplication, QMainWindow
# Importacao da janela principal
from interfaces.janelas.principal import Ui_tela_principal

# Classe para exibição da janela
class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Titulo da janela principal
        self.setWindowTitle('Sistema Academia')

        # Importando as configuraçoes da janela principal
        self.ui = Ui_tela_principal()
        self.ui.configuracao(self)
        conn = create_connection()
        print(conn)

        # Exibe a janela
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    sys.exit(app.exec())