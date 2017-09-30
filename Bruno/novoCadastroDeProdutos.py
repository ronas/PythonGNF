import os,sys
from PyQt4 import QtCore,QtGui

import pymysql





comfig ={'host':'localhost',
         'port':3306,
         'database':'LojaDB',#
         'user':'root',
         'password':'34387'}
db= pymysql.connect(** comfig)
cursor = db.cursor()



  
class ClasseAPP(QtGui.QWidget):
     
    def __init__(self, part=None):
        super(ClasseAPP, self).__init__(part)
        self.initUI()

    def initUI(self):

        super(ClasseAPP, self).__init__()
        self.setGeometry(300,100,0,0)
        self.setFixedSize(700,550)
        self.setWindowTitle("Produtos")
        self.setWindowIcon(QtGui.QIcon('palet03.png'))
        
        self.home()
        
    def home(self):
        
        self.lbcodigo = QtGui.QLabel("Código ",self)
        self.lbcodigo.setGeometry(20, 40, 71, 18)
        
        self.txtcodigo = QtGui.QLineEdit(self)
        self.txtcodigo.setGeometry(90, 40, 113, 21)
        
        self.lblnome = QtGui.QLabel("Nome",self)
        self.lblnome.setGeometry(20, 80, 71, 18)
        
        self.txtnome = QtGui.QLineEdit(self)
        self.txtnome.setGeometry(20, 100, 621, 21)

       
        self.pic = QtGui.QLabel(self)
       
        self.pic.setPixmap(QtGui.QPixmap("palet03.png"))
        self.pic.setGeometry(550, 5, 621,100)
        

        self.txtunidade = QtGui.QLineEdit(self)
        self.txtunidade.setGeometry(20, 150, 191, 21)
        
        self.lblunidade = QtGui.QLabel("Unidade de Medida",self)
        self.lblunidade.setGeometry(20, 130, 141, 18)
        
        self.txtpeso = QtGui.QLineEdit(self)
        self.txtpeso.setGeometry(240, 150, 191, 21)
        
        self.lblpeso = QtGui.QLabel("Peso kg",self)
        self.lblpeso.setGeometry(240, 130, 141, 18)
        
        self.txtcodigoean = QtGui.QLineEdit(self)
        self.txtcodigoean.setGeometry(QtCore.QRect(20, 200, 191, 21))
        
        self.lblcodigoean = QtGui.QLabel("Código  EAN",self)
        self.lblcodigoean.setGeometry(20, 180, 141, 18)
        
        self.txtcodigomoeda = QtGui.QLineEdit(self)
        self.txtcodigomoeda.setGeometry(450, 150, 191, 21)
        
        self.lblcodigomoeda = QtGui.QLabel("Código Moeda",self)
        self.lblcodigomoeda.setGeometry(450, 130, 141, 18)
        
        self.txtpreco = QtGui.QLineEdit(self)
        self.txtpreco.setGeometry(450, 200, 191, 21)
        
        self.lblpreco = QtGui.QLabel("Valor de Venda",self)
        self.lblpreco.setGeometry(450, 180, 141, 18)
        
        self.txtvalor = QtGui.QLineEdit(self)
        self.txtvalor.setGeometry(240, 200, 191, 21)
      
        self.lblvalor = QtGui.QLabel("Preço de compra",self)
        self.lblvalor.setGeometry(240, 180, 141, 18)
        
        self.tabela = QtGui.QTableWidget(3,20,self)
        self.tabela.setGeometry(20, 270, 645, 192)
        self.tabela.setColumnCount(8)
        self.tabela.setRowCount(10)
        self.tabela.setHorizontalHeaderLabels(('Código', 'Nome', 'Unidade de Medida','Peso kg',' Código Moeda  ','Código Ean','Preço de compra ','Valor de venda'  ))
        
        

        
        
        
        self.btnincluir = QtGui.QPushButton("Inserir",self)
        self.btnincluir.setGeometry(20,230, 106, 28)
        self.btnincluir.clicked.connect(self. InserirDados)
        self.btnincluir.clicked.connect(self.create_comsuta)
        self.btnincluir.setIcon(QtGui.QIcon('add.png'))
        
        
        
        
        
        self.create_comsuta()
        
        
        
        self.btnexcluir = QtGui.QPushButton("Excluir",self)
        self.btnexcluir.setGeometry(140, 485, 106, 28)
        self.btnexcluir.clicked.connect(self.EXcluir)
    
        self.btnexcluir.setIcon(QtGui.QIcon('remove.png'))
       
       
        self.btnatualizar = QtGui.QPushButton("Atualizar",self)
        self.btnatualizar.setGeometry(20,485, 106, 28)
        self.btnatualizar.clicked.connect(self. ATualizar)
        
        self.btnatualizar.setIcon(QtGui.QIcon('up.png'))
       
        
        self.btnsair = QtGui.QPushButton("Sair",self)
        self.btnsair.setGeometry(260,485, 106, 28)
        self.btnsair.clicked.connect(self.sair)
        self.btnsair .clicked.connect(self. InserirDados)
        self.btnsair .setIcon(QtGui.QIcon('accept.png'))
       


        self.TelaExcluir = Excluir(self)
        self.TelaAtulizar = Atualizar(self)
        
        self.show()
      
    def EXcluir(self):
        self.TelaExcluir.exec_()
        
    def ATualizar(self):
        self.TelaAtulizar .exec_()

    def sair(self):
        print("Fim!!!")
        sys.exit()
      
        
    def InserirDados (self):
        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        comando =("select Codigo from  LojaDB.Produtos " " WHERE Codigo = %s " )
        fui = self.txtcodigo.text() 
        cursor.execute (comando,fui)
        registros = cursor.fetchall()
        for registros in registros:
            rui = (registros[0])
        
        ppreco = self. txtpreco.text()
        propreco = len(ppreco)
        pvalor = self. txtvalor.text()
        provalor = len(pvalor)
        pcodigoean = self.txtcodigoean.text()
        procodigoean = len(pcodigoean)
        pcodigomoeda = self.txtcodigomoeda.text()
        procodigomoeda = len(pcodigomoeda)
        
        ppeso = self.txtpeso.text()
        propeso = len(ppeso)
        
        pcodigo = self.txtcodigo.text()
        procodigo = len(pcodigo)
        print("codigo",procodigo)
        pnome = self.txtnome.text()
        pronome = len(pnome)
        print("vaca",pronome )
        punidade = self.txtunidade.text()
        prounidade = len (punidade)
         
        pean = self.txtcodigoean.text()
        proean = len (pean)
        pmoeda = self.txtcodigomoeda.text()
        promoeda = len (pmoeda)
        
        
            
        
        try:
            ppeso = float(self.txtpeso.text())
            peso ="PESO SERTO"
        except ValueError:
                peso =" Peso errado ? "
        try:
            ppvalor = float(self.txtvalor.text())
            valor = 'VALOR SERTO'
        except ValueError:
                valor =" valor errado? "
        try:
            pppreco = float(self.txtpreco.text())
            preco =  "PREÇO SERTO"
        except ValueError:
            preco= " preco erro? "
        try:
            rui
            deletar = "carro"
        except NameError:
            deletar= "Não esta cadastrado"
        
        
        
        
        
            
        if 0 == procodigo :
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Código esta Vazio !",
                                            QtGui.QMessageBox.Ok  )
        elif 0 ==pronome:
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Nome esta Vazio !",
                                                  QtGui.QMessageBox.Ok  )
        
        
        elif 0 ==prounidade:
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Uidade de Medida esta Vazio !",
                                                  QtGui.QMessageBox.Ok  )
        
        elif 0 ==propeso :
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Peso esta Vazio !",
                                                  QtGui.QMessageBox.Ok  )
            
            
        elif 0 ==procodigomoeda :
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Código Moeda esta Vazio !",
                                                  QtGui.QMessageBox.Ok  )
            
            
        elif 0 ==procodigoean :
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Código EAN esta Vazio !",
                                                  QtGui.QMessageBox.Ok  )
            
        elif 0 ==provalor  :
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Preço de Compra esta Vazio !",
                                                  QtGui.QMessageBox.Ok  )
        elif 0 == propreco  :
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Valor de Venda esta Vazio !",
                                              QtGui.QMessageBox.Ok  )
            
        elif deletar == "carro":
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Código já Cadastrado",
                                            QtGui.QMessageBox.Ok)

        
        elif  10 < procodigo :
           
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O canpo codigo suporta só 10 letras !",
                                            QtGui.QMessageBox.Ok)         

        elif 50<pronome:
            choice = QtGui.QMessageBox.question(self, 'Extract!',
            "O canpo Nome suporta só 50 letras",
            QtGui.QMessageBox.Ok)
            
        elif 3 < prounidade:
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo  Unidade  de Medida  suporta só 3 letras !",
                                            QtGui.QMessageBox.Ok)
        

        

        
        
         
         
        elif peso == " Peso errado ? ":
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Peso só aceita Números !",
                                            QtGui.QMessageBox.Ok)      

        elif 3 < promoeda:
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo  Código Moeda suporta só 3 letras !",
                                             QtGui.QMessageBox.Ok)
        elif 13 < proean:
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo  CódigoEAN suporta só 13 letras !",
                                            QtGui.QMessageBox.Ok)

             
             

            
        elif valor == " valor errado? ":
            
            
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "O campo Preço de Compra só aceita Números !",
                                            QtGui.QMessageBox.Ok  )
        
        
                      
        elif preco ==" preco erro? ":
            choice = QtGui.QMessageBox.question(self, 'Extract!',
            "O campo Valor de Venda só aceita Números !",
            QtGui.QMessageBox.Ok)
             
             
        else:
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            " Salvar Registro  ?",
                                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        
            if choice == QtGui.QMessageBox.No:
               
                print("VOCE NÃO QUIS SALVAR")
                
            
            else:
            
        
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
        
        
                comando =("insert into LojaDB .Produtos (Codigo,Nome,UnidadeMedida,Peso,CodigoEAN,CodigoMoeda,PrecoCompra,ValorVenda) "  " values (%s,%s,%s,%s,%s,%s,%s,%s)" )  # meto
            
                pcodigo = self.txtcodigo .text()

                pnome= self.txtnome.text()
        
                punidade =self.txtunidade.text()             
        
                ppeso = float(self.txtpeso.text())
        
                pcodigoean = self.txtcodigoean.text()
        
                pcodigomoeda = self.txtcodigomoeda.text()
        
                ppreco = float(self.txtpreco.text())
        
                pvalor = float(self.txtvalor.text())
            
            
                dados = (pcodigo ,pnome,punidade,ppeso,pcodigoean,pcodigomoeda,ppreco,pvalor )
                
                cursor.execute (comando,dados)

                db.commit()
                print('ja foi')

                cursor.close()
                db.close

                
    def create_comsuta (self):
        
        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        
        cursor.execute("select *from  LojaDB.Produtos")# comando mostrando itenis 
        self.tabela.setRowCount(0)
        for row, form in enumerate(cursor):
            self.tabela.insertRow(row)
            for column, item in enumerate(form):
                #print(str(item))
                self.tabela.setItem(row, column, QtGui.QTableWidgetItem(str(item)))       
               
                

