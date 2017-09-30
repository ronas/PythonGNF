# 
# Autor: Igor Nunes
# Materia: Programa Python
# Orientador : Ronaldo
# Aula de Banco Basico 01
    
    
import pymysqlconfig = 
{
            'host':'localhost',
            'port': 3306,
            'database':'LojaDB',
            'user':'admin',
            'password':'admin'
            }
db = pymysql.connect(**config)
cursor = db.cursor()
comando= (
    "insert into produtos (Codigo,Nome,Valor)"
     "values (%s,%s,%s)"
    )
varCodigo = input ("Digite Codigo:")
varNome = input ("Digite Nome:")
varValor = input ("Qual Valor:")
dados = (varCodigo,varNome,varValor)
cursor.execute(comando,dados)
db.commit()
cursor.close()
db.close()