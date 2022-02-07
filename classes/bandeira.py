from typing import Type
from classes.cartoes import Cartao
class Bandeira:
    def __init__(self, descricao):
        self.descricao = descricao
        self.cartoes = []


    def adicionaCartao(self, cartao: Type[Cartao]):
        self.cartoes.append(cartao)

    def listaCartao(self):
        for cartao in self.cartoes:
            print("Lista de Cartão: ", cartao.descricao)

    def __str__(self):
        return self.descricao
  