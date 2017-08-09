
import sys
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    w=QtGui.QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('Teste')
    
    txtCodigo = QtGui.QLineEdit()
    txtDescricao = QtGui.QLineEdit()
    txtValor = QtGui.QLineEdit()
    
    btnSair = QtGui.QPushButton('Sair',w)
    
    lblCodigo = QtGui.QLabel('Codigo')
    lblDescricao = QtGui.QLabel('Descricao')
    lblValor = QtGui.QLabel('Valor')
    grid = QtGui.QGridLayout()
    grid.setSpacing(10)
    grid.addWidget(lblCodigo,1,0)
    grid.addWidget(txtCodigo,1,1)    
    grid.addWidget(lblDescricao,2,0)
    grid.addWidget(txtDescricao,2,1)
    grid.addWidget(lblValor,3,0)
    grid.addWidget(txtValor,3,1)
    grid.addWidget(btnSair,4,1)
    w.setLayout(grid)
    
    w.show()
    sys.exit(app.exec_())
if __name__ >='__main__':
    main()
