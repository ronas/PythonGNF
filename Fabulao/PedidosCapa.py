# -*- coding: latin -*-
import sys 

#from PyQt5 import QtGui, QtCore, QtWidgets #, QTableWidget, QTableWidgetItem

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
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
        self.resize(800, 400)
        self.move(300, 300)

        self.tabela = QTableWidget(3,5,self)
        self.tabela.setGeometry(20,20,760,300)
        self.tabela.setHorizontalHeaderLabels(('Numero Pedido','Data','Codigo Cliente','Telefone','Cond Pagamento'))
        self.dbBuscarPedidos()






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