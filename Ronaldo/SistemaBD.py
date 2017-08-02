import mysql.connector 
config = {
    'host':'localhost',
    'port' : 3306,
    'database' : 'LojaDB',
    'user' : 'root',
    'password' : 'fabulao1978'
    }
def bdMostrarProdutos():

    db = mysql.connector.connect(**config)
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

    db = mysql.connector.connect(**config)
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
    
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    comando = (
        "update LojaDB.Produtos "
        "set valor = %s where codigo = %s "
    )
    varcodigo = input("digitar codigo ")
    varvalor = float(input("digitar o valor "))
    dados =(varvalor, varcodigo)
    cursor.execute(comando, dados)
    db.commit()
    cursor.close
    db.close
    
def bdDeleteProdutos():
    db = mysql.connector.connect(**config)
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
    
    print("i) Inserir: \n" 
          "a) Atualizar: \n"
          "e) Excluir: \n"
          "m) Mostrar: \n"
          "s) Sair: \n")
    OpcaoMenu = input("Digite a Opcao: ")
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    
    if OpcaoMenu == 'S':
        print("Fechando o Sistema! ")
        break
    
    elif OpcaoMenu == 'i':        
        #print("Inserir")
        bdInserirProdutos()
    
    elif OpcaoMenu == 'a':        
        #print("Atualizar")
        bdUpDateProdutos()
        
    elif OpcaoMenu == 'e':        
        #print("Excluir")
        bdDeleteProdutos(
            )
    elif OpcaoMenu == 'm':        
        #print("Mostrar")
        bdMostrarProdutos()
        
    elif OpcaoMenu == 's':        
        print("Sair")    
 