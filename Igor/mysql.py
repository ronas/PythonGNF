pymysql importação
config = {
'Host': 'localhost',
'Porto': 3306,
'Banco de dados': 'LojaDB',
'User': 'admim',
'Password': 'adimim'
}

def bdMostrarParceiros ():
db = pymysql.connect (** config)
cursor = db.cursor ()
Comando = 'SELECT * FROM PARCEIROS'
cursor.execute (Comando)
Registros = cursor.fechall ()
para registro de Registros:
print ( "\ n")
imprimir ( "Código", registro [0])
print ( "Razão", registro [1])
print ( "apelido", registro [2])
imprimir ( "CNPJ", registro [3])
print ( "TIPO", registro [4])
print ( "EMAIL", registro [5])
print ( "Telefone", registro [6])
print ( "\ n")
cursor.close
db.close
def bdInserirParceiros ():
db = pymysql.connect (** config)
cursor = db.cursor ()
Comando = (
"Inserir PARCEIROS (CODIGO, Razão, apelido, CNPJ, TIPO, E-MAIL, TELEFONE)"
"Valores (% s% s% s)"
)
varcodigo = entrada ( "DigiTar codigo:")
varrazao = entrada ( "DigiTar A Razão:")
varapelido = entrada ( "DigiTar o apelido")
varcnpj = entrada ( "CNPJ DigiTar")
vartipo = entrada ( "digite o tipo")
varemail = input ( "digite o e-mail")
vartelefone = entrada ( "digite o telefone")
Dados = (varcodigo,
varrazao,
varapelido,
varcnpj,
vartipo,
varemail,
vartelefone)
cursor.execute (Comando, Dados)
db.commit ()
cursor.close
db.close
def bdUpDateParceiros ():
db = pymysql.connect (** config)
cursor = db.cursor ()
Comando = ( "LojaDB.Parceiros atualização"
"Definido valor =% s onde codigo =% s"
)
varcodigo = entrada ( "codigo DigiTar")
varrazao = entrada ( "DigiTar A Razão:")
varapelido = entrada ( "DigiTar o apelido")
varcnpj = entrada ( "CNPJ DigiTar")
vartipo = entrada ( "digite o tipo")
varemail = input ( "digite o e-mail")
vartelefone = entrada ( "digite o telefone")
Dados = (varcodigo, varrazao, varapelido, varcnpj, vartipo, varemail, vartelefone)
cursor.execute (Comando, Dados)
db.commit ()
cursor.close
db.close
def bdDeleteParceiros ():
db = pymysql.connect (** config)
cursor = db.cursor ()
Comando = ( "excluir LojaDB.Produtos"
"Onde codigo = '% s'")

varcodigo = entrada ( "codigo DigiTar")
varrazao = entrada ( "DigiTar A Razão:")
varapelido = entrada ( "DigiTar o apelido")
varcnpj = entrada ( "CNPJ DigiTar")
vartipo = entrada ( "digite o tipo")
varemail = input ( "digite o e-mail")
vartelefone = entrada ( "digite o telefone")
cursor.execute (Comando, varcodigo, varrazao, varapelido, varcnpj, vartipo,
varemail, vartelefone)
db.commit ()
print ( 'jafoi')
cursor.close ()
db.close ()
def bdMostrarProdutos ():

db = pymysql.connect (** config)
cursor = db.cursor ()
Comando = 'SELECT * FROM Produtos'
cursor.execute (Comando)
Registros = cursor.fechall ()
para registro de Registros:
print ( "\ n")
print ( "Codigo:", registro [0])
print ( "Nome:", registro [1])
print ( "Valor", registro [2])
print ( "\ n")
cursor.close
db.close
def bdInserirProdutos ():

db = pymysql.connect (** config)
cursor = db.cursor ()
Comando = (
"Inserir em Produtos (codigo, nome, valentes)"
"Valores (% s% s% s)"
)
varcodigo = entrada ( "DigiTar codigo:")
varnome = entrada ( "DigiTar Nome:")
varvalor = flutuador (entrada ( "digite o valor:"))
Dados = (varcodigo,
varnome,
varvalor)
cursor.execute (Comando, Dados)
db.commit ()
cursor.close
db.close
def bdUpDateProdutos ():
db = pymysql.connect (** config)
cursor = db.cursor ()
Comando = (
"LojaDB.Produtos atualização"
"Definido valor =% s onde codigo =% s"
)
varcodigo = entrada ( "codigo DigiTar")
varvalor = flutuador (entrada ( "DigiTar o valor"))
Dados = (varvalor, varcodigo)
cursor.execute (Comando, Dados)
db.commit ()
cursor.close
db.close
def bdDeleteProdutos ():
db = pymysql.connect (** config)
cursor = db.cursor ()
Comando = ( "excluir LojaDB.Produtos"
"Onde codigo = '% s'")
varcodigo = entrada ( 'diga o codigo')
cursor.execute (Comando, varcodigo)
db.commit ()
print ( 'jafoi')
cursor.close ()
db.close ()
while True:
print ( "| _____________________________________________________ | \ n"
"| PRDTUTOS | PARCEIROS | \ n"
"| | | \ N"
"| 1) Inserir: | 5) Inserir: | \ n"
"| 2) Atualizar: | 6) Atualizar: | \ n"
"| 3) Excluir: | 7) Excluir: | \ n"
"| 4) Mostrar: | 8) Mostrar: | \ n"
"| _______________________ | _____________________________ | \ n"
"S) Sair: \ n")
OpcaoMenu = entrada ( "Digite uma Opção:")
#print ( "\ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n \ n ");
se OpcaoMenu == 'S':
imprimir ( "Fechando o Sistema!")
pausa
elif OpcaoMenu == '1':
bdInserirParceiros ()
elif OpcaoMenu == '2':
bdUpDateParceiros ()
elif OpcaoMenu == '3':
bdDeleteParceiros ()
elif OpcaoMenu == '4':
bdMostrarParceiros ()
elif OpcaoMenu == '5':
#print ( "Inserir")
bdInserirProdutos ()
elif OpcaoMenu == '6':
#print ( "Atualizar")
bdUpDateProdutos ()
elif OpcaoMenu == '7':
#print ( "Excluir")
bdDeleteProdutos (
)
elif OpcaoMenu == '8':
#print ( "Mostrar")
bdMostrarProdutos ()
elif OpcaoMenu == 's':
imprimir ( "Sair")