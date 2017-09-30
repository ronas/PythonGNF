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

class ClasseAPP (QtGui.QWidget): 

    def __init__(self): 
        super(ClasseAPP, self).__init__() 
        self.initUI () 

    def initUI (self): 

        self.setWindowTitle ( 'Parceiros') 
        self.resize (250, 150) 
        self.move (300, 300) 

        self.lblCodigo = QtGui.QLabel('Codigo') 
        self.lblRazao = QtGui.QLabel('Razao') 
        self.lblApelido = QtGui.QLabel('Apelido')
        self.lblCNPJ = QtGui.QLabel('CNPJ')
        self.lblTipo = QtGui.QLabel('Tipo')
        self.lblEmail = QtGui.QLabel('Email')
        self.lblTelefone = QtGui.QLabel('Telefone') 
        self.txtCodigo = QtGui.QLineEdit() 
        self.txtRazao = QtGui.QLineEdit() 
        self.txtApelido = QtGui.QLineEdit()
        self.txtCNPJ = QtGui.QLineEdit()
        self.txtTipo = QtGui.QLineEdit() 
        self.txtEmail = QtGui.QLineEdit()
        self.txtTelefone = QtGui.QLineEdit()

        self.btnBuscar = QtGui.QPushButton('Buscar',self) 
        self.btnBuscar.clicked.connect(self.dbMostrarProdutos) 
        self.btnSair = QtGui.QPushButton('Sair',self) 
        self.btnSair.clicked.connect(self.Sair) 
        self.grid = QtGui.QGridLayout() 
        self.grid.setSpacing(10) 

        self.grid.addWidget (self.lblCodigo, 1,0) 
        self.grid.addWidget (self.txtCodigo,1,1) 
        self.grid.addWidget (self.lblRazao, 2,0) 
        self.grid.addWidget (self.txtRazao,2,1) 
        self.grid.addWidget (self.lblApelido,3,0) 
        self.grid.addWidget (self.txtApelido,3,1)
        self.grid.addWidget (self.lblCNPJ,4,0)
        self.grid.addWidget (self.txtCNPJ,4,1)
        self.grid.addWidget (self.lblTipo,5,0)
        self.grid.addWidget (self.txtTipo,5,1)
        self.grid.addWidget (self.lblEmail,6,0)
        self.grid.addWidget (self.txtEmail,6,1)
        self.grid.addWidget (self.lblTelefone,7,0)
        self.grid.addWidget (self.txtTelefone,7,1) 
        self.grid.addWidget (self.btnBuscar, 8,0) 
        self.grid.addWidget (self.btnSair, 8,1) 
        self.setLayout      (self.grid) 
        self.show () 

    def dbMostrarProdutos (self): 
        db = pymysql.connect (** config) 
        cursor = db.cursor () 
        Comando = 'SELECT * FROM Parceiros' 
        cursor.execute (Comando) 
        Registros = cursor.fetchall () 
        for registro in Registros: 

            self.txtCodigo.setText(registro[1]) 
            self.txtRazao.setText(registro [2]) 
            self.txtApelido.setText (str (registro [3]))
            self.txtCNPJ.setText (registro[4])
            self.txtTipo.setText(registro[5])
            self.txtEmail.setText(registro[6])
            self.TxtTelefone.setText(registro[7]) 
            break 

    def Sair (self): 
        sys.exit () 

def main(): 
    app = QtGui.QApplication (sys.argv) 
    MeuAPP = ClasseAPP () 
    sys.exit (app.exec_ ()) 

if __name__ == '__main__': 
    main() 
