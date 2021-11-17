
from classes.aluno import Aluno
from classes.plano import Plano
from classes.especialidade import Especialidade
from classes.instrutor import Instrutor

musculacao = Especialidade('Musculação')

instrutor = Instrutor('Paulo Cintura', '014.545.788-78', 2500)
instrutor.adicionar_especialidade(musculacao)

print(instrutor)



aluno = Aluno('Francisco Araujo', '017.514.894-78', 'F','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'francisco@hotmail.com', '1212121')
aluno2 = Aluno('Rogerio Sousa', '017.514.894-78', 'F','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'francisco@hotmail.com', '1212121')
aluno3 = Aluno('Maria Rosa', '017.514.894-78', 'F','64060-115', 'Q C', '50',' Vila Maria', 'Teresina', 'Piaui', '86-98841-7874', 'francisco@hotmail.com', '1212121')

plano_smart = Plano('Plano Smart',
 'Treine o quanto quiser na sua unidade, sem taxa de cancelamento.',79.90)

plano_smart.matricular_aluno(aluno)
plano_smart.matricular_aluno(aluno2)
plano_smart.matricular_aluno(aluno3)


print(plano_smart)