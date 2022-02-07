import PySimpleGUI as sg

class Matricula:
    def __init__(self) -> None:

        layout = [
            [sg.Text('Aluno'), sg.Input('', key='aluno')],
            [sg.Button('Salvar', key='salvar')]
            
        ]
        self.janela = sg.Window('Matricula').layout(layout)

        window = sg.Window('window', layout)

        while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Date Popup':
            sg.popup('You chose:', sg.popup_get_date())
window.close()
            



matricula = Matricula()
matricula.iniciar()