class Excluir(QtGui.QDialog):
    def __init__(self, parent=None):
       
        super(Excluir, self).__init__(parent)
        self.initUI()

    def initUI(self):

        super(Excluir, self).__init__()
        #self.setGeometry(400, 100, 278, 247)
        self.setGeometry(450,260,0,0)
        self.setFixedSize(380,120)
        self.setWindowTitle("Excluir  Produtos")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        
        self.home()
        
    def home(self):
        
        
        self.deleti =QtGui.QLabel("Digite o Código do Produto",self)
        self.deleti.setGeometry(20, 25, 200, 18)
        self.txtdeleti = QtGui.QLineEdit(self)
        self.txtdeleti.setGeometry(20,50, 200, 21)
        
        
        
        self.btnexcluir = QtGui.QPushButton("Excluir",self)
        self.btnexcluir.setGeometry(250, 45, 106, 28)
        self.btnexcluir.clicked.connect(self.deletou)
        self.btnexcluir.clicked.connect(self.txtdeleti.clear)
       
    def deletou (self):
        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        comando =("select Codigo from  LojaDB.Produtos " " WHERE Codigo = %s " )
        fui = self.txtdeleti.text() 
        cursor.execute (comando,fui)
        registros = cursor.fetchall()
        for registros in registros:
            
            rui = registros[0]
        try:
            rui
            deletar=("carro")
        except NameError:
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            " Código Não Existente ?",
                                            QtGui.QMessageBox.Ok)
            print ("Bem, não foi definido depois de tudo!")
        
        if deletar == "carro":
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Você quer Excluir este Registro ?",
                                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.No:
                print("não pode apagar")
        
            else:
                print("pode apagar")
        
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
        
                comando=(" delete from LojaDB.Produtos " " where Codigo = %s ")
                varcodigo = self.txtdeleti.text()
                cursor.execute(comando, varcodigo)
                db.commit()
                print('ja foi')

                cursor.close()
                db.close
        
       
