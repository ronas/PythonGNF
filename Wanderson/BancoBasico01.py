
# import mysql.connector
import pymysql
config = {
    'host':'localhost',
    'port': 3306,
    'database': 'LojaDB',
    'user': 'root',
    'password': '12345'
     }

#db = mysql.connector.connect(**config)
db = pymysql.connect(**config)
cursor = db.cursor()
comando = 'select*from Produtos'
cursor. execute(comando)
registros = cursor.fetchall()
print(registros)
cursor.close()
db.close()
