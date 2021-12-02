import sqlite3
from sqlite3 import Error
import os

class DataBase:
    def tabela_avaliacaoFisica(self):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS avaliacaoFisica('\
                'id integer primary key autoincrement,'\
                'id varchar(10),'\
                'data varchar (20),'\
                'frequenciaCardiaca varchar (10),'\
                'peso varchar (10),'\
                'altura varchar (50),'\
                'abdominal varchar (10),'\
                'flexaoBracos varchar (50),'\
                'antopometria varchar (30),'\
                'dobraCultanea varchar (30),'\
                'diametro varchar (30),'\
                'circunferencia varchar (10),'\
                'aluno varchar (50),'\
                'avaliador varchar (50))'            
            return sql
        except Error as e:
            print('Erro ao criar tabelas avaliacaoFisica', e)


    
    def tabela_bandeiras(self):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS bandeiras('\
                'id integer primary key autoincrement,'\
                'bandeira1 varchar(10),'\
                'bandeira2 varchar (20),'\
                'bandeira3 varchar (20),'\
                'bandeira4 varchar (10))'            
            return sql
        except Error as e:
            print('Erro ao criar tabela bandeiras', e)



    def contrato(self):
        try:
            sql = 'CREATE TABLE IF NOT EXISTS contrato('\
                'id integer primary key autoincrement,'\
                'numero varchar(50),'\
                'cliente varchar (50),'\
                'plano varchar (50),'\
                'meio_pagamento varchar (50))'            
            return sql
        except Error as e:
            print('Erro ao criar tabelas contrato', e)
  
    
