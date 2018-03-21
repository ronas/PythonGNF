# -*- coding: latin -*-
import sys

import pymysql

from PyQt4 import QtGui

config = {
    'host':'localhost',
    'port' : 3306,
    'database' : 'LojaDB',
    'user' : 'root',
    'password' : ''
    }
    
class classApp(QtGui.QWidget):
    
    def bdExcluirProdutos(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ("delete from LojaDB.Produtos "
                   "where Codigo = (%s) ")
        varcodigodelete = self.txtCodigoDeletar.text()
    
        cursor.execute(comando,varcodigodelete)
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
#correto
        varcodigoin = self.txtCodigoIn.text()
        varnomein = self.txtNomeIn.text()  
        varunidademedidain = self.txtUnidadeMedidaIn.text()
        varpesoin = self.txtPesoIn.text()
        varcodigoeanin = self.txtCodigoEANIn.text()
        varcodigomoedain = self.txtCodigoMoedaIn.text() 
        varprecocomprain = self.txtPrecoCompraIn.text()
        varvalorvendain = self.txtValorVendaIn.text() 

        varExisteErro = False

        if self.txtCodigoIn.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Codigo esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True




        if varExisteErro = False
            dados = (varcodigoin,
                    varnomein,
                    varunidademedidain,
                    varpesoin,
                    varcodigoeanin,
                    varcodigomoedain,
                    varprecocomprain,
                    varvalorvendain)
            cursor.execute(comando,dados)
            db.commit()
            cursor.close
            db.close

    def bdAtualizar(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = (
            "update LojaDB.Produtos "
            "set Nome = %s,UnidadeMedida = %s,Peso = %s,CodigoEAN = %s,CodigoMoeda = %s,PrecoCompra = %s,ValorVenda = %s where Codigo = %s "
            )
        varcodigoat = self.txtCodigoAt.text()
        varnomeat = self.txtNomeAt.text() 
        varunidademedidaat = self.txtUnidadeMedidaAt.text()
        varpesoat = self.txtPesoAt.text()
        varcodigoeanat = self.txtCodigoEANAt.text()
        varcodigomoedaat = self.txtCodigoMoedaAt.text()
        varprecocompraat = self.txtPrecoCompraAt.text()
        varvalorvendaat = self.txtValorVendaAt.text()

        dados =(varnomeat,varunidademedidaat,varpesoat,varcodigoeanat,varcodigomoedaat,varprecocompraat,varvalorvendaat,varcodigoat)
        cursor.execute(comando,dados)
        db.commit()
        cursor.close
        db.close    
                 
        
    def bdMostrarProdutos(self):

        db = pymysql.connect(**config)
        cursor = db.cursor()

        comando = ('select * from LojaDB.produtos where Codigo = %s ')
        dados = (self.txtCodigoM.text())

        cursor.execute(comando, dados)

        registros = cursor.fetchall()

        for registro in registros:
            self.txtCodigoM.setText(registro[0])
            self.txtNomeM.setText(registro[1])
            self.txtUnidadeMedidaM.setText(registro[2])
            self.txtPesoM.setText(str(registro[3]))
            self.txtCodigoEANM.setText(registro[4])
            self.txtCodigoMoedaM.setText(registro[5])
            self.txtPrecoCompraM.setText(str(registro[6]))
            self.txtValorVendaM.setText(str(registro[7]))
            break

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

        
        
        self.txtCodigoIn = QtGui.QLineEdit()
        self.txtNomeIn = QtGui.QLineEdit()
        self.txtUnidadeMedidaIn = QtGui.QLineEdit()
        self.txtPesoIn = QtGui.QLineEdit()
        self.txtCodigoEANIn = QtGui.QLineEdit()
        self.txtCodigoMoedaIn = QtGui.QLineEdit()
        self.txtPrecoCompraIn = QtGui.QLineEdit()
        self.txtValorVendaIn = QtGui.QLineEdit()

        self.txtCodigoAt = QtGui.QLineEdit()
        self.txtNomeAt = QtGui.QLineEdit()
        self.txtUnidadeMedidaAt = QtGui.QLineEdit()        
        self.txtPesoAt = QtGui.QLineEdit()
        self.txtCodigoEANAt = QtGui.QLineEdit()
        self.txtCodigoMoedaAt = QtGui.QLineEdit()
        self.txtPrecoCompraAt = QtGui.QLineEdit()
        self.txtValorVendaAt = QtGui.QLineEdit()

        self.txtCodigoM = QtGui.QLineEdit()
        self.txtNomeM = QtGui.QLineEdit()
        self.txtUnidadeMedidaM = QtGui.QLineEdit()
        self.txtPesoM = QtGui.QLineEdit()
        self.txtCodigoEANM = QtGui.QLineEdit()
        self.txtCodigoMoedaM = QtGui.QLineEdit()
        self.txtPrecoCompraM = QtGui.QLineEdit()
        self.txtValorVendaM = QtGui.QLineEdit()

        self.txtCodigoDeletar = QtGui.QLineEdit()

        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(self.sair)
        self.btnBuscar = QtGui.QPushButton('Buscar',self)
        self.btnBuscar.clicked.connect(self.bdMostrarProdutos)
        self.btnInserir = QtGui.QPushButton('Inserir',self)
        self.btnInserir.clicked.connect(self.bdInserirProdutos)
        self.btnDeletar = QtGui.QPushButton('Deletar',self)
        self.btnDeletar.clicked.connect(self.bdExcluirProdutos)
        self.btnAtualizar = QtGui.QPushButton('Atualizar',self)
        self.btnAtualizar.clicked.connect(self.bdAtualizar)
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)         
# Codigo  Nome  UnidadeMedida  Peso  CodigoEAN CodigoMoeda  PrecoCompra  ValorVenda        
        self.grid.addWidget(self.btnBuscar,1,1)
        self.grid.addWidget(self.btnInserir,1,2)
        self.grid.addWidget(self.btnAtualizar,1,3)


        self.grid.addWidget(self.lblCodigo,2,0)
        self.grid.addWidget(self.txtCodigoM,2,1)
        self.grid.addWidget(self.txtCodigoIn,2,2)
        self.grid.addWidget(self.txtCodigoAt,2,3)

        self.grid.addWidget(self.lblNome,3,0)
        self.grid.addWidget(self.txtNomeM,3,1)
        self.grid.addWidget(self.txtNomeIn,3,2)
        self.grid.addWidget(self.txtNomeAt,3,3)

        self.grid.addWidget(self.lblUnidadeMedida,4,0)
        self.grid.addWidget(self.txtUnidadeMedidaM,4,1)
        self.grid.addWidget(self.txtUnidadeMedidaIn,4,2)
        self.grid.addWidget(self.txtUnidadeMedidaAt,4,3)

        self.grid.addWidget(self.lblPeso,5,0)
        self.grid.addWidget(self.txtPesoM,5,1)
        self.grid.addWidget(self.txtPesoIn,5,2)
        self.grid.addWidget(self.txtPesoAt,5,3)

        self.grid.addWidget(self.lblCodigoEAN,6,0)
        self.grid.addWidget(self.txtCodigoEANM,6,1)
        self.grid.addWidget(self.txtCodigoEANIn,6,2)
        self.grid.addWidget(self.txtCodigoEANAt,6,3)

        self.grid.addWidget(self.lblCodigoMoeda,7,0)
        self.grid.addWidget(self.txtCodigoMoedaM,7,1)
        self.grid.addWidget(self.txtCodigoMoedaIn,7,2)
        self.grid.addWidget(self.txtCodigoMoedaAt,7,3)

        self.grid.addWidget(self.lblPrecoCompra,8,0)
        self.grid.addWidget(self.txtPrecoCompraM,8,1)
        self.grid.addWidget(self.txtPrecoCompraIn,8,2)
        self.grid.addWidget(self.txtPrecoCompraAt,8,3)

        self.grid.addWidget(self.lblValorVenda,9,0)
        self.grid.addWidget(self.txtValorVendaM,9,1)
        self.grid.addWidget(self.txtValorVendaIn,9,2)
        self.grid.addWidget(self.txtValorVendaAt,9,3)

        self.grid.addWidget(self.txtCodigoDeletar,10,1)

        self.grid.addWidget(self.btnDeletar,10,0)

        self.grid.addWidget(self.btnSair,10,2)
 
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