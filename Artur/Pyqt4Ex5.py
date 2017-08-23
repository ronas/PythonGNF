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
    
    def bdMostrarProdutos(self):

        db = pymysql.connect(**config)
        cursor = db.cursor() 
        comando = 'select * from Produtos' 
        cursor.execute(comando)
        registros = cursor.fetchall()
        for registro in registros:
            self.txtCodigo.setText(registro[0])
            self.txtNome.setText(registro[1])
            self.txtValor.setText(str(registro[2]))

        cursor.close
        db.close
    
    def __init__(self):
        super(classApp,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('SistemaLojinha3')
        self.resize(250,150)
        self.move(300,300)
        
        self.lblCodigo = QtGui.QLabel('codigo')
        self.lblNome = QtGui.QLabel('nome')
        self.lblValor = QtGui.QLabel('valor')
        self.txtCodigo = QtGui.QLineEdit()
        self.txtNome = QtGui.QLineEdit()
        self.txtValor = QtGui.QLineEdit()
        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(self.sair)
        self.btnBuscar = QtGui.QPushButton('Buscar',self)
        self.btnBuscar.clicked.connect(self.bdMostrarProdutos)
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1)
        self.grid.addWidget(self.lblNome,2,0)
        self.grid.addWidget(self.txtNome,2,1)
        self.grid.addWidget(self.lblValor,3,0)
        self.grid.addWidget(self.txtValor,3,1)
        self.grid.addWidget(self.btnSair,4,1)
        self.grid.addWidget(self.btnBuscar,4,0)
        
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
