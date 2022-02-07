from classes.aluno import Aluno
from classes.plano import Plano

class Mensalidade:
    def __init__(self, titular, numero, vencimento, valor) -> None:
        self.titular = titular
        self.numero = numero
        self.vencimento = vencimento
        self.valor = valor
        self.status = ""
        
    def adicionaTitular(self,aluno):
        self.aluno.append(aluno)
    
    def statusPendente(self):
        self.status = "Pendente"

    def dadosMensalidade(self):
        return  f"Titular: {self.titular} Parcela N: {self.numero} Vencimento: {self.vencimento} Valor: {self.valor} Status: {self.status}"

   

    

        