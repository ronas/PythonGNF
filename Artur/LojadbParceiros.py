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
  
    def bdExcluirParceiros(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ("delete from LojaDB.Parceiros "
                   "where Codigo = (%s) ")
        varcodigodelete = self.txtCodigoDeletar.text()
    
        cursor.execute(comando,varcodigodelete)
        db.commit()
        cursor.close()
        db.close()


    def bdInserirParceiros(self):
 
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando =(
            "insert into Parceiros (Codigo,Razao,CNPJ,Endereco,Bairro,CEP,Cidade,Estado,Pais,Contato,Telefone,Email,LimiteDeCredito,AprovadorFinanceiro,Bloqueado)"
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            )

        varcodigoin = self.txtCodigo.text()
        varrazaoin = self.txtRazao.text()  
        varcnpjin = self.txtCNPJ.text()
        varenderecoin = self.txtEndereco.text()
        varbairroin = self.txtBairro.text()
        varcepin = self.txtCEP.text() 
        varcidadein = self.txtCidade.text()
        varestadoin = self.txtEstado.text()
        varpaisin = self.txtPais.text()
        varcontatoin = self.txtContato.text()
        vartelefonein = self.txtTelefone.text()
        varemailin = self.txtEmail.text()
        varlimitedecreditoin = self.txtLimiteDeCredito.text()
        varaprovadorfinanceiroin = self.txtAprovadorFinanceiro.text() 
        varbloqueadoin = self.txtBloqueado.text()

        varExisteErro = False

        if self.txtCodigo.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Codigo esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtRazaoIn.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Razao esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtCNPJ.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo CNPJ esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtEndereco.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Endereco esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtBairro.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Bairro esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtCEP.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo CEP esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtCidade.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Cidade esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtEstadoIn.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Estado esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtPais.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Pais esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtContatoIn.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Contato esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtTelefone.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Telefone esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtEmail.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Email esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtLimiteDeCredito.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo LimiteDeCredito esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtAprovadorFinanceiro.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo AprovadoFinanceiro esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        if self.txtBloqueado.text() == '':
            choice = QtGui.QMessageBox.question(self,'Aviso!','O campo Bloqueado esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok  )
            varExisteErro = True

        


        if varExisteErro == False:
            dados = (varcodigoin,varrazaoin,varcnpjin,varenderecoin,varbairroin,varcepin,varcidadein,varestadoin,varpaisin,varcontatoin,vartelefonein,varemailin,varlimitedecreditoin,varaprovadorfinanceiroin,varbloqueadoin)
            cursor.execute(comando,dados)
            db.commit()
            cursor.close
            db.close

    def bdAtualizarParceiros(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = (
            "update LojaDB.Parceiros "
            "set Razao = %s,CNPJ = %s,Endereco = %s,Bairro = %s,CEP = %s,Cidade = %s,Estado = %s,Pais = %s,Contato = %s,Telefone = %s,Email = %s,LimiteDeCredito = %s,AprovadorFinanceiro = %s,Bloqueado = %s where Codigo = %s "
            )
#Codigo,Razao,CNPJ,Endereco,Bairro,CEP,Cidade,Estado,Pais,Contato,Telefone,Email,LimiteDeCredito,AprovadorFinanceiro,Bloqueado
        varcodigoat = self.txtCodigo.text()
        varrazaoat = self.txtRazao.text() 
        varcnpjat = self.txtCNPJ.text()
        varenderecoat = self.txtEndereco.text()
        varbairroat = self.txtBairro.text()
        varcepat = self.txtCEP.text()
        varcidadeat = self.txtCidade.text()
        varestadoat = self.txtEstado.text()
        varpaisat = self.txtPais.text()
        varcontatoat = self.txtContato.text()
        vartelefoneat = self.txtTelefone.text()
        varemailat = self.txtEmail.text()
        varlimitedecreditoat = self.txtLimiteDeCredito.text()
        varaprovadorfinanceiroat = self.txtAprovadorFinanceiro.text()
        varbloqueadoat = self.txtBloqueado.text()

        dados =(varrazaoat,varcnpjat,varenderecoat,varbairroat,varcepat,varcidadeat,varestadoat,varpaisat,varcontatoat,vartelefoneat,varemailat,varlimitedecreditoat,varaprovadorfinanceiroat,varbloqueadoat,varcodigoat)
        cursor.execute(comando,dados)
        db.commit()
        cursor.close
        db.close    
                 
        
    def bdMostrarParceiros(self):

        db = pymysql.connect(**config)
        cursor = db.cursor()

        self.txtCodigo.setText(registro[0])
        self.txtRazao.setText('')
        self.txtCNPJ.setText('')
        self.txtEndereco.setText('')
        self.txtBairro.setText('')
        self.txtCEP.setText('')
        self.txtCidade.setText('')
        self.txtEstado.setText('')
        self.txtPais.setText('')
        self.txtContato.setText('')
        self.txtTelefone.setText('')
        self.txtEmail.setText('')
        self.txtLimiteDeCredito.setText('')
        self.txtAprovadorFinanceiro.setText('')
        self.txtBloqueado.setText('')

        comando = ('select * from LojaDB.parceiros where Codigo = %s ')
        dados = (self.txtCodigo.text())

        cursor.execute(comando, dados)

        registros = cursor.fetchall()
#Codigo,Razao,CNPJ,Endereco,Bairro,CEP,Cidade,Estado,Pais,Contato,Telefone,Email,LimiteDeCredito,AprovadorFinanceiro,Bloqueado
        for registro in registros:
            self.txtCodigo.setText(registro[0])
            self.txtRazao.setText(registro[1])
            self.txtCNPJ.setText(registro[2])
            self.txtEndereco.setText(registro[3])
            self.txtBairro.setText(registro[4])
            self.txtCEP.setText(registro[5])
            self.txtCidade.setText(registro[6])
            self.txtEstado.setText(registro[7])
            self.txtPais.setText(registro[8])
            self.txtContato.setText(registro[9])
            self.txtTelefone.setText(registro[10])
            self.txtEmail.setText(registro[11])
            self.txtLimiteDeCredito.setText(str(registro[12]))
            self.txtAprovadorFinanceiro.setText(registro[13])
            self.txtBloqueado.setText(registro[14])
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
        self.lblRazao = QtGui.QLabel('Razao')
        self.lblCNPJ = QtGui.QLabel('CNPJ')
        self.lblEndereco = QtGui.QLabel('Endereco')
        self.lblBairro = QtGui.QLabel('Bairro')
        self.lblCEP = QtGui.QLabel('CEP')
        self.lblCidade = QtGui.QLabel('Cidade')
        self.lblEstado = QtGui.QLabel('Estado')
        self.lblPais = QtGui.QLabel('Pais')
        self.lblContato = QtGui.QLabel('Contato')
        self.lblTelefone = QtGui.QLabel('Telefone')
        self.lblEmail = QtGui.QLabel('Email')
        self.lblLimiteDeCredito = QtGui.QLabel('LimiteDeCredito')
        self.lblAprovadorFinanceiro = QtGui.QLabel('AprovadorFinanceiro')
        self.lblBloqueado = QtGui.QLabel('Bloqueado')

        self.txtCodigo = QtGui.QLineEdit()
        self.txtRazao = QtGui.QLineEdit()
        self.txtCNPJ = QtGui.QLineEdit()
        self.txtEndereco = QtGui.QLineEdit()
        self.txtBairro = QtGui.QLineEdit()
        self.txtCEP = QtGui.QLineEdit()
        self.txtCidade = QtGui.QLineEdit()
        self.txtEstado = QtGui.QLineEdit()
        self.txtPais = QtGui.QLineEdit()
        self.txtContato = QtGui.QLineEdit()
        self.txtTelefone = QtGui.QLineEdit()
        self.txtEmail = QtGui.QLineEdit()
        self.txtLimiteDeCredito = QtGui.QLineEdit()
        self.txtAprovadorFinanceiro = QtGui.QLineEdit()
        self.txtBloqueado = QtGui.QLineEdit()



        self.txtCodigoDeletar = QtGui.QLineEdit()

        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(self.sair)
        self.btnBuscar = QtGui.QPushButton('Buscar',self)
        self.btnBuscar.clicked.connect(self.bdMostrarParceiros)
        self.btnInserir = QtGui.QPushButton('Inserir',self)
        self.btnInserir.clicked.connect(self.bdInserirParceiros)
        self.btnDeletar = QtGui.QPushButton('Deletar',self)
        self.btnDeletar.clicked.connect(self.bdExcluirParceiros)
        self.btnAtualizar = QtGui.QPushButton('Atualizar',self)
        self.btnAtualizar.clicked.connect(self.bdAtualizarParceiros)
        
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)         
        
        self.grid.addWidget(self.btnBuscar,17,0)
        self.grid.addWidget(self.btnInserir,17,1)
        self.grid.addWidget(self.btnAtualizar,17,2)
        self.grid.addWidget(self.btnDeletar,17,3)


        self.grid.addWidget(self.lblCodigo,2,0)
        self.grid.addWidget(self.txtCodigo,2,1)


        self.grid.addWidget(self.lblRazao,3,0)
        self.grid.addWidget(self.txtRazao,3,1)


        self.grid.addWidget(self.lblCNPJ,4,0)
        self.grid.addWidget(self.txtCNPJ,4,1)


        self.grid.addWidget(self.lblEndereco,5,0)
        self.grid.addWidget(self.txtEndereco,5,1)


        self.grid.addWidget(self.lblBairro,6,0)
        self.grid.addWidget(self.txtBairro,6,1)


        self.grid.addWidget(self.lblCEP,7,0)
        self.grid.addWidget(self.txtCEP,7,1)


        self.grid.addWidget(self.lblCidade,8,0)
        self.grid.addWidget(self.txtCidade,8,1)


        self.grid.addWidget(self.lblEstado,9,0)
        self.grid.addWidget(self.txtEstado,9,1)


        self.grid.addWidget(self.lblPais,10,0)
        self.grid.addWidget(self.txtPais,10,1)


        self.grid.addWidget(self.lblContato,11,0)
        self.grid.addWidget(self.txtContato,11,1)


        self.grid.addWidget(self.lblTelefone,12,0)
        self.grid.addWidget(self.txtTelefone,12,1)


        self.grid.addWidget(self.lblEmail,13,0)
        self.grid.addWidget(self.txtEmail,13,1)


        self.grid.addWidget(self.lblLimiteDeCredito,14,0)
        self.grid.addWidget(self.txtLimiteDeCredito,14,1)


        self.grid.addWidget(self.lblAprovadorFinanceiro,15,0)
        self.grid.addWidget(self.txtAprovadorFinanceiro,15,1)

        self.grid.addWidget(self.lblBloqueado,16,0)
        self.grid.addWidget(self.txtBloqueado,16,1)


        self.grid.addWidget(self.txtCodigoDeletar,1,1)

        self.grid.addWidget(self.lblCodigoDeletar,1,0)

        self.grid.addWidget(self.btnSair,18,0)
 
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