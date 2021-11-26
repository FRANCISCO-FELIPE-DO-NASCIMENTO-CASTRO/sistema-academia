

from sqlite3.dbapi2 import register_adapter


class Aluno:
    def __init__(self, nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email, matricula):
        self.__nome = nome
        self.__cpf = cpf
        self.__sexo = sexo
        self.__cep = cep
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__cidade = cidade
        self.__estado = estado
        self.__telefone = telefone
        self.__email = email
        self.__matricula = matricula


    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def sexo(self):
        return self.__sexo

    @property
    def cep(self):
        return self.__cep

    @property
    def endereco(self):
        return self.__endereco

    @property
    def numero(self):
        return self.__numero
    @property
    def complemento(self):
        return self.__complemento

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email
        
    @property
    def matricula(self):
        return self.__matricula
        
    def __str__(self) -> str:
        return self.__nome
        

    
    