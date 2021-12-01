
from models.aluno import Aluno
from views.aluno import AlunoView

class Controller:
    def __init__(self):
       
        self.model = Aluno()
        self.view = AlunoView()
    
  
        
    def adiciona_aluno(self, aluno):        
        self.model.salvar(aluno)

    def listar_aluno(self):        
        self.view.listar_alunos()

    def atualizar(self, aluno):        
        self.model.salvar(aluno)

    def deletar(self, aluno):        
        self.model.salvar(aluno)