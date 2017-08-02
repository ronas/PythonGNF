import sys
from PyQt4 import QtGui

class subwindow(QtGui.QWidget):
    def createWindow(self,WindowWidth,WindowHeight):
       parent=None
       super(subwindow,self).__init__(parent)
       selt.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
       self.resize(WindowWidth,WindowHeight)

class mainwindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
       [...]

    def createsASubwindow(self):
       self.mySubwindow=subwindow()
       self.mySubwindow.createWindow(500,400)
       #make pyqt items here for your subwindow
       #for example self.mySubwindow.button=QtGui.QPushButton(self.mySubwindow)

       self.mySubwindow.show()
       
