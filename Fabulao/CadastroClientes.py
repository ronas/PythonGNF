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

        self.setWindowTitle('Parceiros')
        self.resize(500, 500)
        self.move(500, 500)

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
        self.lblBloqueado = QtGui.QLabel('BLoqueado')
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

        self.btnConsultar = QtGui.QPushButton('Consultar' ,self)
        self.btnConsultar.clicked.connect(self.dbConsultarClientes)
        self.btnIncluir = QtGui.QPushButton('Incluir' ,self)
        self.btnIncluir.clicked.connect(self.dbIncluirClientes)
        self.btnExcluir = QtGui.QPushButton('Excluir' ,self)
        self.btnExcluir.clicked.connect(self.dbExcluirClientes)
        self.btnAtualizar = QtGui.QPushButton('Atualizar' ,self)
        self.btnAtualizar.clicked.connect(self.dbAtualizarClientes)
        self.btnSair = QtGui.QPushButton('Sair' ,self)
        self.btnSair.clicked.connect(self.Sair)
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(20)

        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1)
        self.grid.addWidget(self.lblRazao,1,2)
        self.grid.addWidget(self.txtRazao,1,3)
        self.grid.addWidget(self.lblCNPJ,3,0)
        self.grid.addWidget(self.txtCNPJ,3,1)
        self.grid.addWidget(self.lblEndereco,4,0)
        self.grid.addWidget(self.txtEndereco,4,1)
        self.grid.addWidget(self.lblBairro,5,0)
        self.grid.addWidget(self.txtBairro,5,1)
        self.grid.addWidget(self.lblCEP,6,0)
        self.grid.addWidget(self.txtCEP,6,1)
        self.grid.addWidget(self.lblCidade,7,0)
        self.grid.addWidget(self.txtCidade,7,1)
        self.grid.addWidget(self.lblEstado,8,0)
        self.grid.addWidget(self.txtEstado,8,1)
        self.grid.addWidget(self.lblPais,9,0)
        self.grid.addWidget(self.txtPais,9,1)
        self.grid.addWidget(self.lblContato,10,0)
        self.grid.addWidget(self.txtContato,10,1)
        self.grid.addWidget(self.lblTelefone,11,0)
        self.grid.addWidget(self.txtTelefone,11,1)
        self.grid.addWidget(self.lblEmail,12,0)
        self.grid.addWidget(self.txtEmail,12,1)
        self.grid.addWidget(self.lblLimiteDeCredito,13,0)
        self.grid.addWidget(self.txtLimiteDeCredito,13,1)
        self.grid.addWidget(self.lblAprovadorFinanceiro,14,0)
        self.grid.addWidget(self.txtAprovadorFinanceiro,14,1)
        self.grid.addWidget(self.lblBloqueado,15,0)
        self.grid.addWidget(self.txtBloqueado,15,1)
        self.grid.addWidget(self.btnSair,16,1)
        self.grid.addWidget(self.btnConsultar,17,0)
        self.grid.addWidget(self.btnIncluir,18,1)
        self.grid.addWidget(self.btnExcluir,19,0)
        self.grid.addWidget(self.btnAtualizar,20,1)
        self.setLayout(self.grid)
        self.show()


    def dbConsultarClientes(self):
        
        db = pymysql.connect(**config)
        cursor =db.cursor()
        comando = ( 'select * fron LojaDB.Parceiros'
        'set, Razao = %s, CNPJ = %s, Endereco = %s, Bairro = %s, CEP = %s, Cidade = %s, Estado = %s, Pais = %s, Contato = %s, Telefone = %s, Email = %s, LimitedeCredito = %s, AprovadorFinanceiro = %s, Bloqurado = %s '        
        )

        dados = (

            self.txtRazao.text(),
            self.txtCNPJ.text(),
            self.txtEndereco.text(),
            self.txtBairro.text(),
            self.txtCEP.text(),
            self.txtCidade.text(),
            self.txtEstado.text(),
            self.txtPais.text(),
            self.txtContato.text(),
            self.txtTelefone.text(),
            self.txtEmail.text(),
            self.txtLimitedeCredito.text(),
            self.txtAprovadorFinanceiro.text(),
            self.txtBloqueado.text(),
        )

        cursor.execute(comando, dados)
        db.commit()
        cursor.close()
        db.close()


    def dbIncluirClientes(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = (
            'INSERT INTO LojaDB.Parceiros (Codigo, Razao, CNPJ, Endereco, Bairro, CEP, Cidade, Estado, Pais, Contato, Telefone, Email, LimiteDeCredito, AprovadorFinanceiro, Bloqueado ) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'     
        )

        dados = (
            self.txtCodigo.text(),
            self.txtRazao.text(),
            self.txtCNPJ.text(),
            self.txtEndereco.text(),
            self.txtBairro.text(),
            self.txtCEP.text(),
            self.txtCidade.text(),
            self.txtEstado.text(),
            self.txtPais.text(),
            self.txtContato.text(),
            self.txtTelefone.text(),
            self.txtEmail.text(),
            self.txtLimiteDeCredito.text(),
            self.txtAprovadorFinanceiro.text(),
            self.txtBloqueado.text(),
        )

        cursor.execute(comando, dados)
        db.commit()
        
        cursor.close()
        db.close()


    def dbExcluirClientes(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ('delete fron LojaDB.Parceiros'
        'Where Codigo = (%s) '
        )

        dados = (
            self.txtCodigo.text(),
            
        )

        cursor.execute(comando, dados)
        db.commit()

        cursor.close()
        db.close()

    def dbAtualizarClientes(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ('update LojaDB.Parceiros'
        'set Razao = %s, CNPJ = %s, Endereco = %s, Bairro = %s, CEP = %s, Cidade = %s, Estado = %s, Pais = %s, Contato = %s, Telefone = %s, Email = %s, LimiteDeCredito = %s, AprovadorFinanceiro = %s, Bloqueado = %s '

        )

        dados = (
            self.txtRazao.text(),
            self.txtCNPJ.text(),
            self.txtEndereco.text(),
            self.txtBairro.text(),
            self.txtCEP.text(),
            self.txtCidade.text(),
            self.txtEstado.text(),
            self.txtPais.text(),
            self.txtContato.text(),
            self.txtTelefone.text(),
            self.txtEmail.text(),
            self.txtLimiteDeCredito.text(),
            self.txtAprovadorFinanceiro.text(),
            self.Bloqueado.text(),
        )

        cursor.execute(comando, dados)
        db.commit()
        
        cursor.close()
        db.close()



    def Sair(self):
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)
    MeuApp = ClasseAPP()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()