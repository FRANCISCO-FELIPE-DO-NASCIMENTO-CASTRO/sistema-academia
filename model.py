
from peewee import *
import datetime


db = SqliteDatabase('banco_peewee/academia.db')

class BaseModel(Model):
    class Meta:
        database = db

class Plano(BaseModel):
    descricao = CharField()
    adesao = FloatField()
    complemento = CharField()
    bairro = CharField()
    estado = CharField()
    cidade = CharField()
    debito = FloatField(default=0.0)

    class Meta:
        table_name = 'aluno'

class Plano(BaseModel):
    descricao = CharField()
    adesao = FloatField()
    mensalidade = FloatField()
    taxaManutencao = FloatField()

class Matricula(BaseModel):
    aluno = ForeignKeyField(Aluno)
    plano = ForeignKeyField(Plano)
    criado_em = DateTimeField(default=datetime.datetime.now()) 

   
db.connect()
db.create_tables([Plano,Aluno, Matricula])