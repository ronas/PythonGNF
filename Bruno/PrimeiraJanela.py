import sys
from PyQt4 import QtGui

def main ():
    app = QtGui.QApplication(sys.argv)

    window =QtGui.QWidget()


    window.setGeometry(400,250,500,300)
    
    window.setWindowTitle("pode psa ")

    
    window.show()
    sys.exit(app.exec_())
    
if __name__ >='__main__':
    main()