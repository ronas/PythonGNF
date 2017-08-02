import sys
from PyQt4 import QtGui
import mysql.connector

config = {
    'host':'localhost',
    'port' : 3306,
    'database' : 'LojaDB',
    'user' : 'root',
    'password' : '12345'
    }
       
class SistemaBD(QtGui.QWidget):
     
    def __init__(self):
        super(SistemaBD, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Sistema Lojinha 0.1')
        self.resize(250, 150)
        self.move(300, 300)
   
        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblDescricao = QtGui.QLabel('Descricao')
        self.txtCodigo = QtGui.QLineEdit()
        self.txtDescricao = QtGui.QLineEdit()
    
        self.btnSair = QtGui.QPushButton('Sair', self)
        self.btnSair.clicked.connect(self.sair)
        
        self.btnBuscar = QtGui.QPushButton('Buscar', self)
        self.btnBuscar.clicked.connect(self.bdMostrarProdutos)
    
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
    
        self.grid.addWidget(self.lblCodigo, 1, 0)
        self.grid.addWidget(self.txtCodigo, 1, 1)
        self.grid.addWidget(self.lblDescricao, 2, 0)
        self.grid.addWidget(self.txtDescricao, 2, 1)
        self.grid.addWidget(self.btnBuscar, 3, 0)
        self.grid.addWidget(self.btnSair, 3, 1)
       
        self.setLayout(self.grid)
        self.show()

    def bdMostrarProdutos(self):
    
        db = mysql.connector.connect(**config)
        cursor = db.cursor() 
        comando = 'select * from Produtos' 
        cursor.execute(comando)
        registros = cursor.fetchall()
    
        for registro in registros:
            self.txtCodigo.setText( registro[0] )
            self.txtDescricao.setText( registro[1] )        
            break
    
        cursor.close
        db.close
        
    def sair(self):
        sys.exit()
    
def main():
    app = QtGui.QApplication(sys.argv)
    sbd = SistemaBD()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
