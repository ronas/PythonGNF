import sys
from PyQt4 import QtGui

  
class ClasseAPP(QtGui.QWidget):

    def __init__(self):
        super(ClasseAPP, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Sistema Lojinha 0.1')
        self.resize(250, 150)
        self.move(300, 300)
    
        self.lblCodigo = QtGui.QLabel('Codigo')
        self.lblDescricao = QtGui.QLabel('Descricao')
        self.txtCodigo = QtGui.QLineEdit()
        self.txtDescricao = QtGui.QLineEdit()
    
        self.btnSair = QtGui.QPushButton('Sair', self)
        self.btnSair.clicked.connect(self.sair)
    
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)
    
        self.grid.addWidget(self.lblCodigo, 1, 0)
        self.grid.addWidget(self.txtCodigo, 1, 1)
        self.grid.addWidget(self.lblDescricao, 2, 0)
        self.grid.addWidget(self.txtDescricao, 2, 1)
        self.grid.addWidget(self.btnSair, 3, 1)
           
        self.setLayout(self.grid)
        self.show()
        
    def sair(self):
        if Numero(self.txtCodigo.text()) ==  True:
            sys.exit()

def Numero(ParamEntrada):
    try:
        val = float(ParamEntrada)
        return(True)

    except ValueError:
        return(False)        
        
def main():
    app = QtGui.QApplication(sys.argv)
    MeuAPP = ClasseAPP()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
