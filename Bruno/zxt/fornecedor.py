import os,sys
from PyQt4 import QtCore,QtGui

import pymysql


comfig ={'host':'localhost',# criando metodo de entrada do Mysql
         'port':3306,
         'database':'lojaDB',
         'user':'root',
         'password':'34387'}
db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
cursor = db.cursor()



  
class ClasseAPP(QtGui.QWidget):
     
    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):

        super(ClasseAPP, self).__init__()
        #self.setGeometry(400, 100, 278, 247)
        self.setGeometry(300,200,0,0)
        self.setFixedSize(882, 500)
        self.setWindowTitle("Cadastro de Fornecedores")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        
        self.home()
        
    def home(self):
       
        self.lblnome = QtGui.QLabel("Nome:",self)
        self.lblnome.setGeometry(40, 60, 68, 17)
        self.txtnome = QtGui.QLineEdit(self)
        self.txtnome.setGeometry(130, 60, 341, 21)
        
        self.txtempresa = QtGui.QLineEdit(self)
        self.txtempresa.setGeometry(130, 90, 551, 21)
        self.lblempresa = QtGui.QLabel("Empresa:",self)
        self.lblempresa.setGeometry(40, 90, 68, 17)
        
        self.lblbairro = QtGui.QLabel("Bairro:",self)
        self.lblbairro.setGeometry(40, 150, 68, 17)   
        self.txtbairro = QtGui.QLineEdit(self)
        self.txtbairro.setGeometry(130, 150, 231, 21)     

       
        self.txtendereco = QtGui.QLineEdit(self)
        self.txtendereco.setGeometry(130, 120, 421,21)
        self.lblendereco = QtGui.QLabel("Endereço:",self)
        self.lblendereco.setGeometry(40, 120, 68, 17)
        
        
      
        self.lblnumero = QtGui.QLabel("N°:",self)
        self.lblnumero.setGeometry(560, 120, 31, 17)
        self.txtnumero = QtGui.QLineEdit(self)
        self.txtnumero.setGeometry(580, 120, 101, 21)
       
        self.txttelefone = QtGui.QLabel("Telefone:",self)
        self.txttelefone.setGeometry(40, 180, 68, 17)
        self.txttelefone= QtGui.QLineEdit(self)
        self.txttelefone.setGeometry(130, 180, 131, 21)

        
        self.lblcidade = QtGui.QLabel("Cidade:",self)
        self.lblcidade.setGeometry(370, 150, 68, 17)
        self.txtcidade = QtGui.QLineEdit(self)
        self.txtcidade.setGeometry(430, 150, 113, 21)
        

        
        self.txtestado = QtGui.QLineEdit(self)
        self.txtestado.setGeometry(610, 150, 71, 21)
        self.lblestado = QtGui.QLabel("Estado:",self)
        self.lblestado.setGeometry(550, 150, 68, 17)
        
        self.lblcelular = QtGui.QLabel("Celular:",self)
        self.lblcelular.setGeometry(270, 180, 68, 17)
        self.txtcelular = QtGui.QLineEdit(self)
        self.txtcelular.setGeometry(330, 180, 113, 21)
   
        self.lblcnpj = QtGui.QLabel("CNPJ:",self)
        self.lblcnpj.setGeometry(480, 60, 41, 17)
        self.txtcnpj = QtGui.QLineEdit(self)
        self.txtcnpj.setGeometry(550, 60, 131, 21)
        
        self.lblemail = QtGui.QLabel("Email:",self)
        self.lblemail.setGeometry(450, 180, 68, 17)
        self.txtemail = QtGui.QLineEdit(self)
        self.txtemail.setGeometry(502, 180, 181, 21)
       
        self.tabela = QtGui.QTableWidget(3,11,self)
        self.tabela.setGeometry(30, 210, 800, 211)
        self.tabela.setColumnCount(11)
        self.tabela.setRowCount(10)
        self.tabela.setHorizontalHeaderLabels(('Nome ', 'CNPJ', 'Empresa ','Endereço','Numero','Bairro','Cidade','Estado','Telefone','Celular','Email'   ))
       
        
        
        
        
        self.pic = QtGui.QLabel(self)
       
        self.pic.setGeometry(697, 55, 131, 150)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/users.png"))
        
    
        btnincluir = QtGui.QPushButton("&Incluir",self)
        btnincluir.setGeometry(20, 440, 115, 35)
        btnincluir.clicked.connect(self.create_new_windows)
        self.pio = QtGui.QLabel(self)
        self.pio.setGeometry(22, 445, 25, 27)
        self.pio.setPixmap(QtGui.QPixmap(os.getcwd() + "/add.png"))
        
        
       
        
        btnalterar = QtGui.QPushButton("&Alterar",self)
        btnalterar.setGeometry(140, 440, 115, 35)
        self.picou = QtGui.QLabel(self)
        self.picou.setGeometry(142, 445, 25, 27)
        self.picou.setPixmap(QtGui.QPixmap(os.getcwd() + "/accept.png"))
        
        
        
        btnatualizar = QtGui.QPushButton(" Atualizar ",self)
        btnatualizar.setGeometry(260, 440, 115, 35)
        btnatualizar.clicked.connect(self.create_comsuta)
        
        self.pico = QtGui.QLabel(self)
        self.pico.setGeometry(262, 445, 25, 27)
        self.pico.setPixmap(QtGui.QPixmap(os.getcwd() + "/up.png"))
        
        
        
        btnatualizar.clicked.connect(self.txtnome.clear)
        btnatualizar.clicked.connect(self.txtcnpj.clear)
        btnatualizar.clicked.connect(self.txtempresa.clear)
        btnatualizar.clicked.connect(self.txtendereco.clear)
        btnatualizar.clicked.connect(self.txtnumero.clear)
        btnatualizar.clicked.connect(self.txttelefone.clear)
        btnatualizar.clicked.connect(self.txtcelular.clear)
        btnatualizar.clicked.connect(self.txtemail.clear)
        btnatualizar.clicked.connect(self.txtbairro.clear)
        btnatualizar.clicked.connect(self.txtcidade.clear)
        btnatualizar.clicked.connect(self.txtestado.clear)
     
        
        
        
        btnsair = QtGui.QPushButton("&Sair",self)
        btnsair.setGeometry(730, 440, 105, 35)
        btnsair.clicked.connect(self.close_application)
        self.picoi = QtGui.QLabel(self)
        self.picoi.setGeometry(735, 445, 25, 27)
        self.picoi.setPixmap(QtGui.QPixmap(os.getcwd() + "/remove.png"))
        

        self.show()
    
    
    def close_application(self):
        print("Fim!!!")
        sys.exit()
    

    def create_new_windows (self):
        
        
        
        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        
        
        comando =("insert into lojaDB.fornecedordb (for_name,for_cnpj,for_empresa,for_endereco,for_numero,for_Bairro,for_cidade,for_estado,for_telefone,for_celular,for_email) " " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" )  # meto
            
        fornome = self.txtnome .text()

        forcnpj = int(self.txtcnpj.text())
        
        forempresa =self.txtempresa.text()
        
        forendereco = self.txtendereco.text()
        
        fornumero = int(self.txtnumero.text())
        
        forbairro = self.txtbairro.text()
        
        forcidade = self.txtcidade.text()
        
        forestado = self.txtestado.text()
        
        fortelefone =int(self.txttelefone.text())
        
        forcelular = int(self.txtcelular.text())
        
        foremail = self.txtemail.text()
        
        
 

       
        
       
        
        
        dados = (fornome ,forcnpj,forempresa,forendereco,fornumero ,forbairro,forcidade,forestado ,fortelefone,forcelular,foremail)
                
        cursor.execute (comando,dados)

        db.commit()
        print('ja foi')

        cursor.close()
        db.close
        
   
    def create_comsuta (self):



        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        
        cursor.execute("select *from  lojaDB.fornecedordb")# comando mostrando itenis 
        self.tabela.setRowCount(0)
        for row, form in enumerate(cursor):
            self.tabela.insertRow(row)
            for column, item in enumerate(form):
                #print(str(item))
                self.tabela.setItem(row, column, QtGui.QTableWidgetItem(str(item)))       
               


            
            db.commit()
            print('ja foi')

            cursor.close()
            db.close

      
    



def main():
    app = QtGui.QApplication(sys.argv)
    ui = ClasseAPP()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()