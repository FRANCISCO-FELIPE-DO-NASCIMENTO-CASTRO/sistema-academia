from ctypes.wintypes import SIZE
import PySimpleGUI as sg
import sys
sys.path.append('..')
import controllers


from controllers.alunoController import AlunoController

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

class TelaAluno:
        def __init__(self) -> None:
            self.aluno = AlunoController()

        def janela_aluno(self):
                sg.theme('Sistema Academia')

               
                layout = [
                        [sg.Text('CPF', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key="-CPF-", font=('Helveltica', 12),  border_width=(0), pad=(20,5), background_color="#fff" , size=(20,1),do_not_clear=False), sg.Button('Buscar', key="-BUSCAR-CPF-", border_width="0")],
                        [sg.Text('NOME', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-NOME-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('EMAIL', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-EMAIL-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('DATA NASCIMENTO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-NASCIMENTO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('SEXO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-SEXO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('TELEFONE', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-TELEFONE-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('CEP', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-CEP-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('ENDERECO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-ENDERECO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('NUMERO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-NUMERO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('COMPLEMENTO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-COMPLEMENTO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('BAIRRO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-BAIRRO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('ESTADO', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-ESTADO-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                        [sg.Text('CIDADE', size=(15,1), background_color="#fff", text_color="black"), sg.Input(key='-CIDADE-',  border_width=(0) , pad=(10,5), background_color="#fff" , size=(50,50),do_not_clear=False)],
                
                        [sg.Button('Salvar', key='salvar', pad=(10, 1)), sg.Button('Editar', key='-EDITAR-', pad=(10, 1)), sg.Button('Apagar', k='-APAGAR-')]
                
                ]
                       
                # , background_color="#e9e9e9"
                janela = sg.Window('Cadastro de Cliente', size=(960 ,540), margins=(150,70),default_element_size=(12, 1),layout=layout, background_color="#F2F5FA ", finalize=True)
                janela.set_min_size((960, 540))
               
        

                # janela['-CPF-'].Widget.configure(highlightbackground="#F2F5FA ",highlightthickness = 1)
                # janela['-NOME-'].Widget.configure(highlightbackground="#F2F5FA " , highlightthickness = 1)
                
                while True:
                        event, values = janela.Read() 
                        if event == sg.WINDOW_CLOSED or event == 'Sair':
                                break
                        
                        # if event == sg.WIN_MAXIMIZED:
                        #         window.maximize()

                        elif event == '-BUSCAR-CPF-':
                                cpf = values['-CPF-']
                                aluno = AlunoController()
                                result = aluno.getCpf(cpf)

                                if result:
                                        # janela['-CPF-'].Update(result.cpf)
                                        # janela['-NOME-'].Update(result.nome)

                                        janela['-CPF-'].Update(result.cpf)
                                        janela['-NOME-'].Update(result.nome) 
                                        janela['-EMAIL-'].Update(result.email)
                                        janela['-NASCIMENTO-'].Update(result.data_nascimento)
                                        janela['-SEXO-'].Update(result.sexo)
                                        janela['-TELEFONE-'].Update(result.telefone)
                                        janela['-CEP-'].Update(result.cep)
                                        janela['-ENDERECO-'].Update(result.endereco)
                                        janela['-NUMERO-'].Update(result.numero)
                                        janela['-COMPLEMENTO-'].Update(result.complemento)
                                        janela['-BAIRRO-'].Update(result.bairro)
                                        janela['-ESTADO-'].Update(result.estado)
                                        janela['-CIDADE-'].Update(result.cidade)
                                        

                                else:
                                        [sg.popup('Usuario nao cadastrado')]
                        
                        if event ==  'salvar':
                                self.aluno = AlunoController()
                                cpf = values['-CPF-']
                                nome = values['-NOME-']
                                email = values['-EMAIL-']
                                nascimento = values['-NASCIMENTO-']
                                sexo = values['-SEXO-']
                                telefone = values['-TELEFONE-']
                                cep = values['-CEP-']
                                endereco = values['-ENDERECO-']
                                numero = values['-NUMERO-']
                                complemento = values['-COMPLEMENTO-']
                                bairro = values['-BAIRRO-']
                                estado = values['-ESTADO-']
                                cidade = values['-CIDADE-']
                                self.aluno.criar(cpf, nome, email, nascimento, sexo, telefone, cep, endereco, numero, complemento, bairro, estado, cidade )
                                [sg.popup('Cadastrado com sucesso !', text_color="#04BEB3")]

                        if event == '-APAGAR-':
                                cpf = values['-CPF-']
                                aluno = self.aluno.getCpf(cpf)
                                self.aluno.apagar(aluno.id)
                                janela['-CPF-'].Update('')
                                janela['-NOME-'].Update('') 
                                janela['-EMAIL-'].Update('')
                                janela['-NASCIMENTO-'].Update('')
                                janela['-SEXO-'].Update('')
                                janela['-TELEFONE-'].Update('')
                                janela['-CEP-'].Update('')
                                janela['-ENDERECO-'].Update('')
                                janela['-NUMERO-'].Update('')
                                janela['-COMPLEMENTO-'].Update('')
                                janela['-BAIRRO-'].Update('')
                                janela['-ESTADO-'].Update('')
                                janela['-CIDADE-'].Update('')
                                [sg.popup('Deletado com sucesso !')]
                                
                
                # janela.Maximize()
                return janela
       
            
        # controller = AlunoController()
        # print(controller.getCpf('0761432389'))

        # janela1, janela2 = janela_aluno(), None
        # while True:
        #         window, event, values = sg.read_all_windows()
        #         cpf = values['cpf']
        #         nome = values['nome']

                
        #         controller.criar(cpf, nome) 
        #         print(values)

        #         if window == janela1 and event == sg.WIN_CLOSED:
        #                 break 
                
        #         # if window == janela1 and event == 'salvar':
        #         #     janela2 = sucesso()
                        
        #         # if window == janela2 and event =='ok':
        #         #     janela2.hide()
        #         #     janela1.un_hide()

        


