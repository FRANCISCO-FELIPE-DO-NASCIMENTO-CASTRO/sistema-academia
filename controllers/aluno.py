
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

    def buscar_aluno_por_id(self, aluno_id):
        print("Controller ", type(aluno_id))
        self.view.buscar_aluno(aluno_id)

    # def atualizar(self, aluno):        
    #     self.model.atualizar(aluno)

    def deletar(self, id_aluno):        
        self.model.deletar(id_aluno)