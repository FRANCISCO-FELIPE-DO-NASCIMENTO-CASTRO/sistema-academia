from classes.meios_de_pagamento import MeiosDePagamento


class Contrato:
    def __init__(self, numero, Cliente, Plano, Funcionario):
        self.numero = numero
        self.cliente = Cliente
        self.plano = Plano
        self.funcionario = Funcionario
        self.meio_pagamento = MeiosDePagamento