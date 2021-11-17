from classes.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email, matricula):
        super().__init__(nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email)
        self.matricula = matricula

    def __str__(self) -> str:
        return super().__str__()
        

    
    