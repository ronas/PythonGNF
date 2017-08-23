import sys

import pymysql

from PyQt4 import QtGui

config = {
    'host':'localhost',
    'port' : 3306,
    'database' : 'LojaDB',
    'user' : 'root',
    'password' : 'admin'
    }

def sair():
    sys.exit() 

class classApp(QtGui.QWidget):
    
    def bdMostrarParceiros(self):

        db = pymysql.connect(**config)
        cursor = db.cursor() 
        comando = 'select * from Parceiros' 
        cursor.execute(comando)
        registros = cursor.fetchall()
        for registro in registros:
            self.txtCodigo.setText(registro[0])
            self.txtRazao.setText(registro[1])
            self.txtApelido.setText(str(registro[2]))
            self.txtCnpj.setText(registro[3])
            self.txtTipo.setText(registro[4])
            self.txtEmail.setText(registro[5])
            self.txtTelefone.setText(registro[6])                        

        cursor.close
        db.close
    
    def __init__(self):
        super(classApp,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('SistemaLojinha4')
        self.resize(250,150)
        self.move(300,300)
        
        self.lblCodigo = QtGui.QLabel('codigo')
        self.lblRazao = QtGui.QLabel('razao')
        self.lblApelido = QtGui.QLabel('apelido')
        self.lblCnpj = QtGui.QLabel('cnpj')
        self.lblTipo = QtGui.QLabel('tipo')
        self.lblEmail = QtGui.QLabel('email')
        self.lblTelefone = QtGui.QLabel('telefone')
        self.txtCodigo = QtGui.QLineEdit()
        self.txtRazao = QtGui.QLineEdit()
        self.txtApelido = QtGui.QLineEdit()
        self.txtCnpj = QtGui.QLineEdit()
        self.txtTipo = QtGui.QLineEdit()
        self.txtEmail = QtGui.QLineEdit()
        self.txtTelefone = QtGui.QLineEdit()
        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(self.sair)
        self.btnBuscar = QtGui.QPushButton('Buscar',self)
        self.btnBuscar.clicked.connect(self.bdMostrarParceiros)
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1)
        self.grid.addWidget(self.lblRazao,2,0)
        self.grid.addWidget(self.txtRazao,2,1)
        self.grid.addWidget(self.lblApelido,3,0)
        self.grid.addWidget(self.txtApelido,3,1)
        self.grid.addWidget(self.lblCnpj,4,0)
        self.grid.addWidget(self.txtCnpj,4,1)
        self.grid.addWidget(self.lblTipo,5,0)
        self.grid.addWidget(self.txtTipo,5,1)
        self.grid.addWidget(self.lblEmail,6,0)
        self.grid.addWidget(self.txtEmail,6,1)
        self.grid.addWidget(self.lblTelefone,7,0)
        self.grid.addWidget(self.txtTelefone,7,1)
        self.grid.addWidget(self.btnSair,9,1)
        self.grid.addWidget(self.btnBuscar,9,0)
        
        self.setLayout(self.grid)
        
        self.show()
    def sair(self):
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)
    meuapp = classApp()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()     
