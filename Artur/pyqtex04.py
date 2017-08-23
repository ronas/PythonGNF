import sys

from PyQt4 import QtGui

def sair():
    sys.exit() 

class classApp(QtGui.QWidget):
    def __init__(self):
        super(classApp,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('SistemaLojinha2')
        self.resize(250,150)
        self.move(300,300)
        
        self.lblCodigo = QtGui.QLabel('codigo')
        self.lblDescricao = QtGui.QLabel('descricao')
        self.lblValor = QtGui.QLabel('valor')
        self.txtCodigo = QtGui.QLineEdit()
        self.txtDescricao = QtGui.QLineEdit()
        self.txtValor = QtGui.QLineEdit()
        self.btnSair = QtGui.QPushButton('Sair',self)
        self.btnSair.clicked.connect(sair)
         
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1)
        self.grid.addWidget(self.lblDescricao,2,0)
        self.grid.addWidget(self.txtDescricao,2,1)
        self.grid.addWidget(self.lblValor,3,0)
        self.grid.addWidget(self.txtValor,3,1)
        self.grid.addWidget(self.btnSair,4,1)
        
        self.setLayout(self.grid)
        
        self.show()
    def sair(self):
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)
    meuapp = classApp()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()     
