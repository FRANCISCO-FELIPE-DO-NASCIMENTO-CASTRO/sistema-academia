class Pessoa:
    def __init__(self, nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email ):
        self.__nome = nome
        self.cpf = cpf,
        self.sexo = sexo
        self.cep = cep
        self.endereco = endereco 
        self.numero = numero 
        self.complemento = complemento 
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone 
        self.email = email

    @property
    def nome(self):
        return self.__nome

    def __str__(self) -> str:
        return self.nome