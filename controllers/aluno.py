
from models.aluno import Aluno
from views.aluno import AlunoView

class Controller:
    def __init__(self):
       
        self.model = Aluno()
        self.view = AlunoView()
    
    def criar_banco(self):
        pass

         
        
    def adiciona_aluno(self, aluno):        
        self.model.salvar(aluno)

    def listar_clientes(self):        
        self.view.lista_cliente()

    def atualizar(self, aluno):        
        self.model.salvar(aluno)

    def deletar(self, aluno):        
        self.model.salvar(aluno)