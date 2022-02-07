import PySimpleGUI as sg



class TelaPlano:
    def tela(self):
        layout = [
                [sg.Text('DESCRICAO'), sg.Input()],
                [sg.Text('ADESÃO'), sg.Input()],
                [sg.Text('MENSALIDADE'), sg.Input()],
                [sg.Text("TAXA MANUTENCAO"), sg.Input()]
        ]
        
        window = sg.Window('Cadastro de Cliente', background_color="#e9e9e9", margins=(100,100),finalize=True).layout(layout)

        while True:
            event, values = window.Read()

            if event == sg.WINDOW_CLOSED or event == 'Sair':
                break


        return window

