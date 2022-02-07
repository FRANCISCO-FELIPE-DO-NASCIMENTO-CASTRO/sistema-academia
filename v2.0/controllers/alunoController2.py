
from msilib.schema import Error
import sys
sys.path.append('..')
import models

from models.model import Aluno

class AlunoController:
    def __init__(self):
        self.alunoModel = Aluno

    def salvarAluno(self, aluno):
        try:    
            self.alunoModel.create(aluno.nome, aluno.cpf, aluno.endereco, aluno.bairro, aluno.estado, aluno.cidade)
            print("Aluno salvo com sucesso")
            return True
        except Error as e:
            print("Erro ao salvar aluno", e)