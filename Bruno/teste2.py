import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit) #evento no botao
        btn.resize(45,35) # tamano do botao 
        btn.move(360,250)# localização dentro da janela
        
        txtCodigo = QtGui.QLineEdit("bora",self)
        txtCodigo.resize(150,30)
        txtCodigo.move(200,255)
        self.show()
        
    

        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()