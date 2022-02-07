import sys
sys.path.append('..')
import controllers

import PySimpleGUI as sg

from controllers.alunoController import AlunoController
from controllers.planoController import PlanoController

class Plano:
    def __init__(self) -> None:
        self.controller = PlanoController()

    def tela(self):
        layout = [
            [sg.Text('Descrição'),sg.Input(key="-DESCRICAO-")],
            [sg.Text('Adesão'), sg.Input(key="-ADESAO-")],
            [sg.Text('Mensalidade'), sg.Input(key="-MENSALIDADE-")],
            [sg.Text('Taxa de Manutenção'), sg.Input(key="-MANUTENCAO-")],
            [sg.Button("Salvar", key="-SALVAR-"), sg.Button('Deletar')]
        ]

        window = sg.Window('Cadastro Plano', layout=layout, size=(960 ,540), finalize=True)

        while True:
            event, values = window.Read()

            if event == sg.WIN_CLOSED or event == '-SAIR-':
                break

            if event == "-SALVAR-":
                descricao = values['-DESCRICAO-']
                adesao = values['-ADESAO-']
                mensalidade = values['-MENSALIDADE-']
                manutencao = values['-MANUTENCAO-']
                self.controller.salvar(descricao, adesao, mensalidade, manutencao)

         

        return window

