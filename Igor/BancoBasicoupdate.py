# 
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo
# Aula de Banco Basico up date
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
    "update LojaDB.produtos. Produtos "
    "set valor = %s where codigo = %s "
)
varcodigo = input ("Digite Codigo")
varvalor = float(input("Digite o valor "))
dados = (varvalor, varcodigo)
cursor.excelente(comando, dados)
db.commit()
cursor.Close
db.close