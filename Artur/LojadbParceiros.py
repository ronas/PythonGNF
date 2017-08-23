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

    def AtualizarParceiros(self):
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

    def MostrarParceiros(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = 'select * from Parceiros'
        cursor.execute(comando)
        registros = cursor.fetchall()
#Codigo Razao CNPJ Endereco Bairro CEP Cidade Estado Pais Contato TELEFONE email LimiteDeCredito AprovadoFinanceiro Bloqueado        
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
            self.txtAprovadoFinanceiro.setText(registro[13])
            self.txtBloqueado.setText(registro[14])
        cursor.close
        db.close




    def bdExcluirParceiros(self):
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando = ("delete from LojaDB.Parceiros "
                   "where Codigo = '%s' ")
        varcodigo = self.txtCodigoDeletar.text()
    
        cursor.execute(comando,varcodigo)
        db.commit()
        cursor.close()
        db.close()



    def bdInserirParceiros(self):
 
        db = pymysql.connect(**config)
        cursor = db.cursor()
        comando =(
            "insert into Parceiros (Codigo,Razao,CNPJ,Endereco,Bairro,CEP,Cidade,Estado,Pais,Contato,TELEFONE,email,LimiteDeCredito,AprovadoFinanceiro,Bloqueado)"
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            )
#   Codigo   Razao  CNPJ  Endereco  Bairro  CEP  Cidade  Estado  Pais  Contato  TELEFONE  email  LimiteDeCredito  AprovadoFinanceiro  Bloqueado
        varcodigo = self.txtCodigo.text()   
        varRazao = self.txtRazao.text()  
        varCNPJ = self.txtCNPJ.text()  
        varEndereco = self.txtEndereco.text() 
        varBairro = self.txtBairro.text()   
        varCEP = self.txtCEP.text()   
        varCidade = self.txtCidade.text()   
        varEstado = self.txtEstado.text()
        varPais = self.txtPais.text()
        varContato = self.txtContato.text()
        varTelefone = self.txtTelelfone.text()
        varEmail = self.txtEmail.text()
        varLimiteDeCredito = self.txtLimiteDeCredito.text()
        varAprovadoFinanceiro = self.txtAprovadoFinanceiro.text()
        varBloqueado = self.txtBloqueado.text()  
        dados = (varcodigo,
                 varRazao,
                 varCNPJ,
                 varEndereco,
                 varBairro,
                 varCEP,
                 varCidade,
                 varEstado,
                 varPais,
                 varContato,
                 varTelefone,
                 varEmail,
                 varLimiteDeCredito,
                 varAprovadoFinanceiro,
                 varBloqueado)
        cursor.execute(comando,dados)
        db.commit()
        cursor.close
        db.close
    













