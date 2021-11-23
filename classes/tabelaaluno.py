import sqlite3
conexão = sqlite3.connect("aluno.db")
cursor = conexão.cursor()
# senteça sql para criar tabela
sql = 'create table aluno('\
      'id integer primary key autoincrement,'\
      'nome varchar(50),'\
      'cpf varchar (20),'\
      'sexo varchar (10),'\
      'cep varchar (10),'\
      'endereço varchar (50),'\
      'numero varchar (10),'\
      'complemento varchar (50),'\
      'cidade varchar (30),'\
      'estado varchar (30),'\
      'telefone varchar (30),'\
      'email varchar (50),'\

cursor.execute(sql)
# sentença sql para inserir registros
sql = 'insert into aluno (nome,cpf,sexo,cep,endereço,numero,complemento,cidade,estado,telefone,email) values (?,?)'
registros = [('Maria', '01425802547', 'F', '64055650', 'rua 100', '2438', 'proximo à praça', 'timon', 'Maranhão', '89988273443', 'maria123@gmail.com'),('João', '01425802547', 'M', '64554050', 'rua 54', '2883', 'proximo ao colégio', 'Teresina', 'Piauí', '895648122', 'joao123@gmail.com')]
for reg in registros:
    cursor.execute(sql,reg)

# gravação no banco de dados. sem commit os dados não são gravados.
conexão.commit()

cursor.close()
conexão.close()