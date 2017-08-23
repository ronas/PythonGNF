import sys
import pymysql

from PyQt4 import QtGui
config = {
    'host':'localhost',
    'port': 3306,
    'database': 'LojaDB',
    'user': 'root',
    'password': '12345'
     }
class classApp(QtGui.QWidget):bay

    def __init__(self):
        super(classApp,self).__init__()
        self.initUI()
    
    def initUI(self):
        
        self.setWindowTitle('Sistema Lojinha 0.1')
        self.resize(250,150)
        self.move(300,300)
         
        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblDescricao = QtGui.QLabel('Descricao')
        self.lblRazao = QtGui.QLabel('Razao')
        self.lblApelido = QtGui.QLabel('Apelido')
        self.lblCNPJ = QtGui.QLabel('CNPJ')
        self.lblTipo = QtGui.QLabel('Tipo')
        self.lblEmail = QtGui.QLabel('Email')
        self.lblTelefone = QtGui.QLabel('Telefone')
        self.txtCodigo = QtGui.QLineEdit()
        self.txtDescricao = QtGui.QLineEdit()
        self.txtRazao = QtGui.QLineEdit()
        self.txtApelido = QtGui.QLineEdit()
        self.txtCNPJ = QtGui.QLineEdit()
        self.txtTipo = QtGui.QLineEdit()
        self.txtEmail = QtGui.QLineEdit()
        self.txtTelefone = QtGui.QLineEdit()
        self.btnBuscar= QtGui.QLineEdit()
        self.btnBuscar= QtGui.QPushButton('Buscar',self)
        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(self.sair)
        self.btnBuscar.clicked.connect(self.dbMostrarParceiros)
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1)  
        self.grid.addWidget(self.lblRazao,2,0)
        self.grid.addWidget(self.txtRazao,2,1)
        self.grid.addWidget(self.lblApelido,3,0)
        self.grid.addWidget(self.txtApelido,3,1)
        self.grid.addWidget(self.lblCNPJ,4,0)
        self.grid.addWidget(self.txtCNPJ,4,1)
        self.grid.addWidget(self.lblTipo,5,0)
        self.grid.addWidget(self.txtTipo,5,1)
        self.grid.addWidget(self.lblEmail,6,0)
        self.grid.addWidget(self.txtEmail,6,1)
        self.grid.addWidget(self.lblTelefone,7,0)
        self.grid.addWidget(self.txtTelefone,7,1)
        self.grid.addWidget(self.btnBuscar,8,0)
        self.grid.addWidget(self.btnSair,8,1)
       

        self.setLayout(self.grid)
        self.show()
        
    def sair(self):
        sys.exit()
    def dbMostrarParceiros(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = 'select*from Parceiros'
        cursor. execute(comando)
        registros = cursor.fetchall()
        for registro in registros:
            self.txtCodigo.setText(registro[0])
            self.txtRazao.setText(registro[1])
            self.txtApelido.setText(registro[2])
            self.txtCNPJ.setText(registro[3])
            self.txtTipo.setText(registro[4])
            self.txtEmail.setText(registro[5])
            self.txtTelefone.setText(registro[6])
            break

def main():
    app = QtGui.QApplication(sys.argv)
    MeuApp = classApp()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
     main()