from typing import Type


# Refinar a forma de pagamento


from classes.matricula import Matricula
class Pagamento:
    def __init__(self, matricula: Type[Matricula], dataPagamento, formaPagamento) -> None:
        self.matricula = matricula
        self.dataPagamento = dataPagamento
        self.formaPagemento = formaPagamento
        self.valor = matricula.valor_final()

    def efetuarPagamento(self):


    
