from models.aluno import Model
from views.cliente import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def criar_banco(self):
        self.model.criar_tabela_aluno()
        
    def adiciona_aluno(self, aluno):        
        self.model.salvar(aluno)

    def listar(self, aluno):        
        self.model.salvar(aluno)

    def atualizar(self, aluno):        
        self.model.salvar(aluno)

    def deletar(self, aluno):        
        self.model.salvar(aluno)