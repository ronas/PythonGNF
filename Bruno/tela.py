# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(400, 240)
        self.pushButton = QtGui.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 190, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.nome = QtGui.QLabel(dialog)
        self.nome.setGeometry(QtCore.QRect(100, 120, 68, 17))
        self.nome.setObjectName(_fromUtf8("nome"))
        self.lineEdit = QtGui.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 120, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Dialog", None))
        self.pushButton.setText(_translate("dialog", "linpar", None))
        self.nome.setText(_translate("dialog", "nome", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

