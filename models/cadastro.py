from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout= [
    [sg.Text('Usuario'),sg.Imput(Key='usuario')],
    [sg.Text('Senha'),sg.Input(Key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de Login',layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Entrar':
        if valores['usuario'] == 'felipe' and valores['senha'] == '12345':
            print('bem-vindo')