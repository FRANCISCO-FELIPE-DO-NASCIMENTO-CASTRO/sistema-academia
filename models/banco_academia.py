
import sqlite3
from sqlite3 import Error
import os

class DataBase:
    def tabela_aluno(self):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS aluno('\
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
            return sql
        except Error as e:
            print('Erro ao criar tabelas aluno', e)

    
    def tabela_usuario(self):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS usuario('\
                'id integer primary key autoincrement,'\
                'usuario varchar(50),'\
                'senha varchar (20),'\
                'email varchar (10))'            
            return sql
        except Error as e:
            print('Erro ao criar tabelas usuario', e)


    def tabela_empresa(self):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS empresa('\
                'id integer primary key autoincrement,'\
                'razao_social varchar(50),'\
                'fantasia varchar (50),'\
                'endereco varchar (50),'\
                'telefone varchar (50))'            
            return sql
        except Error as e:
            print('Erro ao criar tabelas usuario', e)
  
    def criar_banco(self):
        if not os.path.exists('./database/academia.db'):
            conn = None
            try:
                conn = sqlite3.connect('./database/academia.db')
                print("Banco criado com sucesso")
                return conn
            
            except Error as e:
                print("Erro ao criar banco de dados")
            
            return conn

    def criar_conexao(self):
        conn = None
        try:
            conn = sqlite3.connect('./database/academia.db')

        except sqlite3.Error as error:
            print('Erro ao criar a conexão com o banco: ', error)
    
        return conn

    def criar_tabela(self, conn, criar_tabela_sql):
        try:
            cursor = conn.cursor()
            cursor.execute(criar_tabela_sql)
            

        except Error as e:
            print("Erro ao criar tabelas")

        

    


        

        
        