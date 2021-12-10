
from classes.aluno import Aluno
from classes.plano import Plano
from classes.modalidade import Modalidade
from classes.especialidade import Especialidade
from classes.instrutor import Instrutor
from classes.matricula import Matricula
from controllers.controller import Controller
from controllers.databasecontroller import DataBaseController
from models.banco_academia import DataBase


# musculacao = Especialidade('Musculação')

# instrutor = Instrutor('Paulo Cintura', '014.545.788-78', 2500)
# instrutor.adicionar_especialidade(musculacao)

# print(instrutor)

modalidade = Modalidade('Musculação', 500.00)

modalidade2 = Modalidade('CrossFit', 500.00)

aluno = Aluno('Francisco dos Anzois', 'Q C', 'Vila Maria', '64060-115','Teresina','Piaui', '869998444', '86 9880045474','M', '01761432389', '11-03-1985','fra@hotmail.com','casado','estudante', 'Solution', 'Emagrecer', 0.0, False)
# aluno2 = Aluno('Isaac Nunes dos Santos', '016.514.000-99', 'M','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'isaac@hotmail.com', '12221')
# aluno3 = Aluno('Maria Rosa', '017.514.894-78', 'F','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'francisco@hotmail.com', '1212121')

plano_smart = Plano('Plano Smart',
 'Treine o quanto quiser na sua unidade, sem taxa de cancelamento.',79.90)

matricula = Matricula(1)
# matricula.gerar_comprovante()

plano_smart.matricular_aluno(aluno)
# plano_smart.matricular_aluno(aluno2)
# plano_smart.matricular_aluno(aluno3)


print(plano_smart)


def main():
    banco = DataBaseController()
    banco.criar_banco()
    banco.criar_tabelas()
    controller = Controller()
    controller.adiciona_modalidade(modalidade)
    controller.adiciona_modalidade(modalidade2)

    controller.adiciona_aluno(aluno)
    # controller.adiciona_aluno(aluno2)
    # controller.adiciona_aluno(aluno3)
    # controller.deletar(1)
    # controller.buscar_aluno_por_id(10)
    # controller.listar_aluno()    

if __name__ == '__main__':
    main()
    
