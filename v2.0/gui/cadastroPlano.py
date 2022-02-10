
import PySimpleGUI as sg
import sys
sys.path.append('..')
from controllers.planoController import PlanoController

# from pyUFbr.baseuf import ufbr
# print(ufbr.list_uf)
# print(ufbr.list_cidades('PI'))
 



# def sucesso():
#     layout = [
#         [sg.Text("Salvo com sucesso")],
#         [sg.Button('Ok', key='ok')]        
#     ]
    

#     janela = sg.Window("Sucesso", layout=layout, finalize=True)
#     return janela
academia = {'BACKGROUND': '#F2F5FA',
                            'TEXT': '#04BEB3',
                            'INPUT': '#c7e78b',
                            'TEXT_INPUT': '#495960',
                            'SCROLL': '#c7e78b',
                            'BUTTON': ('white', '#04BEB3'),
                            'PROGRESS': ('#01826B', '#D0D0D0'),
                            'BORDER': 0,
                            'SLIDER_DEPTH': 0,
                            'PROGRESS_DEPTH': 0}

sg.theme_add_new('Sistema Academia', academia)

class TelaPlano:
        def __init__(self) -> None:
            self.plano = PlanoController()

        def tela(self):
                sg.theme('Sistema Academia')

              
                layout = [
                        [sg.Text('DECRICAO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key="-DESCRICAO-", font=('Helveltica', 12),  border_width=(0), pad=(20,5), background_color="#fff" , size=(20,1),do_not_clear=False)],
                        [sg.Text('ADESÃO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-ADESAO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('MENSALIDADE', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-MENSALIDADE-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('TX. MANUTENCÃO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-MANUTENCAO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Button('Salvar', key='salvar', pad=(10, 1)), sg.Button('Editar', key='-EDITAR-', pad=(10, 1)), sg.Button('Apagar', k='-APAGAR-')]
                
                ]
                       
                # , background_color="#e9e9e9"
                janela = sg.Window('Cadastro de Cliente', size=(960 ,340), margins=(150,70),default_element_size=(12, 1),layout=layout, background_color="#F2F5FA ", finalize=True)
                janela.set_min_size((800, 340))
               
        

                # janela['-CPF-'].Widget.configure(highlightbackground="#F2F5FA ",highlightthickness = 1)
                # janela['-NOME-'].Widget.configure(highlightbackground="#F2F5FA " , highlightthickness = 1)
                
                while True:
                        event, values = janela.Read() 
                        if event == sg.WINDOW_CLOSED or event == 'Sair':
                                break
                        
                        # if event == sg.WIN_MAXIMIZED:
                        #         window.maximize()

                                              
                        
                        if event ==  'salvar':
                                
                                descricao = values['-DESCRICAO-']
                                adesao = values['-ADESAO-']
                                mensalidade = values['-MENSALIDADE-']
                                manutencao = values['-MANUTENCAO-']
                                
                                self.plano.salvar(descricao, adesao, mensalidade, manutencao)
                                [sg.popup('Cadastrado com sucesso !', text_color="#04BEB3")]

                        # if event == '-APAGAR-':
                        #         cpf = values['-CPF-']
                        #         aluno = self.aluno.getCpf(cpf)
                        #         self.aluno.apagar(aluno.id)
                        #         janela['-DESCRICAO-'].Update('')
                        #         janela['-ADESAO-'].Update('') 
                        #         janela['-MENSALIADE-'].Update('')
                        #         janela['-MANUTENCAO-'].Update('')                          
                        #         [sg.popup('Deletado com sucesso !')]
                                
                
                # janela.Maximize()
                return janela
       
            

        


