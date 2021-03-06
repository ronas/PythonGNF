# -*- coding: latin -*-
import sys 

from PyQt4 import QtGui,QtCore

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
        self.txtCodigo.setMaxLength(10)
        self.txtRazao = QtGui.QLineEdit()
        self.txtCNPJ = QtGui.QLineEdit()
        self.txtCNPJ.setMaxLength(16)
        self.txtEndereco = QtGui.QLineEdit()
        self.txtBairro = QtGui.QLineEdit()
        self.txtCEP = QtGui.QLineEdit()
        self.txtCEP.setMaxLength(9)
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
        self.grid.addWidget(self.lblCNPJ,2,0)
        self.grid.addWidget(self.txtCNPJ,2,1)
        self.grid.addWidget(self.lblEndereco,2,2)
        self.grid.addWidget(self.txtEndereco,2,3)
        self.grid.addWidget(self.lblBairro,3,0)
        self.grid.addWidget(self.txtBairro,3,1)
        self.grid.addWidget(self.lblCEP,3,2)
        self.grid.addWidget(self.txtCEP,3,3)
        self.grid.addWidget(self.lblCidade,4,0)
        self.grid.addWidget(self.txtCidade,4,1)
        self.grid.addWidget(self.lblEstado,4,2)
        self.grid.addWidget(self.txtEstado,4,3)
        self.grid.addWidget(self.lblPais,5,0)
        self.grid.addWidget(self.txtPais,5,1)
        self.grid.addWidget(self.lblContato,5,2)
        self.grid.addWidget(self.txtContato,5,3)
        self.grid.addWidget(self.lblTelefone,6,0)
        self.grid.addWidget(self.txtTelefone,6,1)
        self.grid.addWidget(self.lblEmail,6,2)
        self.grid.addWidget(self.txtEmail,6,3)
        self.grid.addWidget(self.lblLimiteDeCredito,7,0)
        self.grid.addWidget(self.txtLimiteDeCredito,7,1)
        self.grid.addWidget(self.lblAprovadorFinanceiro,7,2)
        self.grid.addWidget(self.txtAprovadorFinanceiro,7,3)
        self.grid.addWidget(self.lblBloqueado,8,0)
        self.grid.addWidget(self.txtBloqueado,8,1)
        self.grid.addWidget(self.btnSair,10,0)
        self.grid.addWidget(self.btnConsultar,9,0)
        self.grid.addWidget(self.btnIncluir,9,1)
        self.grid.addWidget(self.btnExcluir,9,2)
        self.grid.addWidget(self.btnAtualizar,9,3)
        self.setLayout(self.grid)
        self.show()


    def dbConsultarClientes(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()

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
        
        comando = ('select * from LojaDB.Parceiros where Codigo = %s ')
        dados = (self.txtCodigo.text())

        cursor.execute(comando, dados)

        registros = cursor.fetchall()

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

        cursor.close()
        db.close()


    def dbIncluirClientes(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = (
            'INSERT INTO LojaDB.Parceiros (Codigo, Razao, CNPJ, Endereco, Bairro, CEP, Cidade, Estado, Pais, Contato, Telefone, Email, LimiteDeCredito, AprovadorFinanceiro, Bloqueado )'
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
            self.txtBloqueado.text()
        )

        varExisteErro = False

        if self.txtCodigo.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Codigo esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True 

        if self.txtRazao.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Razao esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )      
            varExisteErro = True

        if self.txtCNPJ.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo CNPJ esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if testafloat(self.txtCNPJ.text()) == False:
            choice = QtGui.QMessageBox.question(self,'AVISO!','Caracter Invalido no Campo CNPJ.',QtGui.QMessageBox.Ok )
            varExiteErro = True

        if self.txtEndereco.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Endereco esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtBairro.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Bairro esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtCEP.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo CEP esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if testafloat(self.txtCEP.text()) == False:
            choice = QtGui.QMessageBox.question(self,'AVISO!','Caracter Invalido no Campo CEP.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtCidade.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Cidade esta Vazio! Por Favor, Preencher,',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtEstado.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Estado esta Vazio! Por Favor, Preencher,',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtPais.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Pais esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtContato.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Contato esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtTelefone.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Telefone esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if testafloat(self.txtTelefone.text()) == False:
            choice = QtGui.QMessageBox.question(self,'AVISO!','CARACTER Invalido no Campo Telefone.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtEmail.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Email esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtLimiteDeCredito.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Limite De Credito esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if testafloat(self.txtLimiteDeCredito.text()) == False:
            choice = QtGui.QMessageBox.question(self,'AVISO!','Caracter Invalido no Campo Limite De Credito.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtAprovadorFinanceiro.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Aprovador Financeiro esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtBloqueado.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Bloqueado esta Vazio! Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if varExisteErro == False:
            try:
                cursor.execute(comando, dados)
                db.commit()
                choice = QtGui.QMessageBox.question(self,'RESULTADO!','Dados Incluidos com Sucesso.',QtGui.QMessageBox.Ok )

            except pymysql.err.IntegrityError as error:
                code, message = error.args
                if code == 1062: #Erro de duplicidade no Insert
                    choice = QtGui.QMessageBox.question(self,'AVISO!','Registro em Duplicidade! CODIGO Cadastrado! ',QtGui.QMessageBox.Ok )
                else:
                    choice = QtGui.QMessageBox.question(self,'RESULTADO!','Falha ao Incluir Dados.',QtGui.QMessageBox.Ok )
        
        cursor.close()
        db.close()


    def dbExcluirClientes(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ('delete from LojaDB.Parceiros '
        'Where Codigo = (%s) '
        )

        dados = (
            self.txtCodigo.text()    
        )

        choice = QtGui.QMessageBox.question(self,'Extract!',"Excluir Registro?",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            cursor.execute(comando, dados)
            db.commit()

        cursor.close()
        db.close()

    def dbAtualizarClientes(self):
        
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ('update LojaDB.Parceiros '
        'set Razao = %s, CNPJ = %s, Endereco = %s, Bairro = %s, CEP = %s, Cidade = %s, Estado = %s, Pais = %s, Contato = %s, Telefone = %s, Email = %s, LimiteDeCredito = %s, AprovadorFinanceiro = %s, Bloqueado = %s '
        'where Codigo = (%s)'

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
            self.txtBloqueado.text(),
            self.txtCodigo.text()
        )

        varExisteErro = False

        if self.txtRazao.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Razao esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtCNPJ.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo CNPJ esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if testafloat(self.txtCNPJ.text()) == False:
            choice = QtGui.QMessageBox.question(self,'AVISO!','Caracter Invalido no Campo CNPJ.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtEndereco.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Endereco esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtBairro.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Bairro esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtCEP.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo CEP esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if testafloat(self,txtCEP.text()) == False:
            choice = QtGui.QMessageBox.question(self,'AVISO!','Caracter Invalido no Campo CEP.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtCidade.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Cidade esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtEstado.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Estado esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtPais.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Pais esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtContato.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Contato esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtTelefone.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Telefone esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if testafloat(self.txtTelefone.text()) == False:
            choice = QtGui.QMessageBox.question(self,'AVISO!','CARACTER Invalido no Campo Telefone.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtEmail.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Email esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtLimiteDeCredito.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Limite De Cradito esta Vazio!, Por Favor Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if testafloat(self.txtLimiteDeCredito.text()) == False:
            choice = QtGui.QMessageBox.question(self,'AVISO!','CARACTER Invalido no Campo Limite De Credito.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtAprovadorFinanceiro.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Aprovador Financeiro esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtBloqueado.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Bloqueado esta Vazio!, Por Favor, Preencher.',QtGui.QMessageBox.Ok )
            varExisteErro = True

        if self.txtCodigo.text() == '':
            choice = QtGui.QMessageBox.question(self,'AVISO!','O Campo Codigo esta Vazio!, Por Favor, Preencher.',QtGui.QmessageBox.Ok )
            varExisteErro = True

        if varExisteErro == False:
            try:
                cursor.execute(comando, dados)
                db.commit()
                choice = QtGui.QMessageBox.question(self,'RESULTADO!','Dados Atualizados com Sucesso.',QtGui.QMessageBox.Ok )

            except pymysql.err.IntegrityError as error:
                code, message = error.args
                if code == 1062: #Erro de duplicidade no Inserts
                    choice = QtGui.QMessageBox.question(self,'AVISO!','Registro em Duplicidade! CODIGO Cadastrado! ',QtGui.QMessageBox.Ok )
                else:
                    choice = QtGui.QMessageBox.question(self,'RESULTADO!','Falha ao Atualizar Dados.',QtGui.QMessageBox.Ok )
                    
        cursor.close()
        db.close()

    def Sair(self):
        sys.exit()

def testafloat(prmEntrada):
    try: 
        varfloat =float(prmEntrada)
        return(True)

    except ValueError:
        return(False)

def main():
    app = QtGui.QApplication(sys.argv)
    MeuApp = ClasseAPP()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()