import peewee
db = peewee.SqliteDatabase('aluno.db')
class BaseModel(peewee.Model):
    class Meta:
        database = db

class aluno(BaseModel):
    nome=peewee.CharField()
    endereco=peewee.CharField()
    bairro=peewee.CharField()
    cep=peewee.CharField()
    cidade=peewee.CharField()
    estado=peewee.CharField()
    fone=peewee.CharField()
    celular=peewee.CharField()
    sexo=peewee.CharField()
    cpf=peewee.CharField()
    nascimento=peewee.CharField()
    email=peewee.CharField()
    estadoCivil=peewee.CharField()
    profissao=peewee.CharField()
    empresa=peewee.CharField()
    objetivo=peewee.CharField()
    debito=peewee.CharField()
    matriculado=peewee.CharField()

class usuario(BaseModel):
    usuario=peewee.CharField(unique=True)
    email=peewee.CharField(uniqui=True)
    senha=peewee.CharField()

if __name__ == '__main__':
    try:
        aluno.create_table()
        print("Tabela 'aluno' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'aluno' ja existe!")

    try:
        usuario.create_table()
        print("Tabela 'usuario' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'usuario' ja existe")

maria= usuario.create(usuario='1234',email='maria123@gmail.com', senha='256201')





