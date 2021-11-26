
from conexao import criar_conexao
conn = criar_conexao()

cursor = conn.cursor()
# senteca sql para criar tabela
sql = 'create table aluno('\
      'id integer primary key autoincrement,'\
      'nome varchar(50),'\
      'cpf varchar (20),'\
      'sexo varchar (10),'\
      'cep varchar (10),'\
      'endereco varchar (50),'\
      'numero varchar (10),'\
      'complemento varchar (50),'\
      'cidade varchar (30),'\
      'estado varchar (30),'\
      'telefone varchar (30),'\
      'email varchar (50))'

cursor.execute(sql)
# sentenca sql para inserir registros
sql = 'insert into aluno (nome,cpf,sexo,cep,endereco,numero,complemento,cidade,estado,telefone,email) values (?,?,?,?,?,?,?,?,?,?,?)'
registros = [('Maria', '01425802547', 'F', '64055650', 'rua 100', '2438', 'proximo a praca', 'timon', 'Maranhao', '89988273443', 'maria123@gmail.com'),('Joao', '01425802547', 'M', '64554050', 'rua 54', '2883', 'proximo ao colegio', 'Teresina', 'Piaui', '895648122', 'joao123@gmail.com')]
for reg in registros:
    cursor.execute(sql,reg)

# gravacao no banco de dados. sem commit os dados nao sao gravados.
conn.commit()

cursor.close()
conn.close()