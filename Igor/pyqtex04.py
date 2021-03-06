import sys
import pymysql

from PyQt4 import QtGui

config = {
    'host':'localhost',
    'port': 3306,
    'database':'LojaDB',
    'user':'admin',
    'password':'admin'
    }
  
class classApp(QtGui.QWidget):
     
    def __init__(self):
        super(classApp, self).__init__()
        self.initUI()

    def initUI(self):
        
        
        
        self.setWindowTitle('Sistema Lojinha 0.1')
        self.resize(250, 150)
        self.move(300, 300)
        
        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblDescricao = QtGui.QLabel('Descricao')
        self.lblValor = QtGui.QLabel('Valor')
        
        self.txtCodigo = QtGui.QLineEdit()
        self.txtDescricao = QtGui.QLineEdit()
        self.txtValor = QtGui.QLineEdit()
        
        self.btnbuscar=QtGui.QLineEdit()
        self.btnbuscar=QtGui.QPushButton('Buscar',self)
        self.btnbuscar.clicked.connect(self.dbMostrarProduto)
        
        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(self.sair)
       
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        
        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1)
        self.grid.addWidget(self.lblDescricao,2,0)
        self.grid.addWidget(self.txtDescricao,2,1)
        self.grid.addWidget(self.lblValor,3,0)
        self.grid.addWidget(self.txtValor,3,1)
        self.grid.addWidget(self.btnbuscar,4,0)
        self.grid.addWidget(self.btnSair,4,1)
        
        
        self.setLayout(self.grid)
        self.show()
        
    def sair(self):
        sys.exit()
    
    def dbMostrarProduto(self): 
        db = pymysql.connect (** config)
        cursor = db.cursor ()
        Comando = ('SELECT * FROM Produtos')
        cursor.execute (Comando)
        registros = cursor.fetchall()
        for registro in registros:
            self.txtCodigo.setText(registro[0])
            self.txtDescricao.setText(registro[1])
            self.txtValor.setText(registro[0])
            break       
       
def main():
    app = QtGui.QApplication(sys.argv)
    MeuAPP = classApp()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
