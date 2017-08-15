#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import sys
import pymysql
from PyQt4 import QtCore,QtGui

  
  
comfig ={'host':'localhost',# criando metodo de entrada do Mysql
         'port':3306,
         'database':'Lojadb',
         'user':'root',
         'password':'34387'}
db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
cursor = db.cursor()

class ClasseAPP(QtGui.QWidget):
     
    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Sistema Lojinha 0.1')
        self.resize(250, 150)
        self.move(400, 300)
    
        self.txtCodigo = QtGui.QLineEdit()
        self.txtDescricao = QtGui.QLineEdit()
        self.txtValor = QtGui.QLineEdit()
    
        self.btnSair = QtGui.QPushButton('Sair')
        
        self.btnSair.clicked.connect(self.sair)
        
        self.btnbuscar =  QtGui.QPushButton('Buscar')
        self.btnbuscar.clicked.connect(self.dbmontrarProdutos )
    
        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblDescricao = QtGui.QLabel('Descricao')
        self.lblValor = QtGui.QLabel('Valor')
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1)    
        self.grid.addWidget(self.lblDescricao,2,0)
        self.grid.addWidget(self.txtDescricao,2,1)
        self.grid.addWidget(self.lblValor,3,0)
        self.grid.addWidget(self.txtValor,3,1)
        self.grid.addWidget(self.btnSair,4,1)
        self.grid.addWidget(self.btnbuscar,4,0)
        self.setLayout(self.grid)
        self.show()
        
    def sair(self):#  criando merodo sair
        
    
        sys.exit()
        
        
    def dbmontrarProdutos (self):
        db= pymysql.connect(** comfig)# criando ponteiro que o intermediario 
        cursor = db.cursor()
        
        
        comando =("select * from  Lojadb.fornecedordb" )  
        cursor.execute (comando)
        registros = cursor.fetchall()
        
        
        
        for  registros in registros:
            
            self.txtCodigo.setText(registros[0])
            
            self.txtDescricao.setText(str(registros[1]))
            self.txtValor.setText(str(registros[2]))
            
            break
            
            db.commit()
            print('ja foi')

            cursor.close()
            db.close
            
 
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    MeuAPP = ClasseAPP()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()