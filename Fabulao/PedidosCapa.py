# -*- coding: latin -*-
import sys 

#from PyQt5 import QtGui, QtCore, QtWidgets #, QTableWidget, QTableWidgetItem

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QLabel
from PyQt5.QtCore import QSize, Qt

import pymysql

config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'LojaDB',
    'user': 'root',
    'password' : 'fbl1978'
}

class ClasseAPP(QWidget):

    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):


        self.setWindowTitle('Pedidos')
        self.resize(850, 400)
        self.move(300, 200)

        self.tabela = QTableWidget(3,5,self)
        self.tabela.setGeometry(20,20,760,300)
        self.tabela.setHorizontalHeaderLabels(('Numero Pedido','Data','Codigo Cliente','Telefone','Cond Pagamento'))
        self.dbBuscarPedidos()

        self.lblNumeroPedido = QLabel('Numero Pedido',self)
        self.lblNumeroPedido.setGeometry(20,330,130,25)
        self.lblData = QLabel('Data',self)
        self.lblData.setGeometry(100.360,50,25)
        #self.lblCodigoCliente = QLabel('Codigo Cliente',self)
        #self.lblCodigoCliente.setGeometry()
        #self.lblTelefone = QLabel('Telefone',self)
        #self.lblTelefone.setGeometry()
        #self.lblCondPagamento = QLabel('Cond Pagamento',self)
        #self.lblCondPagamento.setGeometry()
        
        self.txtNumeroPedido = QLineEdit(self)
        self.txtNumeroPedido.setGeometry(130,330,130,25)
        self.txtData = QLineEdit(self)
        self.txtData.setGeometry(130,360,50,25)
        #self.txtCodigoCliente = QLineEdit(self)
        #self.txtCOdigoCliente.setGeometry()
        #self.txtTelefone = QLineEdit(self)
        #self.txtTelefone.setGeometry()
        #self.txtCondPagamento = QLineEdit(self)
        #self.txtCondPagamento.setGeometry()
        
        self.tabela.resizeColumnsToContents()
               
        self.show()

    def dbBuscarPedidos(self):
    
        db = pymysql.connect(**config)
        cursor = db.cursor()    

        comando = ('select * from LojaDB.Pedidos ')

        cursor.execute(comando )

        self.tabela.setRowCount(0)


        registros = cursor.fetchall()
        
        for registro in registros:
            numerolinhas = self.tabela.rowCount()
            self.tabela.insertRow(numerolinhas)
            self.tabela.setItem(numerolinhas, 0, QTableWidgetItem(  str(registro[0])   ))
            self.tabela.setItem(numerolinhas, 1, QTableWidgetItem(  str(registro[1])   ))
            self.tabela.setItem(numerolinhas, 2, QTableWidgetItem(      registro[2]    ))
            self.tabela.setItem(numerolinhas, 3, QTableWidgetItem(  str(registro[3])   ))
            self.tabela.setItem(numerolinhas, 4, QTableWidgetItem(      registro[4]    ))



        cursor.close()
        db.close()


def main():
    app = QApplication(sys.argv)
    MeuApp = ClasseAPP()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()