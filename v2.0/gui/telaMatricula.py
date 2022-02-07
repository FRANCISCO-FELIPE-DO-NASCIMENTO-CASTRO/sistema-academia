import PySimpleGUI as sg
import sys
sys.path.append('..')
import controllers

from controllers.alunoController import AlunoController



class TelaMatricula:
    def __init__(self) -> None:
        self.controller = AlunoController()

        alunos = self.controller.listaAlunos()
                
                
    def tela(self):
        layout = [
                [sg.Text('CPF'), sg.Input('',k='-CPF-'), sg.Button('-BUSCAR-'), sg.Button('Inserir')],
                                    
                [sg.Listbox(values=[['nome']], size=(30, 6))],
                [sg.Button('Registrar Matricula', key='-MATRICULA-')]
        ]
        
        window = sg.Window('Matricula', background_color="#e9e9e9",size=(800 ,580), finalize=True).layout(layout)

        while True:
            event, values = window.Read()         

            if event == sg.WINDOW_CLOSED or event == 'Sair':
                break

            if event == '-BUSCAR-':
                cpf = values['-CPF-']
                aluno = self.controller.getCpf(cpf)
                alunos = self.controller.listaAlunos()
                for a in alunos:
                    print (a['id'])
                
                # print(alunos)
                
                id = aluno.id
                print(id)
                
                




            


        return window

