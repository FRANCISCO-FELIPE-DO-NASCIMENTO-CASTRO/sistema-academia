from qt_core import *

# Aqui vamos importar as nossas paginas
from interfaces.paginas.ui_pages import Ui_applications_pages


# Criando janela principal
class Ui_tela_principal(object):
    def configuracao(self, parent):
        if not parent.objectName():
            parent.setObjectName('Janela Principal')

    
        # Define o tamanho inicial da tela
        parent.resize(960, 540)
        parent.setMinimumSize(960, 540)
        # Temos que criar um wigets pai para nossa aplicação ele é quem vai receber o conteudo da aplicação
        self.central_frame = QFrame()
        # Criar estilos
        self.central_frame.setStyleSheet("background-color: #e6eaec")        
        # Criando Layout da tela principal
        # Assim ele preecha toda a area do QFrame
        # para que possamos adcionar nosso widgeets filhos
        self.layout_principal = QHBoxLayout(self.central_frame)
        # Se comentarmos o codigo acima. A opcao abaixo tranforma e layout vertical e o menu fica em cima
        # self.layout_principal = QVBoxLayout(self.central_frame)

        # Remove as bordas 
        self.layout_principal.setContentsMargins(0,0,0,0)
        # Remove os espaços centrais
        self.layout_principal.setSpacing(0)
        
        # Menu lateral esquerda
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet('background-color: #fff')
        self.left_menu.setMaximumWidth(100)
        self.left_menu.setMinimumWidth(100)
        # Se comentarmos o codigo acima. A opcao abaixo tranforma e layout vertical e o menu fica em cima
        # self.left_menu.setMaximumHeight(40)
        # self.left_menu.setMaximumHeight(40)

        self.conteudo = QFrame()
        self.conteudo.setStyleSheet("background-color: #eeeee4") 

        # devemos criar uma layout vertical que seja filho do conteudo para podemos colocar o top_bar nela
        self.conteudo_layout = QVBoxLayout(self.conteudo)
        self.conteudo_layout.setContentsMargins(0,0,0,0)
        self.conteudo_layout.setSpacing(0)
        # Agora podemos adicionar  self_top ao conteudo_top_layout

        # top bar
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(40)
        self.top_bar.setMinimumHeight(40) 
        self.top_bar.setStyleSheet("background-color:  #fff; color: blue")
        # Temos que criar um layout oara podermos adicionar as labels no top_bar
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0) 

        #Criando texto para top_bar
        self.top_label_left = QLabel("Test")        
        # Vamos criar um espaçamento 
        self.top_espacador = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)        
        # criando testo direito para top bar
        self.top_label_right = QLabel("Test")

        # Adicionando as labels ao top_bar_layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_espacador)
        self.top_bar_layout.addWidget(self.top_label_right)


        # Devemos criar mais uma area de conteudo para que o o top bar suba
        # Aqui adicionaremos as paginas do sistema
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #1e81b0;")
        # Adicinando as paginas
        self.ui_pages = Ui_applications_pages()
        self.ui_pages.setupUi(self.pages)

        # rodape
        self.rodape = QFrame()
        self.rodape.setMaximumHeight(40)
        self.rodape.setMinimumHeight(40) 
        self.rodape.setStyleSheet("background-color:  #fff; color: #fff") 

        # Adionando self_top a 
        self.conteudo_layout.addWidget(self.top_bar)
        self.conteudo_layout.addWidget(self.pages)
        self.conteudo_layout.addWidget(self.rodape)

             

        # Adicionar Widget ao app
        self.layout_principal.addWidget(self.left_menu)
        self.layout_principal.addWidget(self.conteudo)
      
  

        # Configuração do central frame para que ele seja mostrado na aplicação
        parent.setCentralWidget(self.central_frame)

