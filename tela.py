import PySimpleGUI as sg 
from classes.aluno import Aluno 

class Tela:
    def __init__(self) -> None:
        sg.change_look_and_fell = ('Default 1')
        
        layout = [ 
            [sg.Text('Descricao'), sg.Input(key="descricao")],
            [sg.Button('Salvar', key="salvar", button_color ="red")]
        ]

        self.janela = sg.Window("Cadastro Cartão").layout(layout)

        

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()

            self.descricao = self.values['descricao']
            print(self.descricao)

tela = Tela()
tela.iniciar()