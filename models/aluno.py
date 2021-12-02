
from os import curdir
import sqlite3
from sqlite3.dbapi2 import Cursor, Error
from models.banco_academia import DataBase

class Aluno:
    def __init__(self) -> None:
        self.database = DataBase()    
    # # senteca sql para criar tabela    
    # def criar_tabela(self):
    #     conn = conexao.criar_conexao()
    #     cursor = conn.cursor()
    #     sql = 'create table aluno('\
    #     'id integer primary key autoincrement,'\
    #     'nome varchar(50),'\
    #     'cpf varchar (20),'\
    #     'sexo varchar (10),'\
    #     'cep varchar (10),'\
    #     'endereco varchar (50),'\
    #     'numero varchar (10),'\
    #     'complemento varchar (50),'\
    #     'cidade varchar (30),'\
    #     'estado varchar (30),'\
    #     'telefone varchar (30),'\
    #     'email varchar (50))'
    #     cursor.execute(sql)
    #     cursor.close()
    #     conn.close()
    #     print('Tabela Aluno criada com sucesso')

    # sentenca sql para inserir registros
    def salvar(self, aluno):        
        conn = self.database.criar_conexao()
        cursor = conn.cursor()       
        sql = 'insert into aluno (nome,cpf,sexo,cep,endereco,numero,complemento,cidade,estado,telefone,email) values (?,?,?,?,?,?,?,?,?,?,?)'
        registros = [(aluno.nome, aluno.cpf, aluno.sexo, aluno.cep ,aluno.endereco, aluno.numero, aluno.complemento, aluno.cidade, aluno.estado, aluno.telefone, aluno.email)]
        # registros = [('Maria', '01425802547', 'F', '64055650', 'rua 100', '2438', 'proximo a praca', 'timon', 'Maranhao', '89988273443', 'maria123@gmail.com'),('Joao', '01425802547', 'M', '64554050', 'rua 54', '2883', 'proximo ao colegio', 'Teresina', 'Piaui', '895648122', 'joao123@gmail.com')]
        for reg in registros:
            cursor.execute(sql,reg)        
        conn.commit()
        print(f"Aluno: {aluno.nome} salvo com sucesso !" )
        cursor.close()
        conn.close()

    def listar(self):
        conn = self.database.criar_conexao()
        cursor = conn.cursor()
        cursor.execute('select * from aluno')
        linhas = cursor.fetchall()
        # for linha in linhas:
        #     return linha
        return linhas

    def buscar(self, aluno):
        conn = None        
        try:
            conn = self.database.criar_conexao()
            cursor = conn.cursor()        
            sql = ("select * from aluno where id=?")        
            cursor.execute(sql,(aluno,))        
            linhas = cursor.fetchall()
            cursor.close()
            conn.close()
            # for linha in linhas:
            #     return linha
            return linhas
        except Error as e:
            return conn
            print("Erro ao buscar por id")
        
        

    def atualizar(self, aluno):
        conn = self.database.criar_conexao()
        sql = 'update aluno \
                set nome = ?,\
                cpf = ?,\
                sexo = ?,\
                cep = ?,\
                endereco = ?,\
                numero = ?,\
                complemento = ?,\
                cidade = ?,\
                estado = ?,\
                telefone = ?,\
                email = ? where id = ?'
        cursor = conn.cursor()
        cursor.execute(sql, aluno)
        conn.commit()
        cursor.close()
        conn.close()


    def deletar(self, id_aluno):        
        conn = self.database.criar_conexao()        
        sql = ('delete from aluno where id=?')
        cursor = conn.cursor()
        cursor.execute(sql, (id_aluno,))
        conn.commit()
        cursor.close()
        conn.close()
            
        




    