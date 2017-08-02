# apt-get install python3-pymysql
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

comando = ( 
    "INSERT INTO LojaDB.Produtos (Codigo, Nome, Valor) "
    "VALUES (%s, %s, %s)"
)

varCodigo = input("Digite o Código: ")
varNome = input("Digite o nome: ")
varValor = float(input("Digite o valor: "))

dados = (varCodigo, varNome, varValor)
cursor.execute(comando, dados)
dbConexao.commit()

cursor.close()
dbConexao.close()