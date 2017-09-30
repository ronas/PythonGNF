import pymysql

config = {
    'host':'localhost',
    'port' : 3306,
    'database' : 'LojaDB',
    'user' : 'admin',
    'password' : 'admin'
    }

def bdMostrarParceiros():
    
    db = pymysql.connect(**config)
    cursor = db.cursor() 
    comando = 'select * from PARCEIROS' 
    cursor.execute(comando)
    registros = cursor.fetchall()
    for registro in registros:
        print("\n")
        print("Codigo", registro[0])
        print("RAZAO",  registro[1])
        print("APELIDO", registro[2])
        print("CNPJ", registro[3])
        print("TIPO", registro[4])
        print("EMAIL", registro[5])
        print("TELEFONE", registro[6])
        print("\n")
    cursor.close
    db.close
    
def bdInserirParceiros():
    
    db = pymysql.connect(**config)
    cursor = db.cursor()
    comando =(
    "insert into PARCEIROS (CODIGO,RAZAO,APELIDO,CNPJ,TIPO,EMAIL,TELEFONE)"
    "values(%s,%s,%s,%s,%s,%s,%s)"
    )
    varcodigo = input("digitar codigo: ")
    varrazao = input("digitar a razao: ")
    varapelido = input("digitar o apelido: ")
    varcnpj = input("digitar cnpj: ")
    vartipo = input("digite o tipo: ")
    varemail = input("digite o email: ")
    vartelefone = input("digite o telefone: ")
    dados = (varcodigo,
             varrazao,
             varapelido,
             varcnpj,
             vartipo,
             varemail,
             vartelefone)
    cursor.execute(comando,dados)
    db.commit()
    cursor.close
    db.close
    
def bdUpDateParceiros():
    
    db = pymysql.connect(**config)
    cursor = db.cursor()
    comando = ("update LojaDB.Parceiros "
        "set valor = %s where codigo = %s "
    )
    varcodigo = input("digitar codigo ")
    varrazao = input("digitar a razao: ")
    varapelido = input("digitar o apelido")
    varcnpj = input("digitar cnpj")
    vartipo = input("digite o tipo ")
    varemail = input("digite o email")
    vartelefone = input("digite o telefone")
    dados =(varcodigo,varrazao,varapelido,varcnpj,vartipo,varemail,vartelefone)
    cursor.execute(comando, dados)
    db.commit()
    cursor.close
    db.close
    
def bdDeleteParceiros():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    comando = ("delete from LojaDB.Produtos "
     "where codigo = '%s' ")

    varcodigo = input("digitar codigo ")
    varrazao = input("digitar a razao: ")
    varapelido = input("digitar o apelido")
    varcnpj = input("digitar cnpj")
    vartipo = input("digite o tipo ")
    varemail = input("digite o email")
    vartelefone = input("digite o telefone")
    cursor.execute(comando, varcodigo,varrazao,varapelido,varcnpj,vartipo,
                   varemail,vartelefone)
    db.commit()
    print('jafoi')
    cursor.close()
    db.close()
    
def bdMostrarProdutos():

    db = pymysql.connect(**config)
    cursor = db.cursor() 
    comando = 'select * from Produtos' 
    cursor.execute(comando)
    registros = cursor.fetchall()
    for registro in registros:
        print("\n")       
        print("Codigo: ", registro[0])
        print("Nome  : ", registro[1])
        print("Valor : ",  registro[2])
        print("\n")
    cursor.close
    db.close
    
def bdInserirProdutos():

    db = pymysql.connect(**config)
    cursor = db.cursor()
    comando =(
    "insert into Produtos (codigo,nome,valor)"
    "values(%s,%s,%s)"
    )
    varcodigo = input("digitar codigo: ")
    varnome = input("digitar nome: ")
    varvalor = float(input("digite o valor: "))
    dados = (varcodigo,
             varnome,
             varvalor)
    cursor.execute(comando,dados)
    db.commit()
    cursor.close
    db.close
    
def bdUpDateProdutos():
    
    db = pymysql.connect(**config)
    cursor = db.cursor()
    comando = (
        "update LojaDB.Produtos "
        "set valor = %s where codigo = %s "
    )
    varcodigo = input("digitar codigo ")
    varvalor = float(input("digitar o valor "))
    dados = (varvalor,varcodigo)
    cursor.execute(comando, dados)
    db.commit()
    cursor.close
    db.close
    
def bdDeleteProdutos():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    comando = ("delete from LojaDB.Produtos "
     "where codigo = '%s' ")
    varcodigo = input('diga o codigo')
    
    cursor.execute(comando, varcodigo)
    db.commit()
    print('jafoi')
    cursor.close()
    db.close()
    
while True:
    
    print("|_____________________________________________________|\n"
          "|    PRDTUTOS           |      PARCEIROS              |\n" 
          "|                       |                             |\n"
          "| 1) Inserir:           |   5) Inserir:               |\n" 
          "| 2) Atualizar:         |   6) Atualizar:             |\n"
          "| 3) Excluir:           |   7) Excluir:               |\n"
          "| 4) Mostrar:           |   8) Mostrar:               |\n"
          "|_______________________|_____________________________|\n"
          "s) Sair: \n")
    
    OpcaoMenu = input("Digite a Opcao: ")
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    
    if OpcaoMenu == 'S':
        print("Fechando o Sistema! ")
        break
    elif OpcaoMenu == '1':
        bdInserirProdutos()
        
    elif OpcaoMenu == '2':
        bdUpDateProdutos()
        
    elif OpcaoMenu == '3':
        bdDeleteProdutos()
        
    elif OpcaoMenu == '4':
        bdMostrarProdutos()
        
    elif OpcaoMenu == '5':        
        #print("Inserir")
        bdInserirParceiros()
    
    elif OpcaoMenu == '6':        
        #print("Atualizar")
        bdUpDateParceiros()
        
    elif OpcaoMenu == '7':        
        #print("Excluir")
        bdDeleteParceiros(
            )
    elif OpcaoMenu == '8':        
        #print("Mostrar")
        bdMostrarParceiros()
        
    elif OpcaoMenu == 's':        
        print("Sair")    
 
 