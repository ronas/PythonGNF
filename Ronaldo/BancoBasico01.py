# import mysql.connector
import pymysql

config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'LojaDB',
    'user': 'root',
    'password': '12345'
}

# db = mysql.connector.Connect(**config)
db = pymysql.Connect(**config)

cursor = db.cursor()

comando = 'SELECT * FROM Produtos'
cursor.execute(comando)
registros = None

registros = cursor.fetchall()
print(registros)

cursor.close()
db.close()

