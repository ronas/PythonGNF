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
        btn = QtGui.QPushButton("Quit", self) # nome do botao 
        btn.clicked.connect(self.close_application)# metodo que fecha atela btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint()) #metodo que cria o botao (btn.minimumSizeHint())
        btn.move(0,0)
        self.show()

    def close_application(self):
        print("whooaaaa so custom!!!")# testando saida 
        sys.exit()
        
        
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()