
from mmap import ALLOCATIONGRANULARITY
from re import A

from peewee import Select
from model import Aluno, Matricula, Plano

for x in Aluno.select().where(Aluno.nome == "Elicarlos Ferreira"):
    print(x.cpf)

for x in Aluno.select().where(Aluno.id == 9):
    print(x.nome, x.cpf)


print(type(Aluno.select().where(Aluno.id == 9).get()))
print(dir(Aluno.select().where(Aluno.id == 9).get()))
print(Aluno.select().where(Aluno.id == 9).get())

pessoa = Aluno.select().where(Aluno.id == 9).get()
print('Aluno:', pessoa.nome)

p = Aluno.select(Aluno.cidade).where(Aluno.id == 9).get()
print(p)


# Join
matriculas = Aluno.select().join(Matricula).where(Matricula.id == 1).get()
print("Matricula:",matriculas)

# Matricula.create(
#     aluno = Aluno.select().where(Aluno.id==2),
#     plano = Plano.select().where(Plano.id == 1)
# )
    
a = Aluno.delete().where(Aluno.id == 8)
a.execute()

print("Matricula:", Matricula.select().get())
print("Aluno: ", Matricula.select().get().aluno)
print("Aluno: ", Matricula.select().get().aluno.nome)

paulo = Aluno.select().where(Aluno.nome != "Paulo")
for row in paulo:
    print(row.nome)