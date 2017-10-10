# -*- coding: latin -*- 

import sys 

import pymysql 

from PyQt4 import QtGui
 
config = {
    'host':'localhost',
    'port': 3306,
    'database': 'LojaDB',
    'user':'root',
    'password':'12345'
}
class classApp(QtGui.QWidget):

    def __init__(self):
        super(classApp,self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Sistema da Lojinha 0.1')
        self.resize(250,150)
        self.move(300,300)

        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblNome = QtGui.QLabel ('Nome')
        self.lblUnidadeMedida = QtGui.QLabel('Unidade da Medida')
        self.lblPeso = QtGui.QLabel('Peso')
        self.lblCodigoEAN = QtGui.QLabel('Codigo do EAN')
        self.lblCodigoMoeda = QtGui.QLabel('Codigo da Moeda')
        self.lblPrecoCompra = QtGui.QLabel('Preco de Compra')
        self.lblValorRenda = QtGui.QLabel('Valor da Compra')
        self.txtCodigo = QtGui.QLineEdit()
        self.txtNome = QtGui.QLineEdit()
        self.txtUnidadeMedida = QtGui.QLineEdit()
        self.txtPeso = QtGui.QLineEdit()
        self.txtCodigoEAN = QtGui.QLineEdit()
        self.txtCodigoMoeda = QtGui.QLineEdit()
        self.txtPrecoCompra = QtGui.QLineEdit()
        self.txtValorRenda = QtGui.QLineEdit()

        self.btnBuscar = QtGui.QLineEdit()
        self.btnBuscar = QtGui.QPushButton('Buscar',self)
        self.btnIncluir = QtGui.QLineEdit()
        self.btnIncluir = QtGui.QPushButton('Incluir',self)
        self.btnExcluir = QtGui.QLineEdit()
        self.btnExcluir = QtGui.QPushButton('Excluir',self)
        self.btnAtualizar = QtGui.QLineEdit()
        self.btnAtualizar = QtGui.QPushButton('Atualizar',self)
        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(self.sair)
        self.btnBuscar.clicked.connect(self.dbCadastrodeProdutos)
        self.btnIncluir.clicked.connect(self.dbCadastrodeProdutos)
        self.btnExcluir.clicked.connect(self.dbCadastrodeProdutos)
        self.btnAtualizar.clicked.connect(self.dbCadastrodeProdutos)

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(11)
        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1) 
        self.grid.addWidget(self.lblNome,2,0)
        self.grid.addWidget(self.txtNome,2,1)
        self.grid.addWidget(self.lblUnidadeMedida,3,0)
        self.grid.addWidget(self.txtUnidadeMedida,3,1)
        self.grid.addWidget(self.lblPeso,4,0)
        self.grid.addWidget(self.txtPeso,4,1)
        self.grid.addWidget(self.lblCodigoEAN,5,0)
        self.grid.addWidget(self.txtCodigoEAN,5,1)
        self.grid.addWidget(self.lblCodigoMoeda,6,0)
        self.grid.addWidget(self.txtCodigoMoeda,6,1)
        self.grid.addWidget(self.lblPrecoCompra,7,0)
        self.grid.addWidget(self.txtPrecoCompra,7,1)
        self.grid.addWidget(self.lblValorRenda,8,0)
        self.grid.addWidget(self.txtValorRenda,8,1)
        self.grid.addWidget(self.btnBuscar,9,0)
        self.grid.addWidget(self.btnAtualizar,9,1)
        self.grid.addWidget(self.btnIncluir,10,0)
        self.grid.addWidget(self.btnExcluir,10,1)
        self.grid.addWidget(self.btnSair,11,0)
        self.setLayout(self.grid)
        self.show()

    

    def dbCadastrodeProdutos(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        
        comando = (
            'INSERT INTO LojaDB.Produtos (Codigo,Nome,UnidadeMedida,Peso,CodigoEAN,CodigoMoeda,PrecoCompra,ValorRenda)'
            'VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        )

        dados = (self.txtCodigo.text(),
                self.txtNome.text(),
                self.txtUnidadeMedida.text(),
                self.txtPeso.text(),
                self.txtCodigoEAN.text(),
                self.txtCodigoMoeda.text(),
                self.txtPrecoCompra.text(),
                self.txtValorRenda.text())


    def sair(self):
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)
    MeuApp = classApp()
    sys.exit(app.exec_())
        
if __name__ == '__main__':

     main()

