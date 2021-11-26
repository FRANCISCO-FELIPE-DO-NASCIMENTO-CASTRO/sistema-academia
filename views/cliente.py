from models.aluno import Model


class View:
    def __init__(self):
        self.__models = Model()
    
    def lista_cliente(self):
        alunos = self.__models.listar()
        for aluno in alunos:
            print(f'Aluno: {aluno}')       
        


