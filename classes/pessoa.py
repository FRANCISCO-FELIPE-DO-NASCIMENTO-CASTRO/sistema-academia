class Pessoa:
    def __init__(self, nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email ):
        self.__nome = nome
        self.__cpf = cpf,
        self.__sexo = sexo
        self.__cep = cep
        self.__endereco = endereco 
        self.__numero = numero 
        self.__complemento = complemento 
        self.__cidade = cidade
        self.__estado = estado
        self.__telefone = telefone 
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    def __str__(self) -> str:
        return self.nome