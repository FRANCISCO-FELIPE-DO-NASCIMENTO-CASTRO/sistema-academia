

from copy import Error
from re import A
from model import Aluno


class AlunoView:
    def getCpf(self, cpf):
        aluno = Aluno.get_or_none(Aluno.cpf==cpf)
        if aluno != None:            
            return aluno

        else:
            print('Aluno não cadastrado')
            return False 

    def getId(self, id):
        aluno = Aluno.get(Aluno.id == id)
        if aluno.id > 0:
            print(aluno.id)

