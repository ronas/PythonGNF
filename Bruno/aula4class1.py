# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banco1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.btnsalvar = QtGui.QPushButton(Dialog)
        self.btnsalvar.setGeometry(QtCore.QRect(190, 210, 99, 27))
        self.btnsalvar.setObjectName(_fromUtf8("btnsalvar"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.linhanome = QtGui.QLineEdit(Dialog)
        self.linhanome.setGeometry(QtCore.QRect(120, 70, 221, 27))
        self.linhanome.setObjectName(_fromUtf8("linhanome"))
        self.linhacodigo = QtGui.QLineEdit(Dialog)
        self.linhacodigo.setGeometry(QtCore.QRect(120, 120, 231, 27))
        self.linhacodigo.setObjectName(_fromUtf8("linhacodigo"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnsalvar, QtCore.SIGNAL(_fromUtf8("clicked()")), self. create_fornecedor)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
   
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btnsalvar.setText(_translate("Dialog", "Salvar", None))
        self.label.setText(_translate("Dialog", "Nome", None))
        self.label_2.setText(_translate("Dialog", "codigo", None))
    def create_fornecedor(self):
        varnome = self.linhanome .text()
        print("foi")       

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    sys.exit(app.exec_())

