# 
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo
# Aula de Banco Basico 01
#
import pymysql
config = {
    'host':'localhost',
    'port': 3306,
    'database':'LojaDB',
    'user':'admin',
    'password':'admin'
    }
db = pymysql.connect(**config)
cursor = db.cursor()
#db = pymysql.connect(**config)
comando= 'Select * From Produtos'
cursor.execute(comando)
registros = cursor.fetchall()
print (registros)
cursor.close()
db.close()
