from models.aluno import Aluno


class AlunoView:
    def __init__(self):
        self.__models = Aluno()

    def matricular_aluno(self):
        pass
    
    def listar_alunos(self):
        alunos = self.__models.listar()
        for aluno in alunos:
            print(f'Aluno: {aluno}')       
        


