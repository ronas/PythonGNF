# import mysql.connector
import pymysql

config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'LojaDB',
    'user': 'root',
    'password': '12345'
}

# dbConexao = mysql.connector.Connect(**config)
dbConexao = pymysql.Connect(**config)

cursor = dbConexao.cursor()

comando = 'SELECT * FROM Produtos'
cursor.execute(comando)
registros = None

registros = cursor.fetchall()

for registro in registros:
    print("Codigo: ", registro[0])
    print("Nome  : ", registro[1])
    print("Valor : ", registro[2])
    print("\n")

cursor.close()
dbConexao.close()