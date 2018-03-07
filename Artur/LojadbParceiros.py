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
        comando = ("delete from LojaDB.parceiros "
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
#Codigo,Razao,CNPJ,Endereco,Bairro,CEP,Cidade,Estado,Pais,Contato,Telefone,Email,LimiteDeCredito,AprovadorFinanceiro,Bloqueado
        varcodigoin = self.txtCodigoIn.text()
        varrazoin = self.txtRazaoIn.text()  
        varcnpjin = self.txtCNPJIn.text()
        varenderecoin = self.txtEnderecoIn.text()
        varbairroin = self.txtBairroIn.text()
        varcepin = self.txtCEPIn.text() 
        varcidadein = self.txtCidadeIn.text()
        varestadoin = self.txtEstadoIn.text()
        varpaisin = self.txtPaisIn.text()
        varcontatoin = self.txtContatoIn.text()
        vartelefonein = self.txtTelefoneIn.text()
        varemailin = self.txtEmailIn.text()
        varlimitedecreditoin = self.txtLimiteDeCreditoIn.text()
        varaprovadorfinanceiroin = self.txtAprovadorFinanceiroIn.text() 
        varbloqueadoin = self.txtBloqueadoIn.text()
        dados = (varcodigoin,
                 varrazaoin,
                 varcnpjin,
                 varenderecoin,
                 varbairroin,
                 varcepin,
                 varcidadein,
                 varestadoin,
                 varpaisin,
                 varcontatoin,
                 vartelefonein,
                 varemailin,
                 varlimitedecreditoin,
                 varbloqueadoin)
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
        varcodigoat = self.txtCodigoAt.text()
        varrazaoat = self.txtRazaoAt.text() 
        varcnpjat = self.txtCNPJAt.text()
        varenderecoat = self.txtEnderecoAt.text()
        varbairroat = self.txtBairroAt.text()
        varcepat = self.txtCEPAt.text()
        varcidadeat = self.txtCidadeAt.text()
        varestadoat = self.txtEstadoAt.text()
        varpaisat = self.txtPaisAt.text()
        varcontatoat = self.txtContatoAt.text()
        vartelefoneat = self.txtTelefoneAt.text()
        varemailat = self.txtEmailAt.text()
        varlimitedecreditoat = self.txtLimiteDeCreditoAt.text()
        varaprovadorfinanceiroat = self.txtAprovadorFinanceiroAt.text()

        dados =(varrazaoat,varcnpjat,varenderecoat,varbairroat,varcepat,varcidadeat,varestadoat,varpaisat,varcontatoat,vartelefoneat,varemailat,varlimitedecreditoat,varaprovadorfinanceiroat,varbloqueadoat,varcodigoat)
        cursor.execute(comando,dados)
        db.commit()
        cursor.close
        db.close    
                 
        
    def bdMostrarParceiros(self):

        db = pymysql.connect(**config)
        cursor = db.cursor()

        comando = ('select * from LojaDB.parceiros where Codigo = %s ')
        dados = (self.txtCodigoM.text())

        cursor.execute(comando, dados)

        registros = cursor.fetchall()
#Codigo,Razao,CNPJ,Endereco,Bairro,CEP,Cidade,Estado,Pais,Contato,Telefone,Email,LimiteDeCredito,AprovadorFinanceiro,Bloqueado
        for registro in registros:
            self.txtCodigoM.setText(registro[0])
            self.txtRazaoM.setText(registro[1])
            self.txtCNPJM.setText(registro[2])
            self.txtEnderecoM.setText(registro[3])
            self.txtBairroM.setText(registro[4])
            self.txtCEPM.setText(registro[5])
            self.txtCidadeM.setText(registro[6])
            self.txtEstadoM.setText(registro[7])
            self.txtPaisM.setText(registro[8])
            self.txtContatoM.setText(registro[9])
            self.txtTelefoneM.setText(registro[10])
            self.txtEmailM.setText(registro[11])
            self.txtLimiteDeCreditoM.setText(str(registro[12]))
            self.txtAprovadorFinanceiroM.setText(registro[13])
            self.txtBloqueadoM.setText(registro[14])
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

        self.txtCodigoIn = QtGui.QLineEdit()
        self.txtRazaoIn = QtGui.QLineEdit()
        self.txtCNPJIn = QtGui.QLineEdit()
        self.txtEnderecoIn = QtGui.QLineEdit()
        self.txtBairroIn = QtGui.QLineEdit()
        self.txtCEPIn = QtGui.QLineEdit()
        self.txtCidadeIn = QtGui.QLineEdit()
        self.txtEstadoIn = QtGui.QLineEdit()
        self.txtPaisIn = QtGui.QLineEdit()
        self.txtContatoIn = QtGui.QLineEdit()
        self.txtTelefoneIn = QtGui.QLineEdit()
        self.txtEmailIn = QtGui.QLineEdit()
        self.txtLimiteDeCreditoIn = QtGui.QLineEdit()
        self.txtAprovadorFinanceiroIn = QtGui.QLineEdit()
        self.txtBloqueadoIn = QtGui.QLineEdit()
#____________________________________________________________________________________________________________________________________________
        self.txtCodigoAt = QtGui.QLineEdit()
        self.txtRazaoAt = QtGui.QLineEdit()
        self.txtCNPJAt = QtGui.QLineEdit()        
        self.txtEnderecoAt = QtGui.QLineEdit()
        self.txtBairroAt = QtGui.QLineEdit()
        self.txtCEPAt = QtGui.QLineEdit()
        self.txtCidadeAt = QtGui.QLineEdit()
        self.txtEstadoAt = QtGui.QLineEdit()
        self.txtPaisAt = QtGui.QLineEdit()
        self.txtContatoAt = QtGui.QLineEdit()
        self.txtTelefoneAt = QtGui.QLineEdit()
        self.txtEmailAt = QtGui.QLineEdit()
        self.txtLimiteDeCreditoAt = QtGui.QLineEdit()
        self.txtAprovadorFinanceiroAt = QtGui.QLineEdit()
        self.txtBloqueadoAt = QtGui.QLineEdit()

        self.txtCodigoM = QtGui.QLineEdit()
        self.txtRazaoM = QtGui.QLineEdit()
        self.txtCNPJM = QtGui.QLineEdit()
        self.txtEnderecoM = QtGui.QLineEdit()
        self.txtBairroM = QtGui.QLineEdit()
        self.txtCEPM = QtGui.QLineEdit()
        self.txtCidadeM = QtGui.QLineEdit()
        self.txtEstadoM = QtGui.QLineEdit()
        self.txtPaisM = QtGui.QLineEdit()
        self.txtContatoM = QtGui.QLineEdit()
        self.txtTelefoneM = QtGui.QLineEdit()
        self.txtEmailM = QtGui.QLineEdit()
        self.txtLimiteDeCreditoM = QtGui.QLineEdit()
        self.txtAprovadorFinanceiroM = QtGui.QLineEdit()
        self.txtBloqueadoM = QtGui.QLineEdit()

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
        
        self.grid.addWidget(self.btnBuscar,1,1)
        self.grid.addWidget(self.btnInserir,1,2)
        self.grid.addWidget(self.btnAtualizar,1,3)


        self.grid.addWidget(self.lblCodigo,2,0)
        self.grid.addWidget(self.txtCodigoM,2,1)
        self.grid.addWidget(self.txtCodigoIn,2,2)
        self.grid.addWidget(self.txtCodigoAt,2,3)

        self.grid.addWidget(self.lblRazao,3,0)
        self.grid.addWidget(self.txtRazaoM,3,1)
        self.grid.addWidget(self.txtRazaoIn,3,2)
        self.grid.addWidget(self.txtRazaoAt,3,3)

        self.grid.addWidget(self.lblCNPJ,4,0)
        self.grid.addWidget(self.txtCNPJM,4,1)
        self.grid.addWidget(self.txtCNPJIn,4,2)
        self.grid.addWidget(self.txtCNPJAt,4,3)

        self.grid.addWidget(self.lblEndereco,5,0)
        self.grid.addWidget(self.txtEnderecoM,5,1)
        self.grid.addWidget(self.txtEnderecoIn,5,2)
        self.grid.addWidget(self.txtEnderecoAt,5,3)

        self.grid.addWidget(self.lblBairro,6,0)
        self.grid.addWidget(self.txtBairroM,6,1)
        self.grid.addWidget(self.txtBairroIn,6,2)
        self.grid.addWidget(self.txtBairroAt,6,3)

        self.grid.addWidget(self.lblCEP,7,0)
        self.grid.addWidget(self.txtCEPM,7,1)
        self.grid.addWidget(self.txtCEPIn,7,2)
        self.grid.addWidget(self.txtCEPAt,7,3)

        self.grid.addWidget(self.lblCidade,8,0)
        self.grid.addWidget(self.txtCidadeM,8,1)
        self.grid.addWidget(self.txtCidadeIn,8,2)
        self.grid.addWidget(self.txtCidadeAt,8,3)

        self.grid.addWidget(self.lblEstado,9,0)
        self.grid.addWidget(self.txtEstadoM,9,1)
        self.grid.addWidget(self.txtEstadoIn,9,2)
        self.grid.addWidget(self.txtEstadoAt,9,3)

        self.grid.addWidget(self.lblPais,10,0)
        self.grid.addWidget(self.txtPaisM,10,1)
        self.grid.addWidget(self.txtPaisIn,10,2)
        self.grid.addWidget(self.txtPaisAt,10,3)

        self.grid.addWidget(self.lblContato,11,0)
        self.grid.addWidget(self.txtContatoM,11,1)
        self.grid.addWidget(self.txtContatoIn,11,2)
        self.grid.addWidget(self.txtContatoAt,11,3)

        self.grid.addWidget(self.lblTelefone,12,0)
        self.grid.addWidget(self.txtTelefoneM,12,1)
        self.grid.addWidget(self.txtTelefoneIn,12,2)
        self.grid.addWidget(self.txtTelefoneAt,12,3)

        self.grid.addWidget(self.lblEmail,13,0)
        self.grid.addWidget(self.txtEmailM,13,1)
        self.grid.addWidget(self.txtEmailIn,13,2)
        self.grid.addWidget(self.txtEmailAt,13,3)

        self.grid.addWidget(self.lblLimiteDeCredito,14,0)
        self.grid.addWidget(self.txtLimiteDeCreditoM,14,1)
        self.grid.addWidget(self.txtLimiteDeCreditoIn,14,2)
        self.grid.addWidget(self.txtLimiteDeCreditoAt,14,3)

        self.grid.addWidget(self.lblAprovadorFinanceiro,15,0)
        self.grid.addWidget(self.txtAprovadorFinanceiroM,15,1)
        self.grid.addWidget(self.txtAprovadorFinanceiroIn,15,2)
        self.grid.addWidget(self.txtAprovadorFinanceiroAt,15,3)

        self.grid.addWidget(self.lblBloqueado,16,0)
        self.grid.addWidget(self.txtBloqueadoM,16,1)
        self.grid.addWidget(self.txtBloqueadoIn,16,2)
        self.grid.addWidget(self.txtBloqueadoAt,16,3)

        self.grid.addWidget(self.txtCodigoDeletar,17,1)

        self.grid.addWidget(self.btnDeletar,17,0)

        self.grid.addWidget(self.btnSair,17,2)
 
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