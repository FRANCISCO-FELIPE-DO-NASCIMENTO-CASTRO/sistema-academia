import PySimpleGUI as sg
from alunoController import AlunoController

class Matricula:
    def __init__(self) -> None:

        layout = [
            [sg.Text('CPF'), sg.Input(key='aluno'), sg.Button('Buscar', key='buscar')],
            [sg.Text('Plano')]
            
        ]
        self.janela = sg.Window('Matricula').layout(layout)
        controller = AlunoController()
        
        while True:
            
            event, values = self.janela.read()
            print(event, values)
    

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == 'buscar':
                cpf = values['cpf']
                aluno = controller.getCpf(cpf)
                self.janela['nome'].update(aluno)
            
           
            



matricula = Matricula()
matricula.iniciar()