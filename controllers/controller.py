
from models.aluno import Aluno
from models.modalidade import Modalidade
from views.aluno import AlunoView

class Controller:
    def __init__(self):
       
        self.aluno = Aluno()
        self.modalidade =  Modalidade()
        self.view = AlunoView()  
        
    def adiciona_aluno(self, aluno):        
        self.aluno.salvar(aluno)

    def listar_aluno(self):
        self.aluno.buscar()        
        self.view.listar_alunos()

    def buscar_aluno_por_id(self, aluno_id):
        print("Controller ", type(aluno_id))
        self.view.buscar_aluno(aluno_id)

    # def atualizar(self, aluno):        
    #     self.model.atualizar(aluno)

    def deletar(self, id_aluno):        
        self.aluno.deletar(id_aluno)


    ############################
            # modadelidade

    def adiciona_modalidade(self, modalidade):        
        self.modalidade.salvar(modalidade)

    def listar_aluno(self):
        self.modalidade.buscar()        
        self.view.listar_alunos()

    def buscar_modalidade_por_id(self, id_modalidade):
        print("Controller ", type(id_modalidade))
        self.view.buscar_aluno(id_modalidade)

    # def atualizar(self, aluno):        
    #     self.model.atualizar(aluno)

    def deletar(self, id_modalidade):        
        self.modalidade.deletar(id_modalidade)