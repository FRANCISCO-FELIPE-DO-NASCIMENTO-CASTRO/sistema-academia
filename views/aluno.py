from prettytable import PrettyTable
from models.aluno import Aluno

tabela_aluno = PrettyTable([
    "id",
    "Nome",
    "cpf"])
    # "sexo",
    # "cep",
    # "endereco",
    # "numero",
    # "complemento",
    # "cidade",
    # "estado",
    # "telefone",
    # "email"])

tabela_por_id = PrettyTable([
    "id",
    "Nome",
    "cpf"])


class AlunoView:
    def __init__(self):
        self.__models = Aluno()

    def matricular_aluno(self):
        pass
    
    def listar_alunos(self):
        print("Buscar todos alunos")       
        alunos = self.__models.listar()    
        for aluno in alunos:            
            tabela_aluno.add_row([aluno[0],aluno[1],aluno[2]])        
        print(tabela_aluno)

    def buscar_aluno(self, aluno_id):
        print("Buscar aluno por id")            
        alunos = self.__models.buscar(aluno_id)
        if alunos != None: 
            for aluno in alunos:                  
                tabela_por_id.add_row([aluno[0],aluno[1],aluno[2]])
            
            
            print(tabela_por_id)

        

    