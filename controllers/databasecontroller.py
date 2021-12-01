
from views.database import DataBaseView
from models.banco_academia import DataBase

class DataBaseController:
    def __init__(self):
        self.database = DataBase()
        self.view = DataBaseView() 
        

    def criar_banco(self):        
        self.database.criar_banco()

    def criar_tabelas(self):        
        conn = self.database.criar_conexao()
        
        sql_create_aluno = self.database.tabela_aluno()
        self.database.criar_tabela(conn, sql_create_aluno)

        sql_create_usuario = self.database.tabela_usuario()
        self.database.criar_tabela(conn, sql_create_usuario)

        sql_create_empresa = self.database.tabela_empresa()
        self.database.criar_tabela(conn, sql_create_empresa)
    
    
    