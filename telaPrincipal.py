from ctypes import alignment
import PySimpleGUI as sg

from cadastroAluno import TelaAluno
from cadastroPlano import TelaPlano
from model import Matricula
from telaPlano import Plano
from telaMatricula import TelaMatricula
academia = {'BACKGROUND': '#0074e8',
                            'TEXT': 'red',
                            'INPUT': '#c7e78b',
                            'TEXT_INPUT': '#000000',
                            'SCROLL': '#c7e78b',
                            'BUTTON': ('white', '#0074e8'),
                            'PROGRESS': ('#01826B', '#D0D0D0'),
                            'BORDER': 0,
                            'SLIDER_DEPTH': 0,
                            'PROGRESS_DEPTH': 0}


sg.theme_add_new('Sistema Academia', academia)

# cinza = "#f1f1f1"
# azul = "#0063c5"
class TelaPrincipal:

    def __init__(self) -> None:
        self.telaAluno = TelaAluno()    
    
    def principal(self):
        sg.theme('Sistema Academia')
        # sg.theme('LightGreen')
        sg.set_options(element_padding=(0, 0))

        # ------ Menu Definition ------ #
        menu_def = [
                    ['&Cadastro', ['&Alunos', 'Planos']],
                    ['&Matricula', ['Matricula']],
                    ['&Relatorios', ['Vendas']]                   
                ]

        

        # ------ GUI Defintion ------ #
        layout = [
            [sg.Menu(menu_def, tearoff=False, pad=(200,1), background_color="#fff")],
        
            
        ]
        # "#1B8EF2"
        self.janela = sg.Window('Tela Principal', size=(800 ,580), default_element_size=(50, 1), resizable=True, layout=layout, finalize=True)
        self.janela.set_min_size((800 ,580))
        # self.janela.Maximize()


        return self.janela
        
tela = TelaPrincipal()
aluno = TelaAluno()
plano = TelaPlano()
matricula = TelaMatricula()
plano = Plano()
janelaPrincipal, janelaAluno, tlplano, tlmatricula, tlPlano = tela.principal(), None, None, None, None


        
while True:
            
    window, event, values = sg.read_all_windows()  

    if window == janelaPrincipal and event == sg.WIN_CLOSED:
        break

    # if  window == janelaPrincipal and event == sg.WIN_MAXIMIZED:
    #     window.maximize()

    elif window == janelaPrincipal and event == "Alunos":
        janelaAluno = aluno.janela_aluno()

    elif window == janelaPrincipal and event == 'Planos':
        tlplano = plano.tela()


    elif window == janelaPrincipal and event == "Matricula":
        tlmatricula = matricula.tela()

    elif window == janelaPrincipal and event == "Planos":
        tlPlano = plano.tela()

        



           
          
           
            



