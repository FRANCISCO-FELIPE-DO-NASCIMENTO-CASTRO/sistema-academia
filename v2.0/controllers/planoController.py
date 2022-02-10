import sys
sys.path.append('..')
import models
from models.model import Plano


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

    
    def listaDePlanos():
        planos = Plano.select().get()
        print(type(planos))
        return planos

        
        