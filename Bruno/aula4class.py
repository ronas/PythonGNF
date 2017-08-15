import sys
from PyQt4 import QtCore,QtGui

  
class ClasseAPP(QtGui.QWidget):
     
    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Sistema Lojinha 0.1')
        self.resize(250, 150) 
        self.move(400, 300)
    
        self.txtCodigo = QtGui.QLineEdit()
        self.txtDescricao = QtGui.QLineEdit()
        self.txtValor = QtGui.QLineEdit()
    
        self.btnSair = QtGui.QPushButton('Sair')
        
        self.btnSair.clicked.connect(self.sair) 
        
    
        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblDescricao = QtGui.QLabel('Descricao')
        self.lblValor = QtGui.QLabel('Valor')
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.lblCodigo,1,0)
        self.grid.addWidget(self.txtCodigo,1,1)    
        self.grid.addWidget(self.lblDescricao,2,0)
        self.grid.addWidget(self.txtDescricao,2,1)
        self.grid.addWidget(self.lblValor,3,0)
        self.grid.addWidget(self.txtValor,3,1)
        self. grid.addWidget(self.btnSair,4,1)
        
        self.setLayout(self.grid)
        self.show()
        
    def sair(self):#  criando merodo sair
        
        sys.exit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    MeuAPP = ClasseAPP()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main() 