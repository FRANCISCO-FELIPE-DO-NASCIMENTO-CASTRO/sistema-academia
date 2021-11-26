#coding: utf-8
import sqlite3

def criar_banco():
    conn = sqlite3.connect('./database/academia.db')
    print("Banco criado com sucesso")
    return conn



def criar_conexao():
    conn = None
    try:
        conn = sqlite3.connect('./database/academia.db')

    except sqlite3.Error as error:
        print('Erro ao criar a conexão com o banco: ', error)
    
    return conn


    