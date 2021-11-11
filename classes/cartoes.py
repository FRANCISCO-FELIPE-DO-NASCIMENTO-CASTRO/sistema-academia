from bandeiras import Bandeiras
class Cartoes:
    def __init__(self, descricao):
       self.descricao = descricao
       self.bandeiras = Bandeiras()

from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email, matricula):
        super().__init__(nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email)
        self.matricula = matricula

class Especialidade:
    def __init__(self, especialidade):
        self.especialidade = especialidade

class Empresa:
    def __init__(self, cnpj, razao_social, fantasia, cep, rua, numero, casa, cidaade, estado):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.fantasia = fantasia
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.casa = casa
        self.cidade =  cidaade
        self.estado = estado

from classes.meios_de_pagamento import MeiosDePagamento


class Contrato:
    def __init__(self, numero, Cliente, Plano, Funcionario):
        self.numero = numero
        self.cliente = Cliente
        self.plano = Plano
        self.funcionario = Funcionario
        self.meio_pagamento = MeiosDePagamento

class Plano:
    def __init__(self, nome, descricao, preco) -> None:
        self.nome = nome 
        self.descricao = descricao
        self.preco = preco

class Bandeiras:
    def __init__(self, bandeira):
        self.bandeira = bandeira

from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email,data_admissão):
        super().__init__(nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email)
        self.data_admissão = data_admissão

class Pessoa:
    def __init__(self, nome, cpf, sexo, cep, endereco, numero, complemento, cidade, estado, telefone, email ):
        self.nome = nome
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

from especialidade import Especialidade

class Instrutor:
    def __init__(self) -> None:
        self.especialidade = Especialidade()

class MeiosDePagamento:
    def __init__(self, descricao):
        self.descricao = descricao