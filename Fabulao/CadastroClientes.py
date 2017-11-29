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
        self.resize(500, 250)
        self.move(500, 500)

        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblRazao = QtGui.QLabel('Razao')
        self.lblCNPJ = QtGui.QLabel('CNPJ')
        self.lblEndereco = QtGui.QLabel('Endereco')
        self.lblBairro = QtGui.QLaabel('Bairro')
        self.lblCEP = QtGUi.QLabel('CEP')
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

        self.btnBuscar = QtGui.QPushButton('Consultar' ,self)
        self.btnBuscar.clicked.connect(self.dbConsultarClientes)
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
        self.grid.addWidget(self.lblRazao,2,0)
        self.grid.addWidget(self.txtRazao,2,1)
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
        self.grid.addWidget(self.txtEStado,8,1)
        self.grid.addWidget(self.lblPais,9,0)
        self.grid.addWidget(self.txtPais,9,1)
        self.grid.addwidget(self.lblContato,10,0)
        self.grid.addWidget(self.txtContato,10,1)
        self.grid.addWidget(self.lblTelefone,11,0)
        self.grid.addWidget(self.txtTelefone,11,1)
        self.grid.addWidget(self.lblEmail,12,0)
        self.grid.addWidget(self.txtEmail,12,1)
        self.grid.addWidget(self.lblLimiteDeCredito,13,0)
        self.grid.addwidget(self.txtLimiteDeCredito,13,1)
        self.grid.addWidget(self.lblAprovadorFinanceiro,14,0)
        self.grid.addWidget(self.txtAprovadorFinanceiro,14,1)
        self.grid.addWidget(self.btnSair,15,1)
        self.grid.addWidget(self.btnBuscar,16,0)
        self.grid.addWidget(self.btnIncluir,17,1)
        self.grid.addWidget(self.btnExcluir,18,0)
        self.grid.addWidget(self.btnAtualizar,19,1)
        self.setLayout(self.grid)
        self.show()


    def Sair(self):
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)
    MeuApp = ClasseAPP()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()