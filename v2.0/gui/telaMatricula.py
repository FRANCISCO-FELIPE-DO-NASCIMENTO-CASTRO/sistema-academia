
from unittest import result
import PySimpleGUI as sg
import sys
sys.path.append('..')
import models
from controllers.planoController import PlanoController
from controllers.alunoController import AlunoController
from controllers.matricularController import MatriculaController
from models.model import *

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

class TelaMatricula:
        def __init__(self) -> None:
            self.plano = PlanoController()
            self.aluno = AlunoController()
            self.matricula = MatriculaController()

        def tela(self):
                sg.theme('Sistema Academia')

                query = Plano.select()
    
                lista_tipos = []
                for i in query:            
                    lista_tipos.append(i.descricao)
                


                
                
                
              
                layout = [
                        [sg.Text('ALUNO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key="-ALUNO-", font=('Helveltica', 12),  border_width=(0), pad=(20,5), background_color="#fff" , size=(40,1)), sg.Button('Buscar', key="-BUSCAR-CPF-", border_width="0")],
                        [sg.Text('PLANO', size=(15,1), background_color="#fff", text_color="black"), sg.Listbox(values=lista_tipos, horizontal_scroll=False,  background_color="#fff", size=(15, 1), key='-LIST-TIPO-', enable_events=True)],
                        [sg.Button('Salvar', key='-SALVAR-', pad=(10, 1))]
                
                ]
                       
                # , background_color="#e9e9e9"
                janela = sg.Window('Matricula', size=(960 ,540), margins=(150,70),default_element_size=(12, 1),layout=layout, background_color="#F2F5FA ", finalize=True)
                janela.set_min_size((960 ,540))
               
        

                # janela['-CPF-'].Widget.configure(highlightbackground="#F2F5FA ",highlightthickness = 1)
                # janela['-NOME-'].Widget.configure(highlightbackground="#F2F5FA " , highlightthickness = 1)
                
                while True:
                        event, values = janela.Read() 
                        if event == sg.WINDOW_CLOSED or event == 'Sair':
                                break
                        
                        # if event == sg.WIN_MAXIMIZED:
                        #         window.maximize()
                        elif event == '-BUSCAR-CPF-':
                                cpf = values['-ALUNO-']
                                result = Aluno.select().where(Aluno.cpf == cpf).get()
                            
                                
                                if result:
                                        # janela['-CPF-'].Update(result.cpf)
                                        # janela['-NOME-'].Update(result.nome)

                                        janela['-ALUNO-'].update(result.nome)
                                                                          

                                else:
                                        [sg.popup('Usuario nao cadastrado')]
                        

                                              
                        
                        elif event ==  '-SALVAR-':
                                janela['-ALUNO-'].update(result.nome)
                                plano_descricao = values['-LIST-TIPO-'][0]
                                plano_id = Plano.select(Plano.id).where(Plano.descricao == plano_descricao)
                                aluno_id = result.id                    

                                self.matricula.efetuarMatricula(aluno_id, plano_id)
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
       
            

        


