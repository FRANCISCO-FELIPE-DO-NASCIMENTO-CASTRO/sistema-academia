
from datetime import datetime
import sys
sys.path.append('..')
import models, views

from models.model import Matricula, Aluno, Plano


class MatriculaController:
    def __init__(self) -> None:
        self.matricula = Matricula()
        
        

    def criar(self, cpf, nome, email, nascimento, sexo, telefone, cep, endereco, numero, complemento, bairro, estado, cidade):  
        
        try:
            self.aluno.create(
            cpf=cpf,
            nome = nome, 
            email = email,
            data_nascimento = nascimento,
            sexo = sexo,
            telefone = telefone,
            cep = cep,
            endereco = endereco,
            numero = numero,
            complemento = complemento,
            bairro = bairro,
            estado = estado,
            cidade = cidade             
            )   
            
            return 'Salvo com sucesso'

        except Exception as e:
            return f'Erro ao salvar aluno {e}'

    def efetuarMatricula(self, aluno_id, plano_id):
        Matricula.create(
            aluno = aluno_id,
            plano = plano_id,
            data_matricula = datetime.now()
        )

    def getCpf(self, cpf):        
        return self.view.getCpf(cpf)

    def listar(self):
        return self.view.listaAlunos()

    # def atualizar(self, cpf):
    #     self.aluno = getCpf(cpf)

    def listaAlunos(self):
        alunos = []
        aluno = Aluno.select()
        for a in aluno:
            alunos.append([a.id, a.nome])
        
        return alunos
        # print(aluno)
        # print('Ola')
        # lista_alunos = []
        # aluno = Aluno.select().get()
        # print(type(aluno))
        # print(aluno)
        # # for a in aluno:
        # #     lista_alunos.append(a)

        # # return lista_alunos

    def apagar(self, id):
        aluno = Aluno.get(Aluno.id == id)
        if aluno.id > 0:
            aluno.delete_instance()
            print("Deletado com sucesso")  
        


    def getId(self, id):
        return self.view.getId(id)


