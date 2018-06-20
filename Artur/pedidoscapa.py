# -*- coding: latin -*-

import sys

import pymysql

from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize,Qt


config = {
    'host':'localhost',
    'port' : 3306,
    'database' : 'LojaDB',
    'user' : 'root',
    'password' : ''
    }

class classApp(QtGui.QWidget):
    def __init__(self):
        super(classApp,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Pedidos')
        self.resize(250,150)
        self.move(300,300)  
        self.setGeometry(300,200,850,400)

        self.tabela = QtTableWidget(3,5,self)
        self.tabela.setGeometry(20,20,760,300)
        self.tabela.setHorizontalHeaderLabels(('Pedido','CodigoCliente','AlgumaCoisa'))
        self.table.resizeColumsToContents()

        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    meuapp = classApp()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()                     