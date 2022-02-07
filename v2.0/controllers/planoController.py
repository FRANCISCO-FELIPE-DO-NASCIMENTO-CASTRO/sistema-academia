from PySimpleGUI.PySimpleGUI import Pane
from model import Plano
class PlanoController:
    def __init__(self):
        self.plano = Plano()
    def salvar(self, descricao, adesao, mensalidade, manuntencao):
        self.plano.create(
            descricao=descricao,
            adesao=adesao,
            mensalidade = mensalidade,
            taxaManutencao = manuntencao
        )
        print('Salvo com sucesso')

        
        