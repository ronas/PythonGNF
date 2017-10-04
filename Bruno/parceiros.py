
import sys
from PyQt4 import QtCore,QtGui

import pymysql






comfig ={'host':'localhost',
         'port':3306,
         'database':'LojaDB',
         'user':'root',
         'password':'34387'}
db= pymysql.connect(** comfig)
cursor = db.cursor()



  
class ClasseAPP(QtGui.QWidget):
     
    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):
        super(ClasseAPP, self).__init__()
        self.setGeometry(300,100,0,0)
        self.setFixedSize(790,657)
        self.setWindowTitle("Cadastro de Parceiros ")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        
        self.home()
        
    def home(self):    
        
        
        self.pic = QtGui.QLabel(self)
       
        self.pic.setPixmap(QtGui.QPixmap("user-group-icon.png"))
        self.pic.setGeometry(650, 5, 300,110)
        

    
        self.lblcodigo = QtGui.QLabel("Codigo",self)
        self.lblcodigo.setGeometry(30, 40, 71, 18)
       
        self.txtcodigo = QtGui.QLineEdit(self)
        self.txtcodigo.setGeometry(30, 60, 113, 21)
       
        self.lblcnpj = QtGui.QLabel("CNPJ",self)
        self.lblcnpj.setGeometry(30, 90, 71, 18)
        
        self.txtendereco = QtGui.QLineEdit(self)
        self.txtendereco.setGeometry(30, 160, 341, 21)
        
       
        self.txtrazao = QtGui.QLineEdit(self)
        self.txtrazao.setGeometry(230, 110, 491, 21)
        
        
        
        self.lblrazao = QtGui.QLabel("Razão",self)
        self.lblrazao.setGeometry(230, 90, 71, 18)
        
        self.txtcnpj = QtGui.QLineEdit(self)
        self.txtcnpj.setGeometry(30, 110, 181, 21)
       

        self.lblendereco = QtGui.QLabel("Endereço",self)
        self.lblendereco.setGeometry(30, 140, 71, 18)
        
       
        
      
        self.lblcep = QtGui.QLabel("CEP",self)
        self.lblcep.setGeometry(420, 140, 71, 18)
        
        self.txtcep = QtGui.QLineEdit(self)
        self.txtcep.setGeometry(30, 210, 181, 21)
        
       
       
        self.lblbairro = QtGui.QLabel("Bairro",self)
        self.lblbairro.setGeometry(30, 190, 71, 18)
        
        self.txtbairro = QtGui.QLineEdit(self)
        self.txtbairro.setGeometry(420, 160, 301, 21)
      
   
        self.lblcidade = QtGui.QLabel("Cidade",self)
        self.lblcidade.setGeometry(230, 190, 71, 18)
        
        self.txtcidade = QtGui.QLineEdit(self)
        self.txtcidade.setGeometry(230, 210, 151, 21)
      
        self.lblestado = QtGui.QLabel("Estado",self)
        self.lblestado.setGeometry(390, 190, 71, 18)
        
        self.txtestado = QtGui.QLineEdit(self)
        self.txtestado.setGeometry(390, 210, 151, 21)
        
        self.lblpais = QtGui.QLabel("Pais",self)
        self.lblpais.setGeometry(550, 190, 71, 18)
  
        self.txtpais = QtGui.QLineEdit(self)
        self.txtpais.setGeometry(550, 210, 171, 21)
        
        self.lblcontato = QtGui.QLabel("Contato",self)
        self.lblcontato.setGeometry(30, 240, 71, 18)
        
        self.txtcontato = QtGui.QLineEdit(self)
        self.txtcontato.setGeometry(30, 260, 181, 21)
        
        self.lbltelefone = QtGui.QLabel("Telefone",self)
        self.lbltelefone.setGeometry(230, 240, 71, 18)

        self.txttelefone = QtGui.QLineEdit(self)
        self.txttelefone.setGeometry(230, 260, 151, 21)
        
        self.lblemail = QtGui.QLabel("Email",self)
        self.lblemail.setGeometry(390, 240, 71, 18)
        
        self.txtemail = QtGui.QLineEdit(self)
        self.txtemail.setGeometry(390, 260, 331, 21)
        
        self.lbllimite = QtGui.QLabel("Limite de Credito ",self)
        self.lbllimite.setGeometry(30, 290, 131, 18)
        

        self.txtlimite = QtGui.QLineEdit(self)
        self.txtlimite.setGeometry(30, 310, 171, 21)
     
        self.lblaprovador = QtGui.QLabel("Aprovador Financeiro",self)
        self.lblaprovador.setGeometry(230, 290, 171, 18)
        
        self.txtaprovador = QtGui.QLineEdit(self)
        self.txtaprovador.setGeometry(230, 310, 151, 21)
      
        self.lblbloqueado = QtGui.QLabel('Bloqueado',self)
        self.lblbloqueado.setGeometry(410, 290, 91, 18)
        
        self.txtbloqueador = QtGui.QLineEdit(self)
        self.txtbloqueador.setGeometry(410, 310, 61, 21)
        
        
        
        
        self.tabela = QtGui.QTableWidget(3  ,20,self)
        self.tabela.setGeometry(30, 370, 691, 192)
        self.tabela.setColumnCount(15)
        self.tabela.setRowCount(15)
        self.tabela.setHorizontalHeaderLabels(('Código', 'Razao', 'CNPJ','Endereco',' Bairro  ','CEP','Cidade ','Estado','Pais','Contato','Telefone','Email','Limite De Credito','Aprovador de Financeira','Bloqueado' ))
        
       
        self.btninserir = QtGui.QPushButton("Inserir",self)
        self.btninserir.setGeometry(500, 310, 106, 28)
        self.btninserir.clicked.connect(self.InserirDados)
        self.btninserir.setIcon(QtGui.QIcon('add.png'))
        
        self.btninserir = QtGui.QPushButton("Consutar",self)
        self.btninserir.setGeometry(620, 310, 106, 28)
        self.btninserir.clicked.connect(self.create_comsuta)
        self.btninserir.setIcon(QtGui.QIcon('repeat.png'))
        
        self.btnatualizar = QtGui.QPushButton("Atualizar",self)
        self.btnatualizar.setGeometry(50, 600, 106, 28)
        self.btnatualizar.clicked.connect(self.ATualizar)
        self.btnatualizar.setIcon(QtGui.QIcon('up.png'))
        
        self.btnexcluir = QtGui.QPushButton("Excluir",self)
        self.btnexcluir.setGeometry(180, 600, 106, 28)
        self.btnexcluir.setIcon(QtGui.QIcon('remove.png'))
        self.create_comsuta()
        self.btnexcluir.clicked.connect(self.EXcluir)
        
        self.btnsair = QtGui.QPushButton('Sair',self)
        self.btnsair.setGeometry(310, 600, 106, 28)
        self.btnsair.setIcon(QtGui.QIcon('accept.png'))
        self.btnsair.clicked.connect(self.sair)
        self.TelaExcluir = Excluir(self)
        self.TelaAtulizar = Atualizar(self)
        
        self.show()
        
    def sair(self):
        print("Fim!!!")
        sys.exit()    
    def ATualizar(self):
        self.TelaAtulizar .exec_()
   
    def EXcluir(self):
        self.TelaExcluir.exec_()

        
        
    def InserirDados (self):
            
            db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
            cursor = db.cursor()
        
            
            comando =("insert into LojaDB .Paraceiros (Codigo,Razao,CNPJ,Endereco,Bairro,CEP,Cidade,Estado,Pais,Contato,Telefone,Email,LimiteDeCredito,AprovadorFinanceira,Bloqueado) "  " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" )  # meto
            
            

            
            pcodigo = self.txtcodigo.text()
            prazao = self.txtrazao.text()
            pcnpj = self. txtcnpj.text()
            pendereco = self.txtendereco.text()
            pcep = self.txtcep.text()
            pbairro = self.txtbairro.text()
            pcidade = self.txtcidade.text()
            pestado =self.txtestado.text()
            
            ppais = self.txtpais.text()
            pcontato = self.txtcontato.text()
            ptelefone = self. txttelefone.text()
           
            pemail = self.txtemail.text()
            plimite = float(self.txtlimite.text())
            paprovador = self.txtaprovador.text()
            pbloqueador =self.txtbloqueador.text()
        
            dados = (pcodigo,prazao,pcnpj,pendereco,pcep,pbairro,pcidade,pestado,ppais,pcontato,ptelefone,pemail,plimite,paprovador,pbloqueador)
                
            cursor.execute (comando,dados)

            db.commit()
            print('ja foi')

            cursor.close()
            db.close
    def create_comsuta (self):
        
        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        
        cursor.execute("select *from  LojaDB.Paraceiros")# comando mostrando itenis 
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
        comando =("select Codigo from   LojaDB .Paraceiros " " WHERE Codigo = %s " )
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
        
                comando=(" delete from  LojaDB .Paraceiros " " where Codigo = %s ")
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
        
        self.lblcoluna =QtGui.QLabel("Colunas",self)
        self.lblcoluna.setGeometry(220, 23, 141, 18)
        
        self.cb = QtGui.QComboBox(self)
        self.cb.setGeometry(180, 50, 160, 21)
        self.cb.addItem("CNPJ",self)
        self.cb.addItem("Razão",self)
        self.cb.addItem("Endereço",self)
        self.cb.addItem("CEP",self)
        self.cb.addItem("Bairro",self)
        self.cb.addItem("Cidade",self)
        self.cb.addItem("Estado",self)
    
        self.cb.addItem("Pais",self)
        self.cb.addItem("Contato",self)
        self.cb.addItem("Telefone",self)
        self.cb.addItem("Email",self)
        self.cb.addItem("Limite de credito",self)
        self.cb.addItem("Aprovador Financeiro",self)
        self.cb.addItem("Bloqueado",self)
    
    
        self.lblnovoitem =QtGui.QLabel("Novo Item",self)
        self.lblnovoitem.setGeometry(390, 25, 141, 18)
        self.txtnovoitem  = QtGui.QLineEdit(self)
        self.txtnovoitem .setGeometry(350, 50, 160, 21)
        
        self.btnatualizar = QtGui.QPushButton("Atualizar",self)
        self.btnatualizar.setGeometry(520,45, 120, 28)
        self.btnatualizar.clicked.connect(self.Atualizar)
        
    def Atualizar(self):
        text = self.cb.currentText()
        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        comando =("select Codigo from  LojaDB.Paraceiros  " " WHERE Codigo = %s " )
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
         
            if text == "Razão":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Razao = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('ja foi')

                cursor.close()
                db.close 
            
            elif text == "CNPJ":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  CNPJ = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor =  self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
            
            elif text == "Endereço":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Endereco = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor =  self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
        
            elif text == "CEP":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  CEP = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
        
            elif text == "Bairro":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Bairro = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
        
            elif text == "Cidade":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Cidade = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
            
            elif text == "Estado":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Estado = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
            
            elif text == "Contato":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Contato = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
                
            
            elif text == "Limite de credito":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  LimiteDeCredito = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = float(self.txtnovoitem.text())
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close                

            elif text == "Aprovador Financeiro":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  AprovadorFinanceira = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close  
                
            elif text == "Bloqueado":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Bloqueado = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close      
                
                
            elif text == "Email":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Email = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
                
            
            elif text == "Telefone":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Telefone = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo = self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
                dados =(varvalor,varcodigo)
                cursor.execute (comando,dados)
                db.commit()
                print('Atualizado')

                cursor.close()
                db.close
            
            elif text == "Pais":
                db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
                cursor = db.cursor()
                comando = ("update  LojaDB.Paraceiros  " " set  Pais = %s  where Codigo = %s ")
                text = self.cb.currentText()
                varcodigo =self.txtcodigoproduto.text()
                varvalor = self.txtnovoitem.text()
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