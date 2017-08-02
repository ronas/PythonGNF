import sys
from PyQt4 import QtGui

def main():
    
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.setWindowTitle('Sistema Lojinha 0.1')
    w.resize(250, 150)
    w.move(300, 300)


    lblCodigo = QtGui.QLabel('Codigo')
    lblDescricao = QtGui.QLabel('Descricao')

    txtCodigo = QtGui.QLineEdit()
    txtDescricao = QtGui.QLineEdit()


    grid = QtGui.QGridLayout()
    grid.setSpacing(10)

    grid.addWidget(lblCodigo, 1, 0)
    grid.addWidget(txtCodigo, 1, 1)
    grid.addWidget(lblDescricao, 2, 0)
    grid.addWidget(txtDescricao, 2, 1)

   
    w.setLayout(grid)
    w.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
