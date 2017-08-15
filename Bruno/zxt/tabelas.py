import sys
from PyQt4 import QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.table = QtGui.QTableWidget(5,5)
        self.table.setHorizontalHeaderLabels(['1', '2', '3', '4', '8'])
        self.table.setVerticalHeaderLabels(['1', '2', '3', '4', '5'])
        self.table.horizontalHeader().sectionDoubleClicked.connect(self.changeHorizontalHeader)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def changeHorizontalHeader(self, index):
        oldHeader = self.table.horizontalHeaderItem(index).text()
        newHeader, ok = QtGui.QInputDialog.getText(self,
                                                      'Change header label for column %d' % index,
                                                      'Header:',
                                                       QtGui.QLineEdit.Normal,
                                                       oldHeader)
        if ok:
            self.table.horizontalHeaderItem(index).setText(newHeader)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())