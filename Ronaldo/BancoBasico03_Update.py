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
    "UPDATE LojaDB.Produtos "
    "SET Valor = %s WHERE Codigo = %s "
)

varCodigo = input("Digite o Código: ")
varValor = float(input("Digite o valor: "))

dados = (varValor, varCodigo)
cursor.execute(comando, dados)
dbConexao.commit()

cursor.close()
dbConexao.close()