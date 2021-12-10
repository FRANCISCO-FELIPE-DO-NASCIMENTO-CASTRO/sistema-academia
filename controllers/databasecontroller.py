
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
        
        sql_create_Empresa = self.database.tabela_Empresa()
        self.database.criar_tabela(conn, sql_create_Empresa)

        sql_create_Modalidade = self.database.tabela_Modalidade()
        self.database.criar_tabela(conn, sql_create_Modalidade)

        sql_create_pagamento = self.database.tabela_Pagamento()
        self.database.criar_tabela(conn, sql_create_pagamento)

        sql_create_Antopometria = self.database.tabela_Antopometria()
        self.database.criar_tabela(conn, sql_create_Antopometria)        

        sql_create_DobraCultanea = self.database.tabela_DobraCultanea()
        self.database.criar_tabela(conn, sql_create_DobraCultanea)

        sql_create_Diametro = self.database.tabela_Diametro()
        self.database.criar_tabela(conn, sql_create_Diametro)

        sql_create_Circuferencia = self.database.tabela_Circuferencia()
        self.database.criar_tabela(conn, sql_create_Circuferencia)

        sql_create_AvaliacaoFisica = self.database.tabela_AvaliacaoFisica()
        self.database.criar_tabela(conn, sql_create_AvaliacaoFisica)

        sql_create_Frequencia = self.database.tabela_Frequencia()
        self.database.criar_tabela(conn, sql_create_Frequencia)

        sql_create_Aluno = self.database.tabela_Aluno()
        self.database.criar_tabela(conn, sql_create_Aluno)

        sql_create_Funcao = self.database.tabela_Funcao()
        self.database.criar_tabela(conn, sql_create_Funcao)

        sql_create_Funcionario = self.database.tabela_Funcionario()
        self.database.criar_tabela(conn, sql_create_Funcionario)

        sql_create_FichaTreino = self.database.tabela_FichaTreino()
        self.database.criar_tabela(conn, sql_create_FichaTreino)

        sql_create_Matricula = self.database.tabela_Matricula()
        self.database.criar_tabela(conn, sql_create_Matricula)

        


        









        
         
    