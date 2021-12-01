
from classes.aluno import Aluno
from classes.plano import Plano
from classes.especialidade import Especialidade
from classes.instrutor import Instrutor
from classes.matricula import Matricula
from controllers.aluno import Controller
from controllers.databasecontroller import DataBaseController
from models.banco_academia import DataBase






musculacao = Especialidade('Musculação')

instrutor = Instrutor('Paulo Cintura', '014.545.788-78', 2500)
instrutor.adicionar_especialidade(musculacao)

print(instrutor)



aluno = Aluno('Francisco Araujo', '017.514.894-78', 'F','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'francisco@hotmail.com', '11220')
aluno2 = Aluno('Isaac Nunes dos Santos', '017.514.894-78', 'F','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'francisco@hotmail.com', '12221')
aluno3 = Aluno('Maria Rosa', '017.514.894-78', 'F','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'francisco@hotmail.com', '1212121')

plano_smart = Plano('Plano Smart',
 'Treine o quanto quiser na sua unidade, sem taxa de cancelamento.',79.90)

matricula = Matricula(1)
# matricula.gerar_comprovante()

plano_smart.matricular_aluno(aluno)
plano_smart.matricular_aluno(aluno2)
plano_smart.matricular_aluno(aluno3)


print(plano_smart)








def main():
    banco = DataBaseController()
    controller = Controller()
    controller.adiciona_aluno(aluno)
    controller.adiciona_aluno(aluno2)
    controller.adiciona_aluno(aluno3)
    controller.listar_aluno()
    banco.criar_banco()
    banco.criar_tabelas()
    
 
    # databaseController.criar_tabelas
    
    
    # controller.criar_banco()
    # controller.adiciona_aluno(aluno)
    # controller.adiciona_aluno(aluno2)
    # controller.listar_clientes()

if __name__ == '__main__':
    main()
    
