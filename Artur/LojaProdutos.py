# -*- coding: latin -*-
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
    
    def bdExcluirProdutos(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ("delete from LojaDB.Produtos "
                   "where Codigo = '%s' ")
        varcodigo = self.txtCodigoDeletar.text()
    
        cursor.execute(comando,varcodigo)
        db.commit()
        cursor.close()
        db.close()

    
    def bdInserirProdutos(self):
 
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando =(
            "insert into Produtos (Codigo,Nome,UnidadeMedida,Peso,CodigoEAN,CodigoMoeda,PrecoCompra,ValorVenda)"
            "values(%s,%s,%s,%s,%s,%s,%s,%s)"
            )
# Codigo  Nome  UnidadeMedida  Peso  CodigoEAN CodigoMoeda  PrecoCompra  ValorVenda 
        varcodigo = self.txtCodigo.text()   #QtGui.QLabel()   #QtGui.QLabel(self.txtCodigo)   #input(self.txtCodigo) 
        varnome = self.txtNome.text()   #QtGui.QLabel()   #QtGui.QLabel(self.txtNome)   #input(self.txtNome)
        varunidademedida = self.txtUnidadeMedida.text()   #QtGui.QLabel()   #QtGui.QLabel(self.txtUnidadeMedida)   #input(self.txtUnidadeMedida)
        varpeso = self.txtPeso.text()   #QtGui.QLabel()   #QtGui.QLabel(self.txtPeso)   #input(self.txtPeso)
        varcodigoean = self.txtCodigoEAN.text()   #QtGui.QLabel()   #QtGui.QLabel(self.txtCodigoEAN)   #input(self.txtCodigoEAN)
        varcodigomoeda = self.txtCodigoMoeda.text()   #QtGui.QLabel()   #QtGui.QLabel(self.txtCodigoMoeda)   #input(self.txtCodigoMoeda)
        varprecocompra = self.txtPrecoCompra.text()   #QtGui.QLabel()   #QtGui.QLabel(self.txtPrecoCompra)   #input(self.txtPrecoCompra)
        varvalorvenda = self.txtValorVenda.text()   #QtGui.QLabel()   #QtGui.QLabel(self.txtValorVenda)    #input(self.txtValorVenda)
        dados = (varcodigo,
                 varnome,
                 varunidademedida,
                 varpeso,
                 varcodigoean,
                 varcodigomoeda,
                 varprecocompra,
                 varvalorvenda)
        cursor.execute(comando,dados)
        db.commit()
        cursor.close
        db.close
        
    def bdAtualizarProdutos(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = (
            "update LojaDB.Produtos "
            "set precocompra = %s where codigo = %s "
            )
        varcodigo = self.txtCodigoAtualizar.text()
        varvalor = self.txtPrecoCompraAtualizar.text()
        dados =(varvalor, varcodigo)
        cursor.execute(comando, dados)
        db.commit()
        cursor.close
        db.close    
        
        
        
        
        
        
        
        
        
    
    def bdMostrarProdutos(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = 'select * from Produtos'
        cursor.execute(comando)
        registros = cursor.fetchall()
        for registro in registros:
            self.txtCodigo.setText(registro[0])
            self.txtNome.setText(registro[1])
            self.txtUnidadeMedida.setText(registro[2])
            self.txtPeso.setText(str(registro[3]))
            self.txtCodigoEAN.setText(registro[4])
            self.txtCodigoMoeda.setText(registro[5])
            self.txtPrecoCompra.setText(str(registro[6]))
            self.txtValorVenda.setText(str(registro[7]))
            
        cursor.close
        db.close 
         
    def __init__(self):
        super(classApp,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('SistemaLojinha5')
        self.resize(250,150)
        self.move(300,300)        
        
        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblNome = QtGui.QLabel('Nome')
        self.lblUnidadeMedida = QtGui.QLabel('UnidadeDeMedida')
        self.lblPeso = QtGui.QLabel('Peso')
        self.lblCodigoEAN = QtGui.QLabel('CodigoEAN')
        self.lblCodigoMoeda = QtGui.QLabel('CodigoMoeda')
        self.lblPrecoCompra = QtGui.QLabel('PrecoCompra')
        self.lblValorVenda = QtGui.QLabel('ValorVenda')
        self.lblCodigoDeletar = QtGui.QLabel('CodigoExcluir')
        self.lblCodigoAtualizar = QtGui.QLabel('CodigoAtualizar')
        self.lblPrecoCompraAtualizar = QtGui.QLabel('PrecoCompra')
        
        self.txtCodigo = QtGui.QLineEdit()
        self.txtNome = QtGui.QLineEdit()
        self.txtUnidadeMedida = QtGui.QLineEdit()
        self.txtPeso = QtGui.QLineEdit()
        self.txtCodigoEAN = QtGui.QLineEdit()
        self.txtCodigoMoeda = QtGui.QLineEdit()
        self.txtPrecoCompra = QtGui.QLineEdit()
        self.txtValorVenda = QtGui.QLineEdit()
        self.txtCodigoDeletar = QtGui.QLineEdit()
        self.txtCodigoAtualizar = QtGui.QLineEdit()
        self.txtPrecoCompraAtualizar = QtGui.QLineEdit()
        
        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(self.sair)
        self.btnBuscar = QtGui.QPushButton('Buscar',self)
        self.btnBuscar.clicked.connect(self.bdMostrarProdutos)
        self.btnInserir = QtGui.QPushButton('Inserir',self)
        self.btnInserir.clicked.connect(self.bdInserirProdutos)
        self.btnDeletar = QtGui.QPushButton('Deletar',self)
        self.btnDeletar.clicked.connect(self.bdExcluirProdutos)
        self.btnAtualizar = QtGui.QPushButton('Atualizar',self)
        self.btnAtualizar.clicked.connect(self.bdAtualizarProdutos)
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)         
# Codigo  Nome  UnidadeMedida  Peso  CodigoEAN CodigoMoeda  PrecoCompra  ValorVenda        
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
        self.grid.addWidget(self.lblPrecoCompra,6,0)
        self.grid.addWidget(self.txtPrecoCompra,6,1)
        self.grid.addWidget(self.lblValorVenda,7,0)
        self.grid.addWidget(self.txtValorVenda,7,1)
        
        self.grid.addWidget(self.btnSair,9,1)
        self.grid.addWidget(self.btnBuscar,9,0)
        self.grid.addWidget(self.btnInserir,9,2)
        self.grid.addWidget(self.lblCodigoDeletar,10,0)
        self.grid.addWidget(self.txtCodigoDeletar,10,1)
        self.grid.addWidget(self.btnDeletar,10,2)
        self.grid.addWidget(self.lblCodigoAtualizar,11,0)
        self.grid.addWidget(self.txtCodigoAtualizar,11,1)
        self.grid.addWidget(self.lblPrecoCompraAtualizar,12,0)
        self.grid.addWidget(self.txtPrecoCompraAtualizar,12,1)
        self.grid.addWidget(self.btnAtualizar,13,1)
        
        self.setLayout(self.grid)
        
        self.show()
    def sair(self):
        sys.exit 
        
def main():
    app = QtGui.QApplication(sys.argv)
    meuapp = classApp()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()                 