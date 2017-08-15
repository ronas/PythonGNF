import sys
from PyQt4 import QtGui, QtCore


class bruno(QtGui.QMainWindow):

    def __init__(self):
        super(bruno, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractActon = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractActon.setShortcut("Ctrl+Q")
        extractActon.setStatusTip('Leave The App')
        extractActon.triggered.connect(self.create_new_windows)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractActon)
        
        self.home()

    
    
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        self.show()
     
     
    def create_new_windows(self):
       
        self._ficha = ClasseAPP()
        self._ficha.show()   
    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


def run():
    
    app = QtGui.QApplication(sys.argv)
    GUI = bruno()
    sys.exit(app.exec_())
    
run()