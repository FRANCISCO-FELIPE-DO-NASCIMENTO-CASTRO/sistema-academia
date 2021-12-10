
from os import curdir
import sqlite3
from sqlite3.dbapi2 import Cursor, Error
from models.banco_academia import DataBase

class Aluno:
    def __init__(self) -> None:
        self.database = DataBase()    
    # CREATE TABLE Aluno (
    # id INT  NOT NULL PRIMARY KEY,
    # nome VARCHAR(50) NOT NULL,
    # endereco VARCHAR(50) NOT NULL,
    # bairro VARCHAR(50) NOT NULL,
    # cep VARCHAR(50) NOT NULL,
    # cidade VARCHAR(50) NOT NULL,
    # estado VARCHAR(50) NOT NULL,
    # fone VARCHAR(50) NOT NULL,
    # celular VARCHAR(50) NOT NULL,
    # sexo CHAR(1) NOT NULL,
    # cpf VARCHAR(45) NOT NULL,
    # nascimento DATE NOT NULL,
    # email VARCHAR(50) NOT NULL,
    # estadoCivil VARCHAR(45) NOT NULL,
    # profissao VARCHAR(50) NOT NULL,
    # empresa VARCHAR(50) NOT NULL,
    # objetivo VARCHAR(50),
    # debito DOUBLE NOT NULL,
    # matriculado BOOLEAN NOT NULL);

    # sentenca sql para inserir registros
    def salvar(self, aluno):        
        conn = self.database.criar_conexao()
        cursor = conn.cursor()       
        sql = 'insert into aluno (nome, endereco,bairro, cep,\
                cidade, estado, fone, celular, sexo, cpf,\
                nascimento, email, estadoCivil, profissao,\
                empresa, objetivo, debito, matriculado)\
                values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        registros = [
            (   aluno.nome,
                aluno.endereco,
                aluno.bairro,
                aluno.cep,
                aluno.cidade,
                aluno.estado,
                aluno.fone,
                aluno.celular,
                aluno.sexo,
                aluno.cpf,
                aluno.nascimento,
                aluno.email,
                aluno.estadoCivil,
                aluno.profissao,
                aluno.empresa,
                aluno.objetivo,
                aluno.debito,
                aluno.matriculado          
               
                )]
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
            
        




    