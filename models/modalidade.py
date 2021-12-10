

import sqlite3
from sqlite3.dbapi2 import Cursor, Error
from models.banco_academia import DataBase

class Modalidade:
    def __init__(self) -> None:
        self.database = DataBase()    
         
    # sentenca sql para inserir registros
    def salvar(self, modalidade):        
        conn = self.database.criar_conexao()
        cursor = conn.cursor()       
        sql = 'insert into Modalidade (descricao, valor) values (?,?)'
        registros = [(   
                modalidade.descricao,
                modalidade.valor                                       
                )]
       
        for reg in registros:
            cursor.execute(sql,reg)        
        conn.commit()
        print(f"Modalidade: {modalidade.descricao} salvo com sucesso !" )
        cursor.close()
        conn.close()

    def listar(self):
        conn = self.database.criar_conexao()
        cursor = conn.cursor()
        cursor.execute('select * from Modalidade')
        linhas = cursor.fetchall()
        # for linha in linhas:
        #     return linha
        return linhas

    def buscar(self, modalidade):
        conn = None        
        try:
            conn = self.database.criar_conexao()
            cursor = conn.cursor()        
            sql = ("select * from Modalidade where id=?")        
            cursor.execute(sql,(modalidade,))        
            linhas = cursor.fetchall()
            cursor.close()
            conn.close()
            # for linha in linhas:
            #     return linha
            return linhas
        except Error as e:
            return conn
            print("Erro ao buscar por id")

    def atualizar(self, modalidade):
        conn = self.database.criar_conexao()
        sql = 'update Modalidade \
                set descricao = ?,\
                valor = ? where id = ?'

        cursor = conn.cursor()
        cursor.execute(sql, modalidade)
        conn.commit()
        cursor.close()
        conn.close()


    def deletar(self, id_modalidade):        
        conn = self.database.criar_conexao()        
        sql = ('delete from Modalidade where id=?')
        cursor = conn.cursor()
        cursor.execute(sql, (id_modalidade,))
        conn.commit()
        cursor.close()
        conn.close()
            
        




    