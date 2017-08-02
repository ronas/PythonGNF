import pymysql
 
comfig ={'host':'localhost',
         'port':3306,
         'database':'Lojadb',
         'user':'root',
         'password':'34387'}
db= pymysql.connect(** comfig)
cursor = db.cursor()
comando =("insert into Lojadb.cliente (nome,codigo) " " values (%s,%s)" )

varnome = input('digite o nome ')
varcodigo = input('digiteo codigo ')

dados = (varnome,varcodigo)

cursor.execute (comando,dados)

db.commit()
print('ja foi')

cursor.close()
db.close
