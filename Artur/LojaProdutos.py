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
            "insert into Produtos (Codigo,Nome,UnidadeMedida,Peso,CodigoEAN,CEP,CodigoMoeda,PrecoCompra,ValorVenda)"
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            )

        varExisteErro = False
        varcodigoin = self.txtCodigo.text()   
        if TestaFloat(varcodigoin) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O campo Codigo deve ser preenchido com apenas numeros e não deve conter virgulas.',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varnomein = self.txtNome.text()
        varunidademedidain = self.txtUnidadeMedida.text()
        varpesoin = self.txtPeso.text()
        if TestaFloat(varpesoin) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O campo Peso deve ser preenchido com apenas numeros e não deve conter virgulas.',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varpesoin = varpesoin.replace(',','.')
        varcodigoeanin = self.txtCodigoEAN.text()
        if TestaLength(varcodigoeanin,13) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O campo Codigo EAN deve possuir extamente 13 caracteres',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varcodigomoedain = self.txtCodigoMoeda.text()
        varprecocomprain = self.txtPrecoCompra.text()
        if TestaFloat(varprecocomprain) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O Preco Compra deve ser preenchido com apenas numeros e não deve conter virgulas.',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varprecocomprain = varprecocomprain.replace(',','.')
        varvalorvendain = self.txtValorVenda.text()
        if TestaFloat(varvalorvendain) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O campo Valor Venda deve ser preenchido com apenas numeros e não deve conter virgulas.',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varvalorvendain = varvalorvendain.replace(',','.')

        if self.txtCodigo.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Codigo esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtNome.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Nome esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtUnidadeMedida.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo UnidadeMedida esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtPeso.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Peso esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtCodigoEAN.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo CodigoEAN esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtCodigoMoeda.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo CodigoMoeda esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtPrecoCompra.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo PrecoCompra esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtValorVenda() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo ValorVenda esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True


        if varExisteErro == False:
            dados = (varcodigoin,varnomein,varunidademedidain,varpesoin,varcodigoeanin,varcodigomoedain,varprecocomprain,varvalorvendain)
            cursor.execute(comando,dados)
            db.commit()
            cursor.close
            db.close

    def bdAtualizarProdutos(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = (
            "update LojaDB.Produtos "
            "set Nome = %s,UnidadeMedida = %s,Peso = %s,CodigoEAN = %s,CodigoMoeda = %s,PrecoCompra = %s where Codigo = %s "
            )

        varcodigoat = self.txtCodigo.text()
        if TestaFloat(varcodigoat) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O campo Codigo deve ser preenchido com apenas numeros e não deve conter virgulas.',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varnomeat = self.txtNome.text() 
        varunidademedidaat = self.txtUnidadeMedida.text()
        varpesoat = self.txtPeso.text()
        if TestaFloat(varpesoat) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O campo Peso deve ser preenchido com apenas numeros e não deve conter virgulas.',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varpesoat = varpesoat.replace(',','.')
        varcodigoeanat = self.txtCodigoEAN.text()
        varcodigomoedaat = self.txtCodigoMoeda.text()
        varprecocompraat = self.txtPrecoCompra.text()
        if TestaFloat(varprecocompraat) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O campo Preco Compra deve ser preenchido com apenas numeros e não deve conter virgulas.',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varprecocompraat = varprecocompraat.replace(',','.')
        varvalorvendaat = self.txtValorVenda.text()
        if TestaFloat(varvalorvendaat) == False:
            choice = QtGui.QMessageBox.question(self,'Erro!','O campo Valor Venda deve ser preenchido com apenas numeros e não deve conter virgulas.',QtGui.QMessageBox.Ok  )
            varExisteErro = True 
        varvalorvendaat = varvalorvendaat.replace(',','.')

        varExisteErro = False

        if self.txtCodigo.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Codigo esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtNome.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Nome esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtUnidadeMedida.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo UnidadeMedida esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtPeso.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Peso esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtCodigoEAN.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo CodigoEAN esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtCodigoMoeda.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo CodigoMoeda esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtPrecoCompra.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo PrecoCompra esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtValorVenda() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo ValorVenda esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True



        if varExisteErro == False:

            dados = (varcodigoat,varnomeat,varunidademedidaat,varpesoat,varcodigoeanat,varcodigomoedaat,varprecocompraat,varvalorvendaat)
            cursor.execute(comando,dados)
            db.commit()
            cursor.close
            db.close    
                 
        
    def bdMostrarProdutos(self):

        db = pymysql.connect(**config)
        cursor = db.cursor()

        self.txtCodigo.setText(registro[0])
        self.txtNome.setText('')
        self.txtUnidadeMedida.setText('')
        self.txtPeso.setText('')
        self.CodigoEAN.setText('')
        self.txtCodigoMoeda.setText('')
        self.txtPrecoCompra.setText('')
        self.txtValorVenda.setText('')

        comando = ('select * from LojaDB.produtos where Codigo = %s ')
        dados = (self.txtCodigo.text())

        cursor.execute(comando, dados)

        registros = cursor.fetchall()
#Codigo,Razao,CNPJ,Endereco,Bairro,CEP,Cidade,Estado,Pais,Contato,Telefone,Email,LimiteDeCredito,AprovadorFinanceiro,Bloqueado
        for registro in registros:
            self.txtCodigo.setText(registro[0])
            self.txtNome.setText(registro[1])
            self.txtUnidadeMedida.setText(registro[2])
            self.txtPeso.setText(str(registro[3]))
            self.txtCodigoEAN.setText(registro[4])
            self.txtCodigoMoeda.setText(registro[5])
            self.txtPrecoCompra.setText(str(registro[6]))
            self.txtValorVenda.setText(str(registro[7]))

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

        self.lblCodigoDeletar = QtGui.QLabel('CodigoDeletar')
        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblNome = QtGui.QLabel('Nome')
        self.lblUnidadeMedida = QtGui.QLabel('UnidadeMedida')
        self.lblPeso = QtGui.QLabel('Peso')
        self.lblCodigoEAN = QtGui.QLabel('CodigoEAN')
        self.lblCodigoMoeda = QtGui.QLabel('CodigoMoeda')
        self.lblPrecoCompra = QtGui.QLabel('PrecoCompra')
        self.lblValorVenda = QtGui.QLabel('ValorVenda')

        self.txtCodigo = QtGui.QLineEdit()
        self.txtCodigo.setMaxLength(10)

        self.txtNome = QtGui.QLineEdit()
        self.txtNome.setMaxLength(50)

        self.txtUnidadeMedida = QtGui.QLineEdit()
        self.txtUnidadeMedida.setMaxLength(3)

        self.txtPeso = QtGui.QLineEdit()
        self.txtPeso.setMaxLength(8)

        self.txtCodigoEAN = QtGui.QLineEdit()
        self.txtCodigoEAN.setMaxLength(13)

        self.txtCodigoMoeda = QtGui.QLineEdit()
        self.txtCodigoMoeda.setMaxLength(3)

        self.txtPrecoCompra = QtGui.QLineEdit()
        self.txtPrecoCompra.setMaxLength(12)

        self.txtValorVenda = QtGui.QLineEdit()
        self.txtValorVenda.setMaxLength(12)

        self.txtCodigoDeletar = QtGui.QLineEdit()
        self.txtCodigoDeletar.setMaxLength(10)

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
        
        self.grid.addWidget(self.btnBuscar,17,0)
        self.grid.addWidget(self.btnInserir,17,1)
        self.grid.addWidget(self.btnAtualizar,17,2)
        self.grid.addWidget(self.btnDeletar,17,3)


        self.grid.addWidget(self.lblCodigo,2,0)
        self.grid.addWidget(self.txtCodigo,2,1)


        self.grid.addWidget(self.lblNome,3,0)
        self.grid.addWidget(self.txtNome,3,1)


        self.grid.addWidget(self.lblUnidadeMedida,4,0)
        self.grid.addWidget(self.txtUnidadeMedida,4,1)


        self.grid.addWidget(self.lblPeso,5,0)
        self.grid.addWidget(self.txtPeso,5,1)


        self.grid.addWidget(self.lblCodigoEAN,6,0)
        self.grid.addWidget(self.txtCodigoEAN,6,1)


        self.grid.addWidget(self.lblCodigoMoeda,7,0)
        self.grid.addWidget(self.txtCodigoMoeda,7,1)


        self.grid.addWidget(self.lblPrecoCompra,8,0)
        self.grid.addWidget(self.txtPrecoCompra,8,1)


        self.grid.addWidget(self.lblValorVenda,9,0)
        self.grid.addWidget(self.txtValorVenda,9,1)


        self.grid.addWidget(self.txtCodigoDeletar,1,1)

        self.grid.addWidget(self.lblCodigoDeletar,1,0)

        self.grid.addWidget(self.btnSair,10,0)
 
        self.setLayout(self.grid)
        
        self.show()
    def sair(self):
        sys.exit()

def TestaFloat(prmEntrada):
        try:
            varfloat = float(prmEntrada)
            return(True)
        
        except ValueError:
            return(False)

def TestaLength(prmEntrada,prmTamanho):
    if len(prmEntrada) < prmTamanho:
        return False



        
def main():
    app = QtGui.QApplication(sys.argv)
    meuapp = classApp()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()                     