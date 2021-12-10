
from models.modalidade import Modalidade
from views.aluno import AlunoView

class Controller:
    def __init__(self):
       
        self.model = Modalidade()
        self.view = AlunoView()  
        
    def adiciona_modalidade(self, modalidade):        
        self.model.salvar(modalidade)

    def listar_aluno(self):
        self.model.buscar()        
        self.view.listar_alunos()

    def buscar_modalidade_por_id(self, id_modalidade):
        print("Controller ", type(id_modalidade))
        self.view.buscar_aluno(id_modalidade)

    # def atualizar(self, aluno):        
    #     self.model.atualizar(aluno)

    def deletar(self, id_modalidade):        
        self.model.deletar(id_modalidade)