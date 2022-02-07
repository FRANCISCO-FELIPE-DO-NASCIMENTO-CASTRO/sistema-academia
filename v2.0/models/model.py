
import datetime
import sys
sys.path.append("..")
import banco
from peewee import *
db = SqliteDatabase('banco/academia.db')

class BaseModel(Model):
    class Meta:
        database = db

class Aluno(BaseModel):    
    cpf = CharField(max_length=15)
    nome = CharField(max_length=50)
    email = CharField(null=True)
    data_nascimento = DateField(null=True)
    sexo = CharField(null=True)
    telefone = CharField(null=True)
    cep = CharField(null=True)
    endereco = CharField(null=True)
    numero = CharField(null=True)
    complemento = CharField(null=True)
    bairro = CharField(null=True)
    estado = CharField(null=True)
    cidade = CharField(null=True)
    debito = CharField(default=0.0)
    status = BooleanField(default=True)

class Plano(BaseModel):
    descricao = CharField(max_length=50)
    taxa_adesao = FloatField(default=0.0)
    mensalidade = FloatField()
    taxaManutencao = FloatField(default=0.0)


class Matricula(BaseModel):
    matricula = AutoField()
    aluno = ForeignKeyField(Aluno, backref='alunos')
    plano = ForeignKeyField(Plano, backref='planos')
    data_matricula = DateField(datetime.datetime.now())
    IntegerField
    


db.connect()
db.create_tables([Aluno, Plano, Matricula])

