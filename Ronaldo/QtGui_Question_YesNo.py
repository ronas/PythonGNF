# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore,QtGui

import pymysql
from builtins import str
  
class ClasseAPP(QtGui.QWidget):
     
    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):

        super(ClasseAPP, self).__init__()
        #self.setGeometry(400, 100, 278, 247)
        self.setGeometry(300,100,0,0)
        self.setFixedSize(700,650)
        self.setWindowTitle("Produtos")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))





        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                " Salvar Registro  ?",
                                QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.No:
    
            print("VOCE NÃO QUIS SALVAR")

        else:
            print("VOCE QUIS SALVAR")



def main():
    app = QtGui.QApplication(sys.argv)
    ui = ClasseAPP()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
