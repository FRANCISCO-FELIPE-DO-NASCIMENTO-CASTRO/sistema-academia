
# from mysql import connector
# from mysql.connector import connection

# from database.connection import create_connection


# def insert(data):
#     conn = create_connection()
#     sql = """ INSERT INTO  FUNCIONARIO (nome) VALUES (%s)"""

#     try:
#         cur = conn.cursor()
#         cur.execute(sql, data)
#         conn.commit()
#         return True

#     except connector.Error as err:
#         print(f'Errro')