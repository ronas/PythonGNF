# 
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo
# Aula de Banco Basico Delete
#
import mysql.connector
config = 
    {
    'host':'localhost',
    'port': 3306,
    'database':'LojaDB',
    'user':'admin',
    'password':'admin'
    }
db = mysql.connector.connector(**config)
cursor = db.cursor()
comando = (
    "delete from LojaDB.produtos "
    "where codigo = '%s' ")
)
varcodigo = input ("Digite Codigo")
#
cursor.execute(comando, varcodigo)
db.commit()
print('Jáfoi')
cursor.Close
db.close