class Atualizar(QtGui.QDialog):
    def __init__(self, part=None):
       
        super(Atualizar, self).__init__(part)
        self.initUI()

    def initUI(self):

        super(Atualizar, self).__init__()
        #self.setGeometry(400, 100, 278, 247)
        self.setGeometry(325,260,0,0)
        self.setFixedSize(650,120)
        self.setWindowTitle("Produtos")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        
        self.home()
        
    def home(self):
        
        
        self.lblcodigoproduto =QtGui.QLabel(" Código do Produto",self)
        self.lblcodigoproduto .setGeometry(20, 25, 200, 18)
        self.txtcodigoproduto = QtGui.QLineEdit(self)
        self.txtcodigoproduto.setGeometry(20,50, 150, 21)

        self.btnatualizar = QtGui.QPushButton('Atualizar',self)
        self.btnatualizar.setGeometry(520,45, 120, 28)
        self.btnatualizar.clicked.connect(self.Atualizar)
        self.btnatualizar.setIcon(QtGui.QIcon('up.png'))

       
        
        self.lblcoluna =QtGui.QLabel("Colunas",self)
        self.lblcoluna.setGeometry(220, 23, 141, 18)
        
        self.cb = QtGui.QComboBox(self)
        self.cb.setGeometry(180, 50, 160, 21)
        self.cb.addItem("Nome",self)
        self.cb.addItem("UnidadedeMedida",self)
        self.cb.addItem("Peso",self)
        self.cb.addItem("CodigoEAN",self)
        self.cb.addItem("CodigoMoeda",self)
        self.cb.addItem("PrecoCompra",self)
        self.cb.addItem("ValorVenda",self)
    
        self.lblnovoitem =QtGui.QLabel("Novo Item",self)
        self.lblnovoitem.setGeometry(390, 25, 141, 18)
        self.txtnovoitem  = QtGui.QLineEdit(self)
        self.txtnovoitem .setGeometry(350, 50, 160, 21)
        

    def Atualizar(self):
        text = self.cb.currentText()
        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        comando =("select Codigo from  LojaDB.Produtos " " WHERE Codigo = %s " )
        fui = self.txtcodigoproduto.text() 
        cursor.execute (comando,fui)
        registros = cursor.fetchall()
        for registros in registros:
            
            rui = registros[0]
        try:
            rui
            deletar=("carro")
        except NameError:
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            " Código Não Existente ?",
                                            QtGui.QMessageBox.Ok)
            print ("Bem, não foi definido depois de tudo!")
        
        
        
        
        else:
         
            if text == "ValorVenda":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Produtos " " set  ValorVenda = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = float(self.txtnovoitem.text())
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('ja foi')

                cursor.close()
                db.close 
            
            elif text == "UnidadedeMedida":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Produtos " " set  UnidadedeMedada = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo =self.txtcodigoproduto.text()
                varvalor = float (self.txtcodigoproduto.text())
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('atualisou')

                cursor.close()
                db.close
            
            elif text == "Nome":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Produtos " " set  Nome = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor =  self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
        
            elif text == "Peso":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Produtos " " set  Peso = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = float(self.txtnovoitem.text())
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
        
            elif text == "CodigoEAN":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Produtos " " set  CodigoEAN = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
        
            elif text == "CodigoMoeda":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Produtos " " set  CodigoMoeda = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
            
            elif text == "PrecoCompra":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Produtos " " set  PrecoCompra = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = float(self.txtnovoitem.text())
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
            
            elif text == "ValorVenda":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Produtos " " set  ValorVenda = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo =self.txtcodigoproduto.text()
                varvalor = float(self.txtnovoitem.text())
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
            else:
                print("nao tem ")
    
            choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            " Código atualizado ?",
                                            QtGui.QMessageBox.Ok)
            print ("Bem, não foi definido depois de tudo!")
            
                    
    
         
         

       
        
def main():
    app = QtGui.QApplication(sys.argv)
    ui = ClasseAPP()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()