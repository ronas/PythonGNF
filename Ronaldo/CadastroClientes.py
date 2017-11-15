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
        self.resize(300, 150)
        self.move(300, 300)