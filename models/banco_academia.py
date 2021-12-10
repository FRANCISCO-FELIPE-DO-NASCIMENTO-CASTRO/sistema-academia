
import sqlite3
from sqlite3 import Error
import os

class DataBase:

    def tabela_Empresa(self):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS Empresa('\
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                'razao_social varchar(50),'\
                'fantasia varchar (50),'\
                'endereco varchar (50),'\
                'telefone varchar (50))'            
            return sql
        except Error as e:
            print('Erro ao criar tabelas usuario', e)

    def tabela_Modalidade(self):
        try:
            sql =   'CREATE TABLE if not exists Modalidade('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'descricao VARCHAR(50) NOT NULL,'\
                    'valor REAl NOT NULL)'
            return sql
        except sqlite3.Error as error:
            print("Erro ao cria a tabela Modalidade", error)

    def tabela_Pagamento(self):
        try:
            sql = 'CREATE TABLE if not exists Pagamento ('\
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                'id_matricula INT NOT NULL,'\
                'valor DOUBLE NOT NULL,'\
                'dataPagamento DATE,'\
                'formaPagamento VARCHAR(50),'\
                'FOREIGN KEY(id_matricula) REFERENCES Matricula(id));'
            return sql
        except Error as error:
            print('Erro na criação Pagamento', error)

    def tabela_Antopometria(self):
        try:
            sql ='CREATE TABLE if not exists Antopometria ('\
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                'antopometriaPescoco REAl,'\
                'antopometriaToraxica REAl,'\
                'antopometriaCintura REAl,'\
                'antopometriaQuadril REAl,'\
                'antopometriaBracoRelaxado REAl,'\
                'antopometriaContraido REAl,'\
                'antopometriaAnteBraco REAl,'\
                'antopometriaCoxaSuperior REAl,'\
                'antopometriaCoxaMedia REAl,'\
                'antopometriaCoxaInferior REAl,'\
                'antopometriaPerna REAl);'
            return sql
        except Error as error:
            print("Erro ao criar a tabela Antopometria", error)

    def tabela_DobraCultanea(self):
        try:
            sql = 'CREATE TABLE if not exists DobraCultanea ('\
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                'dobraCultaneaSubEscapular REAl,'\
                'dobraCultaneaTriceps REAl,'\
                'dobraCultaneaBiceps REAl,'\
                'dobraCultaneaPeitoral REAl,'\
                'dobraCultaneaAxilarMediaObliqua REAl,'\
                'dobraCultaneaAxilarMediaVertical REAl,'\
                'dobraCultaneaAbdominalVertical REAl,'\
                'dobraCultaneaAbdominalHorizontal REAl,'\
                'dobraCultaneaSupraIliacaObliqua REAl,'\
                'dobraCultaneaSupraIliacaVertical REAl,'\
                'dobraCultaneaSupraEspinhal REAl,'\
                'dobraCultaneaCoxa REAl)'
            return sql
        except Error as error:
            print("Erro ao cria tambela DobraCultanea", error)

    def tabela_Diametro(self):
        try:
            sql =   'CREATE TABLE if not exists Diametro ('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'diametroRadioUlnar REAl,'\
                    'diametroUmeral REAl,'\
                    'diametroBiacromial REAl,'\
                    'diametroToracicoTransversal REAl,'\
                    'diametroToracicoAnterior REAl,'\
                    'diametroToracicoPosterior REAl,'\
                    'diametroBicristal REAl,'\
                    'diametroBitroCanteriano REAl,'\
                    'diametroFemular REAl,'\
                    'diametroMaleonar REAl)'

            return sql
        except Error as error:
            print("Erro ao criar a tabela Diametro", error)

    def tabela_Circuferencia(self):
        try:
            sql =   'CREATE TABLE if not exists Circuferencia ('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'circuferenciaGlutea REAl,'\
                    'circuferenciaPanturrilha REAl,'\
                    'circuferenciaMaleolar REAl,'\
                    'circuferenciaTroncoIM REAl,'\
                    'circuferenciaTroncoEM REAl)'\

            return sql
        except Error as error:
            print("Error ao criar tabela Circuferencia", error)

    def tabela_AvaliacaoFisica(self):
        try:
            sql =   'CREATE TABLE if not exists AvaliacaoFisica ('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'id_aluno NULL,'\
                    'avaliador VARCHAR(50),'\
                    'data DATE,'\
                    'frequenciaCardiaca  INT,'\
                    'pesoAluno REAl,'\
                    'altura REAl,'\
                    'abdominal int,'\
                    'flexaoBracos int,'\
                    'id_antopometria INT NOT NULL,'\
                    'id_dobracultanea INT NOT NULL,'\
                    'id_diametro INT NOT NULL,'\
                    'id_circuferencia INT NOT NULL,'\
                    'FOREIGN KEY(id_aluno) REFERENCES Aluno(id),'\
                    'FOREIGN KEY(id_antopometria) REFERENCES Antopometria(id),'\
                    'FOREIGN KEY(id_dobracultanea) REFERENCES DobraCultanea(id),'\
                    'FOREIGN KEY(id_diametro) REFERENCES Diametro(id),'\
                    'FOREIGN KEY(id_circuferencia) REFERENCES Circuferencia(id))'
            
            return sql
        except Error as error:
            print("Error ao cria a tabela AvaliacaoFisica", error)

    def tabela_Frequencia(self):
        try:
            sql =   'CREATE TABLE if not exists Frequencia  ('\
                    'id INTEGER PRIMARY KEY autoincrement,'\
                    'id_aluno INT NULL,'\
                    'dataEntrada DATE NOT NULL,'\
                    'dataSaida DATE NOT NULL,'\
                    'FOREIGN KEY(id_aluno) REFERENCES Aluno(id))'
            return sql
        except Error as error:
            print("Erro ao criar a tabela Frequencia", error)

    def tabela_Aluno(self):
        try:
            sql =   'CREATE TABLE if not exists Aluno ('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'nome VARCHAR(50) NOT NULL,'\
                    'endereco VARCHAR(50) NOT NULL,'\
                    'bairro VARCHAR(50) NOT NULL,'\
                    'cep VARCHAR(50) NOT NULL,'\
                    'cidade VARCHAR(50) NOT NULL,'\
                    'estado VARCHAR(50) NOT NULL,'\
                    'fone VARCHAR(50) NOT NULL,'\
                    'celular VARCHAR(50) NOT NULL,'\
                    'sexo CHAR(1) NOT NULL,'\
                    'cpf VARCHAR(45) NOT NULL,'\
                    'nascimento DATE NOT NULL,'\
                    'email VARCHAR(50) NOT NULL,'\
                    'estadoCivil VARCHAR(45) NOT NULL,'\
                    'profissao VARCHAR(50) NOT NULL,'\
                    'empresa VARCHAR(50) NOT NULL,'\
                    'objetivo VARCHAR(50),'\
                    'debito DOUBLE NOT NULL,'\
                    'matriculado BOOLEAN NOT NULL)'
            return sql
        except Error as error:
            print("Erro ao criar a tabela Aluno", error)

    def tabela_Funcao(self):
        try:
            sql =   'CREATE TABLE if not exists Funcao ('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'descricao VARCHAR(50) NOT NULL)'
            return sql
        except Error as error:
            print("Error ao criar a tabela Funcao", error)

    def tabela_Funcionario(self):
        try:
            sql =   'CREATE TABLE if not exists Funcionario ('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'id_funcao INT NOT NULL,'\
                    'nome VARCHAR(50) NOT NULL,'\
                    'endereco VARCHAR(50) NOT NULL,'\
                    'bairro VARCHAR(50) NOT NULL,'\
                    'cep VARCHAR(50) NOT NULL,'\
                    'cidade VARCHAR(50) NOT NULL,'\
                    'estado VARCHAR(50) NOT NULL,'\
                    'fone VARCHAR(50) NOT NULL,'\
                    'celular VARCHAR(50) NOT NULL,'\
                    'sexo CHAR(1) NOT NULL,'\
                    'cpf VARCHAR(45) NOT NULL,'\
                    'nascimento DATE NOT NULL,'\
                    'email VARCHAR(50) NOT NULL,'\
                    'estadoCivil VARCHAR(45) NOT NULL,'\
                    'dataAdmissao Date,'\
                    'salario DOUBLE,'\
                    'dataDemissao Date,'\
                    'usuario VARCHAR(50)  NOT NULL,'\
                    'senha VARCHAR(50) NOT NULL, '\
                    'FOREIGN KEY(id_funcao) REFERENCES Funcao(id))'
            return sql
        except Error as error:
            print("Erro ao criar a tabela Funcionario ",error)        

    def tabela_FichaTreino(self):
        try:
            sql =   'CREATE TABLE if not exists FichaTreino ('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'id_aluno NULL,'\
                    'nome VARCHAR (50) NOT NULL,'\
                    'data DATE NOT NULL,'\
                    'professor VARCHAR (50),'\
                    'treinoA VARCHAR(50),'\
                    'diaA VARCHAR(50),'\
                    'treinoB VARCHAR(50),'\
                    'diaB VARCHAR(50),'\
                    'treinoC VARCHAR(50),'\
                    'diaC VARCHAR(50),'\
                    'treinoD VARCHAR(50),'\
                    'diaD VARCHAR(50),'\
                    'treinoE VARCHAR(50),'\
                    'diaE VARCHAR(50),'\
                    'treinoF VARCHAR(50),'\
                    'diaF VARCHAR(50))'
            return sql
        except Error as error:
            print("Error ao criar a tabela FichaTreino", error)

    def tabela_Matricula(self):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS Matricula ('\
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'\
                    'id_aluno integer NULL,'\
                    'id_empresa integer not null,'\
                    'id_modalidade INT NOT NULL,'\
                    'dataVigencia DATE NOT NULL,'\
                    'plano VARCHAR (50) NOT NULL,'\
                    'dataVencimento DATE NOT NULL,'\
                    'desconto DOUBLE NOT NULL,'\
                    'valorFinal DOUBLE NOT NULL,'\
                    'situacao  VARCHAR(50) NOT NULL,'\
                    'dataFim DATE NOT NULL,'\
                    'FOREIGN KEY(id_empresa) REFERENCES Empresa(id),'\
                    'FOREIGN KEY(id_aluno) REFERENCES Aluno(id),'\
                    'FOREIGN KEY(id_modalidade) REFERENCES Modalidade(id))'

            return sql
        except Error as error:
                print('Erro ao criar tabelas aluno', error)


  

    # def criar_tabelas(self):
    #     try:
    #         sql = 'CREATE TABLE IF NOT EXISTS aluno('\
    #             'id integer primary key autoincrement,'\
    #             'nome varchar(50),'\
    #             'cpf varchar (20),'\
    #             'sexo varchar (10),'\
    #             'cep varchar (10),'\
    #             'endereco varchar (50),'\
    #             'numero varchar (10),'\
    #             'complemento varchar (50),'\
    #             'cidade varchar (30),'\
    #             'estado varchar (30),'\
    #             'telefone varchar (30),'\
    #             'email varchar (50))'            
    #         return sql
    #     except Error as e:
    #         print('Erro ao criar tabelas aluno', e)

    
    # def tabela_usuario(self):
    #     try:
    #         sql = 'CREATE TABLE IF NOT EXISTS usuario('\
    #             'id integer primary key autoincrement,'\
    #             'usuario varchar(50),'\
    #             'senha varchar (20),'\
    #             'email varchar (10))'            
    #         return sql
    #     except Error as e:
    #         print('Erro ao criar tabelas usuario', e)


    
  
    def criar_banco(self):
        if not os.path.exists('./database/academia.db'):
            conn = None
            try:
                conn = sqlite3.connect('./database/academia.db')
                print("Banco criado com sucesso")
                return conn
            
            except Error as e:
                print("Erro ao criar banco de dados", e)
            
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
            print("Erro ao criar tabelas", e)

        

    


        

        
