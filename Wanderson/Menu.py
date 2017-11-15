import pymysql

config = {
    'host':'localhost',
    'port': 3306,
    'database': 'LojaDB',
    'user': 'root',
    'password': '12345'
     }
#OpcaoMenu = ''
#while OpcaoMenu != 's':
#    print('menu')
#    OpcaoMenu = input('Digite a Opcao [1,2,s]:')
def bdMostrarProdutos():

    db = pymysql.connect(**config)
    cursor = db.cursor()
    comando = 'select*from Produtos'
    cursor. execute(comando)
    registros = cursor.fetchall()
    for registro in registros:
        print("codigo:",registro[0])
        print("nome:",registro[1])
        print("valor:",registro[2])
        print("\n")
    cursor.close()
    db.close()

def bdInserirProdutos():
    db = pymysql.connect(**config)
    cursor = db.cursor()

    comando = (
    "insert into Produtos(codigo,nome,valor)"
    "values(%s,%s,%s)"
    )

    varcodigo = input("Digite o codigo:")
    varnome   = input("Digite o nome:")
    varvalor  = float(input("Digite o valor:"))

    dados = (varcodigo,varnome,varvalor)

    cursor.execute(comando,dados)

    db.commit()

    cursor.close()

while True:
   # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    print("i) Inserir \n"
          "a) Atualizar \n"
          "e) Excluir \n"
          "m) Mostrar \n"
          "s) Sair \n")
    
#    OpcaoMenu = input("Digite a opcao");
    OpcaoMenu="i"
    if OpcaoMenu == 's':
        print("Sistema Encerrado")
        break
    elif OpcaoMenu == 'i':
        bdInserirProdutos()
    elif OpcaoMenu == 'a':
        print("Atualizar")
    elif OpcaoMenu == 'e':
         print("Excluir")
    elif OpcaoMenu == 'm':
        bdMostrarProdutos()
    elif OpcaoMenu == 's':
        print("Sair")
        