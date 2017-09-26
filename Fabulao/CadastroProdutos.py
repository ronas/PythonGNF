# -*- coding: latin -*-
import sys

from PyQt4 import QtGui

import pymysql

config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'LojaDB',
    'user': 'root',
    'password' : 'fbl1978'
}

class ClasseAPP(QtGui.QWidget):

    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Produtos')
        self.resize(300, 150)
        self.move(300, 300)

        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblNome = QtGui.QLabel('Nome')
        self.lblUnidadeMedida = QtGui.QLabel('UnidadeMedida')
        self.lblPeso = QtGui.QLabel('Peso')
        self.lblCodigoEAN = QtGui.QLabel('CodigoEAN')
        self.lblCodigoMoeda = QtGui.QLabel('CodigoMoeda')
        self.lblPrecoCompra = QtGui.QLabel('PrecoCompra')
        self.lblValorVenda = QtGui.QLabel('ValorVenda')
        self.txtCodigo = QtGui.QLineEdit()
        self.txtNome = QtGui.QLineEdit()
        self.txtUnidadeMedida = QtGui.QLineEdit()
        self.txtPeso = QtGui.QLineEdit()
        self.txtCodigoEAN = QtGui.QLineEdit()
        self.txtCodigoMoeda = QtGui.QLineEdit()
        self.txtPrecoCompra = QtGui.QLineEdit()
        self.txtValorVenda = QtGui.QLineEdit()

        self.btnBuscar = QtGui.QPushButton('Buscar' ,self)
        self.btnBuscar.clicked.connect(self.dbMostrarProdutos)
        self.btnSair = QtGui.QPushButton('Sair' ,self)
        self.btnSair.clicked.connect(self.Sair)
        self.btnIncluir = QtGui.QPushButton('Incluir' ,self)
        self.btnIncluir.clicked.connect(self.dbIncluirProdutos)
        self.btnExcluir = QtGui.QPushButton('Excluir' ,self)
        self.btnExcluir.clicked.connect(self.dbExcluirProdutos)
        self.btnAtualizar = QtGui.QPushButton('Atualizar' ,self)
        self.btnAtualizar.clicked.connect(self.dbAtualizarProdutos)
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)  

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
        self.grid.addWidget(self.lblValorVenda,8,0)
        self.grid.addWidget(self.txtValorVenda,8,1)
        self.grid.addWidget(self.btnSair,9,1)
        self.grid.addWidget(self.btnBuscar,9,0)
        self.grid.addWidget(self.btnIncluir,10,1)
        self.grid.addWidget(self.btnExcluir,10,0)
        self.grid.addWidget(self.btnAtualizar,11,1)
        self.setLayout(self.grid)
        self.show()

    def dbIncluirProdutos(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ( 
            "INSERT INTO LojaDB.Produtos (Codigo, Nome, UnidadeMedida, Peso, CodigoEAN, CodigoMoeda, CodigoCompra, ValorVenda) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )


        dados = (self.txtCodigo.text(),self.txtNome.text())

        cursor.execute(comando, dados)
        db.commit()

        cursor.close()
        db.close()

    def dbExcluirProdutos(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ('delete * from LojaDB.Produtos'
        "where codigo = (%s) "
        )

        dados = (self.txtCodigo.text, self.txtNome.text())

        cursor.execute(comando, dados)
        db.commit()

        cursor.close()
        db.close()

    def dbAtualizarProdutos(self):
        
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        comando = ('update * LojaDB.Produtos '
        'set precocompra = %s  where codigo =  %s '
        )
        
        dados = (self.txtCodigo.text, self.txtNome.text())

        cursor.execute(comando, dados)
        db.commit()

        cursor.close
        db.close()

    def dbMostrarProdutos(self):

        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = 'select * from LojaDB.Produtos'
        cursor.execute(comando, dados)
        db.commit()

        cursor.close()
        db.close()

        for registro in registros:
            self.txtCodigo.setText(registro[0])
            self.txtNome.setText(registro[1])
            self.txtUnidadeMedida.setText(registro[2])
            self.txtPeso.setText(str(registro[3]))
            self.txtCodigoEAN.setText(registro[4])
            self.txtCodigoMoeda.setText(registro[5])
            self.txtPrecoCompra.setText(str(registro[6]))
            self.txtValorVenda.setText(str(registro[7]))
            self.txtIncluir.text(registro[8])
            self.txtExcluir.Text(registro[9])
            self.txtAtualizar.Text(registro[10])
            break
    
    def Sair(self):
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)
    MeuApp = ClasseAPP()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()