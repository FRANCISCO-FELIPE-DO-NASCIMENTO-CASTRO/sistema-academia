from classes.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email,data_admissão):
        super().__init__(nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email)
        self.data_admissão = data_admissão

