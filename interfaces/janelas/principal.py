from qt_core import *


# Criando janela principal
class Ui_tela_principal(object):
    def configuracao(self, parent):
        if not parent.objectName():
            parent.setObjectName('Janela Principal')

        # Define o tamanho inicial da tela
        parent.resize(960, 540)
        parent.setMinimumSize(960, 540)

        # Temos que criar um wigets pai para nossa aplicação
        self.central_frame = QFrame()

        # Criar estilos
        self.central_frame.setStyleSheet("background-color: #00FA9A")
        
        # Criando Layout da tela principal
        # Assim ele preecha toda a area do QFrame
        # para que possamos adcionar nosso widgeets filhos
        self.layout_principal = QHBoxLayout(self.central_frame)
        self.layout_principal.setContentsMargins(0,0,0,0)
        self.layout_principal.setSpacing(0)

        # Configuração do central frame para que ele seja mostrado na aplicação
        parent.setCentralWidget(self.central_frame